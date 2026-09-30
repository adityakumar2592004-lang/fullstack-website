import React from 'react';
import type { Problem, ProblemStatus } from '../types';
import { ProblemCard } from '../components/problem/ProblemCard';
import { Bookmark, BookOpen } from 'lucide-react';

interface BookmarksPageProps {
  problems: Problem[];
  bookmarked: string[];
  getStatus: (id: string) => ProblemStatus;
  onToggleBookmark: (id: string) => void;
  onSelectProblem: (id: string) => void;
  onNavigate: (page: string) => void;
}

export const BookmarksPage: React.FC<BookmarksPageProps> = ({
  problems,
  bookmarked,
  getStatus,
  onToggleBookmark,
  onSelectProblem,
  onNavigate,
}) => {
  const bookmarkedList = problems.filter((p) => bookmarked.includes(p.id));

  return (
    <div className="space-y-6 pb-12">
      {/* Header */}
      <div className="border-b border-slate-800 pb-5">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/20 text-amber-400 text-xs font-semibold uppercase tracking-wider mb-2">
          <Bookmark className="w-3.5 h-3.5" /> Saved Collection
        </div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">
          Bookmarked Problems
        </h1>
        <p className="text-sm text-slate-400 mt-1">
          Review concepts and tricky algorithms you flagged for subsequent interview revision.
        </p>
      </div>

      {bookmarkedList.length === 0 ? (
        <div className="p-12 text-center rounded-2xl bg-slate-900/40 border border-slate-800 space-y-4 max-w-lg mx-auto">
          <div className="w-12 h-12 rounded-2xl bg-amber-500/10 border border-amber-500/20 text-amber-400 flex items-center justify-center mx-auto">
            <Bookmark className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">No bookmarked problems yet</h3>
            <p className="text-xs text-slate-400 mt-1 leading-relaxed">
              When viewing any problem or browsing problem lists, click the bookmark icon to save it here for fast revision.
            </p>
          </div>
          <button
            onClick={() => onNavigate('problems')}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold text-white bg-blue-600 hover:bg-blue-500 transition-colors shadow-md"
          >
            <BookOpen className="w-4 h-4" /> Browse Problems
          </button>
        </div>
      ) : (
        <div className="space-y-4">
          <div className="flex items-center justify-between text-xs text-slate-400">
            <span>
              <strong className="text-slate-200">{bookmarkedList.length}</strong> problems bookmarked
            </span>
          </div>

          <div className="grid grid-cols-1 gap-3">
            {bookmarkedList.map((prob) => (
              <ProblemCard
                key={prob.id}
                problem={prob}
                status={getStatus(prob.id)}
                isBookmarked={true}
                onToggleBookmark={() => onToggleBookmark(prob.id)}
                onSelect={() => onSelectProblem(prob.id)}
              />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
