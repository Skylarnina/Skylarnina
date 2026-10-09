"use client";
import { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { STATUSES, LEADERS, SITE, PAY_METHODS, feeFor, usd, ngn, StatusKey } from "@/lib/content";
import { getSupabase, hasBackend } from "@/lib/supabase";
import { useAuth } from "@/lib/auth";
import { Hosts } from "@/components/Logos";
import { Toast } from "@/components/ui";
import PayMethods from "@/components/PayMethods";

const ED_FALLBACK = "__ed";
type Form = { status: StatusKey | ""; full_name: string; phone: string; email: string; password: string; sponsor: string; sm: string; em: string; dir: string; ed: string };
const EMPTY: Form = { status: "", full_name: "", phone: "+234", email: "", password: "", sponsor: "", sm: "", em: "", dir: "", ed: "" };

export default function Register() {
  const router = useRouter();
  const { session, profile, refresh } = useAuth();
  const [step, setStep] = useState(1);
  const [f, setF] = useState<Form>(EMPTY);
  const [photo, setPhoto] = useState<File | null>(null);
  const [method, setMethod] = useState(""); const [paid, setPaid] = useState(""); const [ref, setRef] = useState(""); const [proof, setProof] = useState<File | null>(null);
  const [msg, setMsg] = useState<string | null>(null); const [busy, setBusy] = useState(false);
  const toast = (m: string) => { setMsg(m); setTimeout(() => setMsg(null), 3500); };
  useEffect(() => { try { const s = localStorage.getItem("reg"); if (s) { const o = JSON.parse(s); setF({ ...EMPTY, ...o.f, password: "" }); if (o.step) setStep(Math.min(o.step, 3)); } } catch {} }, []);
  useEffect(() => { try { localStorage.setItem("reg", JSON.stringify({ f: { ...f, password: "" }, step })); } catch {} }, [f, step]);
  useEffect(() => { if (session && profile && step < 4) { setF((x) => ({ ...x, status: profile.status as StatusKey, full_name: profile.full_name, email: profile.email })); setStep(feeFor(profile.status) ? 4 : 5); } }, [session, profile]); // eslint-disable-line

  const fee = feeFor(f.status); const s = f.status;
  const needSM = ["Member", "Pro", "Distributor", "Manager"].includes(s), needEM = needSM || s === "Senior Manager", needDir = s === "Executive Manager", needED = s !== "Emerald Director" && s !== "";
  const opts = (st: string) => LEADERS.filter((l) => l.status === st).map((l) => <option key={l.name}>{l.name}</option>);
  const res = (v: string) => (v === ED_FALLBACK ? `${f.ed} (Emerald Director)` : v || null);

  async function createAccount() {
    if (!f.full_name.trim() || !f.email.includes("@") || f.password.length < 8) return toast("Fill in your name, a valid email and a password of 8+ characters");
    if (needED && !f.ed) return toast("Choose your Emerald Director");
    if (needSM && !f.sm) return toast("Choose your Senior Manager or the Emerald Director option");
    if (needEM && !f.em) return toast("Choose your Executive Manager or the Emerald Director option");
    if (needDir && !f.dir) return toast("Choose your Director or the Emerald Director option");
    const sb = getSupabase(); if (!sb) { toast("Registration backend is not connected yet."); return; }
    setBusy(true);
    const meta = { full_name: f.full_name, phone: f.phone, status: f.status, sponsor_name: f.sponsor || null, senior_manager: needSM ? res(f.sm) : null, executive_manager: needEM ? res(f.em) : null, director: needDir ? res(f.dir) : null, emerald_director: f.ed || null };
    let uid = session?.user.id;
    if (!uid) {
      const { data, error } = await sb.auth.signUp({ email: f.email, password: f.password, options: { data: meta } });
      if (error) { setBusy(false); return toast(error.message); }
      uid = data.user?.id; if (!data.session) { setBusy(false); setStep(fee ? 4 : 5); toast("Check your email to confirm your account, then log in to finish."); return; }
    }
    if (uid) { await sb.from("profiles").update(meta).eq("id", uid); if (photo) { const path = `${uid}/avatar-${Date.now()}`; const { error } = await sb.storage.from("avatars").upload(path, photo, { upsert: true }); if (!error) { const { data } = sb.storage.from("avatars").getPublicUrl(path); await sb.from("profiles").update({ photo_url: data.publicUrl }).eq("id", uid); } } }
    await refresh(); setBusy(false); setStep(fee ? 4 : 5);
  }
  async function submitPayment() {
    if (!method) return toast("Choose how you paid"); if (!proof) return toast("Upload your proof of payment");
    const sb = getSupabase(); const uid = session?.user.id; if (!sb || !uid) return toast("Please log in first");
    setBusy(true); const m = PAY_METHODS.find((x) => x.key === method)!;
    const path = `${uid}/${Date.now()}-${proof.name}`; const up = await sb.storage.from("proofs").upload(path, proof);
    const { error } = await sb.from("payments").insert({ user_id: uid, type: "registration", method, currency: m.cur, amount_claimed: Number(paid.replace(/[^\d.]/g, "")) || (m.cur === "NGN" ? fee * SITE.rate : fee), amount_due_usd: fee, reference: ref || null, proof_url: up.error ? null : path });
    setBusy(false); if (error) return toast(error.message); setStep(5);
  }
  const Step = ({ n, t }: { n: number; t: string }) => <span className={`text-xs font-bold ${step >= n ? "text-azure" : "text-muted"}`}>{t}</span>;

  return (<section className="wrap py-10 max-w-2xl">
    <Hosts />
    <h1 className="text-3xl mt-6">Register for the bootcamp</h1>
    <p className="text-muted text-sm mt-1">Five steps. Your answers save as you go, so you can come back to this page.</p>
    {!hasBackend() && <div className="mt-4 rounded-xl bg-amber/20 border border-amber p-3 text-sm">Preview mode: the database is not connected yet, so accounts and payments will not be saved.</div>}
    <div className="mt-6 flex justify-between"><Step n={1} t="1 Status" /><Step n={2} t="2 Details" /><Step n={3} t="3 Team" /><Step n={4} t="4 Payment" /><Step n={5} t="5 Done" /></div>
    <div className="h-1.5 rounded-full bg-line mt-2 overflow-hidden"><div className="h-full bg-sky transition-all" style={{ width: `${(step / 5) * 100}%` }} /></div>
    <div className="text-xs font-bold text-azure mt-2">Step {step} of 5: {["Your status", "Your details", "Your team", "Payment", "Done"][step - 1]}</div>

    {step === 1 && <div className="card mt-5"><h2 className="text-xl">What is your current status?</h2><p className="text-sm text-muted">Your fee and the team details we ask for depend on this.</p>
      <div className="grid grid-cols-2 gap-3 mt-4">{STATUSES.map((x) => <button key={x.key} onClick={() => setF({ ...f, status: x.key })} className={`rounded-xl border-2 p-3 text-left ${f.status === x.key ? "border-sky bg-tint" : "border-line hover:border-sky/50"}`}><div className="font-bold text-azure">{x.key}</div><div className="text-xs text-muted">{x.blurb}</div><div className="mt-1 text-sm font-extrabold">{x.fee ? `${usd(x.fee)} · ${ngn(x.fee * SITE.rate)}` : <span className="text-green-700">Free</span>}</div></button>)}</div>
      <div className="mt-5 flex justify-end"><button className="btn btn-primary" onClick={() => (f.status ? setStep(2) : toast("Pick your status"))}>Continue</button></div></div>}

    {step === 2 && <div className="card mt-5 space-y-3"><h2 className="text-xl">Your details</h2>
      <div><label className="label">Full name</label><input className="input" value={f.full_name} onChange={(e) => setF({ ...f, full_name: e.target.value })} /></div>
      <div><label className="label">Phone number</label><input className="input" value={f.phone} onChange={(e) => setF({ ...f, phone: e.target.value })} /></div>
      <div><label className="label">Email</label><input className="input" type="email" value={f.email} onChange={(e) => setF({ ...f, email: e.target.value })} disabled={!!session} /></div>
      {!session && <div><label className="label">Choose a password</label><input className="input" type="password" value={f.password} onChange={(e) => setF({ ...f, password: e.target.value })} /></div>}
      <div><label className="label">Profile photo (optional, up to 2MB)</label><input type="file" accept="image/*" className="text-sm" onChange={(e) => setPhoto(e.target.files?.[0] ?? null)} /></div>
      <div className="flex justify-between pt-2"><button className="btn btn-outline" onClick={() => setStep(1)}>Back</button><button className="btn btn-primary" onClick={() => (f.full_name && f.email.includes("@") && (session || f.password.length >= 8) ? setStep(3) : toast("Enter your name, a valid email and a password of 8+ characters"))}>Continue</button></div></div>}

    {step === 3 && <div className="card mt-5 space-y-3"><h2 className="text-xl">Your team</h2><p className="text-sm text-muted">This helps us group participants correctly on the day.</p>
      <div><label className="label">Sponsor {s === "Emerald Director" ? "(optional)" : ""}</label><input className="input" placeholder="Who introduced you to the business" value={f.sponsor} onChange={(e) => setF({ ...f, sponsor: e.target.value })} /></div>
      {needSM && <div><label className="label">Senior Manager (SM)</label><select className="input" value={f.sm} onChange={(e) => setF({ ...f, sm: e.target.value })}><option value="">Select…</option>{opts("Senior Manager")}<option value={ED_FALLBACK}>I don&apos;t have an SM — my Emerald Director is my SM</option></select></div>}
      {needEM && <div><label className="label">Executive Manager (EM)</label><select className="input" value={f.em} onChange={(e) => setF({ ...f, em: e.target.value })}><option value="">Select…</option>{opts("Executive Manager")}<option value={ED_FALLBACK}>I don&apos;t have an EM — my Emerald Director is my EM</option></select></div>}
      {needDir && <div><label className="label">Director</label><select className="input" value={f.dir} onChange={(e) => setF({ ...f, dir: e.target.value })}><option value="">Select…</option>{opts("Director")}<option value={ED_FALLBACK}>I don&apos;t have a Director — my Emerald Director is my Director</option></select></div>}
      {needED && <div><label className="label">Emerald Director</label><select className="input" value={f.ed} onChange={(e) => setF({ ...f, ed: e.target.value })}><option value="">Select…</option>{opts("Emerald Director")}</select><p className="text-xs text-muted mt-1">Required. Your Emerald Director covers any leadership level you don&apos;t have.</p></div>}
      {s === "Emerald Director" && <p className="text-sm text-muted">As an Emerald Director you do not need to list anyone above you.</p>}
      <div className="flex justify-between pt-2"><button className="btn btn-outline" onClick={() => setStep(2)}>Back</button><button className="btn btn-primary" disabled={busy} onClick={createAccount}>{busy ? "Saving…" : "Continue"}</button></div></div>}

    {step === 4 && <div className="card mt-5 space-y-4"><h2 className="text-xl">Pay your registration fee</h2>
      <div className="rounded-xl bg-azure text-white p-4 flex justify-between items-center"><div><div className="text-xs opacity-80">{f.full_name} · {f.status}</div><div className="text-2xl font-extrabold">{usd(fee)}</div></div><div className="text-right"><div className="text-amber font-bold">{ngn(fee * SITE.rate)} in naira</div><div className="text-xs opacity-80">at ₦{SITE.rate.toLocaleString()} to $1</div></div></div>
      <PayMethods method={method} setMethod={(k) => { setMethod(k); const mm = PAY_METHODS.find((x) => x.key === k)!; setPaid(mm.cur === "NGN" ? String(fee * SITE.rate) : String(fee)); }} amountUsd={fee} />
      <div><label className="label">Amount you paid ({PAY_METHODS.find((x) => x.key === method)?.cur ?? "USD"})</label><input className="input" value={paid} onChange={(e) => setPaid(e.target.value)} /><p className="text-xs text-muted mt-1">Pre-filled with the amount due — edit it if you sent a different amount.</p></div>
      <div><label className="label">Reference / transaction ID or a short note (optional)</label><input className="input" value={ref} onChange={(e) => setRef(e.target.value)} /></div>
      <div><label className="label">Proof of payment (image or PDF, up to 5MB)</label><input type="file" accept="image/*,.pdf" className="text-sm" onChange={(e) => setProof(e.target.files?.[0] ?? null)} /></div>
      <button className="btn btn-primary w-full" disabled={busy} onClick={submitPayment}>{busy ? "Submitting…" : "Submit payment for verification"}</button>
      <button className="w-full text-center text-sm font-semibold text-azure" onClick={() => router.push("/dashboard")}>I&apos;ll pay later</button></div>}

    {step === 5 && <div className="card mt-5"><div className="rounded-xl bg-green-50 border border-green-200 p-4 text-sm text-green-900">{fee ? <><b>Thank you — your payment is pending verification.</b> You will get an email once it is approved.</> : <><b>You&apos;re registered.</b> Members and Pros attend free.</>}</div>
      <h2 className="text-xl mt-4">You&apos;re registered</h2><p className="text-sm text-muted mt-1">Your dashboard shows your payment status, the bootcamp information and your My Plan workspace.</p>
      <div className="mt-5 flex gap-2"><Link href="/dashboard" className="btn btn-primary" onClick={() => localStorage.removeItem("reg")}>Open my dashboard</Link><Link href="/" className="btn btn-outline">Back to home</Link></div></div>}
    <Toast msg={msg} />
  </section>);
}
