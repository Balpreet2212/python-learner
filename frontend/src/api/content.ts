import { z } from "zod";
import { apiFetch } from "./client";
import { LearnerProfileSchema, type LearnerProfile } from "./auth";

// ── Exercise schemas ───────────────────────────────────────────────────────────

const storyBeats = {
  story_before: z.string().nullable().optional(),
  story_after: z.string().nullable().optional(),
};

export const ConceptExSchema = z.object({
  type: z.literal("concept"),
  code: z.string(),
  output: z.string(),
  explanation: z.string(),
  ...storyBeats,
});

export const McqExSchema = z.object({
  type: z.literal("mcq"),
  question: z.string(),
  code: z.string(),
  choices: z.array(z.string()),
  correct: z.string(),
  explanation: z.string(),
  ...storyBeats,
});

export const ArrangeExSchema = z.object({
  type: z.literal("arrange"),
  instruction: z.string(),
  blocks: z.array(z.string()),
  correct: z.array(z.string()),
  explanation: z.string(),
  ...storyBeats,
});

export const FillBlankExSchema = z.object({
  type: z.literal("fill_blank"),
  prompt: z.string(),
  before: z.string(),
  after: z.string(),
  choices: z.array(z.string()),
  answer: z.string(),
  explanation: z.string(),
  ...storyBeats,
});

const SolutionSchema = z.object({
  code: z.string(),
  note: z.string(),
});
export type Solution = z.infer<typeof SolutionSchema>;

export const MiniCodeExSchema = z.object({
  type: z.literal("mini_code"),
  prompt: z.string(),
  starter: z.string(),
  test_count: z.number().int(),
  solutions: z.array(SolutionSchema).default([]),
  ...storyBeats,
});

export const BreakFixExSchema = z.object({
  type: z.literal("break_fix"),
  prompt: z.string(),
  broken_code: z.string(),
  hint: z.string(),
  test_count: z.number().int(),
  explanation: z.string(),
  ...storyBeats,
});

export const ExerciseSchema = z.discriminatedUnion("type", [
  ConceptExSchema,
  McqExSchema,
  ArrangeExSchema,
  FillBlankExSchema,
  MiniCodeExSchema,
  BreakFixExSchema,
]);

export type ConceptEx = z.infer<typeof ConceptExSchema>;
export type McqEx = z.infer<typeof McqExSchema>;
export type ArrangeEx = z.infer<typeof ArrangeExSchema>;
export type FillBlankEx = z.infer<typeof FillBlankExSchema>;
export type MiniCodeEx = z.infer<typeof MiniCodeExSchema>;
export type BreakFixEx = z.infer<typeof BreakFixExSchema>;
export type Exercise = z.infer<typeof ExerciseSchema>;

export const LessonSchema = z.object({
  unit: z.number().int(),
  lesson: z.number().int(),
  title: z.string(),
  xp: z.number().int(),
  total_lessons: z.number().int(),
  exercise_count: z.number().int(),
  exercises: z.array(ExerciseSchema),
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

// ── API functions ─────────────────────────────────────────────────────────────

export async function getLesson(): Promise<Lesson> {
  const raw = await apiFetch<unknown>("/v1/learner/lesson");
  return LessonSchema.parse(raw);
}

export async function getPracticeLesson(unit: number, lesson: number): Promise<Lesson> {
  const raw = await apiFetch<unknown>(`/v1/learner/lesson/practice?unit=${unit}&lesson=${lesson}`);
  return LessonSchema.parse(raw);
}

export async function checkExerciseCode(code: string, exerciseIndex: number): Promise<SubmitResult> {
  const raw = await apiFetch<unknown>("/v1/learner/exercise/code", {
    method: "POST",
    body: JSON.stringify({ code, exercise_index: exerciseIndex }),
  });
  return SubmitResultSchema.parse(raw);
}

export async function checkPracticeExerciseCode(
  code: string,
  exerciseIndex: number,
  unit: number,
  lesson: number,
): Promise<SubmitResult> {
  const raw = await apiFetch<unknown>("/v1/learner/exercise/code/practice", {
    method: "POST",
    body: JSON.stringify({ code, exercise_index: exerciseIndex, unit, lesson }),
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
