import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    outDir: 'build', // Or your desired output directory
    rollupOptions: {
      input: {
        main: 'index.html', // Path to your index.html
      },
    },
  },
});