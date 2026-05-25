import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

type World = "fantasy" | "scifi" | "mystery";

const WORLD_THEME: Record<
  World,
  { bg: string; surface: string; border: string; highlight: string; text: string; muted: string; accent: string }
> = {
  fantasy: {
    bg: "bg-fantasy-bg",
    surface: "bg-fantasy-surface",
    border: "border-fantasy-accent/30",
    highlight: "text-fantasy-highlight",
    text: "text-fantasy-text",
    muted: "text-fantasy-text/60",
    accent: "text-fantasy-accent",
  },
  scifi: {
    bg: "bg-scifi-bg",
    surface: "bg-scifi-surface",
    border: "border-scifi-accent/30",
    highlight: "text-scifi-highlight",
    text: "text-scifi-text",
    muted: "text-scifi-text/60",
    accent: "text-scifi-accent",
  },
  mystery: {
    bg: "bg-mystery-bg",
    surface: "bg-mystery-surface",
    border: "border-mystery-accent/30",
    highlight: "text-mystery-highlight",
    text: "text-mystery-text",
    muted: "text-mystery-text/60",
    accent: "text-mystery-accent",
  },
};

export default function ChallengesPage() {
  const { profile } = useAuth();
  const navigate = useNavigate();

  const world = (profile?.world ?? "fantasy") as World;
  const theme = WORLD_THEME[world];

  return (
    <main className={`min-h-screen ${theme.bg}`}>
      <div className="mx-auto max-w-2xl p-6 space-y-8">
        <div className="pt-4">
          <h1 className={`text-3xl font-bold ${theme.highlight}`}>Challenges</h1>
          <p className={`mt-1 text-sm ${theme.muted}`}>
            Logic puzzles and coding problems to sharpen your skills.
          </p>
        </div>

        <div className="grid grid-cols-1 gap-4">
          {/* Daily — stub */}
          <div
            className={`flex items-center gap-6 rounded-2xl border border-gray-700/40 bg-gray-800/30 p-8 opacity-60 cursor-not-allowed select-none`}
          >
            <span className="text-5xl leading-none">📅</span>
            <div className="min-w-0 flex-1">
              <div className="flex items-center gap-3">
                <p className="text-xl font-bold text-gray-400">Daily Challenge</p>
                <span className="rounded-full bg-gray-700 px-2.5 py-0.5 text-xs font-semibold text-gray-400">
                  Coming soon
                </span>
              </div>
              <p className="mt-1 text-sm text-gray-500">
                A new logic puzzle every day. Streaks, hints, and leaderboards.
              </p>
            </div>
          </div>

          {/* Weekly */}
          <button
            onClick={() => { navigate("/weekly"); }}
            className={`flex items-center gap-6 rounded-2xl border ${theme.border} ${theme.surface} p-8 text-left transition-all hover:brightness-110 active:scale-[0.98]`}
          >
            <span className="text-5xl leading-none">⭐</span>
            <div className="min-w-0 flex-1">
              <p className={`text-xl font-bold ${theme.highlight}`}>Weekly Challenge</p>
              <p className={`mt-1 text-sm ${theme.muted}`}>
                A fresh logic problem each week. Earn bonus XP for completing it.
              </p>
            </div>
            <span className={`shrink-0 text-2xl ${theme.accent}`}>›</span>
          </button>
        </div>
      </div>
    </main>
  );
}
