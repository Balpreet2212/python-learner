import { useEffect, useState } from "react";
import { getBillingStatus, createCheckoutSession, createPortalSession, type BillingStatus } from "../api/billing";
import { ApiError } from "../api/client";
import Button from "../components/ui/Button";

const PLAN_FEATURES = [
  "All 7 units · 35 lessons + 7 capstones",
  "3 story worlds: Fantasy, Sci-Fi, Mystery",
  "Break-and-fix exercises + code runner",
  "Weekly challenges + XP tracking",
  "Unit badges and progress dashboard",
  "Parent dashboard (up to 3 learners)",
];

const FREE_FEATURES = [
  "Unit 1 · Lessons 1 & 2",
  "Daily coding challenge",
];

const STATUS_LABEL: Record<string, { label: string; color: string }> = {
  active:    { label: "Active",    color: "text-green-400 bg-green-500/10 border-green-700/40" },
  past_due:  { label: "Past due",  color: "text-amber-400 bg-amber-500/10 border-amber-700/40" },
  cancelled: { label: "Cancelled", color: "text-red-400 bg-red-500/10 border-red-700/40" },
  trial:     { label: "Trial",     color: "text-indigo-400 bg-indigo-500/10 border-indigo-700/40" },
  none:      { label: "Free",      color: "text-gray-400 bg-gray-800 border-gray-700" },
};

export default function BillingPage() {
  const [billing, setBilling] = useState<BillingStatus | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Check for ?success=1 from Stripe redirect
  const justSubscribed = new URLSearchParams(window.location.search).get("success") === "1";

  useEffect(() => {
    getBillingStatus().then(setBilling).catch(() => {});
  }, []);

  async function handleSubscribe() {
    setLoading(true);
    setError(null);
    try {
      const url = await createCheckoutSession();
      window.location.href = url;
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not start checkout.");
      setLoading(false);
    }
  }

  async function handleManage() {
    setLoading(true);
    setError(null);
    try {
      const url = await createPortalSession();
      window.location.href = url;
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not open portal.");
      setLoading(false);
    }
  }

  const statusKey = billing?.status ?? "none";
  const badge = STATUS_LABEL[statusKey] ?? STATUS_LABEL["none"];
  const hasAccess = billing?.has_full_access ?? false;

  return (
    <div className="mx-auto max-w-xl p-6 space-y-8">
      <h1 className="text-2xl font-bold">Billing</h1>

      {justSubscribed && (
        <div className="rounded-xl border border-green-700/40 bg-green-950/20 px-5 py-4">
          <p className="text-sm font-semibold text-green-400">Subscription activated! Welcome to full access.</p>
        </div>
      )}

      {/* Subscription status card */}
      <section className={`rounded-2xl border p-6 space-y-4 ${hasAccess ? "border-indigo-500/40 bg-indigo-950/20" : "border-gray-700 bg-gray-900"}`}>
        <div className="flex items-start justify-between">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wider text-gray-400">Current plan</p>
            <p className="mt-1 text-2xl font-bold text-white">{hasAccess ? "Full Access" : "Free"}</p>
          </div>
          <span className={`rounded-full border px-3 py-1 text-xs font-semibold ${badge.color}`}>
            {badge.label}
          </span>
        </div>

        {billing?.current_period_end && hasAccess && (
          <p className="text-xs text-gray-500">
            Renews {new Date(billing.current_period_end).toLocaleDateString()}
          </p>
        )}

        {/* Feature list */}
        <ul className="space-y-2">
          {(hasAccess ? PLAN_FEATURES : FREE_FEATURES).map((f) => (
            <li key={f} className="flex items-center gap-2 text-sm text-gray-300">
              <span className="text-green-400">✓</span>
              {f}
            </li>
          ))}
        </ul>

        {/* Actions */}
        <div className="pt-2 space-y-2">
          {!hasAccess && (
            <Button onClick={() => void handleSubscribe()} loading={loading} className="w-full">
              Unlock Full Access
            </Button>
          )}
          {hasAccess && (
            <Button
              variant="ghost"
              onClick={() => void handleManage()}
              loading={loading}
              className="w-full border border-gray-700 hover:border-indigo-500 hover:text-indigo-300"
            >
              Manage subscription
            </Button>
          )}
          {!hasAccess && statusKey === "cancelled" && (
            <p className="text-xs text-center text-gray-500">Your subscription was cancelled. Subscribe again to restore access.</p>
          )}
          {error && <p className="text-xs text-center text-red-400">{error}</p>}
        </div>
      </section>

      {/* What's included when not subscribed */}
      {!hasAccess && (
        <section className="rounded-2xl border border-gray-700 bg-gray-900/60 p-6 space-y-4">
          <p className="text-sm font-semibold text-white">Everything in Full Access</p>
          <ul className="space-y-2">
            {PLAN_FEATURES.map((f) => (
              <li key={f} className="flex items-center gap-2 text-sm text-gray-400">
                <span className="text-indigo-400">✓</span>
                {f}
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
