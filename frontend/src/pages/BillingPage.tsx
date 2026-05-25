import { useAuth } from "../context/AuthContext";

const PLAN_FEATURES = [
  "All 6 units (30 lessons + 6 capstones)",
  "3 story worlds: Fantasy, Sci-Fi, Mystery",
  "Instant code feedback with test runner",
  "XP tracking and unit badges",
  "Parent dashboard (add up to 3 learners)",
];

export default function BillingPage() {
  const { profile } = useAuth();

  const completedUnits = profile ? profile.current_unit - 1 : 0;

  return (
    <div className="mx-auto max-w-xl p-6 space-y-8">
        <h1 className="text-2xl font-bold">Billing</h1>

        {/* Current plan */}
        <section className="rounded-2xl border border-indigo-500/40 bg-indigo-950/30 p-6 space-y-4">
          <div className="flex items-start justify-between">
            <div>
              <p className="text-xs font-semibold uppercase tracking-wider text-indigo-400">Current plan</p>
              <p className="mt-1 text-2xl font-bold text-white">Full Access</p>
            </div>
            <span className="rounded-full bg-green-500/20 px-3 py-1 text-xs font-semibold text-green-400">
              Active
            </span>
          </div>

          <ul className="space-y-2">
            {PLAN_FEATURES.map((f) => (
              <li key={f} className="flex items-center gap-2 text-sm text-gray-300">
                <span className="text-green-400">✓</span>
                {f}
              </li>
            ))}
          </ul>
        </section>

        {/* Progress summary */}
        {profile && (
          <section className="rounded-2xl border border-gray-700 bg-gray-900 p-5 space-y-3">
            <p className="text-sm font-semibold uppercase tracking-wider text-gray-400">Your progress</p>
            <div className="grid grid-cols-3 gap-4 text-center">
              <div>
                <p className="text-2xl font-bold text-white">{completedUnits}</p>
                <p className="text-xs text-gray-500">Units done</p>
              </div>
              <div>
                <p className="text-2xl font-bold text-white">{profile.badges.length}</p>
                <p className="text-xs text-gray-500">Badges earned</p>
              </div>
              <div>
                <p className="text-2xl font-bold text-white">{profile.current_unit}</p>
                <p className="text-xs text-gray-500">Current unit</p>
              </div>
            </div>
          </section>
        )}

        <p className="text-center text-xs text-gray-600">
          Questions about your subscription? Contact support.
        </p>
    </div>
  );
}
