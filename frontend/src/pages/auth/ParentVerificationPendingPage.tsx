import { useEffect, useState } from "react";
import { useSearchParams, Link } from "react-router-dom";
import { parentVerify } from "../../api/auth";
import { ApiError } from "../../api/client";

export default function ParentVerificationPendingPage() {
  const [searchParams] = useSearchParams();
  const token = searchParams.get("token");
  const [status, setStatus] = useState<"idle" | "verifying" | "ok" | "error">(
    token ? "verifying" : "idle",
  );
  const [errorMsg, setErrorMsg] = useState("");

  useEffect(() => {
    if (!token) return;
    parentVerify(token)
      .then(() => setStatus("ok"))
      .catch((err: unknown) => {
        setErrorMsg(
          err instanceof ApiError
            ? err.message
            : "Verification failed. The link may have expired.",
        );
        setStatus("error");
      });
  }, [token]);

  // Shown right after under-13 signup (no token in URL yet)
  if (!token || status === "idle") {
    return (
      <main className="flex min-h-screen flex-col items-center justify-center p-4 text-center gap-4">
        <h1 className="text-2xl font-bold">Almost there!</h1>
        <p className="text-gray-400 max-w-sm">
          We've sent an email to your parent or guardian. Ask them to click the link to activate
          your account.
        </p>
        <p className="text-sm text-gray-500">
          Already activated?{" "}
          <Link to="/auth/login" className="text-indigo-400 underline">
            Sign in
          </Link>
        </p>
      </main>
    );
  }

  if (status === "verifying") {
    return (
      <main className="flex min-h-screen items-center justify-center">
        <p className="text-gray-400">Activating account…</p>
      </main>
    );
  }

  if (status === "ok") {
    return (
      <main className="flex min-h-screen flex-col items-center justify-center p-4 text-center gap-4">
        <div className="text-4xl" aria-hidden="true">✓</div>
        <h1 className="text-2xl font-bold">Account activated!</h1>
        <p className="text-gray-400">
          The learner's account is now active. They can sign in and start their adventure.
        </p>
        <Link
          to="/auth/login"
          className="rounded-lg bg-indigo-600 px-4 py-2 text-sm font-medium text-white hover:bg-indigo-500"
        >
          Sign in
        </Link>
      </main>
    );
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4 text-center gap-4">
      <h1 className="text-2xl font-bold text-red-400">Activation failed</h1>
      <p className="text-gray-400">{errorMsg}</p>
    </main>
  );
}
