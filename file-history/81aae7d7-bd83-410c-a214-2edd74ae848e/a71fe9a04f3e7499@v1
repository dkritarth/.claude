import React from 'react';
import { Github, Instagram, Linkedin, Mail, ArrowRight, ExternalLink, Twitter } from 'lucide-react';
import { CONTACT_INFO, NAV_LINKS } from '../constants';
import { CvDownloadLink } from './CvDownloadLink';

const PORTRAIT = '/data/my-photo.jpg';

export const Hero: React.FC = () => {
  return (
    <section className="relative min-h-[calc(100vh-1px)] flex items-center pt-28 sm:pt-32 pb-16 overflow-hidden border-b border-ink-200/80 bg-ink-50">
      <div className="absolute inset-0 pointer-events-none bg-[radial-gradient(ellipse_80%_50%_at_50%_-20%,rgba(28,25,23,0.06),transparent)]" />

      <div className="max-w-6xl mx-auto px-6 md:px-10 w-full relative z-10 grid md:grid-cols-[1fr_minmax(260px,340px)] gap-12 lg:gap-16 items-center">
        <div className="space-y-8">
          <header className="space-y-3">
            <p className="text-sm font-semibold tracking-wide text-ink-700 uppercase">
              Computer Science · University at Buffalo · MSU PhD Fall 2026
            </p>
            <h1 className="text-4xl md:text-5xl lg:text-[3.25rem] font-serif font-semibold text-ink-900 leading-[1.15] tracking-tight">
              {CONTACT_INFO.name}
            </h1>
            <p className="text-lg md:text-xl text-ink-700 font-sans font-normal max-w-xl">
              {CONTACT_INFO.title}
            </p>
          </header>

          <p className="text-base md:text-[1.05rem] text-ink-800 leading-relaxed max-w-2xl border-l-[3px] border-ink-900 pl-5">
            {CONTACT_INFO.landingLead}
          </p>

          <div className="max-w-2xl rounded-sm border border-ink-200 bg-white/80 px-4 py-3 text-[15px] leading-relaxed text-ink-800 shadow-sm">
            <p className="font-semibold text-ink-900">Inference Foundry</p>
            <p className="mt-1 text-ink-700">
              {CONTACT_INFO.inferenceFoundry.startLabel}. {CONTACT_INFO.inferenceFoundry.description}
            </p>
            <a
              href={CONTACT_INFO.inferenceFoundry.url}
              target="_blank"
              rel="noopener noreferrer"
              className="mt-2 inline-flex items-center gap-1 text-sm font-semibold text-ink-900 underline underline-offset-2 hover:no-underline"
            >
              inference-foundry.rweb.site <ExternalLink size={14} className="opacity-70" aria-hidden />
            </a>
          </div>

          <div className="flex flex-wrap gap-3">
            <a
              href="/research/"
              className="inline-flex items-center justify-center gap-1.5 px-5 py-2.5 bg-ink-900 text-white text-sm font-semibold tracking-wide hover:bg-ink-800 transition-colors"
            >
              Research <ArrowRight size={16} className="opacity-90" aria-hidden />
            </a>
            <CvDownloadLink variant="hero" />
            <a
              href={`mailto:${CONTACT_INFO.email}`}
              className="inline-flex items-center justify-center px-5 py-2.5 text-sm font-semibold text-ink-800 underline-offset-4 hover:underline"
            >
              Email
            </a>
          </div>

          <nav aria-label="Site sections" className="pt-2">
            <p className="text-xs font-semibold uppercase tracking-wide text-ink-500 mb-2">More</p>
            <ul className="flex flex-wrap items-center gap-x-2 gap-y-1 text-sm">
              {NAV_LINKS.map((link, i) => (
                <li key={link.href} className="inline-flex items-center">
                  {i > 0 && <span className="text-ink-300 pr-2 select-none" aria-hidden>·</span>}
                  <a
                    href={link.href}
                    className="text-ink-800 font-medium underline underline-offset-2 hover:text-ink-950 decoration-ink-300 hover:decoration-ink-900"
                  >
                    {link.label}
                  </a>
                </li>
              ))}
            </ul>
          </nav>

          <div className="flex items-center gap-5 pt-4 border-t border-ink-200">
            <a
              href={CONTACT_INFO.github}
              target="_blank"
              rel="noopener noreferrer"
              className="text-ink-600 hover:text-ink-900 transition-colors"
              aria-label="GitHub"
            >
              <Github size={22} />
            </a>
            <a
              href={CONTACT_INFO.linkedin}
              target="_blank"
              rel="noopener noreferrer"
              className="text-ink-600 hover:text-ink-900 transition-colors"
              aria-label="LinkedIn"
            >
              <Linkedin size={22} />
            </a>
            <a
              href={CONTACT_INFO.instagram}
              target="_blank"
              rel="noopener noreferrer"
              className="text-ink-600 hover:text-ink-900 transition-colors"
              aria-label="Instagram"
            >
              <Instagram size={22} />
            </a>
            <a
              href={CONTACT_INFO.twitter}
              target="_blank"
              rel="noopener noreferrer"
              className="text-ink-600 hover:text-ink-900 transition-colors"
              aria-label="X / Twitter"
            >
              <Twitter size={22} />
            </a>
            <a
              href={`mailto:${CONTACT_INFO.email}`}
              className="text-ink-600 hover:text-ink-900 transition-colors"
              aria-label="Email"
            >
              <Mail size={22} />
            </a>
          </div>
        </div>

        <figure className="relative hidden md:block mx-auto w-full max-w-sm">
          <div className="aspect-[4/5] relative border border-ink-200 bg-ink-100 shadow-[0_1px_0_rgba(28,25,23,0.06)] overflow-hidden">
            <img
              src={PORTRAIT}
              alt={`${CONTACT_INFO.name}, portrait`}
              className="w-full h-full object-cover grayscale-[15%]"
            />
            <figcaption className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-ink-900/90 via-ink-900/50 to-transparent px-5 pt-16 pb-5 text-left">
              <p className="text-[11px] font-semibold uppercase tracking-widest text-white/80 mb-1">
                Research areas
              </p>
              <p className="text-sm text-white leading-snug font-sans">
                Spatiotemporal ML · DLWF · AI robustness · Computer vision · Materials ML
              </p>
            </figcaption>
          </div>
        </figure>
      </div>
    </section>
  );
};
