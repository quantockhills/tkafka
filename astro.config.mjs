// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import remarkMath from 'remark-math';
import rehypeMathjax from 'rehype-mathjax';

export default defineConfig({
  site: 'https://tkafka.eu',
  output: 'static',
  integrations: [mdx()],
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeMathjax],
  },
});
