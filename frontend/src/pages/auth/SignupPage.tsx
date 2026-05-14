import { useState, type FormEvent, type ChangeEvent } from "react";
import { Link, useNavigate } from "react-router-dom";
import { signup } from "../../api/auth";
import { ApiError } from "../../api/client";
import Button from "../../components/ui/Button";
import Input from "../../components/ui/Input";
import FormError from "../../components/ui/FormError";

export default function SignupPage() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState<"learner" | "parent">("learner");
  const [isUnder13, setIsUnder13] = useState(false);
  const [parentEmail, setParentEmail] = useState("");
  const [displayName, setDisplayName] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const result = await signup({
        email,
        password,
        role,
        display_name: displayName || undefined,
        is_under_13: isUnder13,
        parent_email: isUnder13 ? parentEmail : undefined,
      });

      if (result.status === "pending_parent_verification") {
        navigate("/auth/parent-pending");
      } else {
        navigate("/auth/login");
      }
    } catch (err) {
      if (err instanceof ApiError) {
        if (err.code === "conflict") {
          setError("An account with that email already exists. Try logging in.");
        } else {
          setError(err.message);
        }
      } else {
        setError("Something went wrong. Please try again.");
      }
    } finally {
      setLoading(false);
    }
  }

  function handleRoleChange(e: ChangeEvent<HTMLInputElement>) {
    setRole(e.target.value as "learner" | "parent");
    if (e.target.value === "parent") setIsUnder13(false);
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4">
      <div className="w-full max-w-sm space-y-6">
        <div className="text-center">
          <h1 className="text-3xl font-bold">PyQuest</h1>
          <p className="mt-1 text-gray-400">Create your free account</p>
        </div>

        <form onSubmit={(e) => void handleSubmit(e)} className="space-y-4" noValidate>
          <FormError message={error} />

          <Input
            label="Display name (optional)"
            type="text"
            value={displayName}
            onChange={(e) => setDisplayName(e.target.value)}
            autoComplete="nickname"
            maxLength={100}
          />
          <Input
            label="Email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            autoComplete="email"
            required
          />
          <Input
            label="Password (8+ characters)"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoComplete="new-password"
            minLength={8}
            required
          />

          {/* Track: learner vs parent */}
          <fieldset className="space-y-2">
            <legend className="text-sm font-medium text-gray-300">I am a…</legend>
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="radio"
                name="role"
                value="learner"
                checked={role === "learner"}
                onChange={handleRoleChange}
                className="accent-indigo-500"
              />
              <span className="text-sm text-gray-200">Learner (student)</span>
            </label>
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="radio"
                name="role"
                value="parent"
                checked={role === "parent"}
                onChange={handleRoleChange}
                className="accent-indigo-500"
              />
              <span className="text-sm text-gray-200">Parent / guardian</span>
            </label>
          </fieldset>

          {/* Under-13 flag (§12.4) */}
          {role === "learner" && (
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="checkbox"
                checked={isUnder13}
                onChange={(e) => setIsUnder13(e.target.checked)}
                className="accent-indigo-500"
              />
              <span className="text-sm text-gray-300">I am under 13 years old</span>
            </label>
          )}

          {isUnder13 && (
            <Input
              label="Parent / guardian email"
              type="email"
              value={parentEmail}
              onChange={(e) => setParentEmail(e.target.value)}
              required
              autoComplete="email"
            />
          )}

          <Button type="submit" loading={loading} className="w-full">
            Create account
          </Button>
        </form>

        <p className="text-center text-sm text-gray-400">
          Already have an account?{" "}
          <Link to="/auth/login" className="text-indigo-400 hover:text-indigo-300 underline">
            Sign in
          </Link>
        </p>
      </div>
    </main>
  );
}
