interface Props {
  message: string | null;
}

export default function FormError({ message }: Props) {
  if (!message) return null;
  return (
    <div role="alert" className="rounded-lg bg-red-900/40 border border-red-700 px-4 py-3 text-sm text-red-300">
      {message}
    </div>
  );
}
