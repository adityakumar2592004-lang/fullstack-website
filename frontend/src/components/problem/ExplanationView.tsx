import React, { useState } from 'react';
import type { Explanation } from '../../types';
import {
  Lightbulb,
  Zap,
  CheckCircle,
  Clock,
  Database,
  AlertTriangle,
  HelpCircle,
  ChevronDown,
  ChevronUp,
  PlayCircle,
} from 'lucide-react';

interface ExplanationViewProps {
  explanation: Explanation;
}

export const ExplanationView: React.FC<ExplanationViewProps> = ({ explanation }) => {
  const [openSection, setOpenSection] = useState<string | null>('all');

  const toggleSection = (id: string) => {
    setOpenSection((prev) => (prev === id ? null : id));
  };

  const sections = [
    {
      id: 'intuition',
      title: '1. Intuition & Key Idea',
      icon: Lightbulb,
      color: 'text-amber-400 bg-amber-500/10 border-amber-500/20',
      content: explanation.intuition,
    },
    {
      id: 'brute_force',
      title: '2. Brute Force Approach',
      icon: Zap,
      color: 'text-slate-400 bg-slate-800 border-slate-700',
      content: explanation.brute_force,
    },
    ...(explanation.better_approach
      ? [
          {
            id: 'better_approach',
            title: '3. Better Approach',
            icon: PlayCircle,
            color: 'text-blue-400 bg-blue-500/10 border-blue-500/20',
            content: explanation.better_approach,
          },
        ]
      : []),
    {
      id: 'optimal_approach',
      title: explanation.better_approach ? '4. Optimal Approach' : '3. Optimal Approach',
      icon: CheckCircle,
      color: 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20',
      content: explanation.optimal_approach,
    },
    {
      id: 'dry_run',
      title: 'Step-by-step Dry Run',
      icon: PlayCircle,
      color: 'text-cyan-400 bg-cyan-500/10 border-cyan-500/20',
      content: explanation.dry_run,
      isCode: true,
    },
    {
      id: 'complexity',
      title: 'Complexity Analysis',
      icon: Clock,
      color: 'text-purple-400 bg-purple-500/10 border-purple-500/20',
      customRender: () => (
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div className="p-3 rounded-xl bg-slate-950/70 border border-slate-800">
            <div className="flex items-center gap-1.5 text-xs font-semibold text-slate-300 mb-1">
              <Clock className="w-3.5 h-3.5 text-blue-400" /> Time Complexity
            </div>
            <div className="text-xs font-mono text-blue-300">{explanation.time_complexity}</div>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/70 border border-slate-800">
            <div className="flex items-center gap-1.5 text-xs font-semibold text-slate-300 mb-1">
              <Database className="w-3.5 h-3.5 text-purple-400" /> Space Complexity
            </div>
            <div className="text-xs font-mono text-purple-300">{explanation.space_complexity}</div>
          </div>
        </div>
      ),
    },
    {
      id: 'common_mistakes',
      title: 'Common Pitfalls & Mistakes',
      icon: AlertTriangle,
      color: 'text-rose-400 bg-rose-500/10 border-rose-500/20',
      content: explanation.common_mistakes,
    },
    {
      id: 'interview_questions',
      title: 'Interview Follow-ups & Variations',
      icon: HelpCircle,
      color: 'text-indigo-400 bg-indigo-500/10 border-indigo-500/20',
      content: explanation.interview_questions,
    },
  ];

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between pb-2 border-b border-slate-800">
        <h2 className="text-base font-bold text-white flex items-center gap-2">
          <Lightbulb className="w-5 h-5 text-amber-400" /> Detailed Editorial & Approaches
        </h2>
        <button
          onClick={() => setOpenSection(openSection === 'all' ? null : 'all')}
          className="text-xs text-blue-400 hover:text-blue-300 transition-colors"
        >
          {openSection === 'all' ? 'Collapse All' : 'Expand All'}
        </button>
      </div>

      <div className="space-y-3">
        {sections.map((sec) => {
          const Icon = sec.icon;
          const isOpen = openSection === 'all' || openSection === sec.id;

          return (
            <div
              key={sec.id}
              className="border border-slate-800 rounded-xl bg-slate-900/50 overflow-hidden transition-colors"
            >
              <button
                onClick={() => toggleSection(sec.id)}
                className="w-full px-4 py-3 flex items-center justify-between text-left hover:bg-slate-800/40 transition-colors"
              >
                <div className="flex items-center gap-2.5">
                  <div className={`p-1.5 rounded-lg border ${sec.color}`}>
                    <Icon className="w-4 h-4" />
                  </div>
                  <span className="text-sm font-semibold text-slate-200">{sec.title}</span>
                </div>
                {isOpen ? (
                  <ChevronUp className="w-4 h-4 text-slate-400" />
                ) : (
                  <ChevronDown className="w-4 h-4 text-slate-400" />
                )}
              </button>

              {isOpen && (
                <div className="px-4 pb-4 pt-1 border-t border-slate-800/60 text-xs sm:text-sm text-slate-300 leading-relaxed">
                  {sec.customRender ? (
                    sec.customRender()
                  ) : sec.isCode ? (
                    <pre className="font-mono text-xs bg-slate-950 p-3 rounded-lg border border-slate-800 text-slate-300 overflow-x-auto whitespace-pre-wrap">
                      {sec.content}
                    </pre>
                  ) : (
                    <p className="whitespace-pre-line">{sec.content}</p>
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
