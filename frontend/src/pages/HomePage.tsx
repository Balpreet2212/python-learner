import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { logout } from "../api/auth";
import { ApiError } from "../api/client";
import Button from "../components/ui/Button";

export default function HomePage() {
  const { account, clearAuth } = useAuth();
  const navigate = useNavigate();
  const [loggingOut, setLoggingOut] = useState(false);

  async function handleLogout() {
    setLoggingOut(true);
    try {
      await logout();
    } catch (err) {
      if (!(err instanceof ApiError)) throw err;
    } finally {
      clearAuth();
      navigate("/auth/login");
    }
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-6 p-8">
      <h1 className="text-5xl font-bold tracking-tight">PyQuest</h1>
      <p className="text-lg text-gray-400">
        A story-driven Python learning platform for grades 5–12
      </p>

      {account && (
        <div className="flex flex-col items-center gap-3 rounded-xl border border-gray-700 bg-gray-900 p-6 text-center">
          <p className="text-gray-300">
            Signed in as{" "}
            <span className="font-medium text-white">
              {account.display_name ?? account.email}
            </span>
          </p>
          <p className="text-xs text-gray-500">
            Role: {account.role} · Track and world: set during onboarding (M3)
          </p>
          <Button
            variant="ghost"
            loading={loggingOut}
            onClick={() => void handleLogout()}
          >
            Sign out
          </Button>
        </div>
      )}

      <p className="text-xs text-gray-600">
        M2 checkpoint — auth working. Onboarding and lesson view come in M3–M4.
      </p>
    </main>
  );
}
