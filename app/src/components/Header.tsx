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

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const menuItems = ["Home", "About Me", "Skills", "Projects", "Contact Me"];

  return (
    <header>
      <Navbar className="bg-transparent" onMenuOpenChange={setIsMenuOpen}>
        <NavbarContent>
          <NavbarMenuToggle
            className="lg:hidden"
            aria-label={isMenuOpen ? "Close menu" : "Open menu"}
          />
          <NavbarBrand>
            <Link className="flex gap-1" href="/">
              <Image
                src="/logo.png"
                alt="Tian Jie Wong portfolio site logo"
                width="24"
                height="24"
              />
              <p>Tian Jie Wong</p>
            </Link>
          </NavbarBrand>
        </NavbarContent>

        <NavbarContent className="hidden gap-4 lg:flex" justify="center">
          <NavbarItem>
            <Link href="#">Home</Link>
          </NavbarItem>
          <NavbarItem>
            <Link href="#">About Me</Link>
          </NavbarItem>
          <NavbarItem>
            <Link href="#">Skills</Link>
          </NavbarItem>
          <NavbarItem>
            <Link href="#">Projects</Link>
          </NavbarItem>
          <NavbarItem>
            <Link href="#">Contact Me</Link>
          </NavbarItem>
        </NavbarContent>

        <NavbarContent justify="end">
          <ThemeToggleButton />
        </NavbarContent>

        <NavbarMenu className="flex gap-0">
          {menuItems.map((item, index) => (
            <NavbarMenuItem key={`${item}-${index}`}>
              <Link className="w-full" href="#">
                {item}
              </Link>
            </NavbarMenuItem>
          ))}
        </NavbarMenu>
      </Navbar>

      <Divider className="mb-2 lg:hidden" />
    </header>
  );
};

export default Header;
