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

const WORLD_LABEL: Record<World, string> = {
  fantasy: "Enchanted Realm",
  scifi: "Starship Command",
  mystery: "Detective Agency",
};

const NAV_CARDS = [
  {
    icon: "🗺️",
    label: "Continue Learning",
    description: "Pick up where you left off on the world map.",
    path: "/learn",
  },
  {
    icon: "⭐",
    label: "Weekly Challenge",
    description: "A fresh coding puzzle every week. Earn bonus XP.",
    path: "/weekly",
  },
  {
    icon: "⚙️",
    label: "Settings",
    description: "Change your learning track or world theme.",
    path: "/settings",
  },
  {
    icon: "💳",
    label: "Billing",
    description: "View your plan and subscription details.",
    path: "/billing",
  },
  {
    icon: "👤",
    label: "Account",
    description: "Manage your email, display name, and security.",
    path: "/account",
  },
] as const;

export default function HomePage() {
  const { account, profile } = useAuth();
  const navigate = useNavigate();

  const world = (profile?.world ?? "fantasy") as World;
  const theme = WORLD_THEME[world];
  const displayName = account?.display_name ?? account?.email ?? "";

  return (
    <main className={`min-h-screen ${theme.bg}`}>
      <div className="mx-auto max-w-2xl p-6 space-y-8">
        {/* Welcome header */}
        <div className="pt-4">
          <p className={`text-sm ${theme.muted}`}>{WORLD_LABEL[world]}</p>
          <h1 className={`mt-1 text-3xl font-bold ${theme.highlight}`}>
            Welcome back{displayName ? `, ${displayName.split("@")[0]}` : ""}
          </h1>
          {profile && (
            <p className={`mt-1 text-sm ${theme.muted}`}>
              Unit {profile.current_unit} · Lesson {profile.current_lesson}
              {profile.badges.length > 0 && ` · 🏅 ${String(profile.badges.length)}`}
            </p>
          )}
        </div>

        {/* Nav cards */}
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
          {NAV_CARDS.map((card) => (
            <button
              key={card.path}
              onClick={() => { navigate(card.path); }}
              className={`flex items-start gap-4 rounded-2xl border ${theme.border} ${theme.surface} p-5 text-left transition-all hover:brightness-110 active:scale-[0.98]`}
            >
              <span className="text-3xl leading-none">{card.icon}</span>
              <div className="min-w-0 flex-1">
                <p className={`font-semibold ${theme.highlight}`}>{card.label}</p>
                <p className={`mt-0.5 text-sm ${theme.muted}`}>{card.description}</p>
              </div>
              <span className={`shrink-0 text-xl ${theme.accent}`}>›</span>
            </button>
          ))}
        </div>
      </div>
    </main>
  );
}
