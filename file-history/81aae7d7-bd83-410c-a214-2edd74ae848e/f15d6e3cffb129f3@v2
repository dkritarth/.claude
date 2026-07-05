# Portfolio Update Plan

## Context
Multiple content and design updates to the academic portfolio at dkritarth.com: brand identity, research section UX, content updates (publications, periods, URL), diploma display, and a richer landing page.

---

## 1. Favicon + Logo in header
**Files:** `index.html`, `components/Header.tsx`

- `index.html`: change `<link rel="icon">` and `<link rel="apple-touch-icon">` from `/data/my-photo.jpg` → `/data/dkritarth_logo.png`
- `Header.tsx`: replace the `<img src="/data/my-photo.jpg" className="w-9 h-9 rounded-full …">` avatar with `<img src="/data/dkritarth_logo.png" className="w-9 h-9 object-contain …">` (square, no border-radius, since a logo usually isn't round)

---

## 2. Banner as blurred background texture
**Files:** `components/Hero.tsx`, and optionally `components/Section.tsx`

- In `Hero.tsx`, inside the `<section>` (which already has `relative overflow-hidden`), add a second `absolute inset-0 pointer-events-none` div **before** the existing radial-gradient div:
  ```tsx
  <div
    className="absolute inset-0 pointer-events-none"
    style={{
      backgroundImage: "url('/data/DK banner.png')",
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      filter: 'blur(12px)',
      opacity: 0.07,
      transform: 'scale(1.05)', // prevent blur edge bleed
    }}
  />
  ```
- The existing radial-gradient div stays on top of it for the vignette. Net effect: very subtle textured background that doesn't interfere with legibility.

---

## 3. Research section — accordion cards
**Files:** `components/Research.tsx`

Convert `ResearchProjectCard` to accordion style:
- Add `const [isOpen, setIsOpen] = useState(false)` at the top of the component
- **Collapsed state** (always visible): project name + period header, technology tag chips, and a `ChevronDown` toggle button
- **Expanded state** (on click): full content — context, narrative, ContentImageGrid, collaboratorsNote, technical contributions, links, CredlyBadgeBlock — followed by a `ChevronUp` to collapse
- The placement-level header (lab name, role, overview, placementLinks) remains always visible and unchanged
- Use `lucide-react`'s `ChevronDown` / `ChevronUp` icons for the toggle affordance
- Transition with `hidden` / block (no animation needed, but can add `transition-all` if desired)

---

## 4. OralScan URL — global replace
**Files:** `newsItems.ts`, `constants.tsx`

- `newsItems.ts`: change `ORALSCAN_WEBSITE` constant from `'https://esc-group-ub.github.io/OralScan-Website/'` → `'https://oralscan.auspexmedix.com/'`
- `constants.tsx`: find the OralScan subproject `links` array; replace any `href` values pointing at the old ESC GitHub URL with `'https://oralscan.auspexmedix.com/'` (currently one entry: `{ label: 'OralScan website', href: '…' }`)

---

## 5. New publications
**File:** `constants.tsx` → `PUBLICATIONS` array (add 4 entries)

```ts
{
  title: 'From Community Feedback to Measurement Redesign: Iterating mRehab for Accessible Home-Based Stroke Rehabilitation',
  authors: 'Dandapat, K., Emily [Surname], Master, T. A., Das, A., Bo, W., Cavuoto, L., and Xu, W.',
  venue: 'HumanSys 2026',
  year: '2026',
  status: 'Under submission',
},
{
  title: 'Separating Safety from Preference: A Role-Gated Evaluation Platform for Clinical Rehabilitation LLMs',
  authors: 'Dandapat, K., Master, T. A., Das, A., Bo, W., Lei, M., Cavuoto, L., Subryan, H., and Xu, W.',
  venue: 'HumanSys 2026',
  year: '2026',
  status: 'Under submission',
},
{
  title: 'Towards AI Agents for Intelligent Voice-Driven Interaction in a Home-Based Stroke Rehabilitation System',
  authors: 'Lei, M., Das, A., Master, T. A., Dandapat, K., Reddipogu, P., Xian, J., Rowe, V., Craft, L., Tabb, K., Cavuoto, L., Bhattacharjya, S., Jo, H. J., Subryan, H., Bo, W., and Xu, W.',
  venue: 'University at Buffalo and Georgia State University',
  year: '2026',
  status: 'Under submission',
},
{
  title: 'Demo: mRehab – A Tangible, Offline-First Mobile Platform for Post-Stroke Upper-Limb Rehabilitation with an Edge-Cloud Voice',
  authors: 'Dandapat, K., et al.',
  venue: 'MobiComm 2026 (Demo Track)',
  year: '2026',
  status: 'Under submission',
},
```

---

## 6. Period end dates
**File:** `constants.tsx`

- mRehab subproject `period`: `'November 2025 – Present'` → `'November 2025 – August 2026'`
- mlip-uma-alchemical subproject `period`: `'December 2025 – Present'` → `'December 2025 – June 2026'`

---

## 7. Duration display utility
**Files:** `constants.tsx` (add utility), `components/Research.tsx`, `components/Timeline.tsx`

Add a utility function near the top of `constants.tsx`:

```ts
const MONTH_NAMES = ['January','February','March','April','May','June',
  'July','August','September','October','November','December'];

export function computeDuration(period: string): string | null {
  const parts = period.split('–').map(s => s.trim());
  if (parts.length !== 2) return null;
  const parseMonthYear = (s: string): { year: number; month: number } | null => {
    if (s === 'Present') return { year: 2026, month: 7 }; // current: July 2026
    const m = s.match(/^([A-Za-z]+)\s+(\d{4})$/);
    if (!m) return null;
    const month = MONTH_NAMES.indexOf(m[1]) + 1;
    if (!month) return null;
    return { year: parseInt(m[2], 10), month };
  };
  const start = parseMonthYear(parts[0]);
  const end = parseMonthYear(parts[1]);
  if (!start || !end) return null;
  const totalMonths = (end.year - start.year) * 12 + (end.month - start.month);
  if (totalMonths <= 0) return null;
  const years = Math.floor(totalMonths / 12);
  const months = totalMonths % 12;
  const parts2: string[] = [];
  if (years > 0) parts2.push(`${years} year${years > 1 ? 's' : ''}`);
  if (months > 0) parts2.push(`${months} month${months > 1 ? 's' : ''}`);
  return parts2.join(' ') || null;
}
```

Apply in:
- `Research.tsx`: In `ResearchProjectCard`, render the period span as `{project.period}{dur ? ` (${dur})` : ''}` where `dur = computeDuration(project.period)`
- `Timeline.tsx`: Same pattern for `edu.period` and `job.period` display lines

---

## 8. Diploma — PDF modal + lightbox
**Files:** Create `components/DiplomaModal.tsx`, update `components/Timeline.tsx`

Since the diploma is a PDF (not an image), use a browser-native `<iframe>` embed in a modal overlay — this renders natively in all modern browsers.

**`DiplomaModal.tsx`** (new file):
```tsx
import React from 'react';
import { X, Download } from 'lucide-react';

type DiplomaModalProps = { isOpen: boolean; onClose: () => void };

export const DiplomaModal: React.FC<DiplomaModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-ink-900/80 backdrop-blur-sm" onClick={onClose}>
      <div className="relative w-full max-w-3xl h-[80vh] bg-white rounded-sm shadow-xl flex flex-col" onClick={e => e.stopPropagation()}>
        <div className="flex items-center justify-between px-5 py-3 border-b border-ink-200 shrink-0">
          <p className="font-semibold text-ink-900 text-sm">BS Diploma — University at Buffalo, June 2026</p>
          <div className="flex items-center gap-3">
            <a href="/Diploma.pdf" download className="inline-flex items-center gap-1.5 text-sm font-semibold text-ink-900 underline underline-offset-2 hover:no-underline">
              <Download size={15} /> Download PDF
            </a>
            <button onClick={onClose} className="text-ink-600 hover:text-ink-900 p-1" aria-label="Close">
              <X size={20} />
            </button>
          </div>
        </div>
        <iframe src="/Diploma.pdf" className="flex-1 w-full" title="BS Diploma — University at Buffalo" />
      </div>
    </div>
  );
};
```

**`Timeline.tsx`**: For the UB BS degree entry, add:
```tsx
const [diplomaOpen, setDiplomaOpen] = useState(false);
// …inside the UB BS edu block:
<button onClick={() => setDiplomaOpen(true)} className="…">View Diploma</button>
<DiplomaModal isOpen={diplomaOpen} onClose={() => setDiplomaOpen(false)} />
```

The trigger should be scoped to the UB BS entry only — detect by checking `edu.institution.includes('University at Buffalo')`.

---

## 9. Landing page — richer hero
**File:** `components/Hero.tsx`

In addition to the banner background (from #2), enhance the hero with a **research domain strip** below the Inference Foundry card, replacing the current small nav-link list. Replace/augment that `<nav>` with a grid of 3 domain cards:

| Domain | Headline | Detail |
|---|---|---|
| Healthcare AI | Geriatric oral screening · stroke rehab · orthodontic remote monitoring | OralScan, OrthoScan, mRehab |
| Materials ML | Symmetry-aware GNNs · equivariant MLIPs · universal atom models | Peng Lab |
| Spatiotemporal ML | PhD focus: DLWF · adversarial robustness | MSU Data Mining Lab |

Each card: small icon (from `lucide-react`: `Stethoscope`, `Atom`, `BrainCircuit` or similar), domain title, one-line description, link to `/research/`. Keep it compact — 3-column grid on wide, stack on mobile. This replaces the "More / About · Research · …" nav link strip.

Keep the portrait photo and social icons unchanged.

---

## Verification

1. `npm run dev` at localhost:3000
2. Favicon: check browser tab shows logo not portrait
3. Header: logo image visible instead of round portrait
4. Hero: subtle banner texture visible in background
5. Hero: 3 domain cards render cleanly; links go to `/research/`
6. Research page: accordion cards collapsed by default, expand on click, show duration in period
7. OralScan links: hover to confirm new URL (`oralscan.auspexmedix.com`)
8. Publications: 4 new entries appear with "Under submission" badge
9. Periods: mRehab shows "August 2026", mlip-uma shows "June 2026"; durations appear in parentheses
10. Education page: "View Diploma" button on UB BS row opens PDF modal; Download link works
