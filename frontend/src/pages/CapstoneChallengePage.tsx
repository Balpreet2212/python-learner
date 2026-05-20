import { useState, useEffect, type KeyboardEvent } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import {
  getCapstone,
  submitCapstone,
  advanceCapstone,
  type Capstone,
  type SubmitResult,
} from "../api/content";
import { ApiError } from "../api/client";
import Button from "../components/ui/Button";

type World = "fantasy" | "scifi" | "mystery";

const WORLD_STYLE: Record<
  World,
  { bg: string; surface: string; accent: string; highlight: string; text: string; muted: string; border: string }
> = {
  fantasy: {
    bg: "bg-fantasy-bg",
    surface: "bg-fantasy-surface",
    accent: "text-fantasy-accent",
    highlight: "text-fantasy-highlight",
    text: "text-fantasy-text",
    muted: "text-fantasy-text/60",
    border: "border-fantasy-accent/40",
  },
  scifi: {
    bg: "bg-scifi-bg",
    surface: "bg-scifi-surface",
    accent: "text-scifi-accent",
    highlight: "text-scifi-highlight",
    text: "text-scifi-text",
    muted: "text-scifi-text/60",
    border: "border-scifi-accent/40",
  },
  mystery: {
    bg: "bg-mystery-bg",
    surface: "bg-mystery-surface",
    accent: "text-mystery-accent",
    highlight: "text-mystery-highlight",
    text: "text-mystery-text",
    muted: "text-mystery-text/60",
    border: "border-mystery-accent/40",
  },
};

function getStyle(world: string) {
  return WORLD_STYLE[(world as World) in WORLD_STYLE ? (world as World) : "fantasy"];
}

// Indices of plan prompts that are required to unlock the editor
const REQUIRED_PLAN_INDICES = [0, 2];

