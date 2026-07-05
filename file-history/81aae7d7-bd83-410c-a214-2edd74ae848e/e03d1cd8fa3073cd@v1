import type { ReactNode } from 'react';
import { Code, GraduationCap, Microscope, Newspaper, Users } from 'lucide-react';
import type {
  NewsItem,
  CompetitionEntry,
  Education,
  Experience,
  Project,
  Publication,
  ResearchPlacement,
  SitePage,
  SkillCategory,
} from './types';
import { NEWS_ITEMS } from './newsItems';
import { PENG_CREDLY_MLIP_UMA, PENG_CREDLY_PEROVSKITE_GNN } from './pengCredly';

/** PDF downloads in public/data/. Resume is the one-page shortened version of the full CV. */
export const DOCUMENT_URLS = {
  cv: '/data/CV%20-%20Kritarth%20Dandapat.pdf',
  resume: '/data/Resume%20-%20Kritarth%20Dandapat.pdf',
} as const;

export const CONTACT_INFO = {
  name: 'Kritarth Dandapat',
  title: 'Incoming PhD Student, Michigan State University · Undergraduate Researcher, University at Buffalo',
  email: 'contact@dkritarth.com',
  phone: '+1 (716) 612-0016',
  location: 'Buffalo, NY',
  github: 'https://github.com/Kritarth-Dandapat',
  linkedin: 'https://www.linkedin.com/in/kritarth-dandapat/',
  instagram: 'https://www.instagram.com/kritarth_dandapat/',
  twitter: 'https://x.com/Kritarth25',
  website: 'https://dkritarth.com',
  bio: 'Computer science researcher at the intersection of research and engineering—mobile health AI, computer vision, and computational materials science. Incoming PhD (Fall 2026) at MSU CSE, Data Mining Laboratory (Dr. Pang-Ning Tan).',
  /** Mirrors cv.tex Professional Summary (paragraphs) */
  professionalSummary: [
    'I am a computer science researcher who genuinely enjoys building things that matter—whether that is a mobile app that helps elderly patients get oral health screenings, a system that tracks orthodontic progress remotely, or models that help scientists discover new materials faster.',
    'I am completing an accelerated three-year BS in Computer Science (Minor: Statistics) at the University at Buffalo with a 3.8+ GPA, and I am starting my PhD at Michigan State University in Fall 2026, joining the Data Mining Laboratory under Dr. Pang-Ning Tan. My doctoral research will focus on spatiotemporal machine learning, deep learning-based weather forecasting, and AI adversarial robustness.',
    'What sets me apart is that I sit at the intersection of research and engineering. I have co-authored papers in digital health and computational materials science, while simultaneously shipping production mobile apps, deploying cloud infrastructure on AWS, and implementing advanced ML models like equivariant graph neural networks. I move quickly from idea to working system.',
    'I have been recognized with the PEARL undergraduate research award ($2,500) and placed second at the UB Health Futures Challenge ($1,000).',
  ],
  /** Short intro for the home page */
  landingLead:
    'I build research systems that ship—geriatric oral screening, orthodontic remote monitoring, telerehabilitation on AWS, and symmetry-aware GNNs for materials discovery. Incoming PhD student (Fall 2026) in MSU CSE\'s Data Mining Laboratory (Dr. Pang-Ning Tan), with planned work in spatiotemporal ML, DLWF, and AI adversarial robustness.',
  sopSnippet:
    'My academic journey has been driven by a fascination with the power of artificial intelligence (AI) to solve tangible, human-centric problems. I am driven to move beyond applying known techniques to creating original, high-impact research.',
  /** Open research software initiative — surfaced on home & About */
  inferenceFoundry: {
    url: 'https://inference-foundry.rweb.site/',
    startLabel: 'Starting May 2026',
    description:
      'Collaborative open-source initiative building reproducible ML inference tooling, standardized research software scaffolding, and shared contributor infrastructure for the scientific ML community.',
  },
};

