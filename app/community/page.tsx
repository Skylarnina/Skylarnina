"use client";
import { Suspense, useEffect, useRef, useState } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { useAuth } from "@/lib/auth";
import { getSupabase } from "@/lib/supabase";
import { ROOMS, STATUSES } from "@/lib/content";
import { Avatar, Spinner } from "@/components/ui";
import type { Profile } from "@/lib/types";

type Msg = { id: string; room: string | null; sender_id: string; recipient_id: string | null; body: string; created_at: string; profiles?: Partial<Profile> };
const TABS = [["rooms", "# Chat rooms"], ["messages", "💬 Messages"], ["members", "👥 Members"], ["connections", "🤝 Connections"]];

function CommunityInner() {
  const { session, profile, loading } = useAuth(); const router = useRouter(); const params = useSearchParams();
  const [tab, setTab] = useState(params.get("tab") ?? "rooms"); const [room, setRoom] = useState("General");
  const [msgs, setMsgs] = useState<Msg[]>([]); const [text, setText] = useState(""); const [members, setMembers] = useState<Profile[]>([]); const [q, setQ] = useState(""); const [fs, setFs] = useState("");
  const [conns, setConns] = useState<any[]>([]); const [dmWith, setDmWith] = useState<Profile | null>(null); const [pinned, setPinned] = useState<string | null>(null);
  const end = useRef<HTMLDivElement>(null);
  useEffect(() => { if (!loading && !session) router.replace("/login"); }, [loading, session, router]);
  const sb = getSupabase();
  async function loadRoom() { if (!sb) return; const { data } = await sb.from("messages").select("*, profiles:sender_id(full_name,photo_url,status)").eq("room", room).order("created_at").limit(200); setMsgs((data as Msg[]) ?? []); const { data: a } = await sb.from("announcements").select("body").order("created_at", { ascending: false }).limit(1); setPinned(a?.[0]?.body ?? null); }
  async function loadDm() { if (!sb || !session || !dmWith) return; const { data } = await sb.from("messages").select("*, profiles:sender_id(full_name,photo_url,status)").is("room", null).or(`and(sender_id.eq.${session.user.id},recipient_id.eq.${dmWith.id}),and(sender_id.eq.${dmWith.id},recipient_id.eq.${session.user.id})`).order("created_at").limit(200); setMsgs((data as Msg[]) ?? []); }
  useEffect(() => { if (!sb || !session) return; if (tab === "rooms") loadRoom(); if (tab === "messages" && dmWith) loadDm();
    const ch = sb.channel("msgs").on("postgres_changes", { event: "INSERT", schema: "public", table: "messages" }, () => { tab === "rooms" ? loadRoom() : loadDm(); }).subscribe(); return () => { sb.removeChannel(ch); }; }, [tab, room, dmWith, session]); // eslint-disable-line
  useEffect(() => { if (!sb || !session) return; sb.from("profiles").select("*").neq("role", "admin").order("full_name").then(({ data }) => setMembers((data as Profile[]) ?? []));
    sb.from("connections").select("*, a:requester_id(id,full_name,photo_url,status), b:addressee_id(id,full_name,photo_url,status)").or(`requester_id.eq.${session.user.id},addressee_id.eq.${session.user.id}`).then(({ data }) => setConns(data ?? [])); }, [session, tab]); // eslint-disable-line
  useEffect(() => { end.current?.scrollIntoView({ block: "end" }); }, [msgs]);
  if (loading || !session || !profile) return <Spinner />;
  async function send() { if (!text.trim() || !sb) return; await sb.from("messages").insert({ sender_id: session!.user.id, room: tab === "rooms" ? room : null, recipient_id: tab === "rooms" ? null : dmWith?.id, body: text.trim() }); setText(""); tab === "rooms" ? loadRoom() : loadDm(); }
  async function connect(id: string) { await sb!.from("connections").insert({ requester_id: session!.user.id, addressee_id: id }); setTab("connections"); }
  async function respond(cid: string, status: string) { await sb!.from("connections").update({ status }).eq("id", cid); const { data } = await sb!.from("connections").select("*, a:requester_id(id,full_name,photo_url,status), b:addressee_id(id,full_name,photo_url,status)").or(`requester_id.eq.${session!.user.id},addressee_id.eq.${session!.user.id}`); setConns(data ?? []); }
  const accepted = conns.filter((c) => c.status === "accepted").map((c) => (c.requester_id === session.user.id ? c.b : c.a));
  const filtered = members.filter((m) => (!q || m.full_name.toLowerCase().includes(q.toLowerCase())) && (!fs || m.status === fs));

  const Chat = () => (<div className="flex-1 flex flex-col min-h-[480px]">
    {tab === "rooms" && pinned && <div className="bg-amber/20 border-b border-amber/40 px-4 py-2 text-xs"><b>📌 Bootcamp Team:</b> {pinned}</div>}
    <div className="flex-1 overflow-y-auto p-4 space-y-3">{msgs.length ? msgs.map((m) => <div key={m.id} className={`flex gap-2.5 ${m.sender_id === session.user.id ? "flex-row-reverse" : ""}`}><Avatar name={m.profiles?.full_name} url={m.profiles?.photo_url} size={32} /><div className={`max-w-[75%] rounded-2xl px-3.5 py-2 text-sm ${m.sender_id === session.user.id ? "bg-sky text-white" : "bg-tint"}`}><div className={`text-[11px] font-bold ${m.sender_id === session.user.id ? "text-white/80" : "text-azure"}`}>{m.profiles?.full_name} · {m.profiles?.status}</div>{m.body}<div className={`text-[10px] mt-0.5 ${m.sender_id === session.user.id ? "text-white/70" : "text-muted"}`}>{new Date(m.created_at).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}</div></div></div>) : <p className="text-center text-sm text-muted py-10">No messages yet. Say hello 👋</p>}<div ref={end} /></div>
    <div className="border-t border-line p-3 flex gap-2"><input className="input" placeholder="Message the room… use @name to mention" value={text} onChange={(e) => setText(e.target.value)} onKeyDown={(e) => e.key === "Enter" && send()} /><button onClick={send} className="btn btn-primary">Send</button></div></div>);

  return (<section className="wrap py-8">
    <h1 className="text-3xl">Community</h1>
    <div className="mt-3 flex flex-wrap gap-2">{TABS.map(([k, l]) => <button key={k} onClick={() => setTab(k)} className={`rounded-full px-4 py-1.5 text-sm font-bold ${tab === k ? "bg-sky text-white" : "bg-tint text-azure"}`}>{l}</button>)}</div>

    {tab === "rooms" && <div className="card !p-0 mt-5 grid md:grid-cols-[200px_1fr] overflow-hidden"><aside className="border-r border-line p-2 bg-tint2"><div className="flex md:flex-col gap-1 overflow-x-auto">{ROOMS.map((r) => <button key={r} onClick={() => setRoom(r)} className={`text-left rounded-lg px-3 py-2 text-sm font-semibold whitespace-nowrap ${room === r ? "bg-sky text-white" : "text-ink hover:bg-tint"}`}># {r}</button>)}</div><p className="text-[11px] text-muted mt-3 px-3 hidden md:block">Your team room appears once teams are assigned.</p></aside><Chat /></div>}

    {tab === "messages" && <div className="card !p-0 mt-5 grid md:grid-cols-[240px_1fr] overflow-hidden min-h-[480px]"><aside className="border-r border-line p-2 bg-tint2"><div className="text-xs font-bold text-muted px-2 py-1">Your connections</div>{accepted.length ? accepted.map((p: any) => <button key={p.id} onClick={() => setDmWith(p)} className={`w-full flex items-center gap-2 rounded-lg px-2 py-2 text-sm text-left ${dmWith?.id === p.id ? "bg-sky text-white" : "hover:bg-tint"}`}><Avatar name={p.full_name} url={p.photo_url} size={28} />{p.full_name}</button>) : <p className="text-xs text-muted p-2">Connect with members to start a private chat.</p>}</aside>{dmWith ? <Chat /> : <div className="grid place-items-center text-sm text-muted">Pick a connection to chat.</div>}</div>}

    {tab === "members" && <div className="mt-5"><div className="flex flex-wrap gap-2"><input className="input !w-64" placeholder="Search by name" value={q} onChange={(e) => setQ(e.target.value)} /><select className="input !w-48" value={fs} onChange={(e) => setFs(e.target.value)}><option value="">All statuses</option>{STATUSES.map((s) => <option key={s.key}>{s.key}</option>)}</select></div>
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3 mt-4">{filtered.map((m) => <Link key={m.id} href={`/members/${m.id}`} className="card !p-3 flex items-center gap-3 hover:border-sky"><Avatar name={m.full_name} url={m.photo_url} size={44} /><div className="min-w-0"><div className="font-bold text-sm truncate">{m.full_name}</div><span className="pill bg-amber text-ink">{m.status}</span><div className="text-[11px] text-muted mt-0.5 truncate">{m.skill ? `Skill: ${m.skill}` : "Skill not set"} · ED: {m.emerald_director ?? "—"}</div></div></Link>)}</div></div>}

    {tab === "connections" && <div className="mt-5 grid gap-4 md:grid-cols-2">
      <div className="card"><h3 className="text-base">Requests</h3>{conns.filter((c) => c.status === "pending" && c.addressee_id === session.user.id).map((c) => <div key={c.id} className="flex items-center gap-3 py-2 border-t border-line"><Avatar name={c.a.full_name} url={c.a.photo_url} size={36} /><div className="flex-1 text-sm font-bold">{c.a.full_name}</div><button onClick={() => respond(c.id, "accepted")} className="btn btn-primary !py-1 !text-xs">Accept</button><button onClick={() => respond(c.id, "ignored")} className="btn btn-outline !py-1 !text-xs">Ignore</button></div>)}{!conns.some((c) => c.status === "pending" && c.addressee_id === session.user.id) && <p className="text-sm text-muted mt-2">No pending requests.</p>}</div>
      <div className="card"><h3 className="text-base">Connected</h3>{accepted.map((p: any) => <div key={p.id} className="flex items-center gap-3 py-2 border-t border-line"><Avatar name={p.full_name} url={p.photo_url} size={36} /><div className="flex-1 text-sm font-bold">{p.full_name}</div><button onClick={() => { setDmWith(p); setTab("messages"); }} className="btn btn-outline !py-1 !text-xs">Message</button></div>)}{!accepted.length && <p className="text-sm text-muted mt-2">No connections yet. Find people in Members and tap Connect.</p>}</div>
      <div className="card md:col-span-2"><h3 className="text-base">Find members to connect with</h3><div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3 mt-3">{members.filter((m) => m.id !== session.user.id && !conns.some((c) => c.requester_id === m.id || c.addressee_id === m.id)).slice(0, 12).map((m) => <div key={m.id} className="flex items-center gap-2 rounded-xl border border-line p-2"><Avatar name={m.full_name} url={m.photo_url} size={32} /><div className="flex-1 text-sm font-bold truncate">{m.full_name}</div><button onClick={() => connect(m.id)} className="btn btn-primary !py-1 !text-xs">Connect</button></div>)}</div></div>
    </div>}
  </section>);
}

export default function Community() { return <Suspense fallback={<Spinner />}><CommunityInner /></Suspense>; }
