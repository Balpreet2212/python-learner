import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { postOnboarding } from "../api/learner";
import { ApiError } from "../api/client";
import Button from "../components/ui/Button";

type World = "fantasy" | "scifi" | "mystery";
type Track = "junior" | "core";

const WORLD_OPTIONS: { value: World; label: string; description: string }[] = [
  { value: "fantasy", label: "Enchanted Realm", description: "Spells, guilds, and magical artifacts" },
  { value: "scifi", label: "Starship Command", description: "Space stations, droids, and alien worlds" },
  { value: "mystery", label: "Detective Agency", description: "Cases, clues, and hidden secrets" },
];

const TRACK_OPTIONS: { value: Track; label: string; description: string }[] = [
  { value: "junior", label: "Junior", description: "Gentler pacing, more guidance (grades 5–7)" },
  { value: "core", label: "Core", description: "Standard pacing, full curriculum (grades 7–12)" },
];

export default function SettingsPage() {
  const { profile, setProfile } = useAuth();
  const navigate = useNavigate();

  const [world, setWorld] = useState<World>((profile?.world ?? "fantasy") as World);
  const [track, setTrack] = useState<Track>((profile?.track ?? "junior") as Track);
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const hasChanges = world !== profile?.world || track !== profile.track;

  async function handleSave() {
    setSaving(true);
    setSaved(false);
    setError(null);
    try {
      const updated = await postOnboarding(track, world);
      setProfile(updated);
      setSaved(true);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Failed to save settings.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <main className="min-h-screen bg-gray-950 text-gray-100">
      <div className="mx-auto max-w-xl p-6 space-y-8">
        <div className="flex items-center gap-3">
          <button
            onClick={() => { navigate("/"); }}
            className="text-gray-500 hover:text-gray-300 transition-colors text-sm"
          >
            ← Home
          </button>
          <h1 className="text-2xl font-bold">Settings</h1>
        </div>

        {/* World */}
        <section className="space-y-3">
          <h2 className="text-sm font-semibold uppercase tracking-wider text-gray-400">World Theme</h2>
          <div className="space-y-2">
            {WORLD_OPTIONS.map((opt) => (
              <button
                key={opt.value}
                onClick={() => { setWorld(opt.value); setSaved(false); }}
                className={`w-full rounded-xl border-2 p-4 text-left transition-all ${
                  world === opt.value
                    ? "border-indigo-500 bg-indigo-950/60"
                    : "border-gray-700 bg-gray-900 hover:border-gray-500"
                }`}
              >
                <p className="font-semibold text-white">{opt.label}</p>
                <p className="mt-0.5 text-sm text-gray-400">{opt.description}</p>
              </button>
            ))}
          </div>
        </section>

        {/* Track */}
        <section className="space-y-3">
          <h2 className="text-sm font-semibold uppercase tracking-wider text-gray-400">Learning Track</h2>
          <div className="space-y-2">
            {TRACK_OPTIONS.map((opt) => (
              <button
                key={opt.value}
                onClick={() => { setTrack(opt.value); setSaved(false); }}
                className={`w-full rounded-xl border-2 p-4 text-left transition-all ${
                  track === opt.value
                    ? "border-indigo-500 bg-indigo-950/60"
                    : "border-gray-700 bg-gray-900 hover:border-gray-500"
                }`}
              >
                <p className="font-semibold text-white">{opt.label}</p>
                <p className="mt-0.5 text-sm text-gray-400">{opt.description}</p>
              </button>
            ))}
          </div>
        </section>

        {error && <p className="text-sm text-red-400">{error}</p>}
        {saved && <p className="text-sm text-green-400">Settings saved.</p>}

        <Button
          onClick={() => void handleSave()}
          loading={saving}
          disabled={!hasChanges}
          className="w-full"
        >
          Save Changes
        </Button>
      </div>
    </main>
  );
}
