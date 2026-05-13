import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { postOnboarding } from "../api/learner";
import { ApiError } from "../api/client";
import { useAuth } from "../context/AuthContext";
import Button from "../components/ui/Button";

type Track = "junior" | "core";
type World = "fantasy" | "scifi" | "mystery";
type Step = "track" | "world" | "intro";

const TRACK_OPTIONS: { value: Track; label: string; desc: string }[] = [
  {
    value: "junior",
    label: "Junior Quest",
    desc: "Grades 5–7 · Visual puzzles, story problems, gentle pacing",
  },
  {
    value: "core",
    label: "Core Track",
    desc: "Grades 8–12 · Typed challenges, real syntax, project capstones",
  },
];

const WORLD_OPTIONS: {
  value: World;
  label: string;
  desc: string;
  bg: string;
  surface: string;
  accent: string;
  highlight: string;
  text: string;
  emoji: string;
}[] = [
  {
    value: "fantasy",
    label: "Enchanted Realm",
    desc: "Cast spells with Python. Variables are potions, loops are incantations.",
    bg: "bg-fantasy-bg",
    surface: "bg-fantasy-surface",
    accent: "border-fantasy-accent text-fantasy-accent",
    highlight: "text-fantasy-highlight",
    text: "text-fantasy-text",
    emoji: "🧙",
  },
  {
    value: "scifi",
    label: "Starship Command",
    desc: "Code the ship's AI. Functions are subroutines, lists are cargo manifests.",
    bg: "bg-scifi-bg",
    surface: "bg-scifi-surface",
    accent: "border-scifi-accent text-scifi-accent",
    highlight: "text-scifi-highlight",
    text: "text-scifi-text",
    emoji: "🚀",
  },
  {
    value: "mystery",
    label: "Detective Agency",
    desc: "Crack the case with code. Conditionals are clues, dicts are case files.",
    bg: "bg-mystery-bg",
    surface: "bg-mystery-surface",
    accent: "border-mystery-accent text-mystery-accent",
    highlight: "text-mystery-highlight",
    text: "text-mystery-text",
    emoji: "🔍",
  },
];

const INTRO_CARDS = [
  {
    title: "Your Adventure Awaits",
    body: "Each unit is a chapter in your world's story. Complete lessons to unlock the next chapter.",
    icon: "📖",
  },
  {
    title: "Learn by Doing",
    body: "Every lesson ends with a Python challenge. Read the hint, write your code, run it — instant feedback.",
    icon: "⌨️",
  },
  {
    title: "Earn Badges",
    body: "Finish a unit to earn a badge. Share your profile or keep it private — your choice.",
    icon: "🏅",
  },
];

