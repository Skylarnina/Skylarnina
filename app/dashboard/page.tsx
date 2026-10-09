"use client";
import { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth";
import { getSupabase } from "@/lib/supabase";
import { SITE, DAYS, feeFor, usd, ngn } from "@/lib/content";
import { Avatar, StatusPill, Spinner, Toast } from "@/components/ui";
import type { Payment } from "@/lib/types";

export default function Dashboard() {
  const { session, profile, loading, refresh } = useAuth(); const router = useRouter();
  const [pays, setPays] = useState<Payment[]>([]); const [att, setAtt] = useState<Record<number, boolean>>({});
  const [name, setName] = useState(""); const [phone, setPhone] = useState(""); const [msg, setMsg] = useState<string | null>(null);
  useEffect(() => { if (!loading && !session) router.replace("/login"); }, [loading, session, router]);
  useEffect(() => { if (profile?.role === "admin") router.replace("/admin"); }, [profile, router]);
  useEffect(() => { const sb = getSupabase(); if (!sb || !session) return; sb.from("payments").select("*").eq("user_id", session.user.id).order("created_at", { ascending: false }).then(({ data }) => setPays((data as Payment[]) ?? []));
    sb.from("attendance").select("day").eq("user_id", session.user.id).then(({ data }) => { const m: Record<number, boolean> = {}; (data ?? []).forEach((r: any) => (m[r.day] = true)); setAtt(m); }); }, [session]);
  useEffect(() => { if (profile) { setName(profile.full_name); setPhone(profile.phone ?? ""); } }, [profile]);
  if (loading || !session || !profile) return <Spinner />;
  const fee = feeFor(profile.status); const reg = pays.filter((p) => p.type === "registration");
  const state = fee === 0 ? "Free" : reg.some((p) => p.status === "approved") ? "Approved" : reg.some((p) => p.status === "pending") ? "Pending" : reg.some((p) => p.status === "rejected") ? "Rejected" : "Unpaid";
  const confirmed = state === "Free" || state === "Approved";
  async function save() { const sb = getSupabase()!; await sb.from("profiles").update({ full_name: name, phone }).eq("id", profile!.id); await refresh(); setMsg("Details saved"); setTimeout(() => setMsg(null), 2000); }
  async function photo(file: File) { const sb = getSupabase()!; const path = `${profile!.id}/avatar-${Date.now()}`; const { error } = await sb.storage.from("avatars").upload(path, file, { upsert: true }); if (error) return setMsg(error.message); const { data } = sb.storage.from("avatars").getPublicUrl(path); await sb.from("profiles").update({ photo_url: data.publicUrl }).eq("id", profile!.id); await refresh(); }

  return (<section className="wrap py-8">
    <div className="card flex flex-wrap items-center gap-5">
      <label className="relative cursor-pointer"><Avatar name={profile.full_name} url={profile.photo_url} size={80} /><input type="file" accept="image/*" className="hidden" onChange={(e) => e.target.files?.[0] && photo(e.target.files[0])} /><span className="absolute -bottom-1 -right-1 h-6 w-6 rounded-full bg-sky text-white grid place-items-center text-xs">✎</span></label>
      <div><h1 className="text-2xl">{profile.full_name}</h1><div className="flex items-center gap-2 mt-1"><span className="pill bg-amber text-ink">{profile.status}</span><span className="text-xs text-muted">Sponsor: {profile.sponsor_name ?? "—"}</span></div>
        <div className="mt-3 flex flex-wrap gap-2"><Link href="/plan" className="btn btn-primary !py-1.5 !text-xs">My Plan</Link><Link href="/community" className="btn btn-outline !py-1.5 !text-xs">Community</Link><Link href="/community?tab=messages" className="btn btn-outline !py-1.5 !text-xs">Messages</Link></div></div>
    </div>
    <div className="mt-8 flex flex-wrap justify-between items-end gap-2"><div><div className="eyebrow">Participant workspace</div><h2 className="text-2xl">Your bootcamp at a glance</h2></div><div className="text-xs text-muted">{profile.status} · {SITE.dates}</div></div>
    <div className="grid gap-4 md:grid-cols-[1fr_1fr_1fr] mt-4">
      <div className={`card ${confirmed ? "bg-azure text-white border-azure" : ""}`}><div className={`text-xs ${confirmed ? "opacity-80" : "text-muted"}`}>YOUR SEAT</div><div className="text-xl font-extrabold mt-1">{confirmed ? "Confirmed" : state === "Pending" ? "Pending verification" : state === "Rejected" ? "Proof rejected" : "Not yet paid"}</div><div className={`text-xs mt-1 ${confirmed ? "opacity-80" : "text-muted"}`}>{confirmed ? "Registration complete" : "Complete your payment below"}</div></div>
      <div className="card"><div className="text-xs text-muted">FEE</div><div className="text-xl font-extrabold text-azure mt-1">{fee ? `${usd(fee)} · ${ngn(fee * SITE.rate)}` : "Free"}</div></div>
      <div className="card"><div className="text-xs text-muted">VENUE</div><div className="font-bold mt-1 text-sm">{SITE.venue}</div></div>
    </div>
    <div className="grid gap-4 lg:grid-cols-[2fr_1fr] mt-4">
      <div className="space-y-4">
        {confirmed ? <div className="card bg-tint border-0"><h3 className="text-base">You&apos;re all set</h3><p className="text-sm text-muted mt-1">Welcome to The Magnificent 5 Days Bootcamp. Come with your laptop or phone, a notebook and an open mind. We start at 10:00 AM sharp each day.</p><a href={SITE.whatsappGroup} target="_blank" rel="noopener" className="btn btn-primary mt-3 !py-1.5 !text-xs">Join the participants WhatsApp group</a></div>
          : <div className="card bg-amber/15 border-amber"><h3 className="text-base">{state === "Pending" ? "Your payment is being verified" : state === "Rejected" ? "Your proof was rejected" : "Complete your payment"}</h3><p className="text-sm text-muted mt-1">{state === "Pending" ? "The team checks every proof by hand, usually within 24 hours. You'll get an email once approved." : state === "Rejected" ? (reg[0]?.rejection_reason ?? "Please upload a clearer proof.") : `Your fee is ${usd(fee)} (${ngn(fee * SITE.rate)}). Pay and upload your proof to be confirmed.`}</p>{state !== "Pending" && <Link href="/register" className="btn btn-primary mt-3 !py-1.5 !text-xs">Open payment page</Link>}</div>}
        <div className="card flex items-center justify-between gap-3"><p className="text-sm text-muted">Donations are optional and help cover the venue and materials.</p><Link href="/donate" className="btn btn-outline !py-1.5 !text-xs">Donate</Link></div>
        <div className="card"><h3 className="text-base">Your payments</h3>{pays.length ? pays.map((p) => <div key={p.id} className="flex flex-wrap items-center justify-between gap-2 border-t border-line py-2.5 mt-2 text-sm"><div><b>{p.type === "registration" ? "Registration fee" : "Donation"} · {p.currency === "NGN" ? ngn(p.amount_claimed) : usd(p.amount_claimed)}</b><div className="text-xs text-muted">{new Date(p.created_at).toLocaleString()} · {p.method}{p.reference ? ` · ref ${p.reference}` : ""}</div>{p.rejection_reason && <div className="text-xs text-red-700">{p.rejection_reason}</div>}</div><StatusPill s={p.status} /></div>) : <p className="text-sm text-muted mt-2">No payments yet.</p>}</div>
        <div className="card"><div className="flex justify-between"><h3 className="text-base">Your attendance</h3><span className="text-xs text-muted">{Object.keys(att).length} of 5 days attended</span></div><div className="grid gap-2 sm:grid-cols-2 mt-3">{DAYS.map((d) => <div key={d.n} className="rounded-xl bg-tint2 border border-line p-3"><div className="font-bold text-sm">Day {d.n} · {d.short}</div><div className="text-xs text-muted">{att[d.n] ? "✓ Attended" : "— Not recorded"}</div></div>)}</div></div>
      </div>
      <div className="space-y-4">
        <div className="card"><h3 className="text-base">Event details</h3><div className="text-sm mt-2"><div className="font-bold">Bootcamp dates</div><div className="text-muted">{SITE.dates}</div></div><div className="text-sm mt-2"><div className="font-bold">Venue</div><div className="text-muted">{SITE.venue}</div></div><Link href="/programme" className="btn btn-outline w-full mt-3 !py-1.5 !text-xs">View programme →</Link></div>
        <div className="card"><h3 className="text-base">Your details</h3><div className="mt-2"><label className="label">Full name</label><input className="input" value={name} onChange={(e) => setName(e.target.value)} /></div><div className="mt-2"><label className="label">Phone</label><input className="input" value={phone} onChange={(e) => setPhone(e.target.value)} /></div><div className="mt-2 text-xs text-muted">Sponsor: {profile.sponsor_name ?? "—"} · ED: {profile.emerald_director ?? "—"}</div><button onClick={save} className="btn btn-primary mt-3 !py-1.5 !text-xs">Save details</button></div>
        <div className="card text-sm"><p className="text-muted">Need help with your registration or payment?</p><Link href="/contact" className="btn btn-outline w-full mt-3 !py-1.5 !text-xs">Contact the team</Link></div>
      </div>
    </div><Toast msg={msg} />
  </section>);
}
