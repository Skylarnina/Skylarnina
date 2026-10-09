"use client";
import { useState } from "react";
import { DAYS, CHALLENGES, SITE } from "@/lib/content";
import { PageHero } from "@/components/ui";
export default function Programme() {
  const [i, setI] = useState(0); const d = DAYS[i];
  return (<>
    <PageHero eyebrow="Programme" title="What happens each day" sub={`${SITE.dates} · ${SITE.time}`} />
    <section className="wrap py-10 max-w-4xl">
      <div className="flex flex-wrap gap-2">{DAYS.map((x, k) => <button key={x.n} onClick={() => setI(k)} className={`rounded-full px-4 py-2 text-sm font-bold ${k === i ? "bg-azure text-white" : "bg-tint text-azure"}`}>Day {x.n}</button>)}</div>
      <div className="card mt-6">
        <h2 className="text-2xl">Day {d.n}: {d.title}</h2><p className="text-muted mt-1">{d.blurb}</p>
        <div className="overflow-x-auto mt-5"><table className="w-full text-sm"><thead className="text-left text-xs uppercase tracking-wider text-muted bg-tint"><tr><th className="px-3 py-2">Time</th><th className="px-3 py-2">Session</th><th className="px-3 py-2">Practical activity</th></tr></thead>
          <tbody>{d.sessions.map((s) => <tr key={s[0]} className="border-t border-line"><td className="px-3 py-2.5 whitespace-nowrap font-semibold">{s[0]}</td><td className="px-3 py-2.5">{s[1]}</td><td className="px-3 py-2.5 text-muted">{s[2]}</td></tr>)}</tbody></table></div>
        <div className="grid gap-4 md:grid-cols-2 mt-5"><div className="rounded-xl bg-tint p-4"><div className="text-xs font-bold text-azure uppercase tracking-wider">What you leave with</div><p className="text-sm mt-1">{d.leave}</p></div><div className="rounded-xl bg-tint p-4"><div className="text-xs font-bold text-azure uppercase tracking-wider">Homework</div><p className="text-sm mt-1">{d.homework}</p></div></div>
      </div>
      <h2 className="text-2xl mt-12">After the bootcamp: the 30-day challenges</h2>
      <div className="grid gap-4 md:grid-cols-2 mt-4">
        <div className="card"><h3 className="text-base">30-day Upwork challenge</h3><ul className="mt-2 space-y-1.5 text-sm text-muted">{CHALLENGES.upwork.map((c) => <li key={c}>• {c}</li>)}</ul></div>
        <div className="card"><h3 className="text-base">30-day Fiverr challenge</h3><ul className="mt-2 space-y-1.5 text-sm text-muted">{CHALLENGES.fiverr.map((c) => <li key={c}>• {c}</li>)}</ul></div>
      </div>
    </section>
  </>);
}
