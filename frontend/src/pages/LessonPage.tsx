import { useState, useEffect, useRef, type KeyboardEvent } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { getLesson, submitChallenge, advanceLesson, type Lesson, type SubmitResult } from "../api/content";
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

export default function LessonPage() {
  const { account, profile, setProfile } = useAuth();
  const navigate = useNavigate();

  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [code, setCode] = useState("");
  const [result, setResult] = useState<SubmitResult | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [advancing, setAdvancing] = useState(false);
  const [hintIndex, setHintIndex] = useState(-1); // -1 = hidden
  const [error, setError] = useState<string | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const world = profile?.world ?? "fantasy";
  const style = getStyle(world);

  useEffect(() => {
    getLesson()
      .then((l) => {
        setLesson(l);
        setCode(l.code_starter);
      })
      .catch((err) => {
        setError(err instanceof ApiError ? err.message : "Failed to load lesson");
      });
  }, []);

  // Reset result when code changes after a run
  function handleCodeChange(value: string) {
    setCode(value);
    if (result) setResult(null);
  }

  // Insert 4 spaces on Tab key instead of changing focus
  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key !== "Tab") return;
    e.preventDefault();
    const el = e.currentTarget;
    const start = el.selectionStart;
    const end = el.selectionEnd;
    const next = code.slice(0, start) + "    " + code.slice(end);
    setCode(next);
    // Restore cursor after React re-render
    requestAnimationFrame(() => {
      el.selectionStart = el.selectionEnd = start + 4;
    });
  }

  async function handleSubmit() {
    if (!lesson) return;
    setSubmitting(true);
    setError(null);
    try {
      const res = await submitChallenge(code);
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
      const updated = await advanceLesson();
      setProfile(updated);
      // Reload the new lesson
      const next = await getLesson();
      setLesson(next);
      setCode(next.code_starter);
      setResult(null);
      setHintIndex(-1);
    } catch (err) {
      if (err instanceof ApiError && err.message.includes("all available units")) {
        // Course complete!
        navigate("/");
      } else {
        setError(err instanceof ApiError ? err.message : "Failed to advance. Try again.");
      }
    } finally {
      setAdvancing(false);
    }
  }

  if (!lesson) {
    return (
      <main className={`flex min-h-screen items-center justify-center ${style.bg}`}>
        {error ? (
          <p className="text-red-400">{error}</p>
        ) : (
          <p className={style.muted}>Loading lesson…</p>
        )}
      </main>
    );
  }

  const allPassed = result?.all_passed ?? false;
  const showHint = hintIndex >= 0 && hintIndex < lesson.hints.length;

  return (
    <main className={`min-h-screen ${style.bg}`}>
      {/* Top bar */}
      <header className={`border-b ${style.border} px-6 py-3 flex items-center justify-between`}>
        <button
          onClick={() => navigate("/")}
          className={`text-sm ${style.muted} hover:${style.text} transition-colors`}
        >
          ← World Map
        </button>
        <div className={`text-sm ${style.muted}`}>
          Unit {lesson.unit} · Lesson {lesson.lesson} of {lesson.total_lessons}
        </div>
        <div className={`text-sm font-semibold ${style.accent}`}>+{lesson.xp} XP</div>
      </header>

      <div className="mx-auto max-w-5xl gap-6 p-6 lg:grid lg:grid-cols-2">
        {/* Left panel: narrative */}
        <div className="space-y-4">
          <h1 className={`text-2xl font-bold ${style.highlight}`}>{lesson.title}</h1>
          <div className={`rounded-xl p-5 ${style.surface} border ${style.border}`}>
            <p className={`whitespace-pre-line text-sm leading-relaxed ${style.text}`}>
              {lesson.narrative}
            </p>
          </div>

          {/* Hints */}
          {lesson.hints.length > 0 && (
            <div>
              <button
                onClick={() => setHintIndex((i) => (i < lesson.hints.length - 1 ? i + 1 : i))}
                className={`text-sm underline ${style.muted} hover:${style.accent}`}
              >
                {hintIndex < 0 ? "Show hint" : hintIndex < lesson.hints.length - 1 ? "Next hint" : "No more hints"}
              </button>
              {showHint && (
                <div className={`mt-2 rounded-lg border ${style.border} px-4 py-3 ${style.surface}`}>
                  <p className={`font-mono text-sm ${style.text}`}>{lesson.hints[hintIndex]}</p>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Right panel: editor + results */}
        <div className="mt-6 space-y-4 lg:mt-0">
          {/* Code editor */}
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
              ref={textareaRef}
              value={code}
              onChange={(e) => handleCodeChange(e.target.value)}
              onKeyDown={handleKeyDown}
              spellCheck={false}
              rows={12}
              className={`w-full resize-none bg-gray-950 p-4 font-code text-sm leading-relaxed text-gray-100 outline-none`}
            />
          </div>

          {/* Run button */}
          <Button
            onClick={() => void handleSubmit()}
            loading={submitting}
            disabled={!code.trim()}
            className="w-full"
          >
            Run Code
          </Button>

          {/* Error */}
          {error && <p className="text-center text-sm text-red-400">{error}</p>}

          {/* Results panel */}
          {result && (
            <div className={`rounded-xl border ${style.border} overflow-hidden`}>
              {/* stdout */}
              {result.stdout && (
                <div className="border-b border-gray-800 bg-gray-950 px-4 py-3">
                  <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-gray-500">Output</p>
                  <pre className="font-code text-sm text-gray-300 whitespace-pre-wrap">{result.stdout}</pre>
                </div>
              )}

              {/* exec error */}
              {result.exec_error && (
                <div className="border-b border-gray-800 bg-red-950/30 px-4 py-3">
                  <p className="mb-1 text-xs font-semibold uppercase tracking-wider text-red-400">Error</p>
                  <pre className="font-code text-sm text-red-300 whitespace-pre-wrap">{result.exec_error}</pre>
                </div>
              )}

              {/* test results */}
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

          {/* Next lesson button */}
          {allPassed && (
            <Button
              onClick={() => void handleAdvance()}
              loading={advancing}
              className="w-full bg-green-600 hover:bg-green-500"
            >
              {lesson.lesson < lesson.total_lessons
                ? `Next Lesson →`
                : `Complete Unit ${lesson.unit} →`}
            </Button>
          )}

          {/* Account info strip */}
          <p className={`text-center text-xs ${style.muted}`}>
            {account?.display_name ?? account?.email}
          </p>
        </div>
      </div>
    </main>
  );
}