export const EDUCATION: Education[] = [
  {
    degree: 'PhD in Computer Science',
    institution: 'Michigan State University',
    location: 'East Lansing, MI',
    period: 'Starting Fall 2026',
    details: [
      'Department of Computer Science and Engineering; Data Mining Laboratory (Advisor: Dr. Pang-Ning Tan)',
      'Planned research focus: spatiotemporal machine learning, deep learning-based weather forecasting (DLWF), and AI adversarial robustness',
    ],
  },
  {
    degree: 'Bachelor of Science in Computer Science (Minor in Statistics)',
    institution: 'University at Buffalo, SUNY',
    location: 'Buffalo, NY',
    period: 'August 2023 – June 2026',
    details: [
      'Specialization in artificial intelligence; coursework spanning reinforcement learning, computer vision, machine learning, quantum computing, and distributed systems',
      "GPA 3.8+; Dean's List all semesters; accelerated three-year completion (21–22 credit semesters)",
      'Presidential Scholarship: $15,000 per year; PEARL Award: $2,500 competitive undergraduate research grant (Experiential Learning Network)',
    ],
  },
];

export const RESEARCH_PLACEMENTS: ResearchPlacement[] = [
  {
    role: 'Research Assistant',
    organization: 'Embedded Sensing and Computing (ESC) Group, University at Buffalo',
    location: 'Buffalo, NY',
    overview: 'Mobile sensing for healthcare and rehabilitation with Prof. Wenyao Xu.',
    subprojects: [
      {
        id: 'oralscan',
        name: 'OralScan: AI-Assisted Geriatric Oral Screening',
        period: 'June 2024 – February 2025',
        context: 'PI: Prof. Wenyao Xu',
        narrative: [
          'OralScan is an AI-assisted mobile health platform for guided intraoral imaging and rapid feedback—designed to complement in-office geriatric oral care.',
        ],
        technicalHighlights: [
          'Architected a full-stack mobile health platform (React Native, React web) integrating end-to-end YOLOv8 vision pipelines for guided intraoral image acquisition, multi-class dental disease screening, and automated tooth numbering across temporal scan sessions.',
          'Formulated a spatio-temporal scan-guidance system that aggregates sequential intraoral frames to produce consistent disease-detection signals robust to user-induced motion variability.',
          'Co-authored formative usability and acceptability study submitted to Smart Health (under review); delivered oral presentations to clinical stakeholders at CTSI and SURC (January 2025).',
          'Awarded second place ($1,000), University at Buffalo Health Futures Challenge (Spring 2026).',
        ],
        links: [
          { label: 'OralScan website', href: 'https://esc-group-ub.github.io/OralScan-Website/' },
          {
            label: 'Health Futures — UB announcement',
            href: 'https://www.buffalo.edu/entrepreneurship/connect/news.host.html/content/shared/www/studentlife/gateway-wide-content/announcements/current/health-futures-25.detail.html',
          },
          {
            label: 'Health Futures Challenge (StartupTree)',
            href: 'https://ubuffalo.startuptree.co/event/s/4rCVkj4dBLVMbA6SWkwitZ/Health-Futures-Challenge---SP2025?utm_source=sfmc&utm_medium=email&utm_campaign=&utm_content=',
          },
        ],
        technologies: ['YOLOv8', 'React Native', 'React', 'Computer vision', 'Mobile health'],
      },
      {
        id: 'orthoscan',
        name: 'OrthoScan',
        period: 'February 2025 – October 2025',
        context: 'PI: Prof. Wenyao Xu',
        narrative: [
          'OrthoScan enables at-home orthodontic progress tracking with intelligent imaging and measurement algorithms that translate visual change into calibrated, actionable feedback.',
        ],
        technicalHighlights: [
          'Engineered mobile and backend systems for at-home orthodontic progress tracking, deploying YOLO-based hardware detection paired with depth-assisted spatial measurement pipelines to quantify structural change across longitudinal patient visits.',
          'Reconstructed and analyzed 3D dental structures from intraoral scans using pre-trained GNNs for 3D mesh processing; computed quantitative tooth position changes in both 2D image space and 3D world coordinates to track orthodontic progress with geometric precision.',
          'Translated sequential intraoral imagery into calibrated geometric progress signals, enabling quantitative remote monitoring between in-office appointments and reducing reliance on subjective clinician assessment.',
        ],
        technologies: ['YOLO', 'GNNs', 'React Native', '3D mesh processing', 'Depth sensing', 'Computer vision'],
        collaboratorsNote:
          'Collaborators included Dr. Wei Bo, Prof. Wenyao Xu, Alexander Gherardi, and Puru Soni (see https://purusoni.com).',
      },
      {
        id: 'mrehab',
        name: 'mRehab',
        period: 'November 2025 – Present',
        context: 'ESC Lab · telerehabilitation',
        narrative: [
          'mRehab is a telerehabilitation platform supporting structured exercise programs, sensor-informed feedback, and therapist-facing analytics in live outpatient workflows.',
        ],
        technicalHighlights: [
          'Provisioned and configured AWS backend infrastructure to host testing and staging environments, enabling AI agent capabilities to operate within the live application stack.',
          'Deployed a real-time live sensor logging site for continuous ingest and monitoring of wearable sensor streams during active therapy sessions.',
          'Implemented Kalman filters for sensor fusion and activity detection, improving signal smoothness and robustness of exercise recognition under noisy real-world IMU conditions.',
          'Contributed to session logging, multi-modal sensor ingest pipelines, and exercise scoring algorithms deployed in live outpatient therapy workflows.',
        ],
        links: [{ label: 'mrehab.agency', href: 'https://mrehab.agency/' }],
        technologies: ['AWS', 'Kalman filters', 'Signal processing', 'Backend', 'Mobile', 'Algorithms'],
      },
    ],
  },
  {
    role: 'Undergraduate Researcher',
    organization: 'Peng Research Lab, University at Buffalo',
    location: 'Buffalo, NY',
    overview: 'Computational materials science and clean-energy applications with Prof. Jiayu Peng.',
    placementLinks: [
      {
        label: 'UB ELN — AI design of disordered materials for clean energy (project profile)',
        href: 'https://www.buffalo.edu/eln/students/project-portal/host-page.host.html/content/shared/www/eln/project-portal/project-profiles/active-projects/ai-design-of-disordered-materials-for-clean-energy-and-sustainable-applications.detail.html',
      },
    ],
    subprojects: [
      {
        id: 'perovskite-gnn',
        name: 'Perovskite ordering and symmetry-aware GNNs',
        period: 'June 2025 – November 2025',
        context: 'Prof. Jiayu Peng · repository open-sourced with ordering paper',
        narrative: [
          'Benchmarking symmetry-aware graph neural networks for ordering-dependent energetics in crystalline perovskites, with reproducible training on atomistic datasets.',
        ],
        technicalHighlights: [
          'Benchmarked symmetry-aware GNN architectures (including ALIGNN) on ordering-dependent energetics in crystalline perovskites; contributed benchmarking results and revised analysis to arXiv:2409.13851 and the open-source PerovskiteOrderingGCNNs repository.',
          'Migrated experiment tracking infrastructure from SigOpt to Weights & Biases; automated training loops, hyperparameter sweeps, and multi-architecture evaluation pipelines, reducing manual overhead and improving reproducibility.',
          'Co-authored commentary on agentic AI for multimetallic catalyst discovery, published on ChemRxiv (2025).',
        ],
        links: [
          {
            label: 'GitHub: PerovskiteOrderingGCNNs',
            href: 'https://github.com/jiayu-peng-lab/PerovskiteOrderingGCNNs',
          },
          { label: 'arXiv:2409.13851', href: 'https://arxiv.org/abs/2409.13851' },
        ],
        credlyBadge: PENG_CREDLY_PEROVSKITE_GNN,
        technologies: ['PyTorch', 'GNNs', 'ALIGNN', 'Weights & Biases', 'Materials ML'],
      },
      {
        id: 'mlip-uma-alchemical',
        name: 'Equivariant MLIPs, alchemical extensions, and universal atom models',
        period: 'December 2025 – Present',
        context: 'Prof. Jiayu Peng · E(3) message-passing potentials, MACE-style alchemical graphs, universal atom models',
        narrative: [
          'Implementing E(3)-equivariant machine learning interatomic potentials with alchemical graph extensions and integrating them with universal atom model (UMA) stacks for materials discovery pipelines.',
        ],
        technicalHighlights: [
          'Implement E(3)-equivariant message-passing machine learning interatomic potentials (MLIPs) augmented with alchemical graph extensions to enable efficient composition sweeps and energy prediction over disordered crystalline structures.',
          'Integrate alchemical treatment with universal atom model (UMA) stacks (MACE) to accelerate structural relaxation and disorder characterization workflows in computational materials discovery pipelines.',
        ],
        links: [
          { label: 'arXiv:2404.10746 (MLIP alchemical framework)', href: 'https://arxiv.org/abs/2404.10746' },
          { label: 'arXiv:2506.23971 (UMA)', href: 'https://arxiv.org/abs/2506.23971' },
        ],
        credlyBadge: PENG_CREDLY_MLIP_UMA,
        technologies: ['MACE', 'UMA', 'E(3)-equivariant MLIPs', 'PyTorch', 'MLIPs', 'Materials simulation'],
      },
    ],
  },
  {
    role: 'Founder, Inference Foundry',
    organization: 'Open Research Software Initiative',
    location: 'Remote',
    overview: 'Collaborative open-source initiative for reproducible scientific ML tooling.',
    subprojects: [
      {
        id: 'inference-foundry',
        name: 'Inference Foundry',
        period: 'Starting May 2026',
        narrative: [
          'Building shared infrastructure for reproducible ML inference, standardized research software scaffolding, and contributor-friendly open-source workflows.',
        ],
        technicalHighlights: [
          'Launched a collaborative open-source initiative building reproducible ML inference tooling, standardized research software scaffolding, and shared contributor infrastructure for the scientific ML community.',
        ],
        links: [{ label: 'inference-foundry.rweb.site', href: 'https://inference-foundry.rweb.site/' }],
        technologies: ['Open source', 'ML inference', 'Research software', 'Reproducible workflows'],
      },
    ],
  },
];

