import React from 'react';
import type { Problem, ProblemStatus } from '../../types';
import { Bookmark, CheckCircle2, Clock, Circle, ArrowRight } from 'lucide-react';

interface ProblemCardProps {
  problem: Problem;
  status: ProblemStatus;
  isBookmarked: boolean;
  onToggleBookmark: () => void;
  onSelect: () => void;
}

export const ProblemCard: React.FC<ProblemCardProps> = ({
  problem,
  status,
  isBookmarked,
  onToggleBookmark,
  onSelect,
}) => {
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

  const getStatusBadge = (st: ProblemStatus) => {
    switch (st) {
      case 'Solved':
        return (
          <span className="flex items-center gap-1.5 text-xs font-medium text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2.5 py-1 rounded-full">
            <CheckCircle2 className="w-3.5 h-3.5" /> Solved
          </span>
        );
      case 'Attempted':
        return (
          <span className="flex items-center gap-1.5 text-xs font-medium text-blue-400 bg-blue-500/10 border border-blue-500/20 px-2.5 py-1 rounded-full">
            <Clock className="w-3.5 h-3.5" /> Attempted
          </span>
        );
      default:
        return (
          <span className="flex items-center gap-1.5 text-xs font-medium text-slate-400 bg-slate-800/60 border border-slate-700/60 px-2.5 py-1 rounded-full">
            <Circle className="w-3.5 h-3.5" /> Not Started
          </span>
        );
    }
  };

  return (
    <div
      onClick={onSelect}
      className={`group relative bg-slate-900/60 hover:bg-slate-900 border rounded-2xl p-4 sm:p-5 transition-all duration-200 cursor-pointer shadow-sm hover:shadow-md ${
        status === 'Solved'
          ? 'border-emerald-500/30 bg-emerald-950/5'
          : status === 'Attempted'
          ? 'border-blue-500/30'
          : 'border-slate-800 hover:border-slate-700'
      }`}
    >
      <div className="flex items-start justify-between gap-3">
        {/* Left: Problem Info */}
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2.5 flex-wrap mb-1.5">
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
            <span className="text-xs text-slate-400 truncate max-w-[200px]">
              {problem.subtopic}
            </span>
          </div>

          <h3 className="text-base font-semibold text-slate-100 group-hover:text-blue-400 transition-colors truncate">
            {problem.title}
          </h3>

          <p className="text-xs text-slate-400 line-clamp-2 mt-1 mb-3">
            {problem.description}
          </p>

          {/* Tags */}
          <div className="flex items-center gap-1.5 flex-wrap">
            {problem.tags.slice(0, 3).map((tag, i) => (
              <span
                key={i}
                className="text-[11px] font-medium text-slate-400 bg-slate-950/70 border border-slate-800/80 px-2 py-0.5 rounded-md"
              >
                {tag}
              </span>
            ))}
            {problem.tags.length > 3 && (
              <span className="text-[11px] text-slate-500">
                +{problem.tags.length - 3} more
              </span>
            )}
          </div>
        </div>

        {/* Right: Actions and Status */}
        <div className="flex flex-col items-end justify-between self-stretch gap-4 shrink-0">
          <button
            onClick={(e) => {
              e.stopPropagation();
              onToggleBookmark();
            }}
            className={`p-2 rounded-lg border transition-all ${
              isBookmarked
                ? 'text-amber-400 bg-amber-500/10 border-amber-500/30'
                : 'text-slate-500 hover:text-amber-400 hover:bg-slate-800 border-transparent hover:border-slate-700'
            }`}
            title={isBookmarked ? 'Remove Bookmark' : 'Bookmark Problem'}
          >
            <Bookmark className={`w-4 h-4 ${isBookmarked ? 'fill-amber-400' : ''}`} />
          </button>

          <div className="flex items-center gap-3">
            {getStatusBadge(status)}
            <div className="w-8 h-8 rounded-lg bg-blue-600/10 group-hover:bg-blue-600 text-blue-400 group-hover:text-white flex items-center justify-center transition-colors">
              <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
