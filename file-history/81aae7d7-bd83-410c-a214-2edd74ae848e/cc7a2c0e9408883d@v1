import React from 'react';
import { Section } from './Section';
import { EDUCATION, PROFESSIONAL_EXPERIENCE } from '../constants';
import { GraduationCap, Briefcase } from 'lucide-react';

export const Timeline: React.FC = () => {
  return (
    <Section
      id="education"
      title="Education & experience"
      subtitle="Degrees, teaching and tutoring, and related roles."
      className="bg-ink-50"
    >
      <div className="grid lg:grid-cols-2 gap-14">
        <div>
          <h3 className="text-base font-semibold text-ink-900 mb-6 flex items-center gap-2 border-b border-ink-200 pb-3 font-sans">
            <GraduationCap className="text-ink-700 shrink-0" size={20} aria-hidden />
            Education
          </h3>
          <div className="space-y-8 relative border-l-2 border-ink-200 ml-2 pl-8 pb-2">
            {EDUCATION.map((edu, idx) => (
              <div key={idx} className="relative">
                <span className="absolute -left-[39px] top-1.5 w-3 h-3 rounded-full bg-white border-2 border-ink-900" aria-hidden />
                <h4 className="text-[17px] font-serif font-semibold text-ink-900">{edu.degree}</h4>
                <p className="text-ink-700 italic text-sm mb-1">{edu.institution}</p>
                <p className="text-sm text-ink-600 mb-3">
                  {edu.period} · {edu.location}
                </p>
                <ul className="space-y-1.5">
                  {edu.details.map((detail, i) => (
                    <li key={i} className="text-sm text-ink-800 bg-white p-2.5 rounded-sm border border-ink-100">
                      {detail}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>

        <div>
          <h3 className="text-base font-semibold text-ink-900 mb-6 flex items-center gap-2 border-b border-ink-200 pb-3 font-sans">
            <Briefcase className="text-ink-700 shrink-0" size={20} aria-hidden />
            Teaching &amp; other experience
          </h3>
          <div className="space-y-9 relative border-l-2 border-ink-200 ml-2 pl-8 pb-2">
            {PROFESSIONAL_EXPERIENCE.map((job, idx) => (
              <div key={idx} className="relative">
                <span
                  className="absolute -left-[39px] top-1.5 w-3 h-3 rounded-full bg-white border-2 border-ink-500"
                  aria-hidden
                />
                <h4 className="text-[17px] font-serif font-semibold text-ink-900">{job.role}</h4>
                <p className="text-ink-800 font-medium text-sm mb-1">{job.organization}</p>
                <p className="text-sm text-ink-600 mb-3">
                  {job.period} · {job.location}
                </p>
                <ul className="list-disc list-outside ml-4 space-y-1.5 marker:text-ink-400">
                  {job.description.map((desc, i) => (
                    <li key={i} className="text-sm text-ink-800 leading-relaxed">
                      {desc}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </div>
      </div>
    </Section>
  );
};
