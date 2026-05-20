import { useState, type FormEvent } from "react";
import { Link, useNavigate } from "react-router-dom";
import { login } from "../../api/auth";
import { ApiError } from "../../api/client";
import { useAuth } from "../../context/AuthContext";
import Button from "../../components/ui/Button";
import Input from "../../components/ui/Input";
import FormError from "../../components/ui/FormError";

export default function LoginPage() {
  const { setAuth } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const { account, csrf_token, profile } = await login(email, password);
      setAuth(account, csrf_token, profile);
      navigate("/");
    } catch (err) {
      if (err instanceof ApiError) {
        if (err.code === "email_not_verified") {
          setError("Please check your email and click the verification link before logging in.");
        } else if (err.code === "account_inactive") {
          setError("Your account is waiting for parent verification. Check your parent's email.");
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

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4">
      <div className="w-full max-w-sm space-y-6">
        <div className="text-center">
          <h1 className="text-3xl font-bold">PyQuest</h1>
          <p className="mt-1 text-gray-400">Sign in to continue your adventure</p>
        </div>

        <form onSubmit={(e) => void handleSubmit(e)} className="space-y-4" noValidate>
          <FormError message={error} />

          <Input
            label="Email"
            type="email"
            value={email}
            onChange={(e) => { setEmail(e.target.value); }}
            autoComplete="email"
            required
          />
          <Input
            label="Password"
            type="password"
            value={password}
            onChange={(e) => { setPassword(e.target.value); }}
            autoComplete="current-password"
            required
          />

          <Button type="submit" loading={loading} className="w-full">
            Sign in
          </Button>
        </form>

        <p className="text-center text-sm text-gray-400">
          No account yet?{" "}
          <Link to="/auth/signup" className="text-indigo-400 hover:text-indigo-300 underline">
            Start free trial
          </Link>
        </p>
      </div>
    </main>
  );
}
