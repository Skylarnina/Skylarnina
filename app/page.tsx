import Link from "next/link";
import { SITE, DAYS, STATUSES, TRAINERS, usd, ngn } from "@/lib/content";
import { Hosts } from "@/components/Logos";
import { Check, Countdown, Avatar } from "@/components/ui";
import SafeImg from "@/components/SafeImg";

export default function Home() {
  return (<>
    <section className="hero text-white relative overflow-hidden">
      <div className="absolute inset-0 pattern opacity-10" />
      <div className="wrap relative py-14 md:py-20 grid gap-10 md:grid-cols-[1.1fr_.9fr] items-center">
        <div>
          <Hosts light />
          <span className="inline-block mt-6 rounded-full bg-amber text-ink text-xs font-bold px-3 py-1">{SITE.dates} · {SITE.time}</span>
          <h1 className="!text-white text-4xl md:text-6xl mt-4 leading-[1.02]">The Magnificent 5 Days Bootcamp</h1>
          <p className="mt-4 text-lg text-white/90 max-w-xl">{SITE.tagline} Five days of hands-on training that ends with you having real profiles, real pitches and a real plan.</p>
          <ul className="mt-5 space-y-1.5 text-sm text-white/90"><li>📅 {SITE.dates} — {SITE.time}</li><li>📍 {SITE.venue}</li></ul>
          <div className="mt-7 flex flex-wrap gap-3"><Link href="/register" className="btn btn-white">Register now →</Link><Link href="/about" className="btn border-2 border-white/60 text-white hover:bg-white/10">Learn more</Link></div>
        </div>
        <SafeImg src="/img/hero.jpg" alt="Participants in training" className="rounded-2xl shadow-lift w-full" />
      </div>
    </section>
    <section className="bg-tint2 border-b border-line"><div className="wrap py-7 flex flex-col items-center gap-3"><span className="eyebrow">Hosted by</span><Hosts size="lg" /></div></section>

    <section className="wrap py-14 text-center">
      <h2 className="text-3xl">Counting down to Day 1</h2>
      <p className="text-muted text-sm mt-1 mb-6">{SITE.dates} · {SITE.venue}</p>
      <Countdown />
    </section>

    <section className="bg-tint2"><div className="wrap py-14">
      <h2 className="text-3xl">The five days at a glance</h2><p className="text-muted mt-1">Every day is practical. You do the work in the room, with help beside you.</p>
      <div className="grid gap-4 md:grid-cols-3 mt-8">
        {DAYS.map((d) => <div key={d.n} className="card"><span className="h-8 w-8 rounded-full bg-sky text-white grid place-items-center font-extrabold text-sm">{d.n}</span><h3 className="mt-3 text-lg">{d.title}</h3><p className="text-sm text-muted mt-1">{d.blurb}</p><p className="text-sm mt-3 flex gap-2"><span className="text-azure">✓</span>{d.leave}</p></div>)}
        <div className="card bg-azure text-white border-azure"><h3 className="!text-white text-lg">Want the full timetable?</h3><p className="text-sm text-white/85 mt-1">Sessions, durations, activities and the 30-day challenges are all on the programme page.</p><Link href="/programme" className="btn btn-white mt-4">See the programme</Link></div>
      </div>
    </div></section>

    <section className="wrap py-14 grid gap-10 md:grid-cols-2">
      <div><h2 className="text-2xl">Who it is for</h2><ul className="mt-4 space-y-2.5">
        <Check>Anyone who wants a skill they can earn from, starting from zero</Check><Check>Students and graduates tired of waiting for a job</Check><Check>Members of the team who want to grow their business the right way</Check><Check>Leaders who want their team trained in one place</Check><Check>Anyone already freelancing but not yet getting clients</Check></ul></div>
      <div><h2 className="text-2xl">What you gain</h2><ul className="mt-4 space-y-2.5">
        <Check>A digital skill you can start earning with</Check><Check>A live Upwork profile and a published Fiverr gig</Check><Check>Proven scripts for prospecting, inviting and pitching</Check><Check>Practical network marketing training from experienced leaders</Check><Check>A community that keeps you accountable after the five days</Check><Check>A certificate of participation</Check></ul></div>
    </section>

    <section className="bg-tint2"><div className="wrap py-14">
      <h2 className="text-3xl">Registration fees</h2><p className="text-muted mt-1">Your fee depends on your current status. It covers the venue, materials and logistics for all five days.</p>
      <div className="card mt-6 overflow-x-auto !p-0"><table className="w-full text-sm"><thead className="bg-tint text-left text-xs uppercase tracking-wider text-muted"><tr><th className="px-4 py-3">Status</th><th className="px-4 py-3">Fee (USD)</th><th className="px-4 py-3">Fee (Naira)</th></tr></thead>
        <tbody>{STATUSES.map((s) => <tr key={s.key} className="border-t border-line"><td className="px-4 py-3 font-bold">{s.key}</td><td className="px-4 py-3">{s.fee ? usd(s.fee) : "Free"}</td><td className="px-4 py-3">{s.fee ? ngn(s.fee * SITE.rate) : "—"}</td></tr>)}</tbody></table></div>
      <p className="text-xs text-muted mt-3">Members and Pros attend free — a donation is welcome but never required. Naira amounts are converted at 1 USD = ₦{SITE.rate.toLocaleString()}.</p>
    </div></section>

    <section className="wrap py-14">
      <h2 className="text-3xl">Your trainers</h2>
      <div className="grid gap-4 sm:grid-cols-2 md:grid-cols-3 mt-6">{TRAINERS.map((t) => <div key={t.name} className="card"><div className="h-28 rounded-xl bg-tint grid place-items-center"><Avatar name={t.name.replace("Mr ", "")} size={72} /></div><h3 className="mt-3 text-base">{t.name}</h3><div className="text-xs font-bold text-sky">{t.role}</div><p className="text-sm text-muted mt-1">{t.bio}</p></div>)}</div>
    </section>

    <section className="bg-tint2"><div className="wrap py-14 text-center"><h2 className="text-3xl">What participants say</h2><div className="card max-w-xl mx-auto mt-6"><div className="text-5xl text-sky font-serif">“</div><p className="text-muted">The first stories land here right after Day 5. Your voice could be one of them.</p></div></div></section>

    <section className="wrap py-14"><div className="hero rounded-3xl text-white p-10 text-center"><h2 className="!text-white text-3xl">Your seat is one form away</h2><p className="mt-2 text-white/90 max-w-xl mx-auto">Register, pay if your status requires it, upload your proof and you are confirmed.</p><div className="mt-6 flex flex-wrap justify-center gap-3"><Link href="/register" className="btn btn-white">Register now →</Link><a href={`https://wa.me/${SITE.phoneIntl}`} target="_blank" rel="noopener" className="btn border-2 border-white/60 text-white hover:bg-white/10">Ask a question on WhatsApp</a></div></div></section>
  </>);
}
