"use client";

import { useState } from "react";

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

const menuItems = ["Home", "About Me", "Skills", "Projects", "Contact Me"];
const menuItemsId = ["", "about", "skills", "projects", "about"];

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

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
              <p className="font-semibold text-black antialiased dark:text-white">
                Tian Jie Wong
              </p>
            </Link>
          </NavbarBrand>
        </NavbarContent>

        <NavbarContent className="hidden gap-8 lg:flex" justify="center">
          {menuItems.map((item, index) => {
            return (
              <NavbarItem key={`${item}-${index}`}>
                <Link
                  className="text-current antialiased hover:opacity-50 active:underline active:underline-offset-4 dark:hover:text-white dark:hover:opacity-100"
                  href={`/#${menuItemsId[index]}`}
                  size="lg"
                >
                  {item}
                </Link>
              </NavbarItem>
            );
          })}
        </NavbarContent>

        <NavbarContent justify="end">
          <ThemeToggleButton />
        </NavbarContent>

        <NavbarMenu className="flex gap-2 dark:bg-black/50">
          {menuItems.map((item, index) => {
            return (
              <NavbarMenuItem key={`menu-${item}-${index}`}>
                <Link
                  className="w-full rounded-xl px-4 py-3 text-current antialiased hover:bg-zinc-200 hover:text-black hover:opacity-100 dark:hover:bg-zinc-700/70 dark:hover:text-white"
                  href={`/#${menuItemsId[index]}`}
                  size="lg"
                >
                  {item}
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
