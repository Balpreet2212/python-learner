import { z } from "zod";
import { apiFetch } from "./client";

// ── Zod schemas (validate at the API boundary) ────────────────────────────

export const AccountSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  role: z.enum(["learner", "parent"]),
  display_name: z.string().nullable(),
  email_verified: z.boolean(),
  is_active: z.boolean(),
  is_under_13: z.boolean(),
});
export type Account = z.infer<typeof AccountSchema>;

export const LearnerProfileSchema = z.object({
  track: z.string(),
  world: z.string(),
  current_unit: z.number().int(),
  current_lesson: z.number().int(),
  badges: z.array(z.string()),
  public_profile: z.boolean(),
});
export type LearnerProfile = z.infer<typeof LearnerProfileSchema>;

export const AuthResponseSchema = z.object({
  account: AccountSchema,
  csrf_token: z.string(),
  profile: LearnerProfileSchema.nullable().optional(),
});
export type AuthResponse = z.infer<typeof AuthResponseSchema>;

// ── API functions ─────────────────────────────────────────────────────────

export interface SignupParams {
  email: string;
  password: string;
  role: "learner" | "parent";
  display_name?: string | undefined;
  is_under_13?: boolean | undefined;
  parent_email?: string | undefined;
}

export async function signup(params: SignupParams): Promise<{ status: string }> {
  return apiFetch<{ status: string }>("/v1/auth/signup", {
    method: "POST",
    body: JSON.stringify(params),
  });
}

export async function login(
  email: string,
  password: string,
): Promise<AuthResponse> {
  const raw = await apiFetch<unknown>("/v1/auth/login", {
    method: "POST",
    body: JSON.stringify({ email, password }),
  });
  return AuthResponseSchema.parse(raw);
}

export async function logout(): Promise<void> {
  await apiFetch<undefined>("/v1/auth/logout", { method: "POST" });
}

export async function verifyEmail(token: string): Promise<{ status: string }> {
  return apiFetch<{ status: string }>("/v1/auth/verify-email", {
    method: "POST",
    body: JSON.stringify({ token }),
  });
}

export async function parentVerify(
  token: string,
): Promise<{ status: string }> {
  return apiFetch<{ status: string }>("/v1/auth/parent-verify", {
    method: "POST",
    body: JSON.stringify({ token }),
  });
}

export async function getMe(): Promise<AuthResponse> {
  const raw = await apiFetch<unknown>("/v1/me");
  return AuthResponseSchema.parse(raw);
}
