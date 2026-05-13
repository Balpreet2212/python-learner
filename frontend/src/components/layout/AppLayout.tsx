import type { ReactNode } from "react";
import NavBar from "./NavBar";

export default function AppLayout({ children }: { children: ReactNode }) {
  return (
    <div className="flex min-h-screen flex-col">
      <NavBar />
      <div className="flex-1">{children}</div>
    </div>
  );
}
