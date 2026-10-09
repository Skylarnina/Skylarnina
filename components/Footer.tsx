import Link from "next/link";
import { SITE } from "@/lib/content";
import { Hosts } from "./Logos";
export default function Footer() {
  return (
    <footer className="bg-tint2 border-t border-line mt-16">
      <div className="wrap py-12 grid gap-10 md:grid-cols-[1.4fr_1fr_1fr]">
        <div><Hosts /><p className="mt-4 text-sm text-muted max-w-sm">Five days of practical skills, real client work and honest business training.</p></div>
        <div><h4 className="text-xs tracking-[.15em] uppercase text-muted mb-3">Explore</h4><ul className="space-y-2 text-sm font-semibold text-ink">
          <li><Link href="/about">About the bootcamp</Link></li><li><Link href="/programme">Programme</Link></li><li><Link href="/trainers">Trainers</Link></li><li><Link href="/register">Register</Link></li><li><Link href="/donate">Donate</Link></li><li><Link href="/faq">FAQ</Link></li></ul></div>
        <div><h4 className="text-xs tracking-[.15em] uppercase text-muted mb-3">Contact</h4><ul className="space-y-2 text-sm font-semibold text-ink">
          <li><a href={`tel:${SITE.phone}`}>📞 {SITE.phone}</a></li><li><a href={`mailto:${SITE.email}`}>✉️ {SITE.email}</a></li><li><a href={`https://wa.me/${SITE.phoneIntl}`} target="_blank" rel="noopener">💬 Chat on WhatsApp</a></li><li><a href={SITE.whatsappGroup} target="_blank" rel="noopener">Join the bootcamp WhatsApp group</a></li></ul></div>
      </div>
      <div className="border-t border-line"><div className="wrap py-4 flex flex-wrap justify-between gap-2 text-xs text-muted"><span>Hosted by The Magnificent and Goal Getters.</span><span><Link href="/privacy">Privacy policy</Link> · <Link href="/terms">Terms</Link></span></div></div>
    </footer>
  );
}
