import { useState, useEffect, useRef, type FormEvent } from "react";
import { useAuth } from "../context/AuthContext";
import { getLinkedLearners, linkLearner, type LearnerSummary } from "../api/parent";
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

const WORLD_COLOR: Record<string, string> = {
  fantasy: "text-purple-400 border-purple-700",
  scifi: "text-cyan-400 border-cyan-700",
  mystery: "text-amber-400 border-amber-700",
};

function ProgressBar({ value, max }: { value: number; max: number }) {
  const pct = max === 0 ? 0 : Math.round((value / max) * 100);
  return (
    <div className="h-1.5 w-full overflow-hidden rounded-full bg-gray-700">
      <div
        className="h-full rounded-full bg-indigo-500 transition-all"
        style={{ width: `${pct}%` }}
      />
    </div>
  );
}

function LearnerCard({ learner }: { learner: LearnerSummary }) {
  const totalLessons = learner.total_units * learner.total_lessons_per_unit;
  const completedLessons =
    (learner.current_unit - 1) * learner.total_lessons_per_unit +
    (learner.current_lesson - 1);
  const worldColor = WORLD_COLOR[learner.world] ?? "text-gray-400 border-gray-700";

  return (
    <div className={`rounded-2xl border bg-gray-900 p-5 ${worldColor.split(" ")[1]}`}>
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
          <span className={worldColor.split(" ")[0]}>
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
      .catch((err) => setError(err instanceof ApiError ? err.message : "Failed to load learners"))
      .finally(() => setLoading(false));
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
      // Reload learner list
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
        {/* Header */}
        <div>
          <h1 className="text-2xl font-bold text-white">Parent Dashboard</h1>
          <p className="mt-1 text-sm text-gray-400">
            Welcome back, {account?.display_name ?? account?.email}
          </p>
        </div>

        {/* Link a learner */}
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

        {/* Learner list */}
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
