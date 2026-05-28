import { z } from "zod";
import { type LearnerProfile, LearnerProfileSchema } from "./auth";
import { apiFetch } from "./client";

export const LearnerStatsSchema = z.object({
  daily_done_today: z.boolean(),
  weekly_done_this_week: z.boolean(),
  daily_total: z.number().int(),
  weekly_total: z.number().int(),
});
export type LearnerStats = z.infer<typeof LearnerStatsSchema>;

export async function getLearnerStats(): Promise<LearnerStats> {
  const raw = await apiFetch<unknown>("/v1/learner/stats");
  return LearnerStatsSchema.parse(raw);
}

export async function resetProgress(): Promise<LearnerProfile> {
  const raw = await apiFetch<unknown>("/v1/learner/reset-progress", {
    method: "POST",
    body: JSON.stringify({}),
  });
  return LearnerProfileSchema.parse(raw);
}

export async function postOnboarding(
  track: "junior" | "core",
  world: "fantasy" | "scifi" | "mystery",
): Promise<LearnerProfile> {
  const raw = await apiFetch<unknown>("/v1/learner/onboarding", {
    method: "POST",
    body: JSON.stringify({ track, world }),
  });
  return LearnerProfileSchema.parse(raw);
}
