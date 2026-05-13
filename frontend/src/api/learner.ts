import { type LearnerProfile, LearnerProfileSchema } from "./auth";
import { apiFetch } from "./client";

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
