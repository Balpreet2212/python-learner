import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { logout, deleteAccount } from "../api/auth";
import { resetProgress } from "../api/learner";
import Button from "../components/ui/Button";
import { useState } from "react";
import { ApiError } from "../api/client";

export default function AccountPage() {
  const { account, profile, clearAuth, setProfile } = useAuth();
  const navigate = useNavigate();
  const [signingOut, setSigningOut] = useState(false);
  const [resetting, setResetting] = useState(false);
  const [resetDone, setResetDone] = useState(false);
  const [deleting, setDeleting] = useState(false);

  async function handleSignOut() {
    setSigningOut(true);
    try {
      await logout();
    } catch (err) {
      if (!(err instanceof ApiError)) throw err;
    } finally {
      clearAuth();
      navigate("/auth/login");
    }
  }

  async function handleDelete() {
    if (!confirm("Permanently delete your account and all data? This cannot be undone.")) return;
    setDeleting(true);
    try {
      await deleteAccount();
      clearAuth();
      navigate("/auth/login");
    } catch {
      // ignore — user stays on page if request fails
    } finally {
      setDeleting(false);
    }
  }

  async function handleReset() {
    if (!confirm("Reset progress to Unit 1, Lesson 1? This cannot be undone.")) return;
    setResetting(true);
    setResetDone(false);
    try {
      const updated = await resetProgress();
      setProfile(updated);
      setResetDone(true);
    } catch {
      // ignore
    } finally {
      setResetting(false);
    }
  }

  const WORLD_LABEL: Record<string, string> = {
    fantasy: "Enchanted Realm",
    scifi: "Starship Command",
    mystery: "Detective Agency",
  };

  const TRACK_LABEL: Record<string, string> = {
    junior: "Junior",
    core: "Core",
  };

  return (
    <div className="mx-auto max-w-xl p-6 space-y-8">
        <h1 className="text-2xl font-bold">Account</h1>

        {/* Account info */}
        <section className="rounded-2xl border border-gray-700 bg-gray-900 divide-y divide-gray-800">
          {account?.display_name && (
            <Row label="Display name" value={account.display_name} />
          )}
          <Row label="Email" value={account?.email ?? ""} />
          <Row label="Role" value={account?.role === "learner" ? "Learner" : "Parent"} />
          {profile && (
            <>
              <Row label="World" value={WORLD_LABEL[profile.world] ?? profile.world} />
              <Row label="Track" value={TRACK_LABEL[profile.track] ?? profile.track} />
            </>
          )}
        </section>

        {/* Progress reset */}
        {profile && (
          <section className="space-y-3">
            <h2 className="text-sm font-semibold uppercase tracking-wider text-gray-400">Progress</h2>
            <Button
              variant="ghost"
              loading={resetting}
              onClick={() => void handleReset()}
              className="w-full border border-gray-700 hover:border-yellow-500 hover:text-yellow-400"
            >
              Reset progress to Unit 1
            </Button>
            {resetDone && (
              <p className="text-center text-xs text-green-400">Progress reset — you're back at Unit 1, Lesson 1.</p>
            )}
          </section>
        )}

        {/* Session */}
        <section className="space-y-3">
          <h2 className="text-sm font-semibold uppercase tracking-wider text-gray-400">Session</h2>
          <Button
            variant="ghost"
            loading={signingOut}
            onClick={() => void handleSignOut()}
            className="w-full border border-gray-700 hover:border-red-500 hover:text-red-400"
          >
            Sign out
          </Button>
        </section>

        {/* Danger zone */}
        <section className="space-y-3">
          <h2 className="text-sm font-semibold uppercase tracking-wider text-red-700">Danger zone</h2>
          <Button
            variant="ghost"
            loading={deleting}
            onClick={() => void handleDelete()}
            className="w-full border border-red-900 text-red-500 hover:border-red-500 hover:text-red-300"
          >
            Delete account
          </Button>
          <p className="text-center text-xs text-gray-600">
            Permanently deletes your account and all associated data.
          </p>
        </section>
    </div>
  );
}

function Row({ label, value }: { label: string; value: string }) {
  return (
    <div className="flex items-center justify-between px-5 py-4">
      <p className="text-sm text-gray-400">{label}</p>
      <p className="text-sm font-medium text-white">{value}</p>
    </div>
  );
}
