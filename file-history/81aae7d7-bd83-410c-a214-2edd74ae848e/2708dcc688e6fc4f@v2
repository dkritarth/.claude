#!/usr/bin/env node
/**
 * After `vite build`: GitHub Pages SPA 404 + sitemap with all path routes.
 */
import { copyFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, '..');
const dist = join(root, 'dist');

const ORIGIN = 'https://dkritarth.com';
const ROUTES = [
  { path: '/', priority: '1.0', changefreq: 'weekly' },
  { path: '/about/', priority: '0.9', changefreq: 'monthly' },
  { path: '/research/', priority: '0.9', changefreq: 'weekly' },
  { path: '/publications/', priority: '0.95', changefreq: 'weekly' },
  { path: '/projects/', priority: '0.85', changefreq: 'monthly' },
  { path: '/education/', priority: '0.8', changefreq: 'monthly' },
  { path: '/news/', priority: '0.8', changefreq: 'weekly' },
];

const lastmod = new Date().toISOString().slice(0, 10);

const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${ROUTES.map(
  (r) => `  <url>
    <loc>${ORIGIN}${r.path === '/' ? '/' : r.path}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>${r.changefreq}</changefreq>
    <priority>${r.priority}</priority>
  </url>`,
).join('\n')}
</urlset>
`;

const spa404 = `<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Redirecting…</title>
    <script>
      sessionStorage.setItem('gh_pages_redirect', location.href);
      location.replace(${JSON.stringify(ORIGIN + '/')});
    </script>
  </head>
  <body>
    <p>Redirecting…</p>
  </body>
</html>
`;

mkdirSync(dist, { recursive: true });
writeFileSync(join(dist, 'sitemap.xml'), sitemap, 'utf8');
writeFileSync(join(dist, '404.html'), spa404, 'utf8');
writeFileSync(join(root, 'public', 'sitemap.xml'), sitemap, 'utf8');

console.log('postbuild-seo: wrote dist/sitemap.xml, dist/404.html, public/sitemap.xml');
