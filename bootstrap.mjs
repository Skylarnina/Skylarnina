// Pulls the full site source from GitHub at build time, then `next build` runs on it.
import { execSync } from "node:child_process";
import { writeFileSync } from "node:fs";
const url = "https://codeload.github.com/Skylarnina/Skylarnina/tar.gz/refs/heads/magnificent-bootcamp";
const r = await fetch(url);
if (!r.ok) throw new Error("source download failed: " + r.status);
writeFileSync("src.tgz", Buffer.from(await r.arrayBuffer()));
execSync("tar -xzf src.tgz --strip-components=1 --exclude='*/bootstrap.mjs' && rm src.tgz", { stdio: "inherit" });
console.log("source extracted");
