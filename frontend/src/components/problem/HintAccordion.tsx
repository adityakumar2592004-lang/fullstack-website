import React, { useState } from 'react';
import { HelpCircle, Eye, EyeOff, Sparkles } from 'lucide-react';

interface HintAccordionProps {
  hints: string[];
}

export const HintAccordion: React.FC<HintAccordionProps> = ({ hints }) => {
  const [revealedHints, setRevealedHints] = useState<number[]>([]);

  const toggleHint = (index: number) => {
    setRevealedHints((prev) =>
      prev.includes(index) ? prev.filter((i) => i !== index) : [...prev, index]
    );
  };

  const hintLabels = [
    'Hint 1: Initial Observation & Data Flow',
    'Hint 2: Algorithmic Direction & Memory Optimization',
    'Hint 3: Edge Cases & Optimal Strategy',
  ];

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2 pb-2 border-b border-slate-800">
        <Sparkles className="w-5 h-5 text-indigo-400" />
        <div>
          <h2 className="text-base font-bold text-white">Progressive Hints</h2>
          <p className="text-xs text-slate-400">
            Reveal hints one step at a time without spoiling the complete solution.
          </p>
        </div>
      </div>

      <div className="space-y-3">
        {hints.map((hint, idx) => {
          const isRevealed = revealedHints.includes(idx);
          const label = hintLabels[idx] || `Hint ${idx + 1}`;

          return (
            <div
              key={idx}
              className={`border rounded-xl transition-all duration-200 overflow-hidden ${
                isRevealed
                  ? 'bg-slate-900/80 border-indigo-500/40 shadow-sm'
                  : 'bg-slate-950/40 border-slate-800 hover:border-slate-700'
              }`}
            >
              <button
                onClick={() => toggleHint(idx)}
                className="w-full px-4 py-3.5 flex items-center justify-between text-left transition-colors"
              >
                <div className="flex items-center gap-3">
                  <div
                    className={`w-7 h-7 rounded-lg flex items-center justify-center font-bold text-xs ${
                      isRevealed
                        ? 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/30'
                        : 'bg-slate-800 text-slate-400'
                    }`}
                  >
                    {idx + 1}
                  </div>
                  <div>
                    <span className="text-sm font-semibold text-slate-200 block">
                      {label}
                    </span>
                    {!isRevealed && (
                      <span className="text-xs text-slate-500">Click to reveal clue</span>
                    )}
                  </div>
                </div>

                <div className="flex items-center gap-1.5 text-xs text-slate-400 font-medium px-2.5 py-1 rounded-md bg-slate-800/80">
                  {isRevealed ? (
                    <>
                      <EyeOff className="w-3.5 h-3.5 text-slate-400" /> Hide
                    </>
                  ) : (
                    <>
                      <Eye className="w-3.5 h-3.5 text-indigo-400" /> Reveal
                    </>
                  )}
                </div>
              </button>

              {isRevealed && (
                <div className="px-4 pb-4 pt-2 border-t border-slate-800/80 text-sm text-slate-300 leading-relaxed bg-slate-900/40">
                  <div className="flex items-start gap-2">
                    <HelpCircle className="w-4 h-4 text-indigo-400 shrink-0 mt-0.5" />
                    <p className="whitespace-pre-line">{hint}</p>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
