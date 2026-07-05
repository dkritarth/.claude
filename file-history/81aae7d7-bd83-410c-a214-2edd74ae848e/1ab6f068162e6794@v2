# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
npm run dev        # dev server at http://localhost:3000
npm run build      # vite build + postbuild SEO script (sitemap, 404.html)
npm run deploy     # build then push dist/ to GitHub Pages via gh-pages
```

There are no tests and no linter config in this repo.

## Architecture

**Stack:** React 19 + TypeScript + Vite, deployed to `dkritarth.com` via GitHub Pages (`gh-pages` package).

### Routing

There is no React Router. `useSiteRoute.ts` implements a custom SPA router using `window.location.pathname` and the browser `popstate` event. Navigation is done with `history.pushState` (not `<Link>` or `<Navigate>`). `parsePathname` maps `/notes` → `news` page (legacy alias) and migrates legacy hash URLs (`#/about`) to path URLs on first load.

### Content data flow

All site content lives in a handful of source-of-truth files:

| File | Purpose |
|---|---|
| `constants.tsx` | All biographical, research, project, education, and skills data. Also exports `NAV_LINKS` and utility functions like `getNewsByYear()`. |
| `newsItems.ts` | `NEWS_ITEMS` array — the News/timeline page data. |
| `pengCredly.ts` | `CredlyBadge` objects for UB ELN Mentored Research micro-credentials. |
| `types.ts` | All shared TypeScript interfaces (`SitePage`, `ResearchPlacement`, `ResearchSubproject`, `Project`, `NewsItem`, `CredlyBadge`, etc.). |
| `seoMeta.ts` | Per-route titles, descriptions, canonical URLs, OG tags, and JSON-LD structured data. Applied client-side via `applyPageSeo(page)` called in `App.tsx`'s `useEffect`. |
| `siteUrls.ts` | Cross-site URLs; swaps to localhost ports when `hostname === 'localhost'`. |

When adding or updating content (new publication, news item, project, etc.), edit `constants.tsx` or `newsItems.ts` — pages read from these directly and do not have their own state.

### SEO / build pipeline

`scripts/postbuild-seo.mjs` runs after `vite build` and:
- Writes `dist/sitemap.xml` and `public/sitemap.xml`
- Writes `dist/404.html` — a GitHub Pages SPA fallback that stores `location.href` in `sessionStorage` and redirects to `/`, where the React router re-parses the path

If you add a new route (new `SitePage` value), update `ROUTES` in `postbuild-seo.mjs`, `PAGE_PATHS` and `SEO` in `seoMeta.ts`, the switch in `App.tsx`, and `ALLOWED_PAGES` in `useSiteRoute.ts`.

### Static assets

Images and PDFs live under `public/data/`:
- `public/data/news/<id>/` — news timeline photos (id matches `NewsItem.id`)
- `public/data/research/<id>/` — research figures (id matches `ResearchSubproject.id`)
- `public/data/projects/<slug>/` — project screenshots (slug matches `Project.slug`)
- `public/data/CV%20-%20Kritarth%20Dandapat.pdf` and `Resume%20-%20Kritarth%20Dandapat.pdf`

`newsItems.ts` exports `newsImagePath(id, file)` and `newsMedia(file)` helpers for building correct `/data/news/...` paths.

### Components

`components/` contains shared UI pieces. `pages/` contains one file per route; each page imports directly from `constants.tsx` / `newsItems.ts` and composes components. `PageLayout` and `Header`/`Footer` provide the shell; `Section` is the standard content wrapper.
