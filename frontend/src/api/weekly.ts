import { z } from "zod";
import { apiFetch } from "./client";
import { SubmitResultSchema, type SubmitResult } from "./content";

export const WeeklyChallengeSchema = z.object({
  challenge_index: z.number().int(),
  week_key: z.string(),
  title: z.string(),
  description: z.string(),
  code_starter: z.string(),
  hints: z.array(z.string()),
  xp: z.number().int(),
  difficulty: z.string(),
  test_count: z.number().int(),
  already_passed: z.boolean(),
});
export type WeeklyChallenge = z.infer<typeof WeeklyChallengeSchema>;

export async function getWeeklyChallenge(): Promise<WeeklyChallenge> {
  const raw = await apiFetch<unknown>("/v1/weekly/challenge");
  return WeeklyChallengeSchema.parse(raw);
}

export async function submitWeekly(code: string): Promise<SubmitResult> {
  const raw = await apiFetch<unknown>("/v1/weekly/submit", {
    method: "POST",
    body: JSON.stringify({ code }),
  });
  return SubmitResultSchema.parse(raw);
}
