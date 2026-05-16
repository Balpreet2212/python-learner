import { z } from "zod";
import { apiFetch } from "./client";
import { LearnerProfileSchema, type LearnerProfile } from "./auth";

// ── Schemas ───────────────────────────────────────────────────────────────────

export const CapstoneSchema = z.object({
  unit: z.number().int(),
  title: z.string(),
  narrative: z.string(),
  story_beat: z.string(),
  code_starter: z.string(),
  hints: z.array(z.string()),
  xp: z.number().int(),
  test_count: z.number().int(),
  plan_prompts: z.array(z.string()),
});
export type Capstone = z.infer<typeof CapstoneSchema>;

export const LessonSchema = z.object({
  unit: z.number().int(),
  lesson: z.number().int(),
  title: z.string(),
  narrative: z.string(),
  code_starter: z.string(),
  hints: z.array(z.string()),
  xp: z.number().int(),
  test_count: z.number().int(),
  total_lessons: z.number().int(),
});
export type Lesson = z.infer<typeof LessonSchema>;

export const TestResultSchema = z.object({
  passed: z.boolean(),
  message: z.string(),
});

export const SubmitResultSchema = z.object({
  all_passed: z.boolean(),
  exec_error: z.string().nullable(),
  stdout: z.string(),
  tests: z.array(TestResultSchema),
});
export type SubmitResult = z.infer<typeof SubmitResultSchema>;

// ── API functions ─────────────────────────────────────────────────────────────

export async function getLesson(): Promise<Lesson> {
  const raw = await apiFetch<unknown>("/v1/learner/lesson");
  return LessonSchema.parse(raw);
}

export async function submitChallenge(code: string): Promise<SubmitResult> {
  const raw = await apiFetch<unknown>("/v1/learner/challenge/submit", {
    method: "POST",
    body: JSON.stringify({ code }),
  });
  return SubmitResultSchema.parse(raw);
}

export async function advanceLesson(): Promise<LearnerProfile> {
  const raw = await apiFetch<unknown>("/v1/learner/lesson/advance", {
    method: "POST",
  });
  return LearnerProfileSchema.parse(raw);
}

export async function getCapstone(): Promise<Capstone> {
  const raw = await apiFetch<unknown>("/v1/learner/capstone");
  return CapstoneSchema.parse(raw);
}

export async function submitCapstone(code: string): Promise<SubmitResult> {
  const raw = await apiFetch<unknown>("/v1/learner/capstone/submit", {
    method: "POST",
    body: JSON.stringify({ code }),
  });
  return SubmitResultSchema.parse(raw);
}

export async function advanceCapstone(): Promise<LearnerProfile> {
  const raw = await apiFetch<unknown>("/v1/learner/capstone/advance", {
    method: "POST",
  });
  return LearnerProfileSchema.parse(raw);
}
