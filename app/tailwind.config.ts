import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: [
    "variant",
    [
      "@media (prefers-color-scheme: dark) { &:not(.light *) }", // If the user prefers dark mode, unless overridden by a .light class
      "&:is(.dark *)", // If there is a .dark class present in any ancestor element
    ],
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        purple: { custom: "hsla(259, 100%, 64%, 0.7)" },
        blue: { custom: "hsla(240, 100%, 70%, 0.48)" },
        pink: { custom: "hsla(325, 100%, 50%, 0.32)" },
        teal: { custom: "hsla(183, 100%, 50%, 0.4)" },
        orange: { custom: "hsla(22, 100%, 77%, 0.59)" },
      },
    },
  },
  plugins: [],
};
export default config;
