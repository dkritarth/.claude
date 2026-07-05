/** SEO helpers: per-route titles, meta tags, canonical URLs, and JSON-LD. */
import type { SitePage } from './types';
import { CONTACT_INFO, PUBLICATIONS } from './constants';

export const PORTFOLIO_ORIGIN = 'https://dkritarth.com';
const SITE_NAME = 'Kritarth Dandapat';
const DEFAULT_OG_IMAGE = `${PORTFOLIO_ORIGIN}/data/my-photo.jpg`;

export const PAGE_PATHS: Record<SitePage, string> = {
  home: '/',
  about: '/about/',
  research: '/research/',
  publications: '/publications/',
  projects: '/projects/',
  education: '/education/',
  news: '/news/',
};

/** Visible page title for screen-reader / document outline (one h1 per view). */
export const PAGE_HEADINGS: Record<SitePage, string> = {
  home: `${CONTACT_INFO.name} — AI researcher and incoming PhD student`,
  about: 'About Kritarth Dandapat',
  research: 'Research',
  publications: 'Publications',
  projects: 'Selected projects',
  education: 'Education and experience',
  news: 'News and milestones',
};

const HOME_TITLE = `${CONTACT_INFO.name} · AI Researcher · Incoming PhD Student`;
const HOME_DESC = CONTACT_INFO.bio;

const SEO: Record<SitePage, { title: string; description: string }> = {
  home: {
    title: HOME_TITLE,
    description: HOME_DESC,
  },
  about: {
    title: `About · ${SITE_NAME}`,
    description:
      'Background, research interests, honors, certifications, and technical skills. Incoming MSU CSE PhD student (Data Mining Laboratory, Dr. Pang-Ning Tan); undergraduate researcher at University at Buffalo.',
  },
  research: {
    title: `Research · ${SITE_NAME}`,
    description:
      'Healthcare AI (OralScan, OrthoScan, mRehab), computational materials science (symmetry-aware GNNs, equivariant MLIPs), and materials discovery pipelines.',
  },
  publications: {
    title: `Publications · ${SITE_NAME}`,
    description:
      'Papers, preprints, and demo tracks across healthcare AI, computational materials science, and rehabilitation systems. Venues include Smart Health, HumanSys, MobiComm, ChemRxiv, and arXiv.',
  },
  projects: {
    title: `Projects · ${SITE_NAME}`,
    description:
      'PaddockPsychRL (F1-informed multi-agent RL), Marine Guardian satellite ship detection, CSRNet crowd counting, and multi-architecture emotion detection benchmarks.',
  },
  education: {
    title: `Education & Experience · ${SITE_NAME}`,
    description:
      'Accelerated BS in Computer Science at UB; incoming PhD at Michigan State University; CSE 341 teaching assistant, tutoring, and student leadership.',
  },
  news: {
    title: `News · ${SITE_NAME}`,
    description:
      'Timeline of research milestones, awards, publications, and project launches with links and photos.',
  },
};

export function pageCanonicalUrl(page: SitePage): string {
  const path = PAGE_PATHS[page];
  return path === '/' ? `${PORTFOLIO_ORIGIN}/` : `${PORTFOLIO_ORIGIN}${path}`;
}

function buildWebSiteNode() {
  return {
    '@type': 'WebSite',
    '@id': `${PORTFOLIO_ORIGIN}/#website`,
    name: `${SITE_NAME} — Academic site`,
    url: `${PORTFOLIO_ORIGIN}/`,
    description: HOME_DESC,
    publisher: { '@id': `${PORTFOLIO_ORIGIN}/#person` },
    inLanguage: 'en-US',
  };
}

function buildPersonNode() {
  return {
    '@type': 'Person',
    '@id': `${PORTFOLIO_ORIGIN}/#person`,
    name: CONTACT_INFO.name,
    url: `${PORTFOLIO_ORIGIN}/`,
    image: DEFAULT_OG_IMAGE,
    email: `mailto:${CONTACT_INFO.email}`,
    jobTitle: 'Incoming PhD Student; Undergraduate Researcher',
    description: HOME_DESC,
    sameAs: [
      CONTACT_INFO.github,
      CONTACT_INFO.linkedin,
      CONTACT_INFO.website,
      CONTACT_INFO.inferenceFoundry.url,
      'https://www.instagram.com/kritarth_dandapat/',
      'https://x.com/Kritarth25',
    ],
    worksFor: {
      '@type': 'CollegeOrUniversity',
      name: 'University at Buffalo, SUNY',
    },
    alumniOf: {
      '@type': 'CollegeOrUniversity',
      name: 'University at Buffalo, SUNY',
    },
    affiliation: {
      '@type': 'CollegeOrUniversity',
      name: 'Michigan State University',
    },
    knowsAbout: [
      'Spatiotemporal machine learning',
      'Deep learning-based weather forecasting',
      'AI adversarial robustness',
      'Computer vision',
      'Healthcare AI',
      'Materials machine learning',
      'Graph neural networks',
    ],
  };
}

