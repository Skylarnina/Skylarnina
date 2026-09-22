import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'
import { viteSingleFile } from 'vite-plugin-singlefile'

// https://vite.dev/config/
export default defineConfig(({ mode }) =>
  mode === 'preview-file'
    ? {
        // `npm run build:preview` → one self-contained HTML file (JS, CSS, fonts, images inlined)
        // for reviewing the design without a server.
        plugins: [react(), tailwindcss(), viteSingleFile()],
        build: { outDir: 'dist-preview', rollupOptions: { input: 'preview.html' } },
      }
    : { plugins: [react(), tailwindcss()] },
)