export default function OnboardingPage() {
  const { setProfile } = useAuth();
  const navigate = useNavigate();
  const [step, setStep] = useState<Step>("track");
  const [track, setTrack] = useState<Track | null>(null);
  const [world, setWorld] = useState<World | null>(null);
  const [introCard, setIntroCard] = useState(0);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleWorldConfirm() {
    if (!track || !world) return;
    setSaving(true);
    setError(null);
    try {
      const profile = await postOnboarding(track, world);
      setProfile(profile);
      setStep("intro");
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Something went wrong. Please try again.");
    } finally {
      setSaving(false);
    }
  }

  function handleIntroNext() {
    if (introCard < INTRO_CARDS.length - 1) {
      setIntroCard((c) => c + 1);
    } else {
      navigate("/");
    }
  }

  const selectedWorld = WORLD_OPTIONS.find((w) => w.value === world);

  // ── Step: track ────────────────────────────────────────────────────────
  if (step === "track") {
    return (
      <main className="flex min-h-screen flex-col items-center justify-center bg-gray-950 p-6">
        <div className="w-full max-w-lg space-y-8">
          <div className="text-center">
            <h1 className="text-4xl font-bold text-white">Welcome to PyQuest</h1>
            <p className="mt-2 text-gray-400">Choose your learning path</p>
          </div>

          <div className="space-y-4">
            {TRACK_OPTIONS.map((opt) => (
              <button
                key={opt.value}
                onClick={() => setTrack(opt.value)}
                className={`w-full rounded-xl border-2 p-5 text-left transition-all ${
                  track === opt.value
                    ? "border-indigo-500 bg-indigo-950"
                    : "border-gray-700 bg-gray-900 hover:border-gray-500"
                }`}
              >
                <p className="text-lg font-semibold text-white">{opt.label}</p>
                <p className="mt-1 text-sm text-gray-400">{opt.desc}</p>
              </button>
            ))}
          </div>

          <Button
            onClick={() => setStep("world")}
            disabled={!track}
            className="w-full"
          >
            Continue
          </Button>
        </div>
      </main>
    );
  }

  // ── Step: world ────────────────────────────────────────────────────────
  if (step === "world") {
    return (
      <main className="flex min-h-screen flex-col items-center justify-center bg-gray-950 p-6">
        <div className="w-full max-w-lg space-y-8">
          <div className="text-center">
            <h1 className="text-3xl font-bold text-white">Choose Your World</h1>
            <p className="mt-2 text-gray-400">
              Same Python skills — different story. You can switch worlds later.
            </p>
          </div>

          <div className="space-y-4">
            {WORLD_OPTIONS.map((opt) => (
              <button
                key={opt.value}
                onClick={() => setWorld(opt.value)}
                className={`w-full rounded-xl border-2 p-5 text-left transition-all ${
                  world === opt.value
                    ? `${opt.surface} border-2 ${opt.accent}`
                    : "border-gray-700 bg-gray-900 hover:border-gray-500"
                }`}
              >
                <span className="text-2xl">{opt.emoji}</span>
                <p className={`mt-1 text-lg font-semibold ${world === opt.value ? opt.highlight : "text-white"}`}>
                  {opt.label}
                </p>
                <p className={`mt-1 text-sm ${world === opt.value ? opt.text : "text-gray-400"}`}>
                  {opt.desc}
                </p>
              </button>
            ))}
          </div>

          {error && <p className="text-center text-sm text-red-400">{error}</p>}

          <div className="flex gap-3">
            <Button variant="ghost" onClick={() => setStep("track")} className="flex-1">
              Back
            </Button>
            <Button
              onClick={() => void handleWorldConfirm()}
              disabled={!world}
              loading={saving}
              className="flex-1"
            >
              Enter {selectedWorld?.label ?? "World"}
            </Button>
          </div>
        </div>
      </main>
    );
  }

  // ── Step: intro cards ──────────────────────────────────────────────────
  const card = INTRO_CARDS[introCard];
  const worldStyle = selectedWorld;
  return (
    <main
      className={`flex min-h-screen flex-col items-center justify-center p-6 ${worldStyle?.bg ?? "bg-gray-950"}`}
    >
      <div className="w-full max-w-sm space-y-8 text-center">
        <div className="flex justify-center gap-2">
          {INTRO_CARDS.map((_, i) => (
            <span
              key={i}
              className={`h-2 w-2 rounded-full transition-all ${
                i === introCard
                  ? (worldStyle?.accent.split(" ")[0] ?? "bg-indigo-500").replace("border-", "bg-")
                  : "bg-gray-700"
              }`}
            />
          ))}
        </div>

        <div className={`rounded-2xl p-8 ${worldStyle?.surface ?? "bg-gray-900"}`}>
          <div className="text-6xl">{card.icon}</div>
          <h2 className={`mt-4 text-2xl font-bold ${worldStyle?.highlight ?? "text-white"}`}>
            {card.title}
          </h2>
          <p className={`mt-3 text-base ${worldStyle?.text ?? "text-gray-300"}`}>{card.body}</p>
        </div>

        <Button onClick={handleIntroNext} className="w-full">
          {introCard < INTRO_CARDS.length - 1 ? "Next" : "Start Your Quest"}
        </Button>
      </div>
    </main>
  );
}
