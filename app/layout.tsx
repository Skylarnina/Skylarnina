import type { Metadata } from "next";
import "./globals.css";
import { AuthProvider } from "@/lib/auth";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";


export const metadata: Metadata = {
  metadataBase: new URL("https://magnificent-bootcamp.vercel.app"),
  title: "The Magnificent 5 Days Bootcamp",
  description: "Learn a skill. Win clients. Build a business. Five days of hands-on training, 30 Nov – 4 Dec 2026, Akure. Hosted by The Magnificent and Goal Getters.",
  icons: { icon: "/img/mark.png" },
  openGraph: { title: "The Magnificent 5 Days Bootcamp", description: "Learn a skill. Win clients. Build a business.", images: ["/img/hero.jpg"] },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head><link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" /><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet" /></head>
      <body><AuthProvider><Nav /><main>{children}</main><Footer /></AuthProvider></body>
    </html>
  );
}
