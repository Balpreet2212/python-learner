import {
  createContext,
  useContext,
  useState,
  useCallback,
  useEffect,
  type ReactNode,
} from "react";
import { type Account, getMe } from "../api/auth";
import { setCsrfToken } from "../api/client";

interface AuthState {
  account: Account | null;
  loading: boolean;
}

interface AuthContextValue extends AuthState {
  setAuth: (account: Account, csrf: string) => void;
  clearAuth: () => void;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<AuthState>({ account: null, loading: true });

  // On mount, try to restore session via GET /v1/me (uses the HttpOnly cookie)
  useEffect(() => {
    getMe()
      .then(({ account, csrf_token }) => {
        setCsrfToken(csrf_token);
        setState({ account, loading: false });
      })
      .catch(() => {
        setState({ account: null, loading: false });
      });
  }, []);

  const setAuth = useCallback((account: Account, csrf: string) => {
    setCsrfToken(csrf);
    setState({ account, loading: false });
  }, []);

  const clearAuth = useCallback(() => {
    setCsrfToken("");
    setState({ account: null, loading: false });
  }, []);

  return (
    <AuthContext.Provider value={{ ...state, setAuth, clearAuth }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used inside AuthProvider");
  return ctx;
}
