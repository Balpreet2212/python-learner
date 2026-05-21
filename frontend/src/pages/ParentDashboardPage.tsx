import { useState, useEffect, useRef, type FormEvent } from "react";
import { useAuth } from "../context/AuthContext";
import {
  getLinkedLearners,
  getLearnerDetail,
  linkLearner,
  type LearnerSummary,
  type LearnerDetail,
} from "../api/parent";
import { ApiError } from "../api/client";
import Button from "../components/ui/Button";

const WORLD_EMOJI: Record<string, string> = {
  fantasy: "🧙",
  scifi: "🚀",
  mystery: "🔍",
};

const WORLD_LABEL: Record<string, string> = {
  fantasy: "Enchanted Realm",
  scifi: "Starship Command",
  mystery: "Detective Agency",
};

const WORLD_BORDER: Record<string, string> = {
  fantasy: "border-purple-700",
  scifi: "border-cyan-700",
  mystery: "border-amber-700",
};

const WORLD_TEXT: Record<string, string> = {
  fantasy: "text-purple-400",
  scifi: "text-cyan-400",
  mystery: "text-amber-400",
};

const WORLD_BAR: Record<string, string> = {
  fantasy: "bg-purple-500",
  scifi: "bg-cyan-500",
  mystery: "bg-amber-500",
};

function ProgressBar({ value, max }: { value: number; max: number }) {
  const pct = max === 0 ? 0 : Math.round((value / max) * 100);
  return (
    <div className="h-1.5 w-full overflow-hidden rounded-full bg-gray-700">
      <div
        className="h-full rounded-full bg-indigo-500 transition-all"
        style={{ width: `${String(pct)}%` }}
      />
    </div>
  );
}

function Sparkline({ data, barClass }: { data: number[]; barClass: string }) {
  const max = Math.max(...data, 1);
  return (
    <div className="flex items-end gap-px" style={{ height: "32px" }}>
      {data.map((v, i) => {
        const h = v === 0 ? 4 : Math.max(Math.round((v / max) * 100), 12);
        return (
          <div
            key={i}
            className={`flex-1 rounded-sm ${v > 0 ? barClass : "bg-gray-700"}`}
            style={{ height: `${String(h)}%` }}
            title={`${String(v)} lesson${v !== 1 ? "s" : ""}`}
          />
        );
      })}
    </div>
  );
}

