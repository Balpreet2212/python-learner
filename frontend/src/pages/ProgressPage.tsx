import { useAuth } from "../context/AuthContext";

const UNIT_NAMES: Record<number, string> = {
  1: "Python Basics",
  2: "Numbers & Booleans",
  3: "Conditionals",
  4: "Loops",
  5: "Functions",
  6: "Lists",
  7: "Classes",
};

const WORLD_LABEL: Record<string, string> = {
  fantasy: "Enchanted Realm",
  scifi: "Starship Command",
  mystery: "Detective Agency",
};

const TOTAL_UNITS = 7;
const LESSONS_PER_UNIT = 5;
const XP_PER_LESSON = 10;
const XP_PER_CAPSTONE = 150;
const XP_PER_UNIT = LESSONS_PER_UNIT * XP_PER_LESSON + XP_PER_CAPSTONE;

function parseBadgeUnit(badge: string): number | null {
  const m = badge.match(/^unit_(\d+)_complete$/);
  return m ? parseInt(m[1], 10) : null;
}

export default function ProgressPage() {
  const { profile } = useAuth();

  if (!profile) {
    return (
      <div className="mx-auto max-w-xl p-6">
        <p className="text-gray-400">No progress data available.</p>
      </div>
    );
  }

  const completedUnits = profile.badges
    .map(parseBadgeUnit)
    .filter((n): n is number => n !== null)
    .sort((a, b) => a - b);

  const lessonsCompletedInCurrentUnit = profile.current_lesson - 1;
  const totalXp =
    completedUnits.length * XP_PER_UNIT +
    lessonsCompletedInCurrentUnit * XP_PER_LESSON;

  // Overall progress: (completed units * 6 steps) + lessons done in current unit
  // Each unit = 5 lessons + 1 capstone = 6 steps; total = 42
  const totalSteps = TOTAL_UNITS * (LESSONS_PER_UNIT + 1);
  const doneSteps =
    completedUnits.length * (LESSONS_PER_UNIT + 1) + lessonsCompletedInCurrentUnit;
  const progressPct = Math.round((doneSteps / totalSteps) * 100);

  return (
    <div className="mx-auto max-w-xl p-6 space-y-8">
      <h1 className="text-2xl font-bold">Progress</h1>

      {/* XP summary */}
      <section className="rounded-2xl border border-yellow-700/40 bg-yellow-950/20 p-6 flex items-center gap-5">
        <div className="text-5xl select-none">⭐</div>
        <div>
          <p className="text-3xl font-bold text-yellow-300">{totalXp.toLocaleString()} XP</p>
          <p className="text-sm text-gray-400 mt-1">
            {WORLD_LABEL[profile.world] ?? profile.world} &middot; {profile.track === "junior" ? "Junior" : "Core"} track
          </p>
        </div>
      </section>

      {/* Journey progress */}
      <section className="space-y-4">
        <h2 className="text-sm font-semibold uppercase tracking-wider text-gray-400">Journey</h2>
        <div className="rounded-2xl border border-gray-700 bg-gray-900 p-6 space-y-4">
          <div className="flex items-baseline justify-between">
            <p className="font-semibold text-white">
              Unit {profile.current_unit} &middot; Lesson {profile.current_lesson}
            </p>
            <p className="text-sm text-gray-400">{progressPct}% complete</p>
          </div>
          <div className="h-2.5 w-full rounded-full bg-gray-800 overflow-hidden">
            <div
              className="h-full rounded-full bg-gradient-to-r from-indigo-500 to-purple-500 transition-all"
              style={{ width: `${progressPct}%` }}
            />
          </div>
          <div className="flex justify-between text-xs text-gray-500">
            <span>Unit 1</span>
            <span>Unit 7</span>
          </div>
          {profile.current_unit <= TOTAL_UNITS && (
            <p className="text-sm text-gray-400">
              Currently studying:{" "}
              <span className="text-white font-medium">
                {UNIT_NAMES[profile.current_unit] ?? `Unit ${profile.current_unit}`}
              </span>
            </p>
          )}
        </div>
      </section>

      {/* Badges */}
      <section className="space-y-4">
        <h2 className="text-sm font-semibold uppercase tracking-wider text-gray-400">
          Badges{" "}
          <span className="normal-case font-normal text-gray-600">
            {completedUnits.length} / {TOTAL_UNITS}
          </span>
        </h2>

        {completedUnits.length === 0 ? (
          <div className="rounded-2xl border border-gray-700 bg-gray-900 p-8 text-center text-gray-500 text-sm">
            Complete your first unit to earn a badge!
          </div>
        ) : (
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
            {completedUnits.map((unit) => (
              <BadgeCard key={unit} unit={unit} />
            ))}
          </div>
        )}

        {/* Locked badges */}
        {TOTAL_UNITS - completedUnits.length > 0 && (
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
            {Array.from({ length: TOTAL_UNITS }, (_, i) => i + 1)
              .filter((u) => !completedUnits.includes(u))
              .map((unit) => (
                <LockedBadgeCard key={unit} unit={unit} />
              ))}
          </div>
        )}
      </section>
    </div>
  );
}

function BadgeCard({ unit }: { unit: number }) {
  return (
    <div className="rounded-xl border border-yellow-700/50 bg-yellow-950/30 p-4 text-center space-y-2">
      <div className="text-3xl select-none">🏅</div>
      <p className="text-xs font-semibold text-yellow-300">Unit {unit} Complete</p>
      <p className="text-xs text-gray-400 leading-snug">
        {UNIT_NAMES[unit] ?? `Unit ${unit}`}
      </p>
    </div>
  );
}

function LockedBadgeCard({ unit }: { unit: number }) {
  return (
    <div className="rounded-xl border border-gray-800 bg-gray-900/50 p-4 text-center space-y-2 opacity-40">
      <div className="text-3xl select-none">🔒</div>
      <p className="text-xs font-semibold text-gray-500">Unit {unit}</p>
      <p className="text-xs text-gray-600 leading-snug">
        {UNIT_NAMES[unit] ?? `Unit ${unit}`}
      </p>
    </div>
  );
}