export const PROFESSIONAL_EXPERIENCE: Experience[] = [
  {
    role: 'Teaching Assistant, CSE 341: Computer Architecture',
    organization: 'Department of Computer Science and Engineering, University at Buffalo',
    location: 'Buffalo, NY',
    period: 'January 2026 – May 2026',
    description: [
      'Conducted weekly tutorial sessions on Assembly and VHDL for 30+ students, live-coding solutions to architecture problems including cache design, memory hierarchies, and instruction pipelining.',
      'Led recitations walking through processor pipeline stages, hazard detection, and cache replacement policies; developed worked examples and problem sets to reinforce lecture material.',
      'Held weekly office hours; graded exams and assignments; supported 100+ students asynchronously on Piazza throughout the semester.',
    ],
  },
  {
    role: 'Tutor and Peer-Assisted Leader (PAL)',
    organization: 'Tutoring and Academic Support Services (TASS), University at Buffalo',
    location: 'Buffalo, NY',
    period: 'August 2024 – December 2025',
    description: [
      'Served as PAL for STA 119 (Introduction to Statistics): designed weekly worksheets aligned to recent lectures, then led two 50-minute collaborative sessions per week; course feedback indicated approximately 30% improvement in quiz performance.',
      'Provided one-to-one 1-hour tutoring appointments across seven courses: STA 119, CSE 115, CSE 116, CSE 220, MTH 141, MTH 142—covering introductory programming, data structures, and calculus.',
    ],
  },
  {
    role: 'Founder and Vice President',
    organization: 'UB National Student Data Corps',
    location: 'Buffalo, NY',
    period: 'October 2023 – May 2024',
    description: [
      'Co-founded the UB chapter; launched the chapter website, organized data science workshops, and built networking programs connecting undergraduates to research and industry opportunities.',
    ],
  },
];

