export const SITE = {
  name: "The Magnificent 5 Days Bootcamp",
  tagline: "Learn a skill. Win clients. Build a business.",
  dates: "30 November 2026 – 4 December 2026",
  startISO: "2026-11-30T10:00:00+01:00",
  time: "10:00 AM WAT sharp, daily",
  venue: "A large hall in Akure, Ondo State, Nigeria",
  phone: "09031358081",
  phoneIntl: "2349031358081",
  email: "themagnificentnetwork@gmail.com",
  whatsappGroup: "https://chat.whatsapp.com/CsJ4Olj4g3nAGG38sqIsfu?mode=gi_t",
  rate: 1360,
};

export type StatusKey = "Member" | "Pro" | "Distributor" | "Manager" | "Senior Manager" | "Executive Manager" | "Director" | "Emerald Director";
export const STATUSES: { key: StatusKey; blurb: string; fee: number }[] = [
  { key: "Member", blurb: "New to the business", fee: 0 },
  { key: "Pro", blurb: "Active and building", fee: 0 },
  { key: "Distributor", blurb: "Selling and enrolling", fee: 20 },
  { key: "Manager", blurb: "Leading a small team", fee: 40 },
  { key: "Senior Manager", blurb: "Growing several legs", fee: 100 },
  { key: "Executive Manager", blurb: "Leading managers", fee: 150 },
  { key: "Director", blurb: "Leading executive managers", fee: 300 },
  { key: "Emerald Director", blurb: "Top leadership", fee: 300 },
];
export const feeFor = (s?: string | null) => STATUSES.find((x) => x.key === s)?.fee ?? 0;
export const usd = (n: number) => `$${n.toLocaleString()}`;
export const ngn = (n: number) => `₦${n.toLocaleString()}`;

export const LEADERS: { name: string; status: StatusKey }[] = [
  { name: "Saliu Taiwo", status: "Emerald Director" }, { name: "Adebisi Joel", status: "Emerald Director" }, { name: "Saliu Rafiu", status: "Emerald Director" },
  { name: "Oseni Aminat", status: "Executive Manager" }, { name: "Blessing Tobi", status: "Executive Manager" }, { name: "Ojo Odunayo", status: "Executive Manager" }, { name: "Saliu Kehinde", status: "Executive Manager" }, { name: "Adelusi Micheal", status: "Executive Manager" },
  { name: "Adebisi Oluwadamilare", status: "Senior Manager" }, { name: "Christopher Bakare", status: "Senior Manager" }, { name: "Israel Awosoro", status: "Senior Manager" }, { name: "Abdulsalam Taofeek", status: "Senior Manager" }, { name: "Favour Adunola", status: "Senior Manager" },
];

export const PAY_METHODS = [
  { key: "cleva", name: "Cleva (USD)", sub: "Send in US dollars", cur: "USD", rows: [["Cleva tag", "@saliukehinde"], ["Name", "Kehinde Saliu"]] },
  { key: "grey", name: "Grey (USD)", sub: "Send in US dollars", cur: "USD", rows: [["Grey tag", "@saliukehinde"], ["Name", "Kehinde Saliu"]] },
  { key: "raenest", name: "Raenest (USD)", sub: "Send in US dollars", cur: "USD", rows: [["Raenest tag", "@saliukehinde"], ["Name", "Kehinde Saliu"]] },
  { key: "naira", name: "Naira bank transfer (NGN)", sub: "Transfer in Naira", cur: "NGN", rows: [["Bank", "Palmpay"], ["Account name", "Saliu Kehinde"], ["Account number", "9066208990"]] },
] as const;

