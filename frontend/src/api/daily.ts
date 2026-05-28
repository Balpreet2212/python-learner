import { z } from "zod";
import { apiFetch } from "./client";
import { SubmitResultSchema, type SubmitResult } from "./content";

export const DailyChallengeSchema = z.object({
  challenge_index: z.number().int(),
  date_key: z.string(),
  title: z.string(),
  description: z.string(),
  code_starter: z.string(),
  hints: z.array(z.string()),
  xp: z.number().int(),
  difficulty: z.string(),
  test_count: z.number().int(),
  already_passed: z.boolean(),
});
export type DailyChallenge = z.infer<typeof DailyChallengeSchema>;

export async function getDailyChallenge(): Promise<DailyChallenge> {
  const raw = await apiFetch<unknown>("/v1/daily/challenge");
  return DailyChallengeSchema.parse(raw);
}

export async function submitDaily(code: string): Promise<SubmitResult> {
  const raw = await apiFetch<unknown>("/v1/daily/submit", {
    method: "POST",
    body: JSON.stringify({ code }),
  });
  return SubmitResultSchema.parse(raw);
}
