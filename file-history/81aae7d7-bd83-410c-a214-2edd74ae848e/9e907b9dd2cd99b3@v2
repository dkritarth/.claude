import React from 'react';
import { X, Download } from 'lucide-react';

type DiplomaModalProps = { isOpen: boolean; onClose: () => void };

export const DiplomaModal: React.FC<DiplomaModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;
  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-ink-900/80 backdrop-blur-sm"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-3xl bg-white rounded-sm shadow-xl flex flex-col"
        style={{ height: '80vh' }}
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center justify-between px-5 py-3 border-b border-ink-200 shrink-0">
          <p className="font-semibold text-ink-900 text-sm">
            BS Diploma — University at Buffalo, June 2026
          </p>
          <div className="flex items-center gap-4">
            <a
              href="/Diploma.pdf"
              download
              className="inline-flex items-center gap-1.5 text-sm font-semibold text-ink-900 underline underline-offset-2 hover:no-underline"
            >
              <Download size={15} aria-hidden />
              Download PDF
            </a>
            <button
              type="button"
              onClick={onClose}
              className="text-ink-600 hover:text-ink-900 p-1 transition-colors"
              aria-label="Close diploma viewer"
            >
              <X size={20} />
            </button>
          </div>
        </div>
        <iframe
          src="/Diploma.pdf"
          className="flex-1 w-full"
          title="BS Diploma — University at Buffalo"
        />
      </div>
    </div>
  );
};
