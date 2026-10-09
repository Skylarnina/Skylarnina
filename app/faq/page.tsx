import Link from "next/link";
import { FAQ, SITE } from "@/lib/content";
import { PageHero } from "@/components/ui";
export const metadata = { title: "FAQ · The Magnificent 5 Days Bootcamp" };
export default function Faq() {
  return (<>
    <PageHero eyebrow="FAQ" title="Questions people ask us" />
    <section className="wrap py-14 max-w-3xl">
      {FAQ.map(([q, a]) => <details key={q} className="card mb-3 group"><summary className="cursor-pointer font-bold text-azure flex justify-between items-center">{q}<span className="text-muted group-open:rotate-180 transition">⌄</span></summary><p className="text-sm text-muted mt-3">{a}</p></details>)}
      <div className="card bg-tint border-0 mt-8 flex flex-wrap items-center justify-between gap-3"><div><h3 className="text-lg">Still have a question?</h3><p className="text-sm text-muted">We answer fastest on WhatsApp.</p></div><div className="flex gap-2"><a href={`https://wa.me/${SITE.phoneIntl}`} target="_blank" rel="noopener" className="btn btn-primary">Chat on WhatsApp</a><Link href="/contact" className="btn btn-outline">Contact page</Link></div></div>
    </section>
  </>);
}
