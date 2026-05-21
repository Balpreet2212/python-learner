import { z } from "zod";
import { apiFetch } from "./client";

export const LearnerSummarySchema = z.object({
  id: z.string().uuid(),
  display_name: z.string().nullable(),
  email: z.string(),
  track: z.string(),
  world: z.string(),
  current_unit: z.number().int(),
  current_lesson: z.number().int(),
  badges: z.array(z.string()),
  total_units: z.number().int(),
  total_lessons_per_unit: z.number().int(),
});

export type LearnerSummary = z.infer<typeof LearnerSummarySchema>;

export const LearnerDetailSchema = z.object({
  id: z.string().uuid(),
  display_name: z.string().nullable(),
  email: z.string(),
  streak_days: z.number().int(),
  last_active: z.string().nullable(),
  lessons_this_week: z.number().int(),
  sparkline_30d: z.array(z.number().int()),
});

export type LearnerDetail = z.infer<typeof LearnerDetailSchema>;

export async function getLinkedLearners(): Promise<LearnerSummary[]> {
  const data = await apiFetch<unknown[]>("/v1/parent/learners");
  return z.array(LearnerSummarySchema).parse(data);
}

export async function getLearnerDetail(learnerId: string): Promise<LearnerDetail> {
  const data = await apiFetch<unknown>(`/v1/parent/learners/${learnerId}/detail`);
  return LearnerDetailSchema.parse(data);
}

export async function linkLearner(email: string): Promise<{ status: string }> {
  return apiFetch<{ status: string }>("/v1/parent/link", {
    method: "POST",
    body: JSON.stringify({ email }),
  });
}
