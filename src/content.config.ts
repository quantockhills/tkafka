import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const science = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: './src/content/science' }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
    description: z.string().optional(),
    tags: z.array(z.string()).optional(),
    bgImage: z.string().optional(),
  }),
});

const music = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: './src/content/music' }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
    description: z.string().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

const art = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: './src/content/art' }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
    description: z.string().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

const writing = defineCollection({
  loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: './src/content/writing' }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
    description: z.string().optional(),
    tags: z.array(z.string()).optional(),
    folder: z.string().optional(),
  }),
});

export const collections = { science, music, art, writing };
