import { z } from "zod";
import { apiFetch } from "./client";

export const BillingStatusSchema = z.object({
  status: z.string(),
  has_full_access: z.boolean(),
  trial_ends_at: z.string().nullable().optional(),
  current_period_end: z.string().nullable().optional(),
});
export type BillingStatus = z.infer<typeof BillingStatusSchema>;

export async function getBillingStatus(): Promise<BillingStatus> {
  const raw = await apiFetch<unknown>("/v1/billing/status");
  return BillingStatusSchema.parse(raw);
}

export async function createCheckoutSession(): Promise<string> {
  const raw = await apiFetch<{ checkout_url: string }>("/v1/billing/checkout", {
    method: "POST",
  });
  return raw.checkout_url;
}

export async function createPortalSession(): Promise<string> {
  const raw = await apiFetch<{ portal_url: string }>("/v1/billing/portal", {
    method: "POST",
  });
  return raw.portal_url;
}
