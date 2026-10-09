"use client";
import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { getSupabase, hasBackend } from "@/lib/supabase";
import { Hosts } from "@/components/Logos";
export default function Login() {
  const router = useRouter();
  const [email, setEmail] = useState(""); const [pw, setPw] = useState(""); const [err, setErr] = useState<string | null>(null); const [mode, setMode] = useState<"login" | "reset">("login"); const [ok, setOk] = useState(false);
  async function go(e: React.FormEvent) { e.preventDefault(); const sb = getSupabase(); if (!sb) return setErr("Login is not connected yet.");
    if (mode === "reset") { const { error } = await sb.auth.resetPasswordForEmail(email, { redirectTo: `${location.origin}/login` }); setErr(error?.message ?? null); setOk(!error); return; }
    const { error } = await sb.auth.signInWithPassword({ email, password: pw }); if (error) return setErr(error.message);
    const { data: u } = await sb.auth.getUser(); const { data: p } = await sb.from("profiles").select("role").eq("id", u.user!.id).maybeSingle();
    router.push(p?.role === "admin" ? "/admin" : "/dashboard"); }
  return (<section className="wrap py-14 max-w-md"><Hosts />
    <h1 className="text-3xl mt-6">{mode === "login" ? "Log in" : "Reset your password"}</h1>
    {!hasBackend() && <div className="mt-4 rounded-xl bg-amber/20 border border-amber p-3 text-sm">Preview mode: the database is not connected yet.</div>}
    <form onSubmit={go} className="card mt-5 space-y-3">
      <div><label className="label">Email</label><input className="input" type="email" required value={email} onChange={(e) => setEmail(e.target.value)} /></div>
      {mode === "login" && <div><label className="label">Password</label><input className="input" type="password" required value={pw} onChange={(e) => setPw(e.target.value)} /></div>}
      {err && <p className="text-sm text-red-700">{err}</p>}{ok && <p className="text-sm text-green-700">Check your email for the reset link.</p>}
      <button className="btn btn-primary w-full">{mode === "login" ? "Log in" : "Send reset link"}</button>
      <div className="flex justify-between text-xs font-semibold text-azure"><button type="button" onClick={() => setMode(mode === "login" ? "reset" : "login")}>{mode === "login" ? "Forgot password?" : "Back to log in"}</button><Link href="/register">Create an account</Link></div>
    </form></section>);
}
