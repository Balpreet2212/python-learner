import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

type World = "fantasy" | "scifi" | "mystery";

const WORLD_META: Record<
  World,
  { bg: string; surface: string; accent: string; highlight: string; text: string; muted: string }
> = {
  fantasy: {
    bg: "bg-fantasy-bg",
    surface: "bg-fantasy-surface",
    accent: "text-fantasy-accent",
    highlight: "text-fantasy-highlight",
    text: "text-fantasy-text",
    muted: "text-fantasy-text/60",
  },
  scifi: {
    bg: "bg-scifi-bg",
    surface: "bg-scifi-surface",
    accent: "text-scifi-accent",
    highlight: "text-scifi-highlight",
    text: "text-scifi-text",
    muted: "text-scifi-text/60",
  },
  mystery: {
    bg: "bg-mystery-bg",
    surface: "bg-mystery-surface",
    accent: "text-mystery-accent",
    highlight: "text-mystery-highlight",
    text: "text-mystery-text",
    muted: "text-mystery-text/60",
  },
};

const UNIT_NAMES: Record<World, string[]> = {
  fantasy: [
    "The Sorcerer's Variables",
    "Loops of Fate",
    "The Function Grimoire",
    "Data Dungeon",
    "The Exception Keep",
    "Kingdom of Classes",
  ],
  scifi: [
    "Boot Sequence",
    "Orbital Loops",
    "Subroutine Nexus",
    "Cargo Manifest",
    "Error Core",
    "AI Uprising",
  ],
  mystery: [
    "The First Clue",
    "Looping Leads",
    "The Informant",
    "Evidence Files",
    "The Alibi Error",
    "The Final Case",
  ],
};

const UNIT_LESSONS = 5;

function UnitCard({
  unitIndex,
  name,
  unlocked,
  current,
  completed,
  style,
  onStart,
}: {
  unitIndex: number;
  name: string;
  unlocked: boolean;
  current: boolean;
  completed: boolean;
  style: (typeof WORLD_META)[World];
  onStart: () => void;
}) {
  const number = unitIndex + 1;

  return (
    <div
      className={`rounded-2xl border-2 p-6 transition-all ${
        completed
          ? `${style.surface} border-green-700`
          : current
            ? `${style.surface} border-2 ${style.accent.replace("text-", "border-")}`
            : unlocked
              ? `${style.surface} border-gray-700`
              : "border-gray-800 bg-gray-900 opacity-50"
      }`}
    >
      <div className="flex items-start justify-between">
        <div>
          <span className={`text-xs font-semibold uppercase tracking-widest ${style.muted}`}>
            Unit {number}
          </span>
          <h2
            className={`mt-1 text-lg font-bold ${
              completed ? "text-green-400" : unlocked ? style.highlight : "text-gray-500"
            }`}
          >
            {name}
          </h2>
          <p className={`mt-1 text-sm ${style.muted}`}>{UNIT_LESSONS} lessons</p>
        </div>
        <div className="text-3xl">
          {completed ? "✅" : current ? "⚡" : unlocked ? "🔓" : "🔒"}
        </div>
      </div>

      {unlocked && !completed && (
        <button
          onClick={onStart}
          className={`mt-4 w-full rounded-lg py-2 text-sm font-semibold transition-colors ${
            current
              ? `${style.accent.replace("text-", "bg-").replace("accent", "surface")} bg-indigo-600 text-white hover:bg-indigo-500`
              : "bg-gray-700 text-white hover:bg-gray-600"
          }`}
        >
          {current ? "Continue" : "Start Unit"}
        </button>
      )}
      {completed && (
        <p className="mt-4 text-center text-xs font-medium text-green-400">Complete!</p>
      )}
    </div>
  );
}

export default function WorldMapPage() {
  const { account, profile } = useAuth();
  const navigate = useNavigate();

  if (!account || !profile) {
    return null;
  }

  const world = (profile.world || "fantasy") as World;
  const style = WORLD_META[world] ?? WORLD_META.fantasy;
  const unitNames = UNIT_NAMES[world] ?? UNIT_NAMES.fantasy;
  const currentUnit = profile.current_unit || 1;

  return (
    <main className={`min-h-screen p-6 ${style.bg}`}>
      {/* Page heading */}
      <div className="mx-auto mb-6 max-w-2xl">
        <h1 className={`text-xl font-bold ${style.highlight}`}>World Map</h1>
        <p className={`text-sm ${style.muted}`}>
          {profile.track === "junior" ? "Junior" : "Core"} track · Unit {currentUnit}
        </p>
      </div>

      {/* Unit grid */}
      <div className="mx-auto grid max-w-2xl gap-4 sm:grid-cols-2">
        {unitNames.map((name, i) => {
          const unitNumber = i + 1;
          const completed = unitNumber < currentUnit;
          const current = unitNumber === currentUnit;
          const unlocked = unitNumber <= currentUnit;

          return (
            <UnitCard
              key={i}
              unitIndex={i}
              name={name}
              unlocked={unlocked}
              current={current}
              completed={completed}
              style={style}
              onStart={() => navigate("/lesson")}
            />
          );
        })}
      </div>
    </main>
  );
}