export const DAYS = [
  { n: 1, title: "Skills Acquisition", short: "Skills Acquisition", blurb: "Discover the in-demand digital skills you can learn and earn from, and pick the one that fits you.", leave: "You leave with a chosen skill and a simple learning plan for the next 30 days.", homework: "Write down your chosen skill and the three free resources you will use this month.",
    sessions: [["10:00 – 10:45", "Opening, vision and bootcamp rules", "Introductions and goal setting"], ["10:45 – 12:15", "The digital skills map: what pays and why", "Skill self-assessment"], ["12:15 – 13:30", "Choosing your skill and free learning paths", "Build your learning plan"], ["13:30 – 15:00", "Practice lab and Q&A", "First hands-on exercise"]] },
  { n: 2, title: "Mastering Upwork", short: "Mastering Upwork", blurb: "Set up a profile that wins trust and learn how to send proposals clients actually reply to.", leave: "You leave with a live Upwork profile and two proposals sent.", homework: "Send five more proposals before Day 3 and note every reply.",
    sessions: [["10:00 – 11:00", "How Upwork really works", "Account creation"], ["11:00 – 12:30", "Profile, title, overview and portfolio", "Write your profile live"], ["12:30 – 14:00", "Proposal writing that converts", "Send two real proposals"], ["14:00 – 15:00", "Pricing, interviews and avoiding scams", "Role-play a client chat"]] },
  { n: 3, title: "Mastering Fiverr", short: "Mastering Fiverr", blurb: "Build gigs that get found, priced right and packaged so buyers choose you.", leave: "You leave with at least one published Fiverr gig.", homework: "Publish a second gig and share both links in the participants group.",
    sessions: [["10:00 – 11:00", "Fiverr vs Upwork: where you fit", "Market research"], ["11:00 – 12:30", "Gig title, tags, images and SEO", "Create your gig"], ["12:30 – 14:00", "Packages, pricing and upsells", "Price your three packages"], ["14:00 – 15:00", "First orders, reviews and buyer requests", "Publish and review together"]] },
  { n: 4, title: "Network Marketing Training", short: "Network Marketing", blurb: "Practical, ethical network marketing: the product, the plan, the people and duplication.", leave: "You leave with a prospect list and a script you are confident using.", homework: "Invite five people from your list using the script you practised.",
    sessions: [["10:00 – 11:15", "Why network marketing works", "Guest session with Mr Bosson"], ["11:15 – 12:45", "Prospecting, inviting and follow-up", "Guest session with Mr Abbey"], ["12:45 – 14:00", "Building and duplicating a team", "Write your prospect list"], ["14:00 – 15:00", "Handling objections", "Live role-play in pairs"]] },
  { n: 5, title: "Scouting, Social Media Pitching and Celebration", short: "Pitching & Celebration", blurb: "Find clients and prospects on social media, pitch clearly, then celebrate the wins together.", leave: "You leave with pitches sent, a content plan and your certificate.", homework: "Run your 7-day content plan and report results in the group.",
    sessions: [["10:00 – 11:15", "Scouting clients and prospects online", "Build a 20-name scouting list"], ["11:15 – 12:45", "Pitching on WhatsApp, Instagram and X", "Send ten real pitches"], ["12:45 – 13:45", "Content that attracts, not chases", "Plan a 7-day content calendar"], ["13:45 – 15:00", "Celebration, certificates and next steps", "Recognition and photos"]] },
];

export const CHALLENGES = {
  upwork: ["Week 1 — Finish your profile, complete skill tests, send 25 proposals.", "Week 2 — Send 25 more proposals, refine your top-performing angle, take one interview.", "Week 3 — Land your first small job, over-deliver and ask for a review.", "Week 4 — Raise your rate, apply to ten better-paid jobs, ask past clients for repeat work."],
  fiverr: ["Week 1 — Publish two gigs with strong images and clear packages.", "Week 2 — Answer ten buyer requests a day and share your gigs daily.", "Week 3 — Deliver your first order early, collect a 5-star review.", "Week 4 — Add an upsell, publish a third gig, aim for Level 1 seller."],
};

export const TRAINERS = [
  { initials: "TS", name: "Mr Taiwo Saliu", role: "Lead Trainer", bio: "Leads the skills acquisition, Upwork and Fiverr training across the bootcamp." },
  { initials: "MB", name: "Mr Bosson", role: "Guest Trainer, Day 4", bio: "Shares practical, ethical network marketing and team-building training." },
  { initials: "MA", name: "Mr Abbey", role: "Guest Trainer, Day 4", bio: "Trains on prospecting conversations, duplication and leadership." },
  { initials: "MR", name: "Mr Raf", role: "Lead Trainer", bio: "Leads the skills acquisition, Upwork and Fiverr training across the bootcamp." },
  { initials: "MJ", name: "Mr Joel", role: "Lead Trainer", bio: "Leads the skills acquisition, Upwork and Fiverr training across the bootcamp." },
];

export const FAQ = [
  ["Do I need a laptop?", "A laptop is best, but a phone with internet works for every session. Create your Gmail, Upwork and Fiverr accounts before Day 2 so no time is lost."],
  ["Is the bootcamp free?", "Members and Pros attend free. Everyone else pays a fee based on their status, from $20 for Distributors to $300 for Directors and Emerald Directors. The fee covers the venue, materials and logistics for all five days."],
  ["How do I pay?", "During registration choose Cleva, Grey, Raenest (all in US dollars) or a Naira bank transfer to the Palmpay account shown. Send the money from your own app, then upload a screenshot or receipt as proof."],
  ["I paid but my status still says pending. What now?", "The verification team checks every proof by hand, usually within 24 hours. Once approved you get an email and your dashboard changes to Confirmed. If it has been longer than a day, message us on WhatsApp with your reference."],
  ["Can I donate even if my status is free?", "Yes. Donations are optional and go towards the venue, materials and logistics. Use the Donate page any time, with any amount."],
  ["Do I get a certificate?", "Everyone who completes all five days receives a certificate of participation at the Day 5 celebration."],
  ["Can I join if I am not part of the team?", "Yes. Anyone who wants a skill they can earn from is welcome. Register as a Member; you attend free."],
];

export const ROOMS = ["General", "Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Upwork", "Fiverr", "Prospecting"];
export const TRACKER_ROWS = ["Proposals sent", "Replies", "Interviews", "Jobs won", "Gigs published", "Orders", "Prospects contacted", "Follow-ups", "Posts published", "Hours learned"];
export const TODO_CATS = ["Skill", "Upwork", "Fiverr", "Prospecting", "Content", "Other"];
