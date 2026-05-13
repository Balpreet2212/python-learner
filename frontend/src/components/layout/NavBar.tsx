import { useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { logout } from "../../api/auth";

type World = "fantasy" | "scifi" | "mystery";

const WORLD_STYLE: Record<World, { surface: string; text: string; muted: string; accent: string; pip: string }> = {
  fantasy: {
    surface: "bg-fantasy-surface",
    text: "text-fantasy-text",
    muted: "text-fantasy-text/60",
    accent: "text-fantasy-highlight",
    pip: "bg-fantasy-accent",
  },
  scifi: {
    surface: "bg-scifi-surface",
    text: "text-scifi-text",
    muted: "text-scifi-text/60",
    accent: "text-scifi-highlight",
    pip: "bg-scifi-accent",
  },
  mystery: {
    surface: "bg-mystery-surface",
    text: "text-mystery-text",
    muted: "text-mystery-text/60",
    accent: "text-mystery-highlight",
    pip: "bg-mystery-accent",
  },
};

const WORLD_LABELS: Record<World, string> = {
  fantasy: "Enchanted Realm",
  scifi: "Starship Command",
  mystery: "Detective Agency",
};

function getStyle(world: string) {
  return WORLD_STYLE[(world as World) in WORLD_STYLE ? (world as World) : "fantasy"];
}

function LessonPips({ total, current }: { total: number; current: number }) {
  const style = useAuth().profile?.world ?? "fantasy";
  const s = getStyle(style);
  return (
    <div className="flex items-center gap-1">
      {Array.from({ length: total }, (_, i) => (
        <span
          key={i}
          className={`h-1.5 w-4 rounded-full transition-all ${
            i < current - 1
              ? "bg-green-500"
              : i === current - 1
                ? s.pip
                : "bg-gray-700"
          }`}
        />
      ))}
    </div>
  );
}

export default function NavBar() {
  const { account, profile, clearAuth } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const world = (profile?.world ?? "fantasy") as World;
  const style = getStyle(world);
  const worldLabel = WORLD_LABELS[world] ?? "PyQuest";

  const onLesson = location.pathname === "/lesson";

  async function handleLogout() {
    try {
      await logout();
    } catch {
      // ignore network errors on logout
    }
    clearAuth();
    navigate("/auth/login");
  }

  return (
    <nav className={`${style.surface} border-b border-white/10 px-4 py-2`}>
      <div className="mx-auto flex max-w-5xl items-center justify-between gap-4">
        {/* Left: logo + world */}
        <div className="flex items-center gap-3 min-w-0">
          <button
            onClick={() => navigate("/")}
            className={`text-lg font-bold ${style.accent} shrink-0`}
          >
            PyQuest
          </button>
          <span className={`hidden text-xs sm:block ${style.muted}`}>·</span>
          <span className={`hidden text-xs sm:block truncate ${style.muted}`}>{worldLabel}</span>
        </div>

        {/* Center: progress (only on lesson page) */}
        {onLesson && profile && (
          <div className="flex flex-col items-center gap-0.5">
            <span className={`text-xs ${style.muted}`}>
              Unit {profile.current_unit} · Lesson {profile.current_lesson} / 5
            </span>
            <LessonPips total={5} current={profile.current_lesson} />
          </div>
        )}

        {/* Right: map link + badges + name + logout */}
        <div className="flex items-center gap-3 shrink-0">
          {onLesson ? (
            <button
              onClick={() => navigate("/")}
              className={`hidden text-xs sm:block ${style.muted} hover:${style.text} transition-colors`}
            >
              World Map
            </button>
          ) : (
            profile && (
              <button
                onClick={() => navigate("/lesson")}
                className={`hidden text-xs sm:block ${style.muted} hover:${style.text} transition-colors`}
              >
                Continue Lesson
              </button>
            )
          )}

          {profile && profile.badges.length > 0 && (
            <span className={`text-xs ${style.muted}`} title="Badges earned">
              🏅 {profile.badges.length}
            </span>
          )}

          <span className={`hidden text-xs md:block ${style.muted} truncate max-w-[120px]`}>
            {account?.display_name ?? account?.email}
          </span>

          <button
            onClick={() => void handleLogout()}
            className={`text-xs ${style.muted} hover:text-red-400 transition-colors`}
          >
            Sign out
          </button>
        </div>
      </div>
    </nav>
  );
}
