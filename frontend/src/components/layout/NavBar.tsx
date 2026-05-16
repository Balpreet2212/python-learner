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

  const isParent = account?.role === "parent";
  const world = (profile?.world ?? "fantasy") as World;
  const style = getStyle(world);
  const worldLabel = isParent ? "Parent Dashboard" : (WORLD_LABELS[world] ?? "PyQuest");

  const onLesson = location.pathname === "/lesson";
  const onCapstone = location.pathname === "/capstone";
  const onLessonOrCapstone = onLesson || onCapstone;

  async function handleLogout() {
    try {
      await logout();
    } catch {
      // ignore network errors on logout
    }
    clearAuth();
    navigate("/auth/login");
  }

  // Parent nav is minimal — no world theming, no progress
  const navSurface = isParent ? "bg-gray-900" : style.surface;
  const navAccent = isParent ? "text-indigo-400" : style.accent;
  const navMuted = isParent ? "text-gray-400" : style.muted;
  const navText = isParent ? "text-gray-200" : style.text;

  return (
    <nav className={`${navSurface} border-b border-white/10 px-4 py-2`}>
      <div className="mx-auto flex max-w-5xl items-center justify-between gap-4">
        {/* Left: logo + context label */}
        <div className="flex items-center gap-3 min-w-0">
          <button
            onClick={() => navigate(isParent ? "/parent" : "/")}
            className={`text-lg font-bold ${navAccent} shrink-0`}
          >
            PyQuest
          </button>
          <span className={`hidden text-xs sm:block ${navMuted}`}>·</span>
          <span className={`hidden text-xs sm:block truncate ${navMuted}`}>{worldLabel}</span>
        </div>

        {/* Center: lesson progress (learners only, on lesson/capstone page) */}
        {!isParent && onLessonOrCapstone && profile && (
          <div className="flex flex-col items-center gap-0.5">
            {onCapstone ? (
              <span className={`text-xs ${style.muted}`}>
                Unit {profile.current_unit} · Capstone ★
              </span>
            ) : (
              <span className={`text-xs ${style.muted}`}>
                Unit {profile.current_unit} · Lesson {profile.current_lesson} / 5
              </span>
            )}
            <LessonPips total={5} current={onCapstone ? 6 : profile.current_lesson} />
          </div>
        )}

        {/* Right: nav link + badges + name + logout */}
        <div className="flex items-center gap-3 shrink-0">
          {isParent ? (
            <button
              onClick={() => navigate("/parent")}
              className={`hidden text-xs sm:block ${navMuted} hover:${navText} transition-colors`}
            >
              Dashboard
            </button>
          ) : onLessonOrCapstone ? (
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

          {!isParent && profile && profile.badges.length > 0 && (
            <span className={`text-xs ${style.muted}`} title="Badges earned">
              🏅 {profile.badges.length}
            </span>
          )}

          <span className={`hidden text-xs md:block ${navMuted} truncate max-w-[120px]`}>
            {account?.display_name ?? account?.email}
          </span>

          <button
            onClick={() => void handleLogout()}
            className={`text-xs ${navMuted} hover:text-red-400 transition-colors`}
          >
            Sign out
          </button>
        </div>
      </div>
    </nav>
  );
}
