export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-6 p-8">
      <h1 className="text-5xl font-bold tracking-tight">PyQuest</h1>
      <p className="text-lg text-gray-400">
        A story-driven Python learning platform for grades 5–12
      </p>
      <p className="text-sm text-gray-600">
        M1 — Foundations checkpoint. Backend is running if{" "}
        <a
          href="/health"
          className="underline text-blue-400 hover:text-blue-300"
          target="_blank"
          rel="noreferrer"
        >
          /health
        </a>{" "}
        returns <code className="font-mono text-green-400">ok</code>.
      </p>
    </main>
  );
}
