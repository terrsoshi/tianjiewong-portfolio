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
        src: "/android-chrome-192x192.png",
        sizes: "192x192",
        type: "image/png",
      },
      {
        src: "/android-chrome-384x384.png",
        sizes: "384x384",
        type: "image/png",
      },
    ],
  };
}
