export type Profile = {
  id: string; full_name: string; email: string; phone: string | null; photo_url: string | null;
  status: string; sponsor_name: string | null; senior_manager: string | null; executive_manager: string | null; director: string | null; emerald_director: string | null;
  role: "participant" | "committee" | "admin"; can_verify_payments: boolean; is_confirmed: boolean; bio: string | null; skill: string | null; created_at: string;
};
export type Payment = {
  id: string; user_id: string; type: "registration" | "donation"; method: string; currency: "USD" | "NGN"; amount_claimed: number; amount_due_usd: number;
  reference: string | null; proof_url: string | null; status: "pending" | "approved" | "rejected"; approved_amount_usd: number | null; rejection_reason: string | null; created_at: string;
  profiles?: Partial<Profile>;
};
