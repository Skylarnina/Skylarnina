"use client";
import { useState } from "react";
import { PAY_METHODS, SITE, usd, ngn } from "@/lib/content";
import { PageHero, Toast } from "@/components/ui";
import { getSupabase } from "@/lib/supabase";
import { useAuth } from "@/lib/auth";
import PayMethods from "@/components/PayMethods";
export default function Donate() {
  const { session, profile } = useAuth();
  const [amount, setAmount] = useState(20); const [method, setMethod] = useState<string>("");
  const [paid, setPaid] = useState(""); const [ref, setRef] = useState(""); const [name, setName] = useState(""); const [email, setEmail] = useState(""); const [file, setFile] = useState<File | null>(null); const [msg, setMsg] = useState<string | null>(null);
  const m = PAY_METHODS.find((x) => x.key === method);
  async function submit() {
    if (!method) return setMsg("Choose how you paid");
    const sb = getSupabase(); if (!sb) return setMsg("Payments are not connected yet.");
    let proof_url: string | null = null;
    if (file) { const path = `${session?.user.id ?? "guest"}/${Date.now()}-${file.name}`; const { error } = await sb.storage.from("proofs").upload(path, file); if (!error) proof_url = path; }
    const { error } = await sb.from("payments").insert({ user_id: session?.user.id ?? null, type: "donation", method, currency: m!.cur, amount_claimed: Number(paid.replace(/[^\d.]/g, "")) || (m!.cur === "NGN" ? amount * SITE.rate : amount), amount_due_usd: amount, reference: ref || null, proof_url, guest_name: session ? null : name, guest_email: session ? null : email });
    setMsg(error ? "Could not save your donation: " + error.message : "Thank you — your donation is pending verification."); setTimeout(() => setMsg(null), 4000);
  }
  return (<>
    <PageHero eyebrow="Donate" title="Support the Bootcamp" sub="Optional. Every donation goes towards the venue, materials and logistics for participants." />
    <section className="wrap py-12 max-w-2xl">
      <div className="card space-y-4">
        <div><label className="label">Choose an amount (USD)</label><div className="flex flex-wrap gap-2">{[5, 10, 20, 50].map((a) => <button key={a} onClick={() => setAmount(a)} className={`rounded-full px-4 py-1.5 text-sm font-bold border ${amount === a ? "bg-sky text-white border-sky" : "border-line text-azure"}`}>${a}</button>)}<input className="input !w-28" type="number" min={1} value={amount} onChange={(e) => setAmount(Number(e.target.value) || 1)} /></div></div>
        <div className="rounded-xl bg-azure text-white p-4 flex justify-between items-center"><div><div className="text-xs opacity-80">Your donation</div><div className="text-2xl font-extrabold">{usd(amount)}</div></div><div className="text-right"><div className="text-amber font-bold">{ngn(amount * SITE.rate)} in naira</div><div className="text-xs opacity-80">at ₦{SITE.rate.toLocaleString()} to $1</div></div></div>
        <PayMethods method={method} setMethod={(k) => { setMethod(k); const mm = PAY_METHODS.find((x) => x.key === k)!; setPaid(mm.cur === "NGN" ? String(amount * SITE.rate) : String(amount)); }} amountUsd={amount} />
        <div className="grid gap-3 sm:grid-cols-2"><div><label className="label">Amount you sent</label><input className="input" value={paid} onChange={(e) => setPaid(e.target.value)} /></div><div><label className="label">Reference / note (optional)</label><input className="input" value={ref} onChange={(e) => setRef(e.target.value)} /></div></div>
        {!session && <div className="grid gap-3 sm:grid-cols-2"><div><label className="label">Your name</label><input className="input" value={name} onChange={(e) => setName(e.target.value)} /></div><div><label className="label">Email</label><input className="input" value={email} onChange={(e) => setEmail(e.target.value)} /></div></div>}
        {profile && <p className="text-xs text-muted">Donating as {profile.full_name}.</p>}
        <div><label className="label">Proof of payment (image or PDF, up to 5MB)</label><input type="file" accept="image/*,.pdf" onChange={(e) => setFile(e.target.files?.[0] ?? null)} className="text-sm" /></div>
        <button onClick={submit} className="btn btn-amber">Submit donation</button>
      </div>
    </section><Toast msg={msg} />
  </>);
}