export const PUBLICATIONS: Publication[] = [
  {
    title:
      'OralScan, an AI-Powered Mobile Tool for Geriatric Oral Healthcare: A Formative Usability and Acceptability Study',
    authors: 'Soni, P., Dandapat, K., Gherardi, A., Bo, W., Li, R., and Xu, W.',
    venue: 'Submitted to Smart Health',
    year: '2025',
    status: 'Under review',
  },
  {
    title: 'Accelerating Multimetallic Catalyst Discovery with Robotics and Agentic AI',
    authors: 'Peng, J., Liu, C., Luo, Y., and Dandapat, K.',
    venue: 'ChemRxiv, ver. 1. DOI: 10.26434/chemrxiv-2025-13n3f',
    year: '2025',
    link: 'https://doi.org/10.26434/chemrxiv-2025-13n3f',
  },
  {
    title: 'Learning Ordering in Crystalline Materials with Symmetry-Aware Graph Neural Networks',
    authors: 'Peng, J., et al.',
    venue: 'arXiv Preprint, arXiv:2409.13851',
    year: '2024',
    link: 'https://arxiv.org/abs/2409.13851',
    status: 'Contributed benchmarking and revisions',
  },
];

/** Selected projects (OralScan and lab work live under Research). Aligned with cv.tex. */
export const PROJECTS: Project[] = [
  {
    slug: 'paddock-psych-rl',
    title: 'PaddockPsychRL: F1-Informed Multi-Agent Reinforcement Learning',
    category: 'Spatiotemporal Modeling and Multi-Agent Systems',
    description: [
      'Formulated a multi-agent RL framework integrating Formula 1 temporal performance signals into agent psychology models within PettingZoo cooperative environments, mapping real-world behavioral dynamics to learned policy structure.',
      'Constructed driver-specific agent profiles from FastF1 2025 lap-time consistency metrics, encoding temporal performance variability as per-agent action-noise scales to reflect authentic decision-making under pressure.',
      'Benchmarked tabular Q-learning and MAPPO baselines against psych-conditioned policies; psych-aware agents improved Strategy Resilience Score from 0.54 to 0.63 (+16.7%) under noisy multi-agent coordination.',
    ],
    technologies: ['Python', 'FastF1', 'PettingZoo', 'Ray RLlib', 'MAPPO', 'Q-learning'],
    stats: 'Strategy Resilience Score 0.63 vs 0.54 (+16.7%)',
    links: [
      { label: 'Project write-up', href: 'https://dkritarth.com/PaddockPsychRL/' },
      { label: 'GitHub', href: 'https://github.com/Kritarth-Dandapat/PaddockPsychRL' },
    ],
  },
  {
    slug: 'marine-guardian',
    title: 'Marine Guardian: Ship Detection in Satellite Imagery',
    category: 'Geospatial Computer Vision and Deep Learning',
    description: [
      'Designed a maritime monitoring pipeline grounded in geometric computer vision principles before applying deep models, achieving low-latency inference on high-resolution satellite imagery for spatial object detection.',
      'Engineered a roundness-based geometric classifier paired with MobileNetV2, attaining 98.72% ship-vs-non-ship classification accuracy while eliminating heavy encoder overhead unsuitable for edge deployment.',
      'Benchmarked EfficientNet transfer learning with a custom decoder against ResNet-50 feature extraction and K-means clustering, systematically validating architecture decisions across spatial generalization scenarios.',
    ],
    technologies: ['Python', 'OpenCV', 'TensorFlow', 'EfficientNet', 'MobileNetV2', 'ResNet-50', 'K-means'],
    stats: '98.72% accuracy',
  },
  {
    slug: 'people-counting-csrnet',
    title: 'People Counting via CSRNet Density Estimation',
    category: 'Deep Learning and Spatial Regression',
    description: [
      'Developed a density-estimation pipeline for crowd counting in highly occluded surveillance scenes where bounding-box detectors fail due to extreme pedestrian overlap, framing the task as spatial regression over density maps.',
      'Trained CSRNet end-to-end in PyTorch to predict per-pixel crowd density fields, enabling robust aggregate counts from integrated spatial density rather than fragile per-instance localization.',
      'Accelerated training and inference with CUDA; preprocessed surveillance-style frames with OpenCV for repeatable benchmarking across public crowd-counting datasets.',
    ],
    technologies: ['PyTorch', 'CSRNet', 'CUDA', 'OpenCV'],
  },
  {
    slug: 'human-emotion-detection',
    title: 'Human Emotion Detection: Multi-Architecture Benchmark',
    category: 'Computer Vision and Model Robustness',
    description: [
      'Constructed a controlled multi-architecture benchmark comparing shallow CNN, ResNet-34, and Vision Transformer (ViT) backbones on facial expression recognition under a unified preprocessing and evaluation protocol, isolating architectural contribution from data effects.',
      'Optimized training schedules and augmentation strategies per architecture; ViT and ResNet-34 variants demonstrated superior generalization over the CNN baseline on held-out facial expression data.',
      'Achieved 87.5% top-1 classification accuracy on the best-performing configuration after systematic cross-architecture ablation.',
    ],
    technologies: ['PyTorch', 'TensorFlow', 'CNN', 'ResNet-34', 'Vision Transformer', 'OpenCV'],
    stats: '87.5% top-1 accuracy',
  },
];

