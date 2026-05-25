import { useState, useEffect, useRef, type KeyboardEvent } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import {
  getLesson,
  checkExerciseCode,
  advanceLesson,
  type Lesson,
  type Exercise,
  type ConceptEx,
  type McqEx,
  type ArrangeEx,
  type FillBlankEx,
  type MiniCodeEx,
  type SubmitResult,
} from "../api/content";
import { ApiError } from "../api/client";
import Button from "../components/ui/Button";

// ── World themes ──────────────────────────────────────────────────────────────

type World = "fantasy" | "scifi" | "mystery";
const WORLD_STYLE: Record<World, {
  bg: string; surface: string; accent: string; highlight: string;
  text: string; muted: string; border: string; progress: string;
}> = {
  fantasy: {
    bg: "bg-fantasy-bg", surface: "bg-fantasy-surface", accent: "text-fantasy-accent",
    highlight: "text-fantasy-highlight", text: "text-fantasy-text", muted: "text-fantasy-text/60",
    border: "border-fantasy-accent/40", progress: "bg-fantasy-accent",
  },
  scifi: {
    bg: "bg-scifi-bg", surface: "bg-scifi-surface", accent: "text-scifi-accent",
    highlight: "text-scifi-highlight", text: "text-scifi-text", muted: "text-scifi-text/60",
    border: "border-scifi-accent/40", progress: "bg-scifi-accent",
  },
  mystery: {
    bg: "bg-mystery-bg", surface: "bg-mystery-surface", accent: "text-mystery-accent",
    highlight: "text-mystery-highlight", text: "text-mystery-text", muted: "text-mystery-text/60",
    border: "border-mystery-accent/40", progress: "bg-mystery-accent",
  },
};
function getStyle(world: string) {
  return WORLD_STYLE[(world as World) in WORLD_STYLE ? (world as World) : "fantasy"];
}

// ── Shared code editor (mini_code) ────────────────────────────────────────────

function CodeEditor({
  value, onChange, rows = 8, disabled = false,
}: { value: string; onChange: (v: string) => void; rows?: number; disabled?: boolean }) {
  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key !== "Tab") return;
    e.preventDefault();
    const el = e.currentTarget;
    const start = el.selectionStart;
    const end = el.selectionEnd;
    const next = value.slice(0, start) + "    " + value.slice(end);
    onChange(next);
    requestAnimationFrame(() => { el.selectionStart = el.selectionEnd = start + 4; });
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

// ── Feedback banner ───────────────────────────────────────────────────────────

function Feedback({ correct, explanation, onContinue }: { correct: boolean; explanation: string; onContinue: () => void }) {
  return (
    <div className={`rounded-xl border p-4 space-y-3 ${correct ? "border-green-700/50 bg-green-950/30" : "border-red-700/50 bg-red-950/30"}`}>
      <p className={`font-semibold ${correct ? "text-green-400" : "text-red-400"}`}>
        {correct ? "Correct!" : "Not quite."}
      </p>
      {explanation && <p className="text-sm text-gray-300">{explanation}</p>}
      <Button onClick={onContinue} className={`w-full ${correct ? "bg-green-700 hover:bg-green-600" : "bg-gray-700 hover:bg-gray-600"}`}>
        Continue
      </Button>
    </div>
  );
}

// ── Concept card ──────────────────────────────────────────────────────────────

function ConceptCard({
  ex, style, onContinue,
}: { ex: ConceptEx; style: ReturnType<typeof getStyle>; onContinue: () => void }) {
  const [showOutput, setShowOutput] = useState(false);
  return (
    <div className="space-y-4">
      <div className={`rounded-xl border ${style.border} overflow-hidden`}>
        <div className={`px-5 py-3 ${style.surface} border-b ${style.border}`}>
          <p className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>Example</p>
        </div>
        <div className="bg-gray-950 px-5 py-4">
          <pre className="font-code text-sm leading-relaxed text-gray-100 whitespace-pre-wrap">{ex.code}</pre>
        </div>
        <div className={`border-t ${style.border} px-5 py-4 ${style.surface}`}>
          <p className={`text-sm leading-relaxed ${style.text}`}>{ex.explanation}</p>
        </div>
        <div className={`border-t ${style.border} px-5 py-3 ${style.surface}`}>
          {!showOutput ? (
            <button onClick={() => { setShowOutput(true); }} className={`text-sm font-medium ${style.accent} underline underline-offset-2`}>
              ▶ Show output
            </button>
          ) : (
            <div>
              <p className={`mb-1 text-xs font-semibold uppercase tracking-wider ${style.muted}`}>Output</p>
              <pre className="font-code text-sm text-green-400 whitespace-pre-wrap">{ex.output || "(no output)"}</pre>
            </div>
          )}
        </div>
      </div>
      <Button onClick={onContinue} className="w-full">Got it — Continue</Button>
    </div>
  );
}

