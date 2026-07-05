import type { NewsItem } from './types';
import { PENG_CREDLY_MLIP_UMA, PENG_CREDLY_PEROVSKITE_GNN } from './pengCredly';

/** Primary OralScan project site (ESC Group, UB). */
export const ORALSCAN_WEBSITE = 'https://esc-group-ub.github.io/OralScan-Website/';

/** Build a public URL for a news image under `public/data/news/<id>/`. */
export function newsImagePath(id: string, file: string): string {
  return `/data/news/${id}/${encodeURIComponent(file)}`;
}

/** Build a public URL for a file in `public/data/news/` (flat folder). */
export function newsMedia(file: string): string {
  return `/data/news/${encodeURIComponent(file)}`;
}

/**
 * News timeline data. Add `images` and `links` per item; drop photos into `public/data/news/<id>/`.
 * LinkedIn: paste the post URL with `kind: 'linkedin'`.
 */
export const NEWS_ITEMS: NewsItem[] = [
  {
    id: 'msu-phd-2026',
    year: 2026,
    month: 8,
    headline: 'Incoming PhD student in MSU CSE, joining the Data Mining Laboratory (Dr. Pang-Ning Tan)',
    summary: 'Starting Fall 2026 — spatiotemporal ML, DLWF, and AI adversarial robustness.',
    images: [
      {
        src: newsMedia('MSU-offer-letter-screenshot.png'),
        alt: 'Screenshot of PhD admission offer letter from Michigan State University',
        caption: 'PhD admission — MSU Department of Computer Science and Engineering',
      },
    ],
    links: [
      { label: 'MSU CSE', href: 'https://www.cse.msu.edu/', kind: 'website' },
      { label: 'Data Mining Lab (Dr. Tan)', href: 'https://www.cse.msu.edu/~ptan/', kind: 'website' },
    ],
  },
  {
    id: 'ub-bs-2026',
    year: 2026,
    month: 6,
    headline: 'Completing accelerated BS in Computer Science at University at Buffalo',
    images: [
      {
        src: newsMedia('honors-graduation-photo.jpg'),
        alt: 'Graduation photo at University at Buffalo',
      },
      {
        src: newsMedia('honors-graduation-photo-2.jpg'),
        alt: 'Honors graduation celebration at UB',
        caption: 'Accelerated three-year BS in Computer Science (AI specialization)',
      },
    ],
    links: [
      { label: 'UB Department of Computer Science', href: 'https://www.buffalo.edu/cas/computer-science.html', kind: 'website' },
    ],
  },
  {
    id: 'inference-foundry-2026',
    year: 2026,
    month: 5,
    headline: 'Launching Inference Foundry, an open research software initiative',
    summary: 'Reproducible ML inference tooling and shared contributor infrastructure for scientific ML.',
    images: [
      {
        src: newsMedia('inference-foundry-logo.jpg'),
        alt: 'Inference Foundry logo',
        caption: 'Open research software initiative for reproducible scientific ML',
      },
    ],
    links: [
      { label: 'Inference Foundry', href: 'https://inference-foundry.rweb.site/', kind: 'website' },
      { label: 'GitHub organization', href: 'https://github.com/Kritarth-Dandapat', kind: 'github' },
    ],
  },
  {
    id: 'ta-cse341-2026',
    year: 2026,
    month: 1,
    headline: 'Started TA role for CSE 341: Computer Architecture at UB',
    links: [{ label: 'UB CSE', href: 'https://www.buffalo.edu/cas/computer-science.html', kind: 'website' }],
  },
  {
    id: 'health-futures-2026',
    year: 2026,
    month: 4,
    headline: 'Second place ($1,000) at UB Health Futures Challenge for OralScan',
    summary:
      'ESC Lab announced OralScan’s second-place finish at the 2026 UB Health Futures Challenge for its potential in geriatric dental screening.',
    links: [
      {
        label: 'LinkedIn — ESC Lab (Health Futures)',
        href: 'https://www.linkedin.com/posts/embedded-sensing-and-computing-lab_we-are-thrilled-to-share-that-oralscan-took-activity-7462602815064961025-cHgO',
        kind: 'linkedin',
      },
      { label: 'OralScan website', href: ORALSCAN_WEBSITE, kind: 'website' },
      {
        label: 'UB Health Futures announcement',
        href: 'https://www.buffalo.edu/entrepreneurship/connect/news.host.html/content/shared/www/studentlife/gateway-wide-content/announcements/current/health-futures-25.detail.html',
        kind: 'article',
      },
      {
        label: 'Health Futures Challenge (StartupTree)',
        href: 'https://ubuffalo.startuptree.co/event/s/4rCVkj4dBLVMbA6SWkwitZ/Health-Futures-Challenge---SP2025',
        kind: 'website',
      },
    ],
  },
  {
    id: 'mlip-uma-2025',
    year: 2025,
    month: 12,
    headline: 'Began equivariant MLIPs and UMA integration work in Peng Research Lab',
    links: [
      { label: 'Peng Research Lab', href: 'https://ubwp.buffalo.edu/jiayu-peng-lab/', kind: 'website' },
      { label: 'MLIP alchemical framework (arXiv)', href: 'https://arxiv.org/abs/2404.10746', kind: 'paper' },
      { label: 'Universal atom model (arXiv)', href: 'https://arxiv.org/abs/2506.23971', kind: 'paper' },
    ],
  },
  {
    id: 'credly-mlip-uma-2026',
    year: 2026,
    month: 5,
    headline:
      'Earned UB ELN Mentored Research badge (Credly) — equivariant MLIPs and UMA with Prof. Jiayu Peng',
    summary:
      'Verified micro-credential issued May 11, 2026 for MLIP / universal atom model work in the Peng Research Lab, with project outcomes on UB Box.',
    credlyBadge: PENG_CREDLY_MLIP_UMA,
    links: [
      { label: 'Peng Research Lab', href: 'https://ubwp.buffalo.edu/jiayu-peng-lab/', kind: 'website' },
      { label: 'Research — MLIP project', href: '/research/#mlip-uma-alchemical', kind: 'website' },
    ],
  },
  {
    id: 'ub-our-research-spotlight-2026',
    year: 2026,
    month: 5,
    headline: 'Featured on the UB Office for Undergraduate Research homepage with Prof. Jiayu Peng',
    summary:
      'Mentoring photo highlighted on the university undergraduate research site, showcasing faculty–student research partnerships.',
    images: [
      {
        src: newsMedia('UG-research-photo.png'),
        alt: 'Kritarth Dandapat and Prof. Jiayu Peng reviewing work on a laptop',
        caption:
          'Featured on the UB Office for Undergraduate Research homepage — May 2026',
      },
    ],
    links: [
      {
        label: 'UB Office for Undergraduate Research',
        href: 'https://www.buffalo.edu/undergrad-research.html',
        kind: 'website',
      },
      { label: 'Peng Research Lab', href: 'https://ubwp.buffalo.edu/jiayu-peng-lab/', kind: 'website' },
    ],
  },
  {
    id: 'pearl-2025',
    year: 2025,
    month: 11,
    headline: 'Received PEARL undergraduate research award ($2,500) from UB ELN',
    images: [
      {
        src: newsMedia('Rceiving-PEARL-award.png'),
        alt: 'Receiving the PEARL undergraduate research award at UB',
        caption: 'PEARL Award — $2,500, Experiential Learning Network (November 2025)',
      },
    ],
    links: [
      {
        label: 'UB Experiential Learning Network',
        href: 'https://www.buffalo.edu/eln.html',
        kind: 'website',
      },
      {
        label: 'ELN project profile (materials ML)',
        href: 'https://www.buffalo.edu/eln/students/project-portal/host-page.host.html/content/shared/www/eln/project-portal/project-profiles/active-projects/ai-design-of-disordered-materials-for-clean-energy-and-sustainable-applications.detail.html',
        kind: 'website',
      },
    ],
  },
  {
    id: 'credly-perovskite-gnn-2025',
    year: 2025,
    month: 10,
    headline:
      'Earned UB ELN Mentored Research badge (Credly) — symmetry-aware GNNs for perovskites with Prof. Jiayu Peng',
    summary:
      'Verified micro-credential issued October 30, 2025 for perovskite ordering and AI-for-materials-science project outcomes in the Peng Research Lab.',
    credlyBadge: PENG_CREDLY_PEROVSKITE_GNN,
    links: [
      { label: 'Peng Research Lab', href: 'https://ubwp.buffalo.edu/jiayu-peng-lab/', kind: 'website' },
      {
        label: 'GitHub: PerovskiteOrderingGCNNs',
        href: 'https://github.com/jiayu-peng-lab/PerovskiteOrderingGCNNs',
        kind: 'github',
      },
      { label: 'Research — perovskite GNNs', href: '/research/#perovskite-gnn', kind: 'website' },
    ],
  },
  {
    id: 'mrehab-2025',
    year: 2025,
    month: 11,
    headline: 'Joined mRehab telerehabilitation engineering at ESC Lab',
    links: [{ label: 'mRehab', href: 'https://mrehab.agency/', kind: 'website' }],
  },
  {
    id: 'peng-lab-2025',
    year: 2025,
    month: 6,
    headline: 'Joined Peng Research Lab as undergraduate researcher (symmetry-aware GNNs)',
    images: [
      {
        src: newsMedia('peng-research-lab-end-of-year-dinner.jpeg'),
        alt: 'Peng Research Lab end-of-year group dinner',
        caption: 'First end-of-year dinner with the Peng Research Lab',
      },
    ],
    links: [
      {
        label: 'LinkedIn — Peng Lab (end-of-year dinner)',
        href: 'https://www.linkedin.com/posts/jiayu-peng_a-great-way-to-close-out-the-yearour-first-activity-7405118724074074112-iDqL',
        kind: 'linkedin',
      },
      { label: 'Peng Research Lab', href: 'https://ubwp.buffalo.edu/jiayu-peng-lab/', kind: 'website' },
      { label: 'PerovskiteOrderingGCNNs', href: 'https://github.com/jiayu-peng-lab/PerovskiteOrderingGCNNs', kind: 'github' },
    ],
  },
  {
    id: 'orthoscan-2025',
    year: 2025,
    month: 2,
    headline: 'Started OrthoScan orthodontic remote monitoring at ESC Lab',
    summary:
      'ESC Lab introduced OrthoScan for at-home orthodontic progress tracking with intelligent imaging and millimeter-level measurement algorithms.',
    links: [
      {
        label: 'LinkedIn — ESC Lab (OrthoScan launch)',
        href: 'https://www.linkedin.com/feed/update/urn:li:activity:7430804286709833728/',
        kind: 'linkedin',
      },
      { label: 'ESC Lab (Prof. Xu)', href: 'https://cse.buffalo.edu/~wenyaoxu/index.html', kind: 'website' },
    ],
  },
  {
    id: 'chemrxiv-2025',
    year: 2025,
    month: 9,
    headline: 'Co-authored ChemRxiv paper on agentic AI for multimetallic catalyst discovery',
    links: [
      {
        label: 'ChemRxiv preprint',
        href: 'https://doi.org/10.26434/chemrxiv-2025-13n3f',
        kind: 'paper',
      },
    ],
  },
  {
    id: 'cybersecurity-2025',
    year: 2025,
    month: 7,
    headline: 'Placed 10th globally at Northeastern Cybersecurity C2C Finals',
    summary:
      'Competed in the 2025 INCS-CoE Country to Country CTF finals at Northeastern after qualifying earlier in the year.',
    images: [
      {
        src: newsMedia('C2C-CTF-image-1.jpeg'),
        alt: 'Country to Country CTF finals at Northeastern University',
      },
      {
        src: newsMedia('C2C-CTF-image-2 (team image).jpeg'),
        alt: 'C2C-CTF team Hasc11s at the competition',
        caption: 'Team Hasc11s — Jeremy, Tenzin, Roy, and Kritarth',
      },
      {
        src: newsMedia('C2C-CTF-image-3.jpeg'),
        alt: 'Cybersecurity C2C finals event',
      },
      {
        src: newsMedia('C2C-CTF-image-4.jpeg'),
        alt: 'Additional photo from the C2C-CTF finals at Northeastern',
      },
    ],
    links: [
      {
        label: 'LinkedIn — C2C-CTF finals',
        href: 'https://www.linkedin.com/posts/kritarth-dandapat_internationalcompetition-cybersecurity-ctf-ugcPost-7351704128718262272-9VMj/',
        kind: 'linkedin',
      },
      {
        label: 'Cybersecurity C2C',
        href: 'https://www.northeastern.edu/cybersecurity-c2c/',
        kind: 'website',
      },
    ],
  },
  {
    id: 'competitions-2024',
    year: 2024,
    month: 11,
    headline: 'Team member for OralScan at Agrusa CSE Innovation and Aging Innovations challenges',
    links: [{ label: 'OralScan website', href: ORALSCAN_WEBSITE, kind: 'website' }],
  },
  {
    id: 'oralscan-pi-2024',
    year: 2024,
    month: 10,
    headline: 'Principal Investigator for OralScan at Community Champions for Disability Health Challenge',
    links: [{ label: 'OralScan website', href: ORALSCAN_WEBSITE, kind: 'website' }],
  },
  {
    id: 'tutor-2024',
    year: 2024,
    month: 8,
    headline: 'Started tutor and peer-assisted leader role in statistics at UB',
    links: [
      {
        label: 'Tutoring & Academic Support Services',
        href: 'https://www.buffalo.edu/studentsuccess/tutoring.html',
        kind: 'website',
      },
    ],
  },
  {
    id: 'esc-oralscan-2024',
    year: 2024,
    month: 6,
    headline: 'Joined ESC Lab as research assistant; started OralScan mobile health AI',
    summary:
      'ESC Lab launched OralScan — an AI-powered smartphone app for guided intraoral imaging and geriatric oral health monitoring.',
    images: [
      {
        src: newsMedia('oralscan-image.png'),
        alt: 'OralScan infographic: EHR integration, mobile app, and AI-powered diagnostics',
        caption: 'OralScan system overview — patient app, EHR integration, and AI diagnostics',
      },
    ],
    links: [
      {
        label: 'LinkedIn — ESC Lab (OralScan launch)',
        href: 'https://www.linkedin.com/feed/update/urn:li:activity:7430804267093053440/',
        kind: 'linkedin',
      },
      { label: 'OralScan website', href: ORALSCAN_WEBSITE, kind: 'website' },
      { label: 'ESC Lab (Prof. Xu)', href: 'https://cse.buffalo.edu/~wenyaoxu/index.html', kind: 'website' },
    ],
  },
  {
    id: 'presentations-2025',
    year: 2025,
    month: 1,
    headline: 'Presented OralScan at CTSI clinical group and SUNY Undergraduate Research Conference',
    images: [
      {
        src: newsMedia('presenting-oralscan-ctsi-study.jpeg'),
        alt: 'Presenting the OralScan study to the CTSI research group',
        caption: 'Oral presentation and live demo — CTSI and SURC (January 2025)',
      },
    ],
    links: [
      { label: 'OralScan website', href: ORALSCAN_WEBSITE, kind: 'website' },
    ],
  },
  {
    id: 'arxiv-gnn-2025',
    year: 2025,
    month: 9,
    headline: 'Contributed benchmarking to arXiv paper on symmetry-aware GNNs for crystal ordering',
    links: [
      { label: 'arXiv:2409.13851', href: 'https://arxiv.org/abs/2409.13851', kind: 'paper' },
      { label: 'PerovskiteOrderingGCNNs', href: 'https://github.com/jiayu-peng-lab/PerovskiteOrderingGCNNs', kind: 'github' },
    ],
  },
  {
    id: 'nsdc-2023',
    year: 2023,
    month: 10,
    headline: 'Co-founded and launched UB chapter of the National Student Data Corps',
    links: [{ label: 'National Student Data Corps', href: 'https://nsdc.buffalo.edu/', kind: 'website' }],
  },
  {
    id: 'ub-start-2023',
    year: 2023,
    month: 8,
    headline: 'Started BS in Computer Science (AI specialization) at University at Buffalo, SUNY',
    links: [
      { label: 'UB Department of Computer Science', href: 'https://www.buffalo.edu/cas/computer-science.html', kind: 'website' },
    ],
  },
];
