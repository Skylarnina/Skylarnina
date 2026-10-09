"use client";
export default function SafeImg(props: React.ImgHTMLAttributes<HTMLImageElement>) {
  // eslint-disable-next-line @next/next/no-img-element
  return <img {...props} alt={props.alt ?? ""} onError={(e) => { e.currentTarget.style.display = "none"; }} />;
}
