import "@/app/globals.css";
import type { Metadata } from "next";
import { cn } from "@/lib/utils";

import { Inter } from "next/font/google";

import { Toaster } from "@/components/ui/toaster"

const inter = Inter({ subsets: ["latin"], variable: '--font-sans', });

export const metadata: Metadata = {
  title: "Recipes",
  description: "Make some and share some",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={cn(
        'min-h-screen bg-background font-sans antialiased',
        inter.variable
      )}>
        <main>{children}</main>
        <Toaster />
      </body>
    </html>
  );
}
