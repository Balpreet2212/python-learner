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

export const ExampleSchema = z.object({
  code: z.string(),
  explanation: z.string(),
  output: z.string(),
});

export const FinalChallengeSchema = z.object({
  prompt: z.string(),
  code_starter: z.string(),
  hints: z.array(z.string()),
  test_count: z.number().int(),
});

export const LessonSchema = z.object({
  unit: z.number().int(),
  lesson: z.number().int(),
  title: z.string(),
  setup: z.string(),
  example: ExampleSchema,
  code_starter: z.string(),
  hints: z.array(z.string()),
  xp: z.number().int(),
  test_count: z.number().int(),
  total_lessons: z.number().int(),
  final_challenge: FinalChallengeSchema,
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

export async function submitFinalChallenge(code: string): Promise<SubmitResult> {
  const raw = await apiFetch<unknown>("/v1/learner/final/submit", {
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