export const SKILLS: SkillCategory[] = [
  {
    category: 'Languages',
    skills: ['Python', 'JavaScript', 'Java', 'C++', 'Rust'],
  },
  {
    category: 'Machine learning and AI',
    skills: [
      'PyTorch',
      'TensorFlow',
      'Computer vision',
      'Deep learning',
      'Graph neural networks (GNNs)',
      'YOLOv8',
      'Vision Transformer (ViT)',
      'Reinforcement learning (MAPPO, Q-learning)',
      'Ray RLlib',
    ],
  },
  {
    category: 'Scientific ML and materials',
    skills: [
      'ALIGNN',
      'Machine learning interatomic potentials (MLIPs)',
      'MACE',
      'E(3)-equivariant MPNNs',
      'Weights and Biases',
      'PyTorch Geometric',
    ],
  },
  {
    category: 'Software engineering',
    skills: ['React', 'React Native', 'Node.js', 'Django', 'Git', 'CUDA', 'OpenCV', 'NumPy', 'Matplotlib'],
  },
  {
    category: 'Databases and cloud',
    skills: ['MongoDB', 'SQL', 'Firebase', 'SQLite', 'AWS', 'Google Colab', 'Firebase Hosting'],
  },
];

export const CERTIFICATIONS = [
  'Machine Learning Specialization — Stanford University and DeepLearning.AI (Coursera)',
  'Deep Learning Specialization — Stanford University and DeepLearning.AI (Coursera)',
  'PyTorch for Deep Learning — Udemy',
  'Additional professional coursework: deep learning (TensorFlow), Django, React, Node.js, Python (Udemy)',
];