// ── MCQ card ──────────────────────────────────────────────────────────────────

function McqCard({
  ex, style, onDone,
}: { ex: McqEx; style: ReturnType<typeof getStyle>; onDone: () => void }) {
  const [selected, setSelected] = useState<string | null>(null);
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  function handleCheck() {
    if (!selected) return;
    const correct = selected === ex.correct;
    setIsCorrect(correct);
    setChecked(true);
  }

  function handleContinue() {
    if (isCorrect) {
      onDone();
    } else {
      setChecked(false);
      setIsCorrect(false);
      setSelected(null);
    }
  }

  function choiceClass(c: string) {
    const base = "w-full rounded-xl border px-4 py-3 text-left font-code text-sm transition-all";
    if (!checked) {
      return `${base} ${selected === c ? `${style.border} ${style.surface} ring-2 ring-current` : "border-gray-700 bg-gray-900 hover:border-gray-500"}`;
    }
    if (c === ex.correct) return `${base} border-green-600 bg-green-950/40 text-green-300`;
    if (c === selected) return `${base} border-red-600 bg-red-950/40 text-red-300`;
    return `${base} border-gray-800 bg-gray-900/50 text-gray-600`;
  }

  return (
    <div className="space-y-4">
      <div>
        <p className={`text-base font-semibold ${style.highlight} mb-3`}>{ex.question}</p>
        {ex.code && (
          <div className="rounded-xl bg-gray-950 px-5 py-4 mb-4">
            <pre className="font-code text-sm leading-relaxed text-gray-100 whitespace-pre-wrap">{ex.code}</pre>
          </div>
        )}
        <div className="space-y-2">
          {ex.choices.map((c) => (
            <button key={c} onClick={() => { if (!checked) setSelected(c); }} className={choiceClass(c)}>
              {c}
            </button>
          ))}
        </div>
      </div>
      {!checked ? (
        <Button onClick={handleCheck} disabled={!selected} className="w-full">Check</Button>
      ) : (
        <Feedback correct={isCorrect} explanation={ex.explanation} onContinue={handleContinue} />
      )}
    </div>
  );
}

// ── Arrange card (tap-to-place) ───────────────────────────────────────────────

function ArrangeCard({
  ex, style, onDone,
}: { ex: ArrangeEx; style: ReturnType<typeof getStyle>; onDone: () => void }) {
  const initBank = () => [...ex.blocks].sort(() => Math.random() - 0.5).map((v, i) => ({ v, id: i }));
  const [placed, setPlaced] = useState<string[]>([]);
  const [bank, setBank] = useState<{ v: string; id: number }[]>(initBank);
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  function tapBank(id: number) {
    if (checked) return;
    const item = bank.find((b) => b.id === id);
    if (!item) return;
    setBank((prev) => prev.filter((b) => b.id !== id));
    setPlaced((prev) => [...prev, item.v]);
  }

  function tapPlaced(index: number) {
    if (checked) return;
    const val = placed[index];
    setPlaced((prev) => prev.filter((_, i) => i !== index));
    setBank((prev) => [...prev, { v: val, id: Date.now() + index }]);
  }

  function handleCheck() {
    const correct = placed.length === ex.correct.length && placed.every((v, i) => v === ex.correct[i]);
    setIsCorrect(correct);
    setChecked(true);
  }

  function handleContinue() {
    if (isCorrect) {
      onDone();
    } else {
      setChecked(false);
      setIsCorrect(false);
      setPlaced([]);
      setBank(initBank());
    }
  }

  return (
    <div className="space-y-4">
      <p className={`text-base font-semibold ${style.highlight}`}>{ex.instruction}</p>

      {/* Placed area */}
      <div className={`min-h-12 rounded-xl border-2 ${style.border} p-3 flex flex-wrap gap-2 items-center`}>
        {placed.length === 0 && (
          <span className={`text-sm ${style.muted}`}>Tap a block below to place it here</span>
        )}
        {placed.map((v, i) => (
          <button
            key={i}
            onClick={() => { tapPlaced(i); }}
            disabled={checked}
            className={`rounded-lg border ${style.border} ${style.surface} px-3 py-1.5 font-code text-sm ${style.text} transition-all hover:brightness-110 disabled:cursor-default`}
          >
            {v}
          </button>
        ))}
      </div>

      {/* Bank */}
      <div className="flex flex-wrap gap-2 min-h-10">
        {bank.map((item) => (
          <button
            key={item.id}
            onClick={() => { tapBank(item.id); }}
            disabled={checked}
            className="rounded-lg border border-gray-600 bg-gray-800 px-3 py-1.5 font-code text-sm text-gray-200 transition-all hover:bg-gray-700 disabled:cursor-default"
          >
            {item.v}
          </button>
        ))}
      </div>

      {!checked ? (
        <Button onClick={handleCheck} disabled={placed.length === 0} className="w-full">Check</Button>
      ) : (
        <Feedback correct={isCorrect} explanation={ex.explanation} onContinue={handleContinue} />
      )}
    </div>
  );
}

