import SafeImg from "./SafeImg";
import Link from "next/link";
export function Hosts({ light = false, size = "md" }: { light?: boolean; size?: "sm" | "md" | "lg" }) {
  const h = size === "lg" ? "h-16" : size === "sm" ? "h-8" : "h-11";
  return (
    <div className="flex items-center gap-3">
      <SafeImg src={light ? "/img/logo-white.png" : "/img/logo-blue.png"} alt="The Magnificent" className={`${h} w-auto`} />
      <span className={`w-px ${size === "lg" ? "h-12" : "h-8"} ${light ? "bg-white/30" : "bg-line"}`} />
      <span className={`flex items-center gap-1.5 font-extrabold ${light ? "text-white" : "text-azure"} ${size === "lg" ? "text-2xl" : size === "sm" ? "text-sm" : "text-base"}`}>
        <SafeImg src="/img/gg-mark.png" alt="" className={size === "lg" ? "h-12" : size === "sm" ? "h-6" : "h-8"} />Goal Getters
      </span>
    </div>
  );
}
export function BrandLink() { return <Link href="/" className="flex items-center"><Hosts size="sm" /></Link>; }
