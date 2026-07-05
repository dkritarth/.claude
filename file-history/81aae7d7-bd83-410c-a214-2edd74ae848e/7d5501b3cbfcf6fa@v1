import { useEffect, useState } from 'react';
import type { SitePage } from './types';

const ALLOWED_PAGES: SitePage[] = ['about', 'research', 'projects', 'education', 'news'];

/** Migrate legacy hash URLs (`#/about`) to path URLs (`/about`). */
export function migrateHashRoute(): void {
  if (typeof window === 'undefined') return;
  const hash = window.location.hash;
  if (!hash.startsWith('#/')) return;
  const path = hash.slice(1);
  window.history.replaceState(null, '', path || '/');
}

export function parsePathname(pathname: string): SitePage {
  const normalized = pathname.replace(/\/+$/, '') || '/';
  if (normalized === '/') return 'home';
  const segment = normalized.split('/').filter(Boolean)[0] ?? '';
  if (segment === 'notes') return 'news';
  if (ALLOWED_PAGES.includes(segment as SitePage)) {
    return segment as SitePage;
  }
  return 'home';
}

export function parseSiteRoute(): SitePage {
  if (typeof window === 'undefined') return 'home';
  return parsePathname(window.location.pathname);
}

export function useSiteRoute(): SitePage {
  const [page, setPage] = useState<SitePage>(() => {
    if (typeof window === 'undefined') return 'home';
    migrateHashRoute();
    return parseSiteRoute();
  });

  useEffect(() => {
    migrateHashRoute();
    setPage(parseSiteRoute());

    const onNavigate = () => setPage(parseSiteRoute());
    window.addEventListener('popstate', onNavigate);
    return () => window.removeEventListener('popstate', onNavigate);
  }, []);

  return page;
}