export const AWARDS = [
  'PEARL Award — $2,500 competitive undergraduate research grant, University at Buffalo Experiential Learning Network (November 2025)',
  'Health Futures Challenge — Second place ($1,000) for OralScan, University at Buffalo (Spring 2026)',
  'Cybersecurity Excellence — Top 100 globally, Northeastern Cybersecurity C2C Finals; 10th in world finals (2025)',
  'Collegiate Lockdown — Top two teams representing UB; 4th in finals (2025)',
  "Dean's List — University at Buffalo (Fall 2023, Spring 2024, Fall 2024)",
  'Presidential Scholarship — $15,000 per year',
];

export const COMPETITIONS: CompetitionEntry[] = [
  {
    name: 'IAA AppXcelerate Application',
    host: 'University at Buffalo',
    date: 'January–March 2025',
    role: 'OralScan',
  },
  {
    name: 'Russell L. Agrusa CSE Student Innovation Competition',
    host: 'University at Buffalo',
    date: 'November 2024',
    role: 'Team member, OralScan',
  },
  {
    name: 'Aging Innovations Challenge',
    host: 'University at Buffalo',
    date: 'November 2024',
    role: 'Team member, OralScan',
  },
  {
    name: 'Community Champions for Disability Health Challenge',
    host: 'University at Buffalo',
    date: 'October 2024',
    role: 'OralScan',
  },
];

export const PRESENTATIONS = [
  {
    event: 'CTSI Research Group of Doctors, Nurses, and Medical Students',
    type: 'Oral presentation and live demo',
    date: 'January 2025',
  },
  {
    event: 'SUNY Undergraduate Research Conference (SURC)',
    type: 'Oral presentation',
    date: 'January 2025',
  },
];

export const RESEARCH_INTERESTS: string[] = [
  'Spatiotemporal machine learning and deep learning-based weather forecasting (DLWF)',
  'AI adversarial robustness and out-of-distribution generalization',
  'Geometric and equivariant deep learning; graph neural networks for structured data',
  'Computer vision and sequence modeling for healthcare and scientific applications',
  'Machine learning for materials science and scientific discovery',
];

const MONTH_LABELS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] as const;

export function formatNewsMonth(month: number): string {
  return MONTH_LABELS[Math.max(1, Math.min(12, month)) - 1] ?? '—';
}

/** News items grouped by year, descending; months descending within each year. */
export function getNewsByYear(): { year: number; items: NewsItem[] }[] {
  const byYear = new Map<number, NewsItem[]>();
  for (const item of NEWS_ITEMS) {
    const list = byYear.get(item.year) ?? [];
    list.push(item);
    byYear.set(item.year, list);
  }
  return [...byYear.entries()]
    .sort(([a], [b]) => b - a)
    .map(([year, items]) => ({
      year,
      items: items.sort((a, b) => b.month - a.month || a.id.localeCompare(b.id)),
    }));
}

export type NavLinkItem = {
  label: string;
  href: string;
  page: Exclude<SitePage, 'home'>;
  icon: ReactNode;
};

export const NAV_LINKS: NavLinkItem[] = [
  { label: 'About', href: '/about/', page: 'about', icon: <Users size={18} /> },
  { label: 'Research', href: '/research/', page: 'research', icon: <Microscope size={18} /> },
  { label: 'Projects', href: '/projects/', page: 'projects', icon: <Code size={18} /> },
  { label: 'Education', href: '/education/', page: 'education', icon: <GraduationCap size={18} /> },
  { label: 'News', href: '/news/', page: 'news', icon: <Newspaper size={18} /> },
];
