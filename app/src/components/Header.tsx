"use client";

import { useEffect, useState } from "react";

import Image from "next/image";

import {
  Divider,
  Link,
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
  NavbarMenu,
  NavbarMenuItem,
  NavbarMenuToggle,
} from "@nextui-org/react";

import ThemeToggleButton from "./ThemeToggleButton";

const navItems: { label: string; hash: string }[] = [
  { label: "Home", hash: "" },
  { label: "About Me", hash: "about" },
  { label: "Skills", hash: "skills" },
  { label: "Projects", hash: "projects" },
  { label: "Contact Me", hash: "contact" },
];

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [hash, setHash] = useState("-");
  useEffect(() => {
    setHash(window.location.hash);
    const handleHashChange = () => {
      setHash(window.location.hash);
    };
    window.addEventListener("hashchange", handleHashChange);
    return () => window.removeEventListener("hashchange", handleHashChange);
  }, []);

  return (
    <header>
      <Navbar className="bg-transparent" onMenuOpenChange={setIsMenuOpen}>
        <NavbarContent>
          <NavbarMenuToggle
            className="lg:hidden"
            aria-label={isMenuOpen ? "Close menu" : "Open menu"}
          />
          <NavbarBrand>
            <Link
              className="flex gap-1 text-current hover:opacity-100"
              href="/"
            >
              <Image
                src="/logo.png"
                alt="Tian Jie Wong portfolio site logo"
                width="24"
                height="24"
              />
              <p className="font-semibold text-slate-700 antialiased dark:text-slate-300">
                Tian Jie Wong
              </p>
            </Link>
          </NavbarBrand>
        </NavbarContent>

        <NavbarContent className="hidden gap-8 lg:flex" justify="center">
          {navItems.map((item, index) => {
            const isActive = hash.replace("#", "") === item.hash;
            return (
              <NavbarItem key={`${item.label}-${index}`}>
                <Link
                  className={`antialiased ${isActive ? "text-blue-custom underline decoration-double underline-offset-[12px] hover:opacity-100 dark:text-indigo-400" : "navItem-slide-in text-current hover:opacity-50 motion-reduce:after:transition-none dark:hover:text-white dark:hover:opacity-100"}`}
                  href={`/#${item.hash}`}
                  size="lg"
                >
                  {item.label}
                </Link>
              </NavbarItem>
            );
          })}
        </NavbarContent>

        <NavbarContent justify="end">
          <ThemeToggleButton />
        </NavbarContent>

        <NavbarMenu className="flex gap-2 dark:bg-black/50">
          {navItems.map((item, index) => {
            const isActive = hash.replace("#", "") === item.hash;
            return (
              <NavbarMenuItem key={`menu-${item.label}-${index}`}>
                <Link
                  className={`w-full rounded-xl px-4 py-3 antialiased hover:bg-zinc-200 hover:opacity-100 dark:hover:bg-zinc-700/70 ${isActive ? "text-blue-custom dark:text-indigo-400" : "text-current hover:text-black dark:hover:text-white"}`}
                  href={`/#${item.hash}`}
                  size="lg"
                >
                  {item.label}
                </Link>
              </NavbarMenuItem>
            );
          })}
        </NavbarMenu>
      </Navbar>

      <Divider className="mb-2 lg:hidden" />
    </header>
  );
};

export default Header;
