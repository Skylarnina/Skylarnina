"use client";
import { useState } from "react";
import { SITE } from "@/lib/content";
import { PageHero, Toast } from "@/components/ui";
import { getSupabase } from "@/lib/supabase";
export default function Contact() {
  const [f, setF] = useState({ name: "", email: "", phone: "", subject: "", message: "" });
  const [msg, setMsg] = useState<string | null>(null);
  async function send(e: React.FormEvent) { e.preventDefault(); const sb = getSupabase(); if (sb) { const { error } = await sb.from("contact_messages").insert(f); setMsg(error ? "Could not send. Please use WhatsApp." : "Message sent. We'll reply by email or WhatsApp."); } else setMsg("Message form is not connected yet. Please use WhatsApp."); setTimeout(() => setMsg(null), 3000); if (!msg) setF({ name: "", email: "", phone: "", subject: "", message: "" }); }
  return (<>
    <PageHero eyebrow="Contact" title="Talk to the team" sub="We answer fastest on WhatsApp." />
    <section className="wrap py-14 grid gap-8 md:grid-cols-[.9fr_1.1fr] max-w-5xl">
      <div className="space-y-3">
        <a href={`https://wa.me/${SITE.phoneIntl}`} target="_blank" rel="noopener" className="card block hover:border-sky"><div className="text-xs font-bold text-sky uppercase tracking-wider">WhatsApp</div><div className="font-bold mt-1">Chat with us now</div></a>
        <a href={`tel:${SITE.phone}`} className="card block hover:border-sky"><div className="text-xs font-bold text-sky uppercase tracking-wider">Call</div><div className="font-bold mt-1">{SITE.phone}</div></a>
        <a href={`mailto:${SITE.email}`} className="card block hover:border-sky"><div className="text-xs font-bold text-sky uppercase tracking-wider">Email</div><div className="font-bold mt-1 break-all">{SITE.email}</div></a>
        <a href={SITE.whatsappGroup} target="_blank" rel="noopener" className="btn btn-outline w-full">Join the bootcamp WhatsApp group →</a>
      </div>
      <form onSubmit={send} className="card space-y-3">
        <div><label className="label">Your name</label><input className="input" required value={f.name} onChange={(e) => setF({ ...f, name: e.target.value })} /></div>
        <div><label className="label">Email</label><input className="input" type="email" required value={f.email} onChange={(e) => setF({ ...f, email: e.target.value })} /></div>
        <div><label className="label">Phone (optional)</label><input className="input" value={f.phone} onChange={(e) => setF({ ...f, phone: e.target.value })} /></div>
        <div><label className="label">Subject (optional)</label><input className="input" value={f.subject} onChange={(e) => setF({ ...f, subject: e.target.value })} /></div>
        <div><label className="label">Message</label><textarea className="input min-h-[120px]" required value={f.message} onChange={(e) => setF({ ...f, message: e.target.value })} /></div>
        <button className="btn btn-primary">Send message</button>
      </form>
    </section><Toast msg={msg} />
  </>);
}
