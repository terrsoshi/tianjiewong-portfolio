import { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Tian Jie Wong's Portfolio",
    short_name: "TW's Portfolio",
    description:
      "Discover Tian Jie Wong's diverse skill set as a full stack developer through his portfolio site. Explore his projects, skills, and experience in software development.",
    start_url: "/",
    display: "standalone",
    background_color: "#fff",
    theme_color: "#fff",
    lang: "en",
    icons: [
      {
        src: "/favicon.ico",
        sizes: "any",
        type: "image/x-icon",
      },
    ],
  };
}
