"use client";
import { useEffect, useState } from "react";
import { SITE } from "@/lib/content";
export function PageHero({ eyebrow, title, sub }: { eyebrow: string; title: string; sub?: string }) {
  return <section className="hero text-white"><div className="wrap py-14 text-center"><div className="eyebrow !text-white/80">{eyebrow}</div><h1 className="!text-white text-4xl md:text-5xl mt-2">{title}</h1>{sub && <p className="mt-3 text-white/90 max-w-2xl mx-auto">{sub}</p>}</div></section>;
}
export function Check({ children }: { children: React.ReactNode }) {
  return <li className="flex gap-2.5 text-sm"><span className="mt-0.5 h-5 w-5 flex-none rounded-full bg-tint text-azure grid place-items-center text-xs font-black">✓</span><span>{children}</span></li>;
}
export function Countdown() {
  const [t, setT] = useState<number[]>([0, 0, 0, 0]);
  useEffect(() => { const tick = () => { const ms = Math.max(0, new Date(SITE.startISO).getTime() - Date.now()); const s = Math.floor(ms / 1000); setT([Math.floor(s / 86400), Math.floor((s % 86400) / 3600), Math.floor((s % 3600) / 60), s % 60]); }; tick(); const i = setInterval(tick, 1000); return () => clearInterval(i); }, []);
  return <div className="flex justify-center gap-3">{["Days", "Hours", "Minutes", "Seconds"].map((l, i) => <div key={l} className="card !p-3 min-w-[78px] text-center"><div className="text-3xl font-extrabold text-azure tabular-nums">{String(t[i]).padStart(2, "0")}</div><div className="text-[10px] tracking-[.15em] uppercase text-muted">{l}</div></div>)}</div>;
}
export function StatusPill({ s }: { s: string }) {
  const map: Record<string, string> = { approved: "bg-green-100 text-green-800", confirmed: "bg-green-100 text-green-800", pending: "bg-amber/30 text-yellow-900", rejected: "bg-red-100 text-red-800", free: "bg-green-100 text-green-800", unpaid: "bg-gray-100 text-gray-700" };
  return <span className={`pill ${map[s.toLowerCase()] ?? "bg-tint text-azure"}`}>{s}</span>;
}
export function Avatar({ name, url, size = 48 }: { name?: string | null; url?: string | null; size?: number }) {
  const ini = (name || "?").split(" ").map((x) => x[0]).join("").slice(0, 2).toUpperCase();
  return url ? <img src={url} alt="" style={{ width: size, height: size }} className="rounded-full object-cover flex-none" /> : <div style={{ width: size, height: size, fontSize: size / 2.6 }} className="rounded-full bg-azure text-white grid place-items-center font-extrabold flex-none">{ini}</div>;
}
export function Toast({ msg }: { msg: string | null }) { return msg ? <div className="fixed bottom-5 left-1/2 -translate-x-1/2 z-50 rounded-full bg-azure text-white px-5 py-2.5 text-sm font-semibold shadow-lift">{msg}</div> : null; }
export function Spinner() { return <div className="wrap py-24 text-center text-muted">Loading…</div>; }
