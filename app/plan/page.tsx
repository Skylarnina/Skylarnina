"use client";
import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth";
import { getSupabase } from "@/lib/supabase";
import { DAYS, TRACKER_ROWS, TODO_CATS } from "@/lib/content";
import { Avatar, Spinner } from "@/components/ui";

type Todo = { id: string; title: string; due: string; cat: string; done: boolean };
type Plan = { notes: Record<string, Record<string, string>>; action: Record<string, string>; goals: { t: string; due: string; p: number }[]; todos: Todo[]; tracker: Record<string, number[]> };
const EMPTY: Plan = { notes: {}, action: {}, goals: [{ t: "", due: "", p: 0 }, { t: "", due: "", p: 0 }, { t: "", due: "", p: 0 }], todos: [], tracker: {} };
const TABS = ["Daily notes", "Action plan", "To-do list", "Tracker"];

export default function PlanPage() {
  const { session, profile, loading } = useAuth(); const router = useRouter();
  const [tab, setTab] = useState(0); const [plan, setPlan] = useState<Plan>(EMPTY); const [saved, setSaved] = useState("Everything saves automatically."); const t = useRef<any>(null);
  const [nt, setNt] = useState({ title: "", due: "", cat: "Skill" });
  useEffect(() => { if (!loading && !session) router.replace("/login"); }, [loading, session, router]);
  useEffect(() => { const sb = getSupabase(); if (!sb || !session) return; sb.from("plans").select("data").eq("user_id", session.user.id).maybeSingle().then(({ data }) => { if (data?.data) setPlan({ ...EMPTY, ...(data.data as Plan) }); }); }, [session]);
  function update(p: Plan) { setPlan(p); setSaved("Saving…"); clearTimeout(t.current); t.current = setTimeout(async () => { const sb = getSupabase(); if (sb && session) { await sb.from("plans").upsert({ user_id: session.user.id, data: p, updated_at: new Date().toISOString() }); } setSaved("Saved."); }, 700); }
  if (loading || !session || !profile) return <Spinner />;
  const note = (d: number, k: string) => plan.notes[d]?.[k] ?? "";
  const setNote = (d: number, k: string, v: string) => update({ ...plan, notes: { ...plan.notes, [d]: { ...(plan.notes[d] ?? {}), [k]: v } } });
  const weekTotals = [0, 1, 2, 3].map((w) => TRACKER_ROWS.reduce((a, r) => a + (plan.tracker[r]?.[w] ?? 0), 0));
  const mx = Math.max(1, ...weekTotals);

  return (<section className="wrap py-8 max-w-4xl">
    <div className="card flex items-center gap-4"><Avatar name={profile.full_name} url={profile.photo_url} size={64} /><div><h1 className="text-2xl">{profile.full_name}</h1><span className="pill bg-amber text-ink">{profile.status}</span></div></div>
    <h2 className="text-2xl mt-8">My Plan</h2><p className="text-sm text-muted">Private to you. {saved}</p>
    <div className="mt-4 grid grid-cols-4 rounded-xl bg-tint p-1 text-sm font-bold">{TABS.map((x, i) => <button key={x} onClick={() => setTab(i)} className={`rounded-lg py-2 ${tab === i ? "bg-white text-azure shadow-card" : "text-muted"}`}>{x}</button>)}</div>

    {tab === 0 && <div className="grid gap-4 md:grid-cols-2 mt-5">{DAYS.map((d) => <div key={d.n} className="card"><h3 className="text-base">Day {d.n} · {d.short}</h3>
      {[["learned", "What I learned today"], ["takeaway", "My biggest takeaway"], ["action", "One thing I will do this week"]].map(([k, l]) => <div key={k} className="mt-3"><label className="label">{l}</label><textarea className="input min-h-[70px]" value={note(d.n, k)} onChange={(e) => setNote(d.n, k, e.target.value)} /></div>)}
      <div className="mt-3 rounded-xl bg-tint p-3 text-xs"><b className="text-azure">✦ Build your plan with Magnificent &amp; Goal Getter AI</b><p className="text-muted mt-1">Day {d.n} guidance: {d.leave} Tonight: {d.homework}</p></div></div>)}</div>}

    {tab === 1 && <div className="card mt-5 space-y-3"><h3 className="text-base">30-day action plan</h3>
      {[["skill", "Skill I am learning"], ["hours", "Hours per week"], ["project", "Portfolio project I will finish"], ["platform", "Platform focus (Upwork / Fiverr)"], ["nm", "One network marketing activity per week"], ["content", "One content post per week"]].map(([k, l]) => <div key={k}><label className="label">{l}</label><input className="input" value={plan.action[k] ?? ""} onChange={(e) => update({ ...plan, action: { ...plan.action, [k]: e.target.value } })} /></div>)}
      <h3 className="text-base pt-2">Three measurable goals for Day 30</h3>
      {plan.goals.map((g, i) => <div key={i} className="rounded-xl border border-line p-3 grid gap-2 sm:grid-cols-[1fr_140px]"><input className="input" placeholder={`Goal ${i + 1}`} value={g.t} onChange={(e) => { const gs = [...plan.goals]; gs[i] = { ...g, t: e.target.value }; update({ ...plan, goals: gs }); }} /><input className="input" type="date" value={g.due} onChange={(e) => { const gs = [...plan.goals]; gs[i] = { ...g, due: e.target.value }; update({ ...plan, goals: gs }); }} /><div className="sm:col-span-2 flex items-center gap-3 text-xs text-muted">Progress <input type="range" min={0} max={100} value={g.p} onChange={(e) => { const gs = [...plan.goals]; gs[i] = { ...g, p: Number(e.target.value) }; update({ ...plan, goals: gs }); }} className="flex-1" /><b className="text-azure">{g.p}%</b></div></div>)}</div>}

    {tab === 2 && <div className="card mt-5"><h3 className="text-base">To-do list</h3>
      <div className="grid gap-2 sm:grid-cols-[1fr_150px_140px_auto] mt-3"><input className="input" placeholder="New task" value={nt.title} onChange={(e) => setNt({ ...nt, title: e.target.value })} /><input className="input" type="date" value={nt.due} onChange={(e) => setNt({ ...nt, due: e.target.value })} /><select className="input" value={nt.cat} onChange={(e) => setNt({ ...nt, cat: e.target.value })}>{TODO_CATS.map((c) => <option key={c}>{c}</option>)}</select><button className="btn btn-primary" onClick={() => { if (!nt.title.trim()) return; update({ ...plan, todos: [...plan.todos, { id: String(Date.now()), ...nt, done: false }] }); setNt({ title: "", due: "", cat: "Skill" }); }}>+ Add</button></div>
      <ul className="mt-4 divide-y divide-line">{plan.todos.map((x) => { const over = x.due && !x.done && new Date(x.due) < new Date(); return <li key={x.id} className="flex items-center gap-3 py-2.5 text-sm"><input type="checkbox" checked={x.done} onChange={() => update({ ...plan, todos: plan.todos.map((y) => (y.id === x.id ? { ...y, done: !y.done } : y)) })} /><span className={`flex-1 ${x.done ? "line-through text-muted" : ""}`}>{x.title}</span><span className="pill bg-tint text-azure">{x.cat}</span>{x.due && <span className={`text-xs ${over ? "text-amber font-bold" : "text-muted"}`}>{x.due}</span>}<button className="text-muted text-xs" onClick={() => update({ ...plan, todos: plan.todos.filter((y) => y.id !== x.id) })}>✕</button></li>; })}</ul>
      {!plan.todos.length && <p className="text-sm text-muted mt-3">No tasks yet. Add your first one above.</p>}</div>}

    {tab === 3 && <div className="card mt-5 overflow-x-auto"><h3 className="text-base">Weekly tracker (4 weeks after the bootcamp)</h3>
      <table className="w-full text-sm mt-3"><thead className="text-xs uppercase tracking-wider text-muted"><tr><th className="text-left py-2">After the bootcamp</th>{[1, 2, 3, 4].map((w) => <th key={w} className="py-2">Week {w}</th>)}</tr></thead>
        <tbody>{TRACKER_ROWS.map((r) => <tr key={r} className="border-t border-line"><td className="py-1.5 font-semibold">{r}</td>{[0, 1, 2, 3].map((w) => <td key={w} className="py-1.5 px-1"><input type="number" min={0} className="input !py-1 !px-2 text-center" value={plan.tracker[r]?.[w] ?? ""} onChange={(e) => { const row = [...(plan.tracker[r] ?? [0, 0, 0, 0])]; row[w] = Number(e.target.value) || 0; update({ ...plan, tracker: { ...plan.tracker, [r]: row } }); }} /></td>)}</tr>)}</tbody></table>
      <div className="mt-5"><div className="label">Weekly totals</div><svg viewBox="0 0 400 120" className="w-full max-w-lg"><polyline fill="none" stroke="#FBB71A" strokeWidth="4" strokeLinecap="round" points={weekTotals.map((v, i) => `${30 + i * 110},${100 - (v / mx) * 85}`).join(" ")} />{weekTotals.map((v, i) => <g key={i}><circle cx={30 + i * 110} cy={100 - (v / mx) * 85} r="5" fill="#0075BD" /><text x={30 + i * 110} y="116" fontSize="10" textAnchor="middle" fill="#5B6B7F">W{i + 1} · {v}</text></g>)}</svg></div></div>}
  </section>);
}