// ── Fill blank card ───────────────────────────────────────────────────────────

function FillBlankCard({
  ex, style, onDone,
}: { ex: FillBlankEx; style: ReturnType<typeof getStyle>; onDone: () => void }) {
  const [selected, setSelected] = useState<string | null>(null);
  const [checked, setChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  function handleCheck() {
    if (!selected) return;
    const correct = selected === ex.answer;
    setIsCorrect(correct);
    setChecked(true);
  }

  function handleContinue() {
    if (isCorrect) {
      onDone();
    } else {
      setChecked(false);
      setIsCorrect(false);
      setSelected(null);
    }
  }

  function choiceClass(c: string) {
    const base = "rounded-lg border px-3 py-2 font-code text-sm transition-all";
    if (!checked) {
      return `${base} ${selected === c ? `${style.border} ${style.surface} ring-2 ring-current` : "border-gray-700 bg-gray-900 hover:border-gray-500"}`;
    }
    if (c === ex.answer) return `${base} border-green-600 bg-green-950/40 text-green-300`;
    if (c === selected) return `${base} border-red-600 bg-red-950/40 text-red-300`;
    return `${base} border-gray-800 bg-gray-900/50 text-gray-600`;
  }

  return (
    <div className="space-y-5">
      <p className={`text-base font-semibold ${style.highlight}`}>{ex.prompt}</p>

      {/* Code line with blank */}
      <div className="rounded-xl bg-gray-950 px-5 py-4">
        <span className="font-code text-sm text-gray-100">{ex.before}</span>
        <span className={`inline-block min-w-12 rounded border-b-2 px-2 font-code text-sm font-bold mx-1
          ${checked && isCorrect ? "border-green-500 text-green-300" : checked && !isCorrect ? "border-red-500 text-red-300" : `${style.border} ${style.accent}`}`}>
          {selected ?? "____"}
        </span>
        <span className="font-code text-sm text-gray-100">{ex.after}</span>
      </div>

      {/* Word bank */}
      <div className="flex flex-wrap gap-2">
        {ex.choices.map((c) => (
          <button key={c} onClick={() => { if (!checked) setSelected(c); }} className={choiceClass(c)}>
            {c}
          </button>
        ))}
      </div>

      {!checked ? (
        <Button onClick={handleCheck} disabled={!selected} className="w-full">Check</Button>
      ) : (
        <Feedback correct={isCorrect} explanation={ex.explanation} onContinue={handleContinue} />
      )}
    </div>
  );
}

// ── Mini code card ────────────────────────────────────────────────────────────

function MiniCodeCard({
  ex,
  exerciseIndex,
  style,
  onDone,
}: { ex: MiniCodeEx; exerciseIndex: number; style: ReturnType<typeof getStyle>; onDone: (correct: boolean) => void }) {
  const [code, setCode] = useState(ex.starter);
  const [result, setResult] = useState<SubmitResult | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleCheck() {
    setSubmitting(true);
    setError(null);
    try {
      const res = await checkExerciseCode(code, exerciseIndex);
      setResult(res);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Submission failed.");
    } finally {
      setSubmitting(false);
    }
  }

  const passed = result?.all_passed ?? false;

  return (
    <div className="space-y-4">
      <p className={`text-sm leading-relaxed ${style.text}`}>{ex.prompt}</p>

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
          rows={6}
          disabled={passed}
        />
      </div>

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
            {result.tests.map((t, i) => (
              <div key={i} className="flex items-start gap-2">
                <span className={t.passed ? "text-green-400" : "text-red-400"}>{t.passed ? "✓" : "✗"}</span>
                <span className={`text-sm ${t.passed ? style.text : "text-red-300"}`}>{t.message}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {error && <p className="text-center text-sm text-red-400">{error}</p>}

      {!passed ? (
        <Button onClick={() => void handleCheck()} loading={submitting} disabled={!code.trim()} className="w-full">
          Check Code
        </Button>
      ) : (
        <Button onClick={() => { onDone(true); }} className="w-full bg-green-700 hover:bg-green-600">
          Continue
        </Button>
      )}
    </div>
  );
}

// ── Main lesson page ──────────────────────────────────────────────────────────

export default function LessonPage() {
  const { profile, setProfile } = useAuth();
  const navigate = useNavigate();

  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [done, setDone] = useState(false);
  const [advancing, setAdvancing] = useState(false);

  // Track which mini_code exercise we're on (for server validation index)
  const miniCodeCountRef = useRef(0);

  const world = profile?.world ?? "fantasy";
  const style = getStyle(world);

  useEffect(() => {
    getLesson()
      .then((l) => { setLesson(l); })
      .catch((err: unknown) => {
        setLoadError(err instanceof ApiError ? err.message : "Failed to load lesson");
      });
  }, []);

  function handleExerciseDone(_correct: boolean) {
    if (!lesson) return;
    if (currentIndex + 1 >= lesson.exercises.length) {
      setDone(true);
    } else {
      setCurrentIndex((i) => i + 1);
    }
  }

  async function handleAdvance() {
    setAdvancing(true);
    try {
      const updated = await advanceLesson();
      setProfile(updated);
      const next = await getLesson();
      setLesson(next);
      setCurrentIndex(0);
      setDone(false);
      miniCodeCountRef.current = 0;
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
        {loadError ? <p className="text-red-400">{loadError}</p> : <p className={style.muted}>Loading…</p>}
      </main>
    );
  }

  const progress = done ? 1 : currentIndex / lesson.exercises.length;

  // Count mini_code exercises seen so far to pass correct index to server
  let miniCodeIndex = 0;
  for (let i = 0; i < currentIndex; i++) {
    if (lesson.exercises[i].type === "mini_code") miniCodeIndex++;
  }

  const currentEx: Exercise | undefined = lesson.exercises[currentIndex];

  return (
    <main className={`min-h-screen ${style.bg}`}>
      {/* Progress bar */}
      <div className="sticky top-0 z-10 bg-black/20 backdrop-blur-sm px-6 py-3">
        <div className="mx-auto max-w-xl">
          <div className="flex items-center gap-3">
            <span className={`shrink-0 text-xs font-semibold ${style.muted}`}>
              {lesson.lesson}/{lesson.total_lessons}
            </span>
            <div className="flex-1 h-2.5 rounded-full bg-gray-800">
              <div
                className={`h-2.5 rounded-full ${style.progress} transition-all duration-300`}
                style={{ width: `${progress * 100}%` }}
              />
            </div>
            <span className={`shrink-0 text-xs font-semibold ${style.accent}`}>+{lesson.xp} XP</span>
          </div>
        </div>
      </div>

      <div className="mx-auto max-w-xl p-6 space-y-6">
        {/* Title (only on first exercise) */}
        {currentIndex === 0 && !done && (
          <div>
            <span className={`text-xs font-semibold uppercase tracking-wider ${style.muted}`}>
              Unit {lesson.unit}
            </span>
            <h1 className={`mt-1 text-2xl font-bold ${style.highlight}`}>{lesson.title}</h1>
          </div>
        )}

        {/* Completion screen */}
        {done ? (
          <div className="space-y-6 pt-8 text-center">
            <div className="text-6xl">🎉</div>
            <div>
              <h2 className={`text-2xl font-bold ${style.highlight}`}>Lesson complete!</h2>
              <p className={`mt-1 text-sm ${style.muted}`}>+{lesson.xp} XP earned</p>
            </div>
            {lesson.lesson < lesson.total_lessons ? (
              <Button onClick={() => void handleAdvance()} loading={advancing} className="w-full bg-green-700 hover:bg-green-600 text-lg py-3">
                Next Lesson →
              </Button>
            ) : (
              <Button onClick={() => { navigate("/capstone"); }} className="w-full bg-amber-600 hover:bg-amber-500 text-lg py-3">
                Unit {lesson.unit} Capstone →
              </Button>
            )}
          </div>
        ) : (
          /* Current exercise */
          currentEx && (
            <div key={currentIndex}>
              {currentEx.type === "concept" && (
                <ConceptCard ex={currentEx} style={style} onContinue={() => { handleExerciseDone(true); }} />
              )}
              {currentEx.type === "mcq" && (
                <McqCard ex={currentEx} style={style} onDone={() => { handleExerciseDone(true); }} />
              )}
              {currentEx.type === "arrange" && (
                <ArrangeCard ex={currentEx} style={style} onDone={() => { handleExerciseDone(true); }} />
              )}
              {currentEx.type === "fill_blank" && (
                <FillBlankCard ex={currentEx} style={style} onDone={() => { handleExerciseDone(true); }} />
              )}
              {currentEx.type === "mini_code" && (
                <MiniCodeCard
                  ex={currentEx}
                  exerciseIndex={miniCodeIndex}
                  style={style}
                  onDone={(c) => { if (c) handleExerciseDone(c); }}
                />
              )}
            </div>
          )
        )}
      </div>
    </main>
  );
}