function LearnerCard({ learner }: { learner: LearnerSummary }) {
  const [expanded, setExpanded] = useState(false);
  const [detail, setDetail] = useState<LearnerDetail | null>(null);
  const [detailLoading, setDetailLoading] = useState(false);
  const [detailError, setDetailError] = useState<string | null>(null);

  const totalLessons = learner.total_units * learner.total_lessons_per_unit;
  const completedLessons =
    (learner.current_unit - 1) * learner.total_lessons_per_unit +
    (learner.current_lesson - 1);

  const borderClass = WORLD_BORDER[learner.world] ?? "border-gray-700";
  const textClass = WORLD_TEXT[learner.world] ?? "text-gray-400";
  const barClass = WORLD_BAR[learner.world] ?? "bg-indigo-500";

  function handleToggle() {
    if (!expanded && detail === null && !detailLoading) {
      setDetailLoading(true);
      setDetailError(null);
      getLearnerDetail(learner.id)
        .then((d) => { setDetail(d); })
        .catch((err: unknown) => {
          setDetailError(err instanceof ApiError ? err.message : "Failed to load details");
        })
        .finally(() => { setDetailLoading(false); });
    }
    setExpanded((prev) => !prev);
  }

  return (
    <div className={`rounded-2xl border bg-gray-900 p-5 ${borderClass}`}>
      <div className="flex items-start justify-between gap-2">
        <div className="min-w-0">
          <p className="truncate font-semibold text-white">
            {learner.display_name ?? learner.email}
          </p>
          <p className="truncate text-xs text-gray-500">{learner.email}</p>
        </div>
        <span className="shrink-0 text-2xl" title={WORLD_LABEL[learner.world]}>
          {WORLD_EMOJI[learner.world] ?? "📚"}
        </span>
      </div>

      <div className="mt-4 space-y-2">
        <div className="flex items-center justify-between text-xs">
          <span className={textClass}>
            {WORLD_LABEL[learner.world] ?? learner.world}
          </span>
          <span className="text-gray-400 capitalize">
            {learner.track === "junior" ? "Junior" : "Core"} track
          </span>
        </div>

        <ProgressBar value={completedLessons} max={totalLessons} />

        <div className="flex items-center justify-between text-xs text-gray-400">
          <span>
            Unit {learner.current_unit} · Lesson {learner.current_lesson} /{" "}
            {learner.total_lessons_per_unit}
          </span>
          <span>{completedLessons} / {totalLessons} lessons</span>
        </div>
      </div>

      {learner.badges.length > 0 && (
        <p className="mt-3 text-xs text-gray-500">
          🏅 {learner.badges.length} badge{learner.badges.length !== 1 ? "s" : ""} earned
        </p>
      )}

      <button
        onClick={handleToggle}
        className="mt-3 flex w-full items-center justify-between text-xs text-gray-500 transition-colors hover:text-gray-300"
      >
        <span>Activity details</span>
        <span aria-hidden="true">{expanded ? "▲" : "▼"}</span>
      </button>

      {expanded && (
        <div className="mt-3 space-y-3 border-t border-gray-800 pt-3">
          {detailLoading && (
            <p className="text-xs text-gray-500">Loading…</p>
          )}
          {detailError && (
            <p className="text-xs text-red-400">{detailError}</p>
          )}
          {detail && (
            <>
              <div className="grid grid-cols-3 gap-2 text-xs">
                <div>
                  <p className="text-gray-500">Streak</p>
                  <p className="font-semibold text-white">
                    {detail.streak_days}d
                  </p>
                </div>
                <div>
                  <p className="text-gray-500">This week</p>
                  <p className="font-semibold text-white">
                    {detail.lessons_this_week} lesson{detail.lessons_this_week !== 1 ? "s" : ""}
                  </p>
                </div>
                <div>
                  <p className="text-gray-500">Last active</p>
                  <p className="font-semibold text-white">
                    {detail.last_active ?? "—"}
                  </p>
                </div>
              </div>
              <div>
                <p className="mb-1.5 text-xs text-gray-500">30-day activity</p>
                <Sparkline data={detail.sparkline_30d} barClass={barClass} />
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default function ParentDashboardPage() {
  const { account } = useAuth();
  const [learners, setLearners] = useState<LearnerSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [linkEmail, setLinkEmail] = useState("");
  const [linking, setLinking] = useState(false);
  const [linkError, setLinkError] = useState<string | null>(null);
  const [linkSuccess, setLinkSuccess] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    getLinkedLearners()
      .then(setLearners)
      .catch((err: unknown) => { setError(err instanceof ApiError ? err.message : "Failed to load learners"); })
      .finally(() => { setLoading(false); });
  }, []);

  async function handleLink(e: FormEvent) {
    e.preventDefault();
    if (!linkEmail.trim()) return;
    setLinking(true);
    setLinkError(null);
    setLinkSuccess(null);
    try {
      await linkLearner(linkEmail.trim());
      setLinkSuccess(`Linked ${linkEmail.trim()} successfully.`);
      setLinkEmail("");
      const updated = await getLinkedLearners();
      setLearners(updated);
    } catch (err) {
      setLinkError(err instanceof ApiError ? err.message : "Failed to link learner");
    } finally {
      setLinking(false);
      inputRef.current?.focus();
    }
  }

  return (
    <main className="min-h-screen bg-gray-950 p-6">
      <div className="mx-auto max-w-3xl space-y-8">
        <div>
          <h1 className="text-2xl font-bold text-white">Parent Dashboard</h1>
          <p className="mt-1 text-sm text-gray-400">
            Welcome back, {account?.display_name ?? account?.email}
          </p>
        </div>

        <section className="rounded-2xl border border-gray-800 bg-gray-900 p-6">
          <h2 className="mb-4 text-sm font-semibold uppercase tracking-wider text-gray-400">
            Add a Learner
          </h2>
          <form onSubmit={(e) => void handleLink(e)} className="flex gap-3">
            <input
              ref={inputRef}
              type="email"
              placeholder="Learner's email address"
              value={linkEmail}
              onChange={(e) => {
                setLinkEmail(e.target.value);
                setLinkError(null);
                setLinkSuccess(null);
              }}
              required
              className="min-w-0 flex-1 rounded-lg border border-gray-700 bg-gray-800 px-4 py-2 text-sm text-white placeholder-gray-500 outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
            />
            <Button type="submit" loading={linking} disabled={!linkEmail.trim()}>
              Link
            </Button>
          </form>
          {linkError && <p className="mt-2 text-xs text-red-400">{linkError}</p>}
          {linkSuccess && <p className="mt-2 text-xs text-green-400">{linkSuccess}</p>}
          <p className="mt-3 text-xs text-gray-600">
            The learner must already have a PyQuest account. Enter their sign-up email.
          </p>
        </section>

        <section>
          <h2 className="mb-4 text-sm font-semibold uppercase tracking-wider text-gray-400">
            Your Learners
          </h2>

          {loading && (
            <p className="text-sm text-gray-500">Loading…</p>
          )}

          {error && (
            <p className="text-sm text-red-400">{error}</p>
          )}

          {!loading && !error && learners.length === 0 && (
            <div className="rounded-2xl border border-dashed border-gray-700 p-8 text-center">
              <p className="text-sm text-gray-500">No learners linked yet.</p>
              <p className="mt-1 text-xs text-gray-600">
                Use the form above to connect a learner's account.
              </p>
            </div>
          )}

          {learners.length > 0 && (
            <div className="grid gap-4 sm:grid-cols-2">
              {learners.map((l) => (
                <LearnerCard key={l.id} learner={l} />
              ))}
            </div>
          )}
        </section>
      </div>
    </main>
  );
}
