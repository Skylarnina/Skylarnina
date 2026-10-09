import Link from "next/link";
import { TRAINERS } from "@/lib/content";
import { PageHero, Avatar } from "@/components/ui";
export const metadata = { title: "Trainers · The Magnificent 5 Days Bootcamp" };
export default function Trainers() {
  return (<>
    <PageHero eyebrow="Trainers" title="The people teaching you" sub="Practitioners, not theorists." />
    <section className="wrap py-14 max-w-4xl"><div className="grid gap-5 sm:grid-cols-2 md:grid-cols-3">{TRAINERS.map((t) => <div key={t.name} className="card"><div className="h-32 rounded-xl bg-tint grid place-items-center"><Avatar name={t.name.replace("Mr ", "")} size={84} /></div><h3 className="mt-3 text-base">{t.name}</h3><div className="text-xs font-bold text-sky">{t.role}</div><p className="text-sm text-muted mt-1">{t.bio}</p></div>)}</div>
      <Link href="/register" className="btn btn-primary mt-8">Register now</Link></section>
  </>);
}
