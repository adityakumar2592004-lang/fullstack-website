import React, { useState } from 'react';
import type { Problem, ProblemStatus } from '../types';
import { ProblemCard } from '../components/problem/ProblemCard';
import {
  Repeat,
  Sparkles,
  Bookmark,
  CheckCircle2,
  Clock,
  Play,
  RotateCcw,
  BookOpen,
} from 'lucide-react';

interface RevisionPageProps {
  problems: Problem[];
  solved: string[];
  attempted: string[];
  bookmarked: string[];
  getStatus: (id: string) => ProblemStatus;
  onToggleBookmark: (id: string) => void;
  onSelectProblem: (id: string) => void;
  onNavigate: (page: string) => void;
}

export const RevisionPage: React.FC<RevisionPageProps> = ({
  problems,
  solved,
  attempted,
  bookmarked,
  getStatus,
  onToggleBookmark,
  onSelectProblem,
  onNavigate,
}) => {
  const [activeTab, setActiveTab] = useState<'all' | 'bookmarked' | 'attempted' | 'solved'>('all');

  // Compute revision sets
  const bookmarkedProblems = problems.filter((p) => bookmarked.includes(p.id));
  const attemptedProblems = problems.filter((p) => attempted.includes(p.id) && !solved.includes(p.id));
  const solvedProblems = problems.filter((p) => solved.includes(p.id));

  // Combined queue for revision: bookmarked + attempted + recently solved (deduplicated)
  const revisionQueueMap = new Map<string, Problem>();
  bookmarkedProblems.forEach((p) => revisionQueueMap.set(p.id, p));
  attemptedProblems.forEach((p) => revisionQueueMap.set(p.id, p));
  solvedProblems.forEach((p) => revisionQueueMap.set(p.id, p));
  const allRevisionProblems = Array.from(revisionQueueMap.values());

  const currentList =
    activeTab === 'bookmarked'
      ? bookmarkedProblems
      : activeTab === 'attempted'
      ? attemptedProblems
      : activeTab === 'solved'
      ? solvedProblems
      : allRevisionProblems;

  const handleStartRevision = () => {
    if (currentList.length > 0) {
      onSelectProblem(currentList[0].id);
    }
  };

  return (
    <div className="space-y-6 pb-12">
      {/* Header Banner */}
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-indigo-950/40 via-purple-950/30 to-blue-950/20 border border-slate-800 shadow-md">
        <div className="space-y-2 max-w-xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-semibold uppercase tracking-wider">
            <Sparkles className="w-3.5 h-3.5" /> Spaced Revision Mode
          </div>
          <h1 className="text-3xl font-extrabold text-white tracking-tight">
            Active Revision Center
          </h1>
          <p className="text-sm text-slate-300 leading-relaxed">
            Consolidate your algorithmic patterns. Revisit tricky edge cases, bookmarked interview questions, and previously attempted problems.
          </p>
        </div>

        {currentList.length > 0 && (
          <button
            onClick={handleStartRevision}
            className="flex items-center gap-2.5 px-6 py-3 rounded-2xl text-sm font-bold text-white bg-gradient-to-r from-indigo-600 via-purple-600 to-blue-600 hover:from-indigo-500 hover:to-blue-500 shadow-xl shadow-indigo-600/30 transition-all hover:scale-105 shrink-0"
          >
            <Play className="w-4 h-4 fill-white" />
            <span>Start Revision Session</span>
          </button>
        )}
      </div>

      {/* Revision Category Tabs */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
        <button
          onClick={() => setActiveTab('all')}
          className={`p-4 rounded-2xl border text-left transition-all ${
            activeTab === 'all'
              ? 'bg-slate-900 border-indigo-500 text-white shadow-sm'
              : 'bg-slate-900/40 hover:bg-slate-900/80 border-slate-800 text-slate-400'
          }`}
        >
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs font-medium">All To Revisit</span>
            <Repeat className="w-4 h-4 text-indigo-400" />
          </div>
          <div className="text-2xl font-bold text-white">{allRevisionProblems.length}</div>
        </button>

        <button
          onClick={() => setActiveTab('bookmarked')}
          className={`p-4 rounded-2xl border text-left transition-all ${
            activeTab === 'bookmarked'
              ? 'bg-slate-900 border-amber-500 text-white shadow-sm'
              : 'bg-slate-900/40 hover:bg-slate-900/80 border-slate-800 text-slate-400'
          }`}
        >
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs font-medium text-amber-400">Bookmarked</span>
            <Bookmark className="w-4 h-4 text-amber-400" />
          </div>
          <div className="text-2xl font-bold text-white">{bookmarkedProblems.length}</div>
        </button>

        <button
          onClick={() => setActiveTab('attempted')}
          className={`p-4 rounded-2xl border text-left transition-all ${
            activeTab === 'attempted'
              ? 'bg-slate-900 border-blue-500 text-white shadow-sm'
              : 'bg-slate-900/40 hover:bg-slate-900/80 border-slate-800 text-slate-400'
          }`}
        >
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs font-medium text-blue-400">Incomplete</span>
            <Clock className="w-4 h-4 text-blue-400" />
          </div>
          <div className="text-2xl font-bold text-white">{attemptedProblems.length}</div>
        </button>

        <button
          onClick={() => setActiveTab('solved')}
          className={`p-4 rounded-2xl border text-left transition-all ${
            activeTab === 'solved'
              ? 'bg-slate-900 border-emerald-500 text-white shadow-sm'
              : 'bg-slate-900/40 hover:bg-slate-900/80 border-slate-800 text-slate-400'
          }`}
        >
          <div className="flex items-center justify-between mb-1">
            <span className="text-xs font-medium text-emerald-400">Mastered</span>
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
          </div>
          <div className="text-2xl font-bold text-white">{solvedProblems.length}</div>
        </button>
      </div>

      {/* Revision Problems List */}
      <div className="space-y-4 pt-2">
        <div className="flex items-center justify-between text-xs text-slate-400">
          <span>
            Showing <strong className="text-slate-200">{currentList.length}</strong> problems in this queue
          </span>
          {currentList.length > 0 && (
            <span className="text-[11px] text-indigo-400 font-mono">
              Ready for Rapid Review
            </span>
          )}
        </div>

        {currentList.length === 0 ? (
          <div className="p-12 text-center rounded-2xl bg-slate-900/40 border border-slate-800 space-y-3">
            <RotateCcw className="w-8 h-8 text-slate-600 mx-auto" />
            <h3 className="text-base font-semibold text-slate-300">
              No problems in this revision queue
            </h3>
            <p className="text-xs text-slate-500 max-w-sm mx-auto">
              Problems you solve, attempt, or bookmark are automatically organized here for interview preparation.
            </p>
            <button
              onClick={() => onNavigate('problems')}
              className="inline-flex items-center gap-1.5 px-4 py-2 text-xs font-semibold text-blue-400 hover:text-white bg-slate-800 rounded-xl transition-colors"
            >
              <BookOpen className="w-3.5 h-3.5" /> Practice Problems
            </button>
          </div>
        ) : (
          <div className="grid grid-cols-1 gap-3">
            {currentList.map((prob) => (
              <ProblemCard
                key={prob.id}
                problem={prob}
                status={getStatus(prob.id)}
                isBookmarked={bookmarked.includes(prob.id)}
                onToggleBookmark={() => onToggleBookmark(prob.id)}
                onSelect={() => onSelectProblem(prob.id)}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
