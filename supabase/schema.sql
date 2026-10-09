-- The Magnificent 5 Days Bootcamp — database schema. Run once in Supabase → SQL editor.
create extension if not exists pgcrypto;

create table if not exists public.app_settings (key text primary key, value text);
insert into public.app_settings (key,value) values ('owner_email','themagnificentnetwork@gmail.com'),('ngn_rate','1360') on conflict (key) do nothing;

create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  full_name text not null default '', email text not null default '', phone text, photo_url text,
  status text not null default 'Member', sponsor_name text, senior_manager text, executive_manager text, director text, emerald_director text,
  role text not null default 'participant' check (role in ('participant','committee','admin')),
  can_verify_payments boolean not null default false, is_confirmed boolean not null default false,
  bio text, skill text, created_at timestamptz not null default now());

create table if not exists public.payments (
  id uuid primary key default gen_random_uuid(), user_id uuid references public.profiles(id) on delete cascade,
  type text not null check (type in ('registration','donation')), method text not null, currency text not null,
  amount_claimed numeric not null default 0, amount_due_usd numeric not null default 0, reference text, proof_url text,
  status text not null default 'pending' check (status in ('pending','approved','rejected')),
  approved_amount_usd numeric, rejection_reason text, reviewed_by uuid, reviewed_at timestamptz,
  guest_name text, guest_email text, created_at timestamptz not null default now());

create table if not exists public.attendance (id uuid primary key default gen_random_uuid(), user_id uuid references public.profiles(id) on delete cascade, day int not null check (day between 1 and 5), recorded_by uuid, created_at timestamptz default now(), unique (user_id, day));
create table if not exists public.plans (user_id uuid primary key references public.profiles(id) on delete cascade, data jsonb not null default '{}', updated_at timestamptz default now());
create table if not exists public.messages (id uuid primary key default gen_random_uuid(), room text, sender_id uuid references public.profiles(id) on delete cascade, recipient_id uuid references public.profiles(id) on delete cascade, body text not null, created_at timestamptz default now());
create table if not exists public.connections (id uuid primary key default gen_random_uuid(), requester_id uuid references public.profiles(id) on delete cascade, addressee_id uuid references public.profiles(id) on delete cascade, status text not null default 'pending' check (status in ('pending','accepted','ignored')), created_at timestamptz default now(), unique (requester_id, addressee_id));
create table if not exists public.announcements (id uuid primary key default gen_random_uuid(), body text not null, author_id uuid, created_at timestamptz default now());
create table if not exists public.contact_messages (id uuid primary key default gen_random_uuid(), name text, email text, phone text, subject text, message text, created_at timestamptz default now());
create table if not exists public.audit_log (id uuid primary key default gen_random_uuid(), actor_id uuid, action text, target_id text, details jsonb, created_at timestamptz default now());

-- helpers
create or replace function public.is_admin() returns boolean language sql stable security definer set search_path = public as $$ select exists (select 1 from public.profiles where id = auth.uid() and role = 'admin') $$;
create or replace function public.is_staff() returns boolean language sql stable security definer set search_path = public as $$ select exists (select 1 from public.profiles where id = auth.uid() and role in ('admin','committee')) $$;
create or replace function public.can_verify() returns boolean language sql stable security definer set search_path = public as $$ select exists (select 1 from public.profiles where id = auth.uid() and (role = 'admin' or (role = 'committee' and can_verify_payments))) $$;

-- create profile on sign-up; owner email becomes admin automatically
create or replace function public.handle_new_user() returns trigger language plpgsql security definer set search_path = public as $$
declare owner text; begin
  select value into owner from public.app_settings where key = 'owner_email';
  insert into public.profiles (id, email, full_name, phone, status, sponsor_name, senior_manager, executive_manager, director, emerald_director, role)
  values (new.id, new.email, coalesce(new.raw_user_meta_data->>'full_name',''), new.raw_user_meta_data->>'phone', coalesce(new.raw_user_meta_data->>'status','Member'),
          new.raw_user_meta_data->>'sponsor_name', new.raw_user_meta_data->>'senior_manager', new.raw_user_meta_data->>'executive_manager', new.raw_user_meta_data->>'director', new.raw_user_meta_data->>'emerald_director',
          case when lower(new.email) = lower(owner) then 'admin' else 'participant' end)
  on conflict (id) do nothing; return new; end $$;
drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created after insert on auth.users for each row execute function public.handle_new_user();

-- owner can never be demoted
create or replace function public.protect_owner() returns trigger language plpgsql security definer set search_path = public as $$
declare owner text; begin select value into owner from public.app_settings where key='owner_email';
  if lower(new.email) = lower(owner) then new.role := 'admin'; end if; return new; end $$;
drop trigger if exists protect_owner_trg on public.profiles;
create trigger protect_owner_trg before update on public.profiles for each row execute function public.protect_owner();

-- RLS
alter table public.profiles enable row level security; alter table public.payments enable row level security; alter table public.attendance enable row level security;
alter table public.plans enable row level security; alter table public.messages enable row level security; alter table public.connections enable row level security;
alter table public.announcements enable row level security; alter table public.contact_messages enable row level security; alter table public.audit_log enable row level security; alter table public.app_settings enable row level security;

drop policy if exists p_sel on public.profiles; create policy p_sel on public.profiles for select to authenticated using (true);
drop policy if exists p_upd_self on public.profiles; create policy p_upd_self on public.profiles for update to authenticated using (id = auth.uid()) with check (id = auth.uid() and role = (select role from public.profiles where id = auth.uid()));
drop policy if exists p_upd_admin on public.profiles; create policy p_upd_admin on public.profiles for update to authenticated using (public.is_admin()) with check (true);
drop policy if exists pay_sel on public.payments; create policy pay_sel on public.payments for select to authenticated using (user_id = auth.uid() or public.is_staff());
drop policy if exists pay_ins on public.payments; create policy pay_ins on public.payments for insert to authenticated with check (user_id = auth.uid() or user_id is null);
drop policy if exists pay_ins_anon on public.payments; create policy pay_ins_anon on public.payments for insert to anon with check (user_id is null and type = 'donation');
drop policy if exists pay_upd on public.payments; create policy pay_upd on public.payments for update to authenticated using (public.can_verify()) with check (true);
drop policy if exists att_sel on public.attendance; create policy att_sel on public.attendance for select to authenticated using (user_id = auth.uid() or public.is_staff());
drop policy if exists att_all on public.attendance; create policy att_all on public.attendance for all to authenticated using (public.is_staff()) with check (public.is_staff());
drop policy if exists plan_own on public.plans; create policy plan_own on public.plans for all to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
drop policy if exists plan_count on public.plans; create policy plan_count on public.plans for select to authenticated using (public.is_staff());
drop policy if exists msg_sel on public.messages; create policy msg_sel on public.messages for select to authenticated using (room is not null or sender_id = auth.uid() or recipient_id = auth.uid() or public.is_staff());
drop policy if exists msg_ins on public.messages; create policy msg_ins on public.messages for insert to authenticated with check (sender_id = auth.uid());
drop policy if exists msg_del on public.messages; create policy msg_del on public.messages for delete to authenticated using (sender_id = auth.uid() or public.is_staff());
drop policy if exists con_sel on public.connections; create policy con_sel on public.connections for select to authenticated using (requester_id = auth.uid() or addressee_id = auth.uid() or public.is_staff());
drop policy if exists con_ins on public.connections; create policy con_ins on public.connections for insert to authenticated with check (requester_id = auth.uid());
drop policy if exists con_upd on public.connections; create policy con_upd on public.connections for update to authenticated using (addressee_id = auth.uid()) with check (true);
drop policy if exists ann_sel on public.announcements; create policy ann_sel on public.announcements for select to authenticated using (true);
drop policy if exists ann_ins on public.announcements; create policy ann_ins on public.announcements for insert to authenticated with check (public.is_staff());
drop policy if exists cm_ins on public.contact_messages; create policy cm_ins on public.contact_messages for insert to anon, authenticated with check (true);
drop policy if exists cm_sel on public.contact_messages; create policy cm_sel on public.contact_messages for select to authenticated using (public.is_staff());
drop policy if exists al_ins on public.audit_log; create policy al_ins on public.audit_log for insert to authenticated with check (public.is_staff());
drop policy if exists al_sel on public.audit_log; create policy al_sel on public.audit_log for select to authenticated using (public.is_staff());
drop policy if exists as_sel on public.app_settings; create policy as_sel on public.app_settings for select to anon, authenticated using (true);

