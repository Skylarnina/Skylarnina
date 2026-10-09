import type { Config } from "tailwindcss";
const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: { extend: { colors: { sky: "#15AAF8", azure: "#0075BD", amber: "#FBB71A", ink: "#0B1B2B", tint: "#EAF6FE", tint2: "#F5FAFF", muted: "#5B6B7F", line: "#DCE7F2" },
    fontFamily: { sans: ["var(--font-pjs)", "system-ui", "sans-serif"] },
    boxShadow: { card: "0 10px 30px rgba(0,117,189,.10)", lift: "0 24px 60px rgba(0,25,70,.18)" } } },
  plugins: [],
};
export default config;
