"use client";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useState } from "react";
import { useAuth } from "@/lib/auth";
import { BrandLink } from "./Logos";

const PUBLIC = [["/", "Home"], ["/about", "About"], ["/programme", "Programme"], ["/trainers", "Trainers"], ["/faq", "FAQ"], ["/contact", "Contact"]];
const AUTHED = [["/plan", "My Plan"], ["/community", "Community"]];

export default function Nav() {
  const path = usePathname();
  const router = useRouter();
  const { session, profile, signOut } = useAuth();
  const [open, setOpen] = useState(false);
  const links = session ? [...PUBLIC, ...AUTHED] : PUBLIC;
  const L = ({ href, label }: { href: string; label: string }) => (
    <Link href={href} onClick={() => setOpen(false)} className={`px-3 py-1.5 rounded-full text-sm font-semibold ${path === href ? "bg-tint text-azure" : "text-muted hover:text-azure hover:bg-tint"}`}>{label}</Link>
  );
  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur border-b border-line">
      <div className="wrap flex items-center justify-between gap-4 py-2.5">
        <BrandLink />
        <nav className="hidden lg:flex items-center gap-0.5">{links.map(([h, l]) => <L key={h} href={h} label={l} />)}</nav>
        <div className="hidden lg:flex items-center gap-2">
          <Link href="/donate" className="px-3 py-1.5 rounded-full text-sm font-semibold text-muted hover:text-azure">Donate</Link>
          {session ? (<>
            {profile?.role === "admin" || profile?.role === "committee" ? <Link href="/admin" className="btn btn-outline !py-1.5">Admin</Link> : null}
            <Link href="/dashboard" className="btn btn-primary !py-1.5">Dashboard</Link>
            <button onClick={async () => { await signOut(); router.push("/"); }} className="px-3 py-1.5 rounded-full text-sm font-semibold text-muted hover:text-azure">Log out</button>
          </>) : (<>
            <Link href="/login" className="px-3 py-1.5 rounded-full text-sm font-semibold text-muted hover:text-azure">Log in</Link>
            <Link href="/register" className="btn btn-primary !py-1.5">Register now</Link>
          </>)}
        </div>
        <button className="lg:hidden rounded-xl border border-line px-3 py-1.5 text-sm font-bold text-azure" onClick={() => setOpen(!open)}>Menu</button>
      </div>
      {open && (
        <div className="lg:hidden border-t border-line bg-white px-5 py-3 flex flex-col gap-1">
          {links.map(([h, l]) => <L key={h} href={h} label={l} />)}
          <L href="/donate" label="Donate" />
          {session ? (<><L href="/dashboard" label="Dashboard" />{(profile?.role === "admin" || profile?.role === "committee") && <L href="/admin" label="Admin" />}<button onClick={async () => { await signOut(); setOpen(false); router.push("/"); }} className="text-left px-3 py-1.5 text-sm font-semibold text-muted">Log out</button></>) : (<><L href="/login" label="Log in" /><Link href="/register" onClick={() => setOpen(false)} className="btn btn-primary mt-2">Register now</Link></>)}
        </div>
      )}
    </header>
  );
}
