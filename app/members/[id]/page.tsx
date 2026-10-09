"use client";
import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth";
import { getSupabase } from "@/lib/supabase";
import { Avatar, Spinner } from "@/components/ui";
import type { Profile } from "@/lib/types";
export default function Member() {
  const { id } = useParams<{ id: string }>(); const { session, loading } = useAuth(); const router = useRouter();
  const [p, setP] = useState<Profile | null>(null); const [done, setDone] = useState(false);
  useEffect(() => { if (!loading && !session) router.replace("/login"); }, [loading, session, router]);
  useEffect(() => { const sb = getSupabase(); if (!sb || !id) return; sb.from("profiles").select("*").eq("id", id).maybeSingle().then(({ data }) => setP((data as Profile) ?? null)); }, [id]);
  if (loading || !session) return <Spinner />; if (!p) return <div className="wrap py-20 text-center text-muted">Member not found.</div>;
  async function connect() { await getSupabase()!.from("connections").insert({ requester_id: session!.user.id, addressee_id: p!.id }); setDone(true); }
  return (<section className="wrap py-10 max-w-2xl"><div className="card flex flex-wrap items-center gap-5"><Avatar name={p.full_name} url={p.photo_url} size={96} /><div className="flex-1"><h1 className="text-2xl">{p.full_name}</h1><span className="pill bg-amber text-ink">{p.status}</span><div className="text-sm text-muted mt-2">{p.skill ? `Learning: ${p.skill}` : "Skill not set"} · Emerald Director: {p.emerald_director ?? "—"}</div>{p.bio && <p className="text-sm mt-3">{p.bio}</p>}</div>{p.id !== session.user.id && <button onClick={connect} disabled={done} className="btn btn-primary">{done ? "Request sent" : "Connect"}</button>}</div></section>);
}
