import Link from "next/link";
import { SITE } from "@/lib/content";
import { Hosts } from "@/components/Logos";
import { PageHero, Check } from "@/components/ui";
export const metadata = { title: "About · The Magnificent 5 Days Bootcamp" };
export default function About() {
  return (<>
    <PageHero eyebrow="About" title="Five days that change how you earn" sub="Not a seminar. A working room where you build, publish and pitch before you leave." />
    <section className="wrap py-14 max-w-3xl">
      <p>The Magnificent 5 Days Bootcamp exists for one reason: too many capable people have time, data and ambition, but no clear path to their first income online. We close that gap in five days, in one room, with trainers who have done the work.</p>
      <p className="mt-4">Day by day you pick a digital skill, set up and pitch on Upwork, publish on Fiverr, learn honest network marketing from experienced leaders, then take your first real scouting and social-media pitches. You finish with profiles that exist, messages that are sent, and a plan for the next 30 days.</p>
      <div className="card bg-tint border-0 mt-8"><h3 className="text-lg">When and where</h3><p className="text-sm text-muted mt-1">{SITE.dates} · {SITE.time}<br />{SITE.venue}</p></div>
      <div className="grid gap-8 md:grid-cols-2 mt-10">
        <div><h3 className="text-lg">Who it is for</h3><ul className="mt-3 space-y-2"><Check>Anyone who wants a skill they can earn from, starting from zero</Check><Check>Students and graduates tired of waiting for a job</Check><Check>Members of the team who want to grow their business the right way</Check><Check>Leaders who want their team trained in one place</Check><Check>Anyone already freelancing but not yet getting clients</Check></ul></div>
        <div><h3 className="text-lg">What you leave with</h3><ul className="mt-3 space-y-2"><Check>A digital skill you can start earning with</Check><Check>A live Upwork profile and a published Fiverr gig</Check><Check>Proven scripts for prospecting, inviting and pitching</Check><Check>Practical network marketing training from experienced leaders</Check><Check>A community that keeps you accountable after the five days</Check><Check>A certificate of participation</Check></ul></div>
      </div>
      <div className="card mt-10"><h3 className="text-lg">Hosted by</h3><div className="mt-3"><Hosts /></div><p className="text-sm text-muted mt-3">The Magnificent leads the training and the community. Goal Getters sponsors and supports the bootcamp.</p></div>
      <Link href="/register" className="btn btn-primary mt-8">Register now</Link>
    </section>
  </>);
}
