import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        // Fantasy world palette
        fantasy: {
          bg: "#1a0f2e",
          surface: "#2d1b4e",
          accent: "#9b59b6",
          highlight: "#f1c40f",
          text: "#e8d5f5",
        },
        // Sci-Fi world palette
        scifi: {
          bg: "#0a0e1a",
          surface: "#0f1b2d",
          accent: "#00d4ff",
          highlight: "#00ff88",
          text: "#c8e6ff",
        },
        // Mystery world palette
        mystery: {
          bg: "#12100e",
          surface: "#1f1a14",
          accent: "#c0913a",
          highlight: "#e8c47a",
          text: "#d4c4a0",
        },
        // Shared neutrals
        pyquest: {
          pass: "#27ae60",
          fail: "#e74c3c",
          hint: "#f39c12",
          disabled: "#7f8c8d",
        },
      },
      fontFamily: {
        code: ["JetBrains Mono", "Fira Code", "Cascadia Code", "monospace"],
      },
    },
  },
  plugins: [],
};

export default config;
