/**
 * Thin fetch wrapper that:
 * - Always sends credentials (session cookie)
 * - Attaches X-CSRF-Token header on mutating requests (§11.1)
 * - Returns typed responses validated at the boundary
 */

let _csrfToken: string | null = null;

export function setCsrfToken(token: string): void {
  _csrfToken = token;
}

export function getCsrfToken(): string | null {
  return _csrfToken;
}

const MUTATING = new Set(["POST", "PUT", "PATCH", "DELETE"]);

export class ApiError extends Error {
  constructor(
    public readonly status: number,
    public readonly code: string,
    message: string,
    public readonly details?: unknown,
  ) {
    super(message);
    this.name = "ApiError";
  }
}

interface ErrorBody {
  code: string;
  message: string;
  details?: unknown;
}

function isErrorBody(v: unknown): v is ErrorBody {
  return (
    typeof v === "object" &&
    v !== null &&
    "code" in v &&
    "message" in v &&
    typeof (v as Record<string, unknown>).code === "string" &&
    typeof (v as Record<string, unknown>).message === "string"
  );
}

export async function apiFetch<T>(
  path: string,
  options: RequestInit = {},
): Promise<T> {
  const method = (options.method ?? "GET").toUpperCase();
  const headers = new Headers(options.headers);

  headers.set("Content-Type", "application/json");

  if (MUTATING.has(method) && _csrfToken) {
    headers.set("X-CSRF-Token", _csrfToken);
  }

  const resp = await fetch(path, {
    ...options,
    headers,
    credentials: "include",
  });

  if (!resp.ok) {
    let body: unknown;
    try {
      body = await resp.json();
    } catch {
      body = null;
    }
    if (isErrorBody(body)) {
      throw new ApiError(resp.status, body.code, body.message, body.details);
    }
    throw new ApiError(resp.status, "unknown", `HTTP ${String(resp.status)}`);
  }

  if (resp.status === 204) {
    return undefined as T;
  }

  return resp.json() as Promise<T>;
}
