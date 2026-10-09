"use client";
import { createContext, useContext, useEffect, useState } from "react";
import type { Session } from "@supabase/supabase-js";
import { getSupabase } from "./supabase";
import type { Profile } from "./types";

type Ctx = { session: Session | null; profile: Profile | null; loading: boolean; refresh: () => Promise<void>; signOut: () => Promise<void> };
const AuthCtx = createContext<Ctx>({ session: null, profile: null, loading: true, refresh: async () => {}, signOut: async () => {} });

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [session, setSession] = useState<Session | null>(null);
  const [profile, setProfile] = useState<Profile | null>(null);
  const [loading, setLoading] = useState(true);
  const sb = getSupabase();
  async function loadProfile(s: Session | null) {
    if (!sb || !s) { setProfile(null); return; }
    const { data } = await sb.from("profiles").select("*").eq("id", s.user.id).maybeSingle();
    setProfile((data as Profile) ?? null);
  }
  useEffect(() => {
    if (!sb) { setLoading(false); return; }
    sb.auth.getSession().then(async ({ data }) => { setSession(data.session); await loadProfile(data.session); setLoading(false); });
    const { data: sub } = sb.auth.onAuthStateChange(async (_e, s) => { setSession(s); await loadProfile(s); });
    return () => sub.subscription.unsubscribe();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  return <AuthCtx.Provider value={{ session, profile, loading, refresh: () => loadProfile(session), signOut: async () => { await sb?.auth.signOut(); setProfile(null); } }}>{children}</AuthCtx.Provider>;
}
export const useAuth = () => useContext(AuthCtx);
