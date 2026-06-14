# tkafka.eu — Personal Website

## Stack

| Layer | Choice |
|-------|--------|
| SSG | **Astro 5** (static mode, file-based routing, content collections) |
| Content | **Markdown + MDX** via content collections |
| Styling | **Modern CSS** (Grid, custom properties, no framework) |
| Fonts | **Playfair Display** (serif — headlines) + **Inter** (sans — body) |
| Deploy | **statichost.eu** (`dist/` folder, method TBD later) |

## Architecture

```
tkafka.eu/
├── /                → Landing page (hero + 3 section cards)
├── /science         → PhD / quantum computing / tech research
├── /music           → Indie band, blog, Substack links
├── /art             → Migrated art blog
```

Content stored as Markdown in `src/content/{science,music,art}/`.

## Design System

| Token | Value |
|-------|-------|
| Background | `#FAFAF9` (off-white) |
| Text | `#1A1A1A` (near-black) |
| Body font | Inter (400, 700) |
| Heading font | Playfair Display (600, 700, 900 italic) |
| Swiss accent | `#E63946` (red) or `#0066FF` (blue) |
| 90s pops | `#39FF14` (neon green), `#FF69B4` (hot pink) |
| Grid | CSS Grid, asymmetric Swiss layouts |
| Spacing | 4/8/12/16/24/32/48/64/96 scale |

### Aesthetic

- **Base**: Swiss/International — clean grids, bold typography, generous whitespace, asymmetrical balance
- **Sprinkles**: 90s web nostalgia — pixel-art icons, starfield cursor trail, ironic visitor counter, selective neon color pops

## Phases

### Phase 1 — Scaffold & Configure
- [x] Write this plan
- [ ] `npm create astro@latest` + configure
- [ ] Install `@astrojs/mdx`
- [ ] Set `site` URL, static output
- [ ] Clean boilerplate

### Phase 2 — Global Styles
- [ ] CSS custom properties (colors, fonts, spacing)
- [ ] Typography base (headings, body, links)
- [ ] Reset + global styles
- [ ] Google Fonts: Playfair Display + Inter

### Phase 3 — Layout Shell
- [ ] `BaseLayout.astro` — doctype, meta, fonts, SEO, nav, footer
- [ ] `Nav.astro` — minimal Swiss horizontal nav
- [ ] `Footer.astro` — clean links + retro easter eggs

### Phase 4 — Landing Page
- [ ] Hero block (name, tagline)
- [ ] 3 section cards (Science, Music, Art)
- [ ] Starfield cursor trail component

### Phase 5 — Content Collections
- [ ] `src/content/config.ts` — Zod schemas
- [ ] Sample Markdown posts for each section
- [ ] Asset / image handling

### Phase 6 — Section Pages & Post Pages
- [ ] List pages (`/science`, `/music`, `/art`)
- [ ] Post pages (`/science/[...slug]`, `/music/[...slug]`, `/art/[...slug]`)
- [ ] Pagination / post ordering

### Phase 7 — 90s Sprinkles
- [ ] Pixel-art category icons
- [ ] Ironic visitor counter (footer)
- [ ] Neon color pops on hover / selection
- [ ] Subtle `<marquee>`-style ticker
- [ ] Hidden "under construction" on 404

### Phase 8 — Polish & Build
- [ ] View Transitions (smooth page nav)
- [ ] Responsive layout (mobile grid collapse)
- [ ] Font preloading, performance audit
- [ ] Pixel-art TK favicon
- [ ] `npm run build` → verify `dist/`
