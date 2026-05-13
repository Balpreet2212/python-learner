import { Routes, Route, Navigate } from "react-router-dom";
import { useAuth } from "./context/AuthContext";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/auth/LoginPage";
import SignupPage from "./pages/auth/SignupPage";
import VerifyEmailPendingPage from "./pages/auth/VerifyEmailPendingPage";
import ParentVerificationPendingPage from "./pages/auth/ParentVerificationPendingPage";

function RequireAuth({ children }: { children: React.ReactNode }) {
  const { account, loading } = useAuth();
  if (loading) return null; // session restore in progress
  if (!account) return <Navigate to="/auth/login" replace />;
  return <>{children}</>;
}

export default function App() {
  return (
    <Routes>
      {/* Public auth routes */}
      <Route path="/auth/login" element={<LoginPage />} />
      <Route path="/auth/signup" element={<SignupPage />} />
      <Route path="/auth/verify-email" element={<VerifyEmailPendingPage />} />
      <Route path="/auth/verify-pending" element={<VerifyEmailPendingPage />} />
      <Route path="/auth/parent-verify" element={<ParentVerificationPendingPage />} />
      <Route path="/auth/parent-pending" element={<ParentVerificationPendingPage />} />

      {/* Protected routes */}
      <Route
        path="/"
        element={
          <RequireAuth>
            <HomePage />
          </RequireAuth>
        }
      />

      {/* Fallback */}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
