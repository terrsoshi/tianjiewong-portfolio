import type { Metadata } from "next";
import { Lato } from "next/font/google";

import "./globals.css";
import { Providers } from "./providers";

const lato = Lato({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "Tian Jie Wong | Full Stack Developer",
  description:
    "Welcome to Tian Jie Wong's portfolio site. Discover my diverse skill set as a full stack developer through my portfolio site. Explore my projects, skills, and experience in software development. Let's connect!",
  authors: [{ name: "Tian Jie Wong" }],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${lato.className} bg-white bg-fixed text-black dark:bg-black dark:text-white`}
      >
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
