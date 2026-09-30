import React from 'react';
import type { Problem } from '../../types';
import { HelpCircle, AlertCircle, FileCode2 } from 'lucide-react';

interface ProblemDescriptionProps {
  problem: Problem;
}

export const ProblemDescription: React.FC<ProblemDescriptionProps> = ({ problem }) => {
  const getDifficultyBadge = (diff: string) => {
    switch (diff) {
      case 'Easy':
        return 'text-emerald-400 bg-emerald-500/10 border-emerald-500/30';
      case 'Medium':
        return 'text-amber-400 bg-amber-500/10 border-amber-500/30';
      case 'Hard':
        return 'text-rose-400 bg-rose-500/10 border-rose-500/30';
      default:
        return 'text-slate-400 bg-slate-800 border-slate-700';
    }
  };

  return (
    <div className="space-y-6 text-slate-200">
      {/* Title & Metadata Header */}
      <div>
        <div className="flex items-center gap-2.5 flex-wrap mb-2">
          <span className="font-mono text-xs font-bold text-slate-400 px-2 py-0.5 rounded-md bg-slate-800 border border-slate-700">
            #{problem.order.toString().padStart(2, '0')}
          </span>
          <span
            className={`text-xs font-semibold px-2.5 py-0.5 rounded-full border ${getDifficultyBadge(
              problem.difficulty
            )}`}
          >
            {problem.difficulty}
          </span>
          <span className="text-xs text-blue-400 bg-blue-500/10 px-2.5 py-0.5 rounded-full border border-blue-500/20 font-medium">
            {problem.subtopic}
          </span>
        </div>
        <h1 className="text-2xl font-bold tracking-tight text-white">{problem.title}</h1>
      </div>

      {/* Problem Statement */}
      <div className="prose prose-invert prose-slate max-w-none text-sm leading-relaxed space-y-3">
        <p className="whitespace-pre-line text-slate-300">{problem.description}</p>
      </div>

      {/* Input / Output Formats */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        <div className="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800">
          <div className="font-semibold text-slate-300 flex items-center gap-1.5 mb-1">
            <FileCode2 className="w-3.5 h-3.5 text-blue-400" /> Input Format
          </div>
          <div className="text-slate-400 font-mono">{problem.input_format}</div>
        </div>
        <div className="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800">
          <div className="font-semibold text-slate-300 flex items-center gap-1.5 mb-1">
            <FileCode2 className="w-3.5 h-3.5 text-emerald-400" /> Output Format
          </div>
          <div className="text-slate-400 font-mono">{problem.output_format}</div>
        </div>
      </div>

      {/* Examples */}
      <div className="space-y-4">
        <h3 className="text-sm font-semibold text-slate-200 uppercase tracking-wider">
          Examples
        </h3>
        <div className="space-y-3">
          {problem.examples?.map((ex, idx) => (
            <div
              key={idx}
              className="rounded-xl bg-slate-950/80 border border-slate-800 p-4 space-y-2 text-xs"
            >
              <div className="font-semibold text-slate-400 flex items-center gap-1.5">
                <span>Example {idx + 1}:</span>
              </div>
              <div className="space-y-1 font-mono">
                <div>
                  <span className="text-slate-400">Input: </span>
                  <span className="text-blue-300">{ex.input}</span>
                </div>
                <div>
                  <span className="text-slate-400">Output: </span>
                  <span className="text-emerald-300">{ex.output}</span>
                </div>
              </div>
              {ex.explanation && (
                <div className="text-slate-400 pt-1 border-t border-slate-800/80 flex items-start gap-1.5">
                  <HelpCircle className="w-3.5 h-3.5 text-amber-400 shrink-0 mt-0.5" />
                  <span>
                    <strong className="text-slate-300 font-medium">Explanation: </strong>
                    {ex.explanation}
                  </span>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Constraints */}
      <div className="space-y-2">
        <h3 className="text-sm font-semibold text-slate-200 uppercase tracking-wider flex items-center gap-1.5">
          <AlertCircle className="w-4 h-4 text-amber-400" /> Constraints
        </h3>
        <ul className="list-disc list-inside space-y-1 text-xs font-mono text-slate-400 bg-slate-950/40 p-3 rounded-xl border border-slate-800">
          {problem.constraints?.map((c, idx) => (
            <li key={idx} className="text-slate-300">
              {c}
            </li>
          ))}
        </ul>
      </div>

      {/* Tags */}
      <div className="pt-2">
        <h4 className="text-xs font-medium text-slate-400 mb-2">Topic Tags:</h4>
        <div className="flex items-center gap-2 flex-wrap">
          {problem.tags?.map((tag, idx) => (
            <span
              key={idx}
              className="text-xs font-medium text-slate-300 bg-slate-800 border border-slate-700 px-2.5 py-1 rounded-lg"
            >
              {tag}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
};
