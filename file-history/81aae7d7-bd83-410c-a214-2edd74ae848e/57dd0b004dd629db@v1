import React, { useState, useEffect } from 'react';
import { Menu, X } from 'lucide-react';
import { NAV_LINKS } from '../constants';
import { useSiteRoute } from '../useSiteRoute';
import { CvDownloadLink } from './CvDownloadLink';

export const Header: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);
  const page = useSiteRoute();

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const linkClass = (active: boolean) =>
    `px-2.5 py-1.5 text-sm font-medium rounded-sm transition-colors ${
      active ? 'text-ink-900 bg-ink-200/80' : 'text-ink-700 hover:text-ink-900 hover:bg-ink-100/80'
    }`;

  const mobileLinkClass = (active: boolean) =>
    `text-base font-medium py-3 px-2 rounded-sm border-b border-ink-100 last:border-0 ${
      active ? 'text-ink-950 bg-ink-100' : 'text-ink-800 hover:bg-ink-100'
    }`;

  return (
    <header
      className={`fixed top-0 left-0 w-full z-50 transition-all duration-200 ${
        isScrolled
          ? 'bg-ink-50/95 backdrop-blur-md border-b border-ink-200 py-2.5'
          : 'bg-ink-50/80 backdrop-blur-sm border-b border-ink-200/70 py-3'
      }`}
    >
      <div className="max-w-6xl mx-auto px-6 flex justify-between items-center gap-4">
        <a
          href="/"
          className={`flex items-center gap-3 min-w-0 transition-colors ${
            page === 'home' ? 'text-ink-950' : 'text-ink-900 hover:text-ink-800'
          }`}
        >
          <img
            src="/data/my-photo.jpg"
            alt=""
            aria-hidden
            className="w-9 h-9 rounded-full object-cover border border-ink-300 shrink-0"
          />
          <span className="font-serif text-lg md:text-xl font-semibold tracking-tight truncate">
            Kritarth Dandapat
          </span>
        </a>

        <nav className="hidden lg:flex items-center gap-1 flex-wrap justify-end" aria-label="Site sections">
          {NAV_LINKS.map((link) => (
            <a key={link.label} href={link.href} className={linkClass(page === link.page)}>
              {link.label}
            </a>
          ))}
          <CvDownloadLink variant="header" />
        </nav>

        <button
          type="button"
          className="lg:hidden text-ink-900 p-2 shrink-0"
          onClick={() => setIsOpen(!isOpen)}
          aria-label="Toggle menu"
        >
          {isOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      {isOpen && (
        <div className="lg:hidden border-t border-ink-200 bg-ink-50 max-h-[80vh] overflow-y-auto">
          <nav className="flex flex-col p-4 gap-0.5" aria-label="Site sections">
            {NAV_LINKS.map((link) => (
              <a
                key={link.label}
                href={link.href}
                onClick={() => setIsOpen(false)}
                className={mobileLinkClass(page === link.page)}
              >
                {link.label}
              </a>
            ))}
            <div onClick={() => setIsOpen(false)} role="presentation">
              <CvDownloadLink variant="headerMobile" />
            </div>
          </nav>
        </div>
      )}
    </header>
  );
};
