import { useState, useEffect, type KeyboardEvent } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import {
  getLesson,
  submitChallenge,
  submitFinalChallenge,
  checkPredict,
  submitFix,
  advanceLesson,
  type Lesson,
  type SubmitResult,
  type PredictResult,
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

function CodeEditor({
  value,
  onChange,
  rows = 10,
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

function TestResults({ result, style }: { result: SubmitResult; style: ReturnType<typeof getStyle> }) {
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
      <div className={`${style.surface} px-4 py-3 space-y-2`}>
        <p className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>Tests</p>
        {result.tests.map((t, i) => (
          <div key={i} className="flex items-start gap-2">
            <span className={t.passed ? "text-green-400" : "text-red-400"}>{t.passed ? "✓" : "✗"}</span>
            <span className={`text-sm ${t.passed ? style.text : "text-red-300"}`}>{t.message}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export default function LessonPage() {
  const { profile, setProfile } = useAuth();
  const navigate = useNavigate();

  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);

  // Example section
  const [showOutput, setShowOutput] = useState(false);

  // Exercise section
  const [exerciseCode, setExerciseCode] = useState("");
  const [exerciseResult, setExerciseResult] = useState<SubmitResult | null>(null);
  const [exerciseSubmitting, setExerciseSubmitting] = useState(false);
  const [exerciseError, setExerciseError] = useState<string | null>(null);
  const [exerciseHintIndex, setExerciseHintIndex] = useState(-1);

  // Predict card
  const [predictAnswer, setPredictAnswer] = useState("");
  const [predictResult, setPredictResult] = useState<PredictResult | null>(null);
  const [predictSubmitting, setPredictSubmitting] = useState(false);
  const [predictError, setPredictError] = useState<string | null>(null);

  // Break-and-fix card
  const [fixCode, setFixCode] = useState("");
  const [fixResult, setFixResult] = useState<SubmitResult | null>(null);
  const [fixSubmitting, setFixSubmitting] = useState(false);
  const [fixError, setFixError] = useState<string | null>(null);
  const [fixHintShown, setFixHintShown] = useState(false);

  // Final challenge section
  const [finalCode, setFinalCode] = useState("");
  const [finalResult, setFinalResult] = useState<SubmitResult | null>(null);
  const [finalSubmitting, setFinalSubmitting] = useState(false);
  const [finalError, setFinalError] = useState<string | null>(null);
  const [finalHintIndex, setFinalHintIndex] = useState(-1);

  // Advance
  const [advancing, setAdvancing] = useState(false);

  const world = profile?.world ?? "fantasy";
  const style = getStyle(world);

  useEffect(() => {
    getLesson()
      .then((l) => {
        setLesson(l);
        setExerciseCode(l.code_starter);
        setFinalCode(l.final_challenge.code_starter);
        setFixCode(l.break_and_fix?.broken_code ?? "");
      })
      .catch((err: unknown) => {
        setLoadError(err instanceof ApiError ? err.message : "Failed to load lesson");
      });
  }, []);

  async function handleExerciseSubmit() {
    if (!lesson) return;
    setExerciseSubmitting(true);
    setExerciseError(null);
    try {
      const res = await submitChallenge(exerciseCode);
      setExerciseResult(res);
    } catch (err) {
      setExerciseError(err instanceof ApiError ? err.message : "Submission failed.");
    } finally {
      setExerciseSubmitting(false);
    }
  }

  async function handlePredictCheck() {
    if (!lesson?.predict) return;
    setPredictSubmitting(true);
    setPredictError(null);
    try {
      const res = await checkPredict(predictAnswer);
      setPredictResult(res);
    } catch (err) {
      setPredictError(err instanceof ApiError ? err.message : "Submission failed.");
    } finally {
      setPredictSubmitting(false);
    }
  }

  async function handleFixSubmit() {
    if (!lesson?.break_and_fix) return;
    setFixSubmitting(true);
    setFixError(null);
    try {
      const res = await submitFix(fixCode);
      setFixResult(res);
    } catch (err) {
      setFixError(err instanceof ApiError ? err.message : "Submission failed.");
    } finally {
      setFixSubmitting(false);
    }
  }

  async function handleFinalSubmit() {
    if (!lesson) return;
    setFinalSubmitting(true);
    setFinalError(null);
    try {
      const res = await submitFinalChallenge(finalCode);
      setFinalResult(res);
    } catch (err) {
      setFinalError(err instanceof ApiError ? err.message : "Submission failed.");
    } finally {
      setFinalSubmitting(false);
    }
  }

  async function handleAdvance() {
    setAdvancing(true);
    try {
      const updated = await advanceLesson();
      setProfile(updated);
      const next = await getLesson();
      setLesson(next);
      setExerciseCode(next.code_starter);
      setFinalCode(next.final_challenge.code_starter);
      setFixCode(next.break_and_fix?.broken_code ?? "");
      setExerciseResult(null);
      setFinalResult(null);
      setPredictResult(null);
      setPredictAnswer("");
      setFixResult(null);
      setFixHintShown(false);
      setExerciseHintIndex(-1);
      setFinalHintIndex(-1);
      setShowOutput(false);
      window.scrollTo({ top: 0, behavior: "smooth" });
    } catch (err) {
      if (err instanceof ApiError && err.message.includes("all available units")) {
        navigate("/");
      }
    } finally {
      setAdvancing(false);
    }
  }

  if (!lesson) {
    return (
      <main className={`flex min-h-screen items-center justify-center ${style.bg}`}>
        {loadError ? (
          <p className="text-red-400">{loadError}</p>
        ) : (
          <p className={style.muted}>Loading lesson…</p>
        )}
      </main>
    );
  }

  const exercisePassed = exerciseResult?.all_passed ?? false;
  const predictPassed = !lesson?.predict || (predictResult?.correct ?? false);
  const fixPassed = !lesson?.break_and_fix || (fixResult?.all_passed ?? false);
  const finalUnlocked = exercisePassed && predictPassed && fixPassed;
  const finalPassed = finalResult?.all_passed ?? false;

  return (
    <main className={`min-h-screen ${style.bg}`}>
      <div className="mx-auto max-w-3xl space-y-8 p-6">

        {/* ── Section 1: Setup ─────────────────────────────────────────── */}
        <section className="space-y-3">
          <div className="flex items-start justify-between gap-2">
            <div>
              <span className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>
                Unit {lesson.unit} · Lesson {lesson.lesson} of {lesson.total_lessons}
              </span>
              <h1 className={`mt-1 text-2xl font-bold ${style.highlight}`}>{lesson.title}</h1>
            </div>
            <span className={`shrink-0 text-sm font-semibold ${style.accent}`}>+{lesson.xp} XP</span>
          </div>
          <div className={`rounded-xl border ${style.border} p-5 ${style.surface}`}>
            <p className={`whitespace-pre-line text-sm leading-relaxed ${style.text}`}>{lesson.setup}</p>
          </div>
        </section>

        {/* ── Section 2: Example ───────────────────────────────────────── */}
        <section className={`rounded-xl border ${style.border} overflow-hidden`}>
          <div className={`border-b ${style.border} px-5 py-3 ${style.surface} flex items-center justify-between`}>
            <h2 className={`text-sm font-semibold ${style.highlight}`}>How It Works — Example</h2>
            <span className={`text-xs ${style.muted}`}>Read-only</span>
          </div>

          {/* Code display */}
          <div className="bg-gray-950 px-5 py-4">
            <pre className="font-code text-sm leading-relaxed text-gray-100 whitespace-pre-wrap">
              {lesson.example.code}
            </pre>
          </div>

          {/* Explanation */}
          <div className={`border-t ${style.border} px-5 py-4 ${style.surface}`}>
            <p className={`text-sm leading-relaxed ${style.text}`}>{lesson.example.explanation}</p>
          </div>

          {/* Show output button */}
          <div className={`border-t ${style.border} px-5 py-3 ${style.surface}`}>
            {!showOutput ? (
              <button
                onClick={() => { setShowOutput(true); }}
                className={`text-sm font-medium ${style.accent} underline underline-offset-2`}
              >
                ▶ Run example — see output
              </button>
            ) : (
              <div>
                <p className={`mb-1 text-xs font-semibold uppercase tracking-wider ${style.muted}`}>Output</p>
                <pre className="font-code text-sm text-green-400 whitespace-pre-wrap">
                  {lesson.example.output || "(no output)"}
                </pre>
              </div>
            )}
          </div>
        </section>

        {/* ── Section 3: Exercise ──────────────────────────────────────── */}
        <section className="space-y-4">
          <div>
            <h2 className={`text-base font-semibold ${style.highlight}`}>Exercise — Complete the Code</h2>
            <p className={`text-sm ${style.muted} mt-0.5`}>
              Fill in the blanks to make all tests pass.
            </p>
          </div>

          <div className={`rounded-xl border ${style.border} overflow-hidden`}>
            <div className={`flex items-center justify-between px-4 py-2 ${style.surface} border-b ${style.border}`}>
              <span className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>Python</span>
              {exerciseResult && (
                <span className={`text-xs font-semibold ${exercisePassed ? "text-green-400" : "text-red-400"}`}>
                  {exercisePassed ? "All tests passed ✓" : "Tests failed"}
                </span>
              )}
            </div>
            <CodeEditor
              value={exerciseCode}
              onChange={(v) => { setExerciseCode(v); if (exerciseResult) setExerciseResult(null); }}
            />
          </div>

          {/* Exercise hints */}
          {lesson.hints.length > 0 && (
            <div>
              <button
                onClick={() => { setExerciseHintIndex((i) => Math.min(i + 1, lesson.hints.length - 1)); }}
                className={`text-sm underline ${style.muted}`}
              >
                {exerciseHintIndex < 0 ? "Show hint" : exerciseHintIndex < lesson.hints.length - 1 ? "Next hint" : "No more hints"}
              </button>
              {exerciseHintIndex >= 0 && (
                <div className={`mt-2 rounded-lg border ${style.border} px-4 py-3 ${style.surface}`}>
                  <p className={`font-mono text-sm ${style.text}`}>{lesson.hints[exerciseHintIndex]}</p>
                </div>
              )}
            </div>
          )}

          <Button onClick={() => void handleExerciseSubmit()} loading={exerciseSubmitting} disabled={!exerciseCode.trim()} className="w-full">
            Check Exercise
          </Button>

          {exerciseError && <p className="text-center text-sm text-red-400">{exerciseError}</p>}
          {exerciseResult && <TestResults result={exerciseResult} style={style} />}
        </section>

        {/* ── Section 3b: Predict Card ─────────────────────────────────── */}
        {lesson.predict && (
          <section className={`rounded-xl border ${exercisePassed ? style.border : "border-gray-700"} overflow-hidden transition-all`}>
            <div className={`border-b ${exercisePassed ? style.border : "border-gray-700"} px-5 py-3 ${exercisePassed ? style.surface : "bg-gray-900"} flex items-center justify-between`}>
              <div>
                <h2 className={`text-sm font-semibold ${exercisePassed ? style.highlight : "text-gray-400"}`}>
                  Predict the Output
                </h2>
                {!exercisePassed && (
                  <p className="text-xs text-gray-500 mt-0.5">Complete the exercise to unlock.</p>
                )}
              </div>
              {predictResult?.correct && (
                <span className="text-xs font-semibold text-green-400">Correct ✓</span>
              )}
            </div>

            {exercisePassed && (
              <>
                <div className="bg-gray-950 px-5 py-4">
                  <pre className="font-code text-sm leading-relaxed text-gray-100 whitespace-pre-wrap">
                    {lesson.predict.code}
                  </pre>
                </div>
                <div className={`border-t ${style.border} px-5 py-4 ${style.surface} space-y-3`}>
                  <p className={`text-sm ${style.muted}`}>What will this code print? Type the exact output below.</p>
                  <input
                    type="text"
                    value={predictAnswer}
                    onChange={(e) => { setPredictAnswer(e.target.value); if (predictResult) setPredictResult(null); }}
                    placeholder="Expected output…"
                    disabled={predictResult?.correct}
                    className={`w-full rounded-lg border ${style.border} bg-gray-950 px-4 py-2 font-code text-sm text-gray-100 outline-none placeholder:text-gray-600 disabled:opacity-50`}
                  />
                  <Button
                    onClick={() => void handlePredictCheck()}
                    loading={predictSubmitting}
                    disabled={!predictAnswer.trim() || (predictResult?.correct ?? false)}
                    className="w-full"
                  >
                    Check Answer
                  </Button>
                  {predictError && <p className="text-center text-sm text-red-400">{predictError}</p>}
                  {predictResult && !predictResult.correct && (
                    <div className={`rounded-lg border ${style.border} px-4 py-3 space-y-2 ${style.surface}`}>
                      <p className="text-sm text-red-400">Not quite. The actual output was:</p>
                      <pre className="font-code text-sm text-gray-300 whitespace-pre-wrap">{predictResult.actual_output || "(no output)"}</pre>
                      <p className={`text-sm ${style.text}`}>{predictResult.explanation}</p>
                    </div>
                  )}
                  {predictResult?.correct && (
                    <div className={`rounded-lg border border-green-700/40 bg-green-950/20 px-4 py-3`}>
                      <p className="text-sm text-green-400">{predictResult.explanation}</p>
                    </div>
                  )}
                </div>
              </>
            )}
          </section>
        )}

        {/* ── Section 3c: Break and Fix ────────────────────────────────── */}
        {lesson.break_and_fix && (
          <section className={`rounded-xl border ${exercisePassed ? style.border : "border-gray-700"} overflow-hidden transition-all`}>
            <div className={`border-b ${exercisePassed ? style.border : "border-gray-700"} px-5 py-3 ${exercisePassed ? style.surface : "bg-gray-900"} flex items-center justify-between`}>
              <div>
                <h2 className={`text-sm font-semibold ${exercisePassed ? style.highlight : "text-gray-400"}`}>
                  Break and Fix
                </h2>
                {!exercisePassed && (
                  <p className="text-xs text-gray-500 mt-0.5">Complete the exercise to unlock.</p>
                )}
              </div>
              {fixResult?.all_passed && (
                <span className="text-xs font-semibold text-green-400">Fixed ✓</span>
              )}
            </div>

            {exercisePassed && (
              <>
                <div className={`border-b ${style.border} px-5 py-3 ${style.surface}`}>
                  <p className={`text-sm ${style.muted}`}>The code below has a bug. Find and fix it.</p>
                </div>
                <div className={`border-b ${style.border} overflow-hidden`}>
                  <CodeEditor
                    value={fixCode}
                    onChange={(v) => { setFixCode(v); if (fixResult) setFixResult(null); }}
                    rows={6}
                    disabled={fixResult?.all_passed ?? false}
                  />
                </div>
                <div className={`px-5 py-3 ${style.surface} border-b ${style.border} space-y-2`}>
                  {!fixHintShown ? (
                    <button
                      onClick={() => { setFixHintShown(true); }}
                      className={`text-sm underline ${style.muted}`}
                    >
                      Show hint
                    </button>
                  ) : (
                    <div className={`rounded-lg border ${style.border} px-4 py-3 bg-gray-950`}>
                      <p className={`font-mono text-sm ${style.text}`}>{lesson.break_and_fix.hint}</p>
                    </div>
                  )}
                </div>
                <div className={`p-4 ${style.surface} space-y-3`}>
                  <Button
                    onClick={() => void handleFixSubmit()}
                    loading={fixSubmitting}
                    disabled={!fixCode.trim() || (fixResult?.all_passed ?? false)}
                    className="w-full"
                  >
                    Test Fix
                  </Button>
                  {fixError && <p className="text-center text-sm text-red-400">{fixError}</p>}
                </div>
                {fixResult && (
                  <div className="px-4 pb-4">
                    <TestResults result={fixResult} style={style} />
                  </div>
                )}
              </>
            )}
          </section>
        )}

        {/* ── Section 4: Final Challenge ───────────────────────────────── */}
        <section className={`rounded-xl border-2 ${finalUnlocked ? style.border : "border-gray-700"} overflow-hidden transition-all`}>
          <div className={`px-5 py-4 ${finalUnlocked ? style.surface : "bg-gray-900"} border-b ${finalUnlocked ? style.border : "border-gray-700"}`}>
            <h2 className={`text-base font-semibold ${finalUnlocked ? style.highlight : "text-gray-400"}`}>
              Final Challenge — Code It from Scratch
            </h2>
            {!finalUnlocked && (
              <p className="text-xs text-gray-500 mt-0.5">
                {!exercisePassed
                  ? "Complete the exercise above to unlock."
                  : "Complete the predict and fix cards above to unlock."}
              </p>
            )}
          </div>

          {finalUnlocked && (
            <>
              <div className={`px-5 py-4 ${style.surface} border-b ${style.border}`}>
                <p className={`text-sm leading-relaxed ${style.text}`}>{lesson.final_challenge.prompt}</p>
              </div>

              <div className={`border-b ${style.border} overflow-hidden`}>
                <div className={`flex items-center justify-between px-4 py-2 ${style.surface} border-b ${style.border}`}>
                  <span className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>Python</span>
                  {finalResult && (
                    <span className={`text-xs font-semibold ${finalPassed ? "text-green-400" : "text-red-400"}`}>
                      {finalPassed ? "All tests passed ✓" : "Tests failed"}
                    </span>
                  )}
                </div>
                <CodeEditor
                  value={finalCode}
                  onChange={(v) => { setFinalCode(v); if (finalResult) setFinalResult(null); }}
                  rows={12}
                />
              </div>

              {/* Final challenge hints */}
              {lesson.final_challenge.hints.length > 0 && (
                <div className={`px-5 py-3 ${style.surface} border-b ${style.border}`}>
                  <button
                    onClick={() => { setFinalHintIndex((i) => Math.min(i + 1, lesson.final_challenge.hints.length - 1)); }}
                    className={`text-sm underline ${style.muted}`}
                  >
                    {finalHintIndex < 0 ? "Show hint" : finalHintIndex < lesson.final_challenge.hints.length - 1 ? "Next hint" : "No more hints"}
                  </button>
                  {finalHintIndex >= 0 && (
                    <div className={`mt-2 rounded-lg border ${style.border} px-4 py-3 bg-gray-950`}>
                      <p className={`font-mono text-sm ${style.text}`}>{lesson.final_challenge.hints[finalHintIndex]}</p>
                    </div>
                  )}
                </div>
              )}

              <div className={`p-4 ${style.surface} space-y-3`}>
                <Button onClick={() => void handleFinalSubmit()} loading={finalSubmitting} disabled={!finalCode.trim()} className="w-full">
                  Run Code
                </Button>
                {finalError && <p className="text-center text-sm text-red-400">{finalError}</p>}
              </div>

              {finalResult && (
                <div className="px-4 pb-4">
                  <TestResults result={finalResult} style={style} />
                </div>
              )}
            </>
          )}
        </section>

        {/* ── Advance button ───────────────────────────────────────────── */}
        {finalPassed && (
          <div className="pb-8">
            {lesson.lesson < lesson.total_lessons ? (
              <Button
                onClick={() => void handleAdvance()}
                loading={advancing}
                className="w-full bg-green-600 hover:bg-green-500"
              >
                Next Lesson →
              </Button>
            ) : (
              <Button
                onClick={() => { navigate("/capstone"); }}
                className="w-full bg-amber-600 hover:bg-amber-500"
              >
                Unit {lesson.unit} Capstone →
              </Button>
            )}
          </div>
        )}

      </div>
    </main>
  );
}
