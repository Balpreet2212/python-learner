import { NavLink, Outlet } from "react-router-dom";

const NAV_ITEMS = [
  { to: "/dashboard/account", label: "Account" },
  { to: "/dashboard/billing", label: "Billing" },
  { to: "/dashboard/settings", label: "Settings" },
];

export default function DashboardPage() {
  return (
    <div className="flex bg-gray-950 text-gray-100">
      <aside className="w-52 shrink-0 border-r border-gray-800 p-5">
        <p className="mb-3 px-2 text-xs font-semibold uppercase tracking-wider text-gray-500">
          My Account
        </p>
        <nav className="space-y-0.5">
          {NAV_ITEMS.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) =>
                `block rounded-lg px-3 py-2 text-sm transition-colors ${
                  isActive
                    ? "bg-gray-800 text-white font-medium"
                    : "text-gray-400 hover:bg-gray-800/50 hover:text-gray-200"
                }`
              }
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
      </aside>

      <div className="flex-1 min-h-screen">
        <Outlet />
      </div>
    </div>
  );
}
