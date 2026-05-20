import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { logout } from "../api/auth";
import Button from "../components/ui/Button";
import { useState } from "react";
import { ApiError } from "../api/client";

export default function AccountPage() {
  const { account, profile, clearAuth } = useAuth();
  const navigate = useNavigate();
  const [signingOut, setSigningOut] = useState(false);

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
    <main className="min-h-screen bg-gray-950 text-gray-100">
      <div className="mx-auto max-w-xl p-6 space-y-8">
        <div className="flex items-center gap-3">
          <button
            onClick={() => { navigate("/"); }}
            className="text-gray-500 hover:text-gray-300 transition-colors text-sm"
          >
            ← Home
          </button>
          <h1 className="text-2xl font-bold">Account</h1>
        </div>

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

        {/* Danger zone */}
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
      </div>
    </main>
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