export default function CapstoneChallengePage() {
  const { profile, setProfile } = useAuth();
  const navigate = useNavigate();

  const [capstone, setCapstone] = useState<Capstone | null>(null);
  const [planAnswers, setPlanAnswers] = useState<string[]>([]);
  const [editorUnlocked, setEditorUnlocked] = useState(false);
  const [code, setCode] = useState("");
  const [result, setResult] = useState<SubmitResult | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [advancing, setAdvancing] = useState(false);
  const [hintIndex, setHintIndex] = useState(-1);
  const [error, setError] = useState<string | null>(null);

  const world = profile?.world ?? "fantasy";
  const style = getStyle(world);

  useEffect(() => {
    getCapstone()
      .then((c) => {
        setCapstone(c);
        setPlanAnswers(Array(c.plan_prompts.length).fill(""));
        setCode(c.code_starter);
      })
      .catch((err: unknown) => {
        setError(err instanceof ApiError ? err.message : "Failed to load capstone");
      });
  }, []);

  function handlePlanChange(index: number, value: string) {
    setPlanAnswers((prev) => {
      const next = [...prev];
      next[index] = value;
      return next;
    });
  }

  function canUnlock(): boolean {
    return REQUIRED_PLAN_INDICES.every((i) => planAnswers[i]?.trim().length > 0);
  }

  function handleUnlock() {
    if (canUnlock()) setEditorUnlocked(true);
  }

  function handleCodeChange(value: string) {
    setCode(value);
    if (result) setResult(null);
  }

  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key !== "Tab") return;
    e.preventDefault();
    const el = e.currentTarget;
    const start = el.selectionStart;
    const end = el.selectionEnd;
    const next = code.slice(0, start) + "    " + code.slice(end);
    setCode(next);
    requestAnimationFrame(() => {
      el.selectionStart = el.selectionEnd = start + 4;
    });
  }

  async function handleSubmit() {
    if (!capstone) return;
    setSubmitting(true);
    setError(null);
    try {
      const res = await submitCapstone(code);
      setResult(res);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Submission failed. Try again.");
    } finally {
      setSubmitting(false);
    }
  }

  async function handleAdvance() {
    setAdvancing(true);
    setError(null);
    try {
      const updated = await advanceCapstone();
      setProfile(updated);
      navigate("/");
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Failed to advance. Try again.");
    } finally {
      setAdvancing(false);
    }
  }

  if (!capstone) {
    return (
      <main className={`flex min-h-screen items-center justify-center ${style.bg}`}>
        {error ? (
          <p className="text-red-400">{error}</p>
        ) : (
          <p className={style.muted}>Loading capstone…</p>
        )}
      </main>
    );
  }

  const allPassed = result?.all_passed ?? false;
  const showHint = hintIndex >= 0 && hintIndex < capstone.hints.length;

  return (
    <main className={`min-h-screen ${style.bg}`}>
      <div className="mx-auto max-w-5xl p-6 space-y-6">
        {/* Header */}
        <div className="flex items-start justify-between gap-2">
          <div>
            <span className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>
              Unit {capstone.unit} · Capstone Challenge
            </span>
            <h1 className={`mt-1 text-2xl font-bold ${style.highlight}`}>{capstone.title}</h1>
          </div>
          <span className={`shrink-0 text-sm font-semibold ${style.accent}`}>+{capstone.xp} XP</span>
        </div>

        {/* Narrative */}
        <div className={`rounded-xl border ${style.border} p-5 ${style.surface}`}>
          <p className={`whitespace-pre-line text-sm leading-relaxed ${style.text}`}>
            {capstone.narrative}
          </p>
        </div>

        {/* Plan section */}
        {!editorUnlocked && (
          <div className={`rounded-xl border ${style.border} ${style.surface} overflow-hidden`}>
            <div className={`border-b ${style.border} px-5 py-3`}>
              <h2 className={`text-sm font-semibold ${style.highlight}`}>
                Plan Before You Code
              </h2>
              <p className={`text-xs mt-0.5 ${style.muted}`}>
                Answer the starred questions to unlock the editor.
              </p>
            </div>
            <div className="p-5 space-y-4">
              {capstone.plan_prompts.map((prompt, i) => {
                const required = REQUIRED_PLAN_INDICES.includes(i);
                return (
                  <div key={i} className="space-y-1">
                    <label className={`text-xs font-medium ${style.text}`}>
                      {required && (
                        <span className={`mr-1 ${style.accent}`}>★</span>
                      )}
                      {prompt}
                    </label>
                    <textarea
                      value={planAnswers[i] ?? ""}
                      onChange={(e) => { handlePlanChange(i, e.target.value); }}
                      rows={2}
                      placeholder={required ? "Required…" : "Optional…"}
                      className={`w-full resize-none rounded-lg border ${style.border} bg-gray-950 px-3 py-2 font-mono text-sm text-gray-100 outline-none focus:ring-1 focus:ring-white/20 placeholder:text-gray-600`}
                    />
                  </div>
                );
              })}
              <Button
                onClick={handleUnlock}
                disabled={!canUnlock()}
                className="w-full"
              >
                Unlock Editor →
              </Button>
            </div>
          </div>
        )}

        {/* Code editor + results (shown after plan) */}
        {editorUnlocked && (
          <div className="lg:grid lg:grid-cols-2 gap-6 space-y-6 lg:space-y-0">
            {/* Left: hints */}
            <div className="space-y-4">
              <div className={`rounded-xl border ${style.border} p-4 ${style.surface}`}>
                <p className={`text-xs font-semibold uppercase tracking-wider ${style.muted} mb-2`}>
                  Your Plan
                </p>
                {capstone.plan_prompts.map((prompt, i) =>
                  planAnswers[i]?.trim() ? (
                    <div key={i} className="mb-3">
                      <p className={`text-xs ${style.muted}`}>{prompt}</p>
                      <p className={`text-sm mt-0.5 ${style.text}`}>{planAnswers[i]}</p>
                    </div>
                  ) : null
                )}
              </div>

              {capstone.hints.length > 0 && (
                <div>
                  <button
                    onClick={() => { setHintIndex((i) => (i < capstone.hints.length - 1 ? i + 1 : i)); }}
                    className={`text-sm underline ${style.muted} hover:${style.accent}`}
                  >
                    {hintIndex < 0
                      ? "Show hint"
                      : hintIndex < capstone.hints.length - 1
                        ? "Next hint"
                        : "No more hints"}
                  </button>
                  {showHint && (
                    <div className={`mt-2 rounded-lg border ${style.border} px-4 py-3 ${style.surface}`}>
                      <p className={`font-mono text-sm ${style.text}`}>{capstone.hints[hintIndex]}</p>
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* Right: editor + submit */}
            <div className="space-y-4">
              <div className={`rounded-xl border ${style.border} overflow-hidden`}>
                <div className={`flex items-center justify-between px-4 py-2 ${style.surface} border-b ${style.border}`}>
                  <span className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>
                    Python
                  </span>
                  {result && (
                    <span className={`text-xs font-semibold ${allPassed ? "text-green-400" : "text-red-400"}`}>
                      {allPassed ? "All tests passed ✓" : "Tests failed"}
                    </span>
                  )}
                </div>
                <textarea
                  value={code}
                  onChange={(e) => { handleCodeChange(e.target.value); }}
                  onKeyDown={handleKeyDown}
                  spellCheck={false}
                  rows={14}
                  className="w-full resize-none bg-gray-950 p-4 font-code text-sm leading-relaxed text-gray-100 outline-none"
                />
              </div>

              <Button
                onClick={() => void handleSubmit()}
                loading={submitting}
                disabled={!code.trim()}
                className="w-full"
              >
                Run Code
              </Button>

              {error && <p className="text-center text-sm text-red-400">{error}</p>}

              {result && (
                <div className={`rounded-xl border ${style.border} overflow-hidden`}>
                  {result.stdout && (
                    <div className="border-b border-gray-800 bg-gray-950 px-4 py-3">
                      <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-gray-500">Output</p>
                      <pre className="font-code text-sm text-gray-300 whitespace-pre-wrap">{result.stdout}</pre>
                    </div>
                  )}
                  {result.exec_error && (
                    <div className="border-b border-gray-800 bg-red-950/30 px-4 py-3">
                      <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-red-400">Error</p>
                      <pre className="font-code text-sm text-red-300 whitespace-pre-wrap">{result.exec_error}</pre>
                    </div>
                  )}
                  <div className={`${style.surface} px-4 py-3 space-y-2`}>
                    <p className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>Tests</p>
                    {result.tests.map((t, i) => (
                      <div key={i} className="flex items-start gap-2">
                        <span className={t.passed ? "text-green-400" : "text-red-400"}>
                          {t.passed ? "✓" : "✗"}
                        </span>
                        <span className={`text-sm ${t.passed ? style.text : "text-red-300"}`}>
                          {t.message}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        )}

        {/* Story beat + advance button (after all tests pass) */}
        {allPassed && (
          <div className={`rounded-xl border-2 border-green-500/40 p-6 ${style.surface} space-y-4`}>
            <p className={`text-sm font-semibold ${style.highlight}`}>Unit {capstone.unit} Complete!</p>
            <p className={`whitespace-pre-line text-sm leading-relaxed ${style.text}`}>
              {capstone.story_beat}
            </p>
            <Button
              onClick={() => void handleAdvance()}
              loading={advancing}
              className="w-full bg-green-600 hover:bg-green-500"
            >
              Claim Badge &amp; Start Unit {capstone.unit + 1} →
            </Button>
          </div>
        )}
      </div>
    </main>
  );
}
