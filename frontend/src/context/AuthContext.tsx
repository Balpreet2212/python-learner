import {
  createContext,
  useContext,
  useState,
  useCallback,
  useEffect,
  type ReactNode,
} from "react";
import { type Account, type LearnerProfile, getMe } from "../api/auth";
import { setCsrfToken } from "../api/client";

interface AuthState {
  account: Account | null;
  profile: LearnerProfile | null;
  loading: boolean;
}

interface AuthContextValue extends AuthState {
  setAuth: (account: Account, csrf: string, profile?: LearnerProfile | null) => void;
  setProfile: (profile: LearnerProfile) => void;
  clearAuth: () => void;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<AuthState>({ account: null, profile: null, loading: true });

  useEffect(() => {
    getMe()
      .then(({ account, csrf_token, profile }) => {
        setCsrfToken(csrf_token);
        setState({ account, profile: profile ?? null, loading: false });
      })
      .catch(() => {
        setState({ account: null, profile: null, loading: false });
      });
  }, []);

  const setAuth = useCallback(
    (account: Account, csrf: string, profile?: LearnerProfile | null) => {
      setCsrfToken(csrf);
      setState({ account, profile: profile ?? null, loading: false });
    },
    [],
  );

  const setProfile = useCallback((profile: LearnerProfile) => {
    setState((prev) => ({ ...prev, profile }));
  }, []);

  const clearAuth = useCallback(() => {
    setCsrfToken("");
    setState({ account: null, profile: null, loading: false });
  }, []);

  return (
    <AuthContext.Provider value={{ ...state, setAuth, setProfile, clearAuth }}>
      {children}
    </AuthContext.Provider>
  );
}

// eslint-disable-next-line react-refresh/only-export-components
export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx;
}
