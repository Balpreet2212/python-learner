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
          {/* Daily */}
          <button
            onClick={() => { navigate("/daily"); }}
            className={`flex items-center gap-6 rounded-2xl border ${theme.border} ${theme.surface} p-8 text-left transition-all hover:brightness-110 active:scale-[0.98]`}
          >
            <span className="text-5xl leading-none">📅</span>
            <div className="min-w-0 flex-1">
              <p className={`text-xl font-bold ${theme.highlight}`}>Daily Challenge</p>
              <p className={`mt-1 text-sm ${theme.muted}`}>
                A fresh coding puzzle every day. Earn bonus XP for completing it.
              </p>
            </div>
            <span className={`shrink-0 text-2xl ${theme.accent}`}>›</span>
          </button>

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
