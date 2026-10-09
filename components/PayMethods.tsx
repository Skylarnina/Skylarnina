"use client";
import { useState } from "react";
import { PAY_METHODS, SITE, usd, ngn } from "@/lib/content";
export default function PayMethods({ method, setMethod, amountUsd }: { method: string; setMethod: (k: string) => void; amountUsd: number }) {
  const [copied, setCopied] = useState<string | null>(null);
  const m = PAY_METHODS.find((x) => x.key === method);
  const copy = (v: string) => { navigator.clipboard?.writeText(v).catch(() => {}); setCopied(v); setTimeout(() => setCopied(null), 1200); };
  return (<div>
    <label className="label">Choose how you paid</label>
    <div className="grid grid-cols-2 gap-2">{PAY_METHODS.map((x) => <button key={x.key} type="button" onClick={() => setMethod(x.key)} className={`rounded-xl border-2 p-3 text-left ${method === x.key ? "border-sky bg-tint" : "border-line"}`}><div className="font-bold text-sm text-azure">{x.name}</div><div className="text-xs text-muted">{x.sub}</div></button>)}</div>
    {m && <div className="mt-3 rounded-xl bg-tint2 border border-line p-4">
      <div className="text-xs font-bold text-muted mb-2">Send your payment to</div>
      {m.rows.map(([k, v]) => <div key={k} className="flex items-center justify-between py-2 border-b border-line last:border-0"><div><div className="text-[10px] uppercase tracking-wider text-muted">{k}</div><div className="font-bold text-sm">{v}</div></div><button type="button" onClick={() => copy(v)} className="rounded-lg border border-line bg-white px-2.5 py-1 text-xs font-bold text-azure">{copied === v ? "Copied" : "Copy"}</button></div>)}
      <div className="mt-3 rounded-lg bg-white border border-line p-3 text-sm"><b>Amount due: {usd(amountUsd)} · {ngn(amountUsd * SITE.rate)}</b>{m.cur === "NGN" && <div className="text-xs text-muted mt-0.5">Naira amount = {usd(amountUsd)} × {SITE.rate.toLocaleString()} = {ngn(amountUsd * SITE.rate)}</div>}</div>
    </div>}
  </div>);
}
