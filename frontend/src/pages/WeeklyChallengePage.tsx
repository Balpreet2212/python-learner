import { useState, useEffect, type KeyboardEvent } from "react";
import { useAuth } from "../context/AuthContext";
import { getWeeklyChallenge, submitWeekly, type WeeklyChallenge } from "../api/weekly";
import { type SubmitResult } from "../api/content";
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

const DIFFICULTY_BADGE: Record<string, string> = {
  easy: "bg-green-900/50 text-green-300",
  medium: "bg-amber-900/50 text-amber-300",
  hard: "bg-red-900/50 text-red-300",
};

function CodeEditor({
  value,
  onChange,
  rows = 12,
  disabled = false,
}: {
  value: string;
  onChange: (v: string) => void;
  rows?: number;
  disabled?: boolean;
}) {
  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key !== "Tab") return;
    e.preventDefault();
    const el = e.currentTarget;
    const start = el.selectionStart;
    const end = el.selectionEnd;
    const next = value.slice(0, start) + "    " + value.slice(end);
    onChange(next);
    requestAnimationFrame(() => {
      el.selectionStart = el.selectionEnd = start + 4;
    });
  }
  return (
    <textarea
      value={value}
      onChange={(e) => { onChange(e.target.value); }}
      onKeyDown={handleKeyDown}
      spellCheck={false}
      rows={rows}
      disabled={disabled}
      className="w-full resize-none bg-gray-950 p-4 font-code text-sm leading-relaxed text-gray-100 outline-none disabled:opacity-50"
    />
  );
}

function TestResults({ result, style, hasEverFailed }: { result: SubmitResult; style: ReturnType<typeof getStyle>; hasEverFailed: boolean }) {
  return (
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
      {hasEverFailed && (
        <div className={`${style.surface} px-4 py-3 space-y-2`}>
          <p className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>Tests</p>
          {result.tests.map((t, i) => (
            <div key={i} className="flex items-start gap-2">
              <span className={t.passed ? "text-green-400" : "text-red-400"}>{t.passed ? "✓" : "✗"}</span>
              <span className={`text-sm ${t.passed ? style.text : "text-red-300"}`}>{t.message}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default function WeeklyChallengePage() {
  const { profile } = useAuth();

  const [challenge, setChallenge] = useState<WeeklyChallenge | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);

  const [code, setCode] = useState("");
  const [result, setResult] = useState<SubmitResult | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [submitError, setSubmitError] = useState<string | null>(null);
  const [hintIndex, setHintIndex] = useState(-1);
  const [hasEverFailed, setHasEverFailed] = useState(false);

  const world = profile?.world ?? "fantasy";
  const style = getStyle(world);

  useEffect(() => {
    getWeeklyChallenge()
      .then((c) => {
        setChallenge(c);
        setCode(c.code_starter);
      })
      .catch((err: unknown) => {
        setLoadError(err instanceof ApiError ? err.message : "Failed to load challenge");
      });
  }, []);

  async function handleSubmit() {
    if (!challenge) return;
    setSubmitting(true);
    setSubmitError(null);
    try {
      const res = await submitWeekly(code);
      setResult(res);
      if (!res.all_passed) setHasEverFailed(true);
      if (res.all_passed) {
        setChallenge((prev) => prev ? { ...prev, already_passed: true } : prev);
      }
    } catch (err) {
      setSubmitError(err instanceof ApiError ? err.message : "Submission failed.");
    } finally {
      setSubmitting(false);
    }
  }

  if (!challenge) {
    return (
      <main className={`flex min-h-screen items-center justify-center ${style.bg}`}>
        {loadError ? (
          <p className="text-red-400">{loadError}</p>
        ) : (
          <p className={style.muted}>Loading challenge…</p>
        )}
      </main>
    );
  }

  const passed = result?.all_passed ?? challenge.already_passed;

  return (
    <main className={`min-h-screen ${style.bg}`}>
      <div className="mx-auto max-w-3xl space-y-8 p-6">

        {/* Header */}
        <section className="space-y-3">
          <div className="flex items-start justify-between gap-2">
            <div>
              <span className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>
                Weekly Challenge · {challenge.week_key}
              </span>
              <h1 className={`mt-1 text-2xl font-bold ${style.highlight}`}>{challenge.title}</h1>
            </div>
            <div className="flex shrink-0 flex-col items-end gap-1.5">
              <span className={`text-sm font-semibold ${style.accent}`}>+{challenge.xp} XP</span>
              <span className={`rounded-full px-2.5 py-0.5 text-xs font-semibold ${DIFFICULTY_BADGE[challenge.difficulty] ?? DIFFICULTY_BADGE["medium"]}`}>
                {challenge.difficulty}
              </span>
            </div>
          </div>

          {challenge.already_passed && !result?.all_passed && (
            <div className="rounded-xl border border-green-700/40 bg-green-950/20 px-4 py-3">
              <p className="text-sm text-green-400">You already completed this week's challenge!</p>
            </div>
          )}

          <div className={`rounded-xl border ${style.border} p-5 ${style.surface}`}>
            <p className={`whitespace-pre-line text-sm leading-relaxed ${style.text}`}>{challenge.description}</p>
          </div>
        </section>

        {/* Code editor */}
        <section className="space-y-4">
          <div className={`rounded-xl border ${style.border} overflow-hidden`}>
            <div className={`flex items-center justify-between px-4 py-2 ${style.surface} border-b ${style.border}`}>
              <span className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>Python</span>
              {result && (
                <span className={`text-xs font-semibold ${passed ? "text-green-400" : "text-red-400"}`}>
                  {passed ? "All tests passed ✓" : "Tests failed"}
                </span>
              )}
            </div>
            <CodeEditor
              value={code}
              onChange={(v) => { setCode(v); if (result) setResult(null); }}
              disabled={challenge.already_passed && !result}
            />
          </div>

          {/* Hints */}
          {challenge.hints.length > 0 && (
            <div>
              <button
                onClick={() => { setHintIndex((i) => Math.min(i + 1, challenge.hints.length - 1)); }}
                className={`text-sm underline ${style.muted}`}
              >
                {hintIndex < 0 ? "Show hint" : hintIndex < challenge.hints.length - 1 ? "Next hint" : "No more hints"}
              </button>
              {hintIndex >= 0 && (
                <div className={`mt-2 rounded-lg border ${style.border} px-4 py-3 ${style.surface}`}>
                  <p className={`font-mono text-sm ${style.text}`}>{challenge.hints[hintIndex]}</p>
                </div>
              )}
            </div>
          )}

          <Button
            onClick={() => void handleSubmit()}
            loading={submitting}
            disabled={!code.trim()}
            className={`w-full ${passed ? "bg-green-700 hover:bg-green-600" : ""}`}
          >
            {passed ? "Submit Again" : "Run Code"}
          </Button>

          {submitError && <p className="text-center text-sm text-red-400">{submitError}</p>}
          {result && <TestResults result={result} style={style} hasEverFailed={hasEverFailed} />}

          {passed && (
            <div className="rounded-xl border border-green-700/40 bg-green-950/20 px-5 py-4 text-center">
              <p className="text-lg font-bold text-green-400">Challenge complete! +{challenge.xp} XP</p>
              <p className={`mt-1 text-sm ${style.muted}`}>Come back next week for a new challenge.</p>
            </div>
          )}
        </section>

      </div>
    </main>
  );
}
