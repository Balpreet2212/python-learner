import { Routes, Route, Navigate } from "react-router-dom";
import { useAuth } from "./context/AuthContext";
import AppLayout from "./components/layout/AppLayout";
import HomePage from "./pages/HomePage";
import WorldMapPage from "./pages/WorldMapPage";
import OnboardingPage from "./pages/OnboardingPage";
import LessonPage from "./pages/LessonPage";
import ParentDashboardPage from "./pages/ParentDashboardPage";
import CapstoneChallengePage from "./pages/CapstoneChallengePage";
import SettingsPage from "./pages/SettingsPage";
import BillingPage from "./pages/BillingPage";
import AccountPage from "./pages/AccountPage";
import LoginPage from "./pages/auth/LoginPage";
import SignupPage from "./pages/auth/SignupPage";
import VerifyEmailPendingPage from "./pages/auth/VerifyEmailPendingPage";
import ParentVerificationPendingPage from "./pages/auth/ParentVerificationPendingPage";

function RequireAuth({ children }: { children: React.ReactNode }) {
  const { account, profile, loading } = useAuth();
  if (loading) return null;
  if (!account) return <Navigate to="/auth/login" replace />;
  // Parents go to their dashboard
  if (account.role === "parent") return <Navigate to="/parent" replace />;
  // Learners without a track set must complete onboarding first
  if (!profile?.track) {
    return <Navigate to="/onboarding" replace />;
  }
  return <>{children}</>;
}

function RequireParent({ children }: { children: React.ReactNode }) {
  const { account, loading } = useAuth();
  if (loading) return null;
  if (!account) return <Navigate to="/auth/login" replace />;
  if (account.role !== "parent") return <Navigate to="/" replace />;
  return <>{children}</>;
}

function RequireOnboarding({ children }: { children: React.ReactNode }) {
  const { account, profile, loading } = useAuth();
  if (loading) return null;
  if (!account) return <Navigate to="/auth/login" replace />;
  // Already onboarded — go straight to the map
  if (account.role === "learner" && profile?.track) {
    return <Navigate to="/" replace />;
  }
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

      {/* Onboarding (learners only, redirects away once complete) */}
      <Route
        path="/onboarding"
        element={
          <RequireOnboarding>
            <OnboardingPage />
          </RequireOnboarding>
        }
      />

      {/* Protected routes (all wrapped in AppLayout for persistent nav) */}
      <Route
        path="/"
        element={
          <RequireAuth>
            <AppLayout>
              <HomePage />
            </AppLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/learn"
        element={
          <RequireAuth>
            <AppLayout>
              <WorldMapPage />
            </AppLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/lesson"
        element={
          <RequireAuth>
            <AppLayout>
              <LessonPage />
            </AppLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/capstone"
        element={
          <RequireAuth>
            <AppLayout>
              <CapstoneChallengePage />
            </AppLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/settings"
        element={
          <RequireAuth>
            <AppLayout>
              <SettingsPage />
            </AppLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/billing"
        element={
          <RequireAuth>
            <AppLayout>
              <BillingPage />
            </AppLayout>
          </RequireAuth>
        }
      />
      <Route
        path="/account"
        element={
          <RequireAuth>
            <AppLayout>
              <AccountPage />
            </AppLayout>
          </RequireAuth>
        }
      />

      {/* Parent dashboard */}
      <Route
        path="/parent"
        element={
          <RequireParent>
            <AppLayout>
              <ParentDashboardPage />
            </AppLayout>
          </RequireParent>
        }
      />

      {/* Fallback */}
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
