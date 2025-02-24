import type { Config } from "tailwindcss";

export default {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        linkedin: {
          blue: "#0A66C2",
          lightBlue: "#70B5F9",
          green: "#7FC15E",
          red: "#F5987E",
          orange: "#E7A33E",
          brown: "#915907",
          whiteSmoke: "#F3F2EF",
          white: "#FFFFFF",
          black: "rgba(0,0,0,0.9)",
          gray: "rgba(102,102,102, 0.6)",
          lightGray: "rgba(0, 122, 255, 0.15)",
        },
      },
    },
  },
  plugins: [],
} satisfies Config;

// CORES OPCIONAIS - CHECAR ANTES DE UTILIZAR!!!
// scb: "#0077B5",
// reb: "#00A0DC",
// chinese_silver: "#CACCCE",
// staupe_gray: "#86888A",
// dark_charcoal: "#313335",
// soft_gray: "#EEEEEE",
// light_gray: "rgba(224, 224, 224, 0.6)",