-- realtime for chat
do $$ begin alter publication supabase_realtime add table public.messages; exception when others then null; end $$;

-- storage buckets
insert into storage.buckets (id, name, public) values ('avatars','avatars', true) on conflict (id) do nothing;
insert into storage.buckets (id, name, public) values ('proofs','proofs', false) on conflict (id) do nothing;
drop policy if exists av_read on storage.objects; create policy av_read on storage.objects for select to anon, authenticated using (bucket_id = 'avatars');
drop policy if exists av_write on storage.objects; create policy av_write on storage.objects for insert to authenticated with check (bucket_id = 'avatars' and (storage.foldername(name))[1] = auth.uid()::text);
drop policy if exists av_update on storage.objects; create policy av_update on storage.objects for update to authenticated using (bucket_id = 'avatars' and (storage.foldername(name))[1] = auth.uid()::text);
drop policy if exists pr_write on storage.objects; create policy pr_write on storage.objects for insert to anon, authenticated with check (bucket_id = 'proofs');
drop policy if exists pr_read on storage.objects; create policy pr_read on storage.objects for select to authenticated using (bucket_id = 'proofs' and ((storage.foldername(name))[1] = auth.uid()::text or public.can_verify()));

-- selective reset (admin only)
create or replace function public.admin_reset(targets text[]) returns jsonb language plpgsql security definer set search_path = public as $$
declare out jsonb := '{}'::jsonb; n int; begin
  if not public.is_admin() then raise exception 'admin only'; end if;
  if 'messages' = any(targets) then delete from public.messages where room is not null; get diagnostics n = row_count; out := out || jsonb_build_object('messages', n); delete from public.announcements; end if;
  if 'dms' = any(targets) then delete from public.messages where room is null; get diagnostics n = row_count; out := out || jsonb_build_object('dms', n); end if;
  if 'connections' = any(targets) then delete from public.connections; get diagnostics n = row_count; out := out || jsonb_build_object('connections', n); end if;
  if 'plans' = any(targets) then delete from public.plans; get diagnostics n = row_count; out := out || jsonb_build_object('plans', n); end if;
  if 'attendance' = any(targets) then delete from public.attendance; get diagnostics n = row_count; out := out || jsonb_build_object('attendance', n); end if;
  if 'payments' = any(targets) then delete from public.payments; get diagnostics n = row_count; out := out || jsonb_build_object('payments', n); update public.profiles set is_confirmed = false where role = 'participant'; end if;
  if 'contact' = any(targets) then delete from public.contact_messages; get diagnostics n = row_count; out := out || jsonb_build_object('contact', n); end if;
  if 'audit' = any(targets) then delete from public.audit_log; get diagnostics n = row_count; out := out || jsonb_build_object('audit', n); end if;
  if 'participants' = any(targets) then delete from auth.users where id in (select id from public.profiles where role = 'participant'); get diagnostics n = row_count; out := out || jsonb_build_object('participants', n); end if;
  insert into public.audit_log (actor_id, action, details) values (auth.uid(), 'reset', out); return out; end $$;
