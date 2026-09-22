# Bounded (licensed brand font)

Drop the three licensed files here, with exactly these names:

- `bounded-extralight.ttf` → weight 200
- `bounded-regular.ttf`    → weight 400
- `bounded-black.ttf`      → weight 900

They are already declared in `src/index.css` as separate `@font-face` rules with
explicit `font-weight` values, because the files' internal metadata reports every
weight as "Bounded Regular". No code change is needed once they are here — until
then the page falls back to Archivo Black (Google Fonts) as a stand-in.