function buildProfilePageNode(page: SitePage) {
  return {
    '@type': 'ProfilePage',
    '@id': `${pageCanonicalUrl(page)}#webpage`,
    url: pageCanonicalUrl(page),
    name: SEO[page].title,
    description: SEO[page].description,
    isPartOf: { '@id': `${PORTFOLIO_ORIGIN}/#website` },
    about: { '@id': `${PORTFOLIO_ORIGIN}/#person` },
    inLanguage: 'en-US',
  };
}

function buildBreadcrumbNode(page: SitePage) {
  const items = [
    { '@type': 'ListItem', position: 1, name: 'Home', item: `${PORTFOLIO_ORIGIN}/` },
  ];
  if (page !== 'home') {
    items.push({
      '@type': 'ListItem',
      position: 2,
      name: PAGE_HEADINGS[page],
      item: pageCanonicalUrl(page),
    });
  }
  return {
    '@type': 'BreadcrumbList',
    '@id': `${pageCanonicalUrl(page)}#breadcrumb`,
    itemListElement: items,
  };
}

function buildPublicationNodes() {
  return PUBLICATIONS.filter((p) => p.link).map((pub, index) => ({
    '@type': 'ScholarlyArticle',
    '@id': `${PORTFOLIO_ORIGIN}/#publication-${index}`,
    headline: pub.title,
    author: pub.authors,
    datePublished: pub.year,
    url: pub.link,
    isPartOf: { '@id': `${PORTFOLIO_ORIGIN}/#person` },
  }));
}

function buildStructuredData(page: SitePage): object {
  const graph = [
    buildWebSiteNode(),
    buildPersonNode(),
    buildProfilePageNode(page),
    buildBreadcrumbNode(page),
  ];
  if (page === 'publications') {
    graph.push(...buildPublicationNodes());
  }
  return {
    '@context': 'https://schema.org',
    '@graph': graph,
  };
}

export function applyPageSeo(page: SitePage): void {
  const { title, description } = SEO[page];
  const canonical = pageCanonicalUrl(page);

  document.title = title;

  ensureMetaName('description').setAttribute('content', description);
  ensureMetaName('author').setAttribute('content', CONTACT_INFO.name);
  ensureMetaName('robots').setAttribute('content', 'index, follow, max-image-preview:large');

  ensureLinkRel('canonical').setAttribute('href', canonical);

  ensureMetaProperty('og:type').setAttribute('content', 'profile');
  ensureMetaProperty('og:site_name').setAttribute('content', SITE_NAME);
  ensureMetaProperty('og:title').setAttribute('content', title);
  ensureMetaProperty('og:description').setAttribute('content', description);
  ensureMetaProperty('og:url').setAttribute('content', canonical);
  ensureMetaProperty('og:locale').setAttribute('content', 'en_US');
  ensureMetaProperty('og:image').setAttribute('content', DEFAULT_OG_IMAGE);
  ensureMetaProperty('og:image:alt').setAttribute(
    'content',
    `${CONTACT_INFO.name}, portrait`,
  );

  ensureMetaName('twitter:card').setAttribute('content', 'summary_large_image');
  ensureMetaName('twitter:title').setAttribute('content', title);
  ensureMetaName('twitter:description').setAttribute('content', description);
  ensureMetaName('twitter:image').setAttribute('content', DEFAULT_OG_IMAGE);
  ensureMetaName('twitter:image:alt').setAttribute(
    'content',
    `${CONTACT_INFO.name}, portrait`,
  );

  updateJsonLd(buildStructuredData(page));
}

function updateJsonLd(data: object): void {
  const id = 'site-structured-data';
  let el = document.getElementById(id) as HTMLScriptElement | null;
  if (!el) {
    el = document.createElement('script');
    el.id = id;
    el.type = 'application/ld+json';
    document.head.appendChild(el);
  }
  el.textContent = JSON.stringify(data);
}

function ensureMetaName(name: string): HTMLMetaElement {
  let el = document.querySelector(`meta[name="${name}"]`) as HTMLMetaElement | null;
  if (!el) {
    el = document.createElement('meta');
    el.setAttribute('name', name);
    document.head.appendChild(el);
  }
  return el;
}

function ensureMetaProperty(property: string): HTMLMetaElement {
  let el = document.querySelector(`meta[property="${property}"]`) as HTMLMetaElement | null;
  if (!el) {
    el = document.createElement('meta');
    el.setAttribute('property', property);
    document.head.appendChild(el);
  }
  return el;
}

function ensureLinkRel(rel: string): HTMLLinkElement {
  let el = document.querySelector(`link[rel="${rel}"]`) as HTMLLinkElement | null;
  if (!el) {
    el = document.createElement('link');
    el.setAttribute('rel', rel);
    document.head.appendChild(el);
  }
  return el;
}
