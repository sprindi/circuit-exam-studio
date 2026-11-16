import {defineConfig} from 'vite';
export default defineConfig({define:{'process.env.NODE_ENV':JSON.stringify('production')},build:{outDir:'build',emptyOutDir:true,lib:{entry:'src/index.tsx',name:'CircuitFoundationBundle',formats:['iife']},rollupOptions:{output:{entryFileNames:'lesson-[hash].js',assetFileNames:'lesson-[hash][extname]'}}}});
