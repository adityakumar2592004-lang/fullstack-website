import React from 'react';
import type { Problem, ModuleInfo } from '../types';
import { ROADMAP_MODULES } from '../data/modules';
import {
  CheckCircle2,
  Clock,
  Bookmark,
  TrendingUp,
  ArrowRight,
  Sparkles,
  BookOpen,
  Terminal,
  Layers,
  ChevronRight,
} from 'lucide-react';

interface DashboardPageProps {
  problems: Problem[];
  solved: string[];
  attempted: string[];
  bookmarked: string[];
  recent: string[];
  onNavigate: (page: string, params?: any) => void;
  onSelectProblem: (problemId: string) => void;
}

export const DashboardPage: React.FC<DashboardPageProps> = ({
  problems,
  solved,
  attempted,
  bookmarked,
  recent,
  onNavigate,
  onSelectProblem,
}) => {
  const totalCount = problems.length;
  const solvedCount = solved.length;
  const attemptedCount = attempted.length;
  const remainingCount = Math.max(0, totalCount - solvedCount);
  const overallPercentage = totalCount > 0 ? Math.round((solvedCount / totalCount) * 100) : 0;

  // Find continue learning problem: first recent or first unsolved problem
  const continueProblem =
    (recent && recent.length > 0 && problems.find((p) => p.id === recent[0])) ||
    problems.find((p) => attempted.includes(p.id) && !solved.includes(p.id)) ||
    problems.find((p) => !solved.includes(p.id)) ||
    problems[0];

  // Recently solved problems
  const recentlySolvedProblems = solved
    .map((id) => problems.find((p) => p.id === id))
    .filter(Boolean) as Problem[];

  // Bookmarked problems
  const bookmarkedProblems = bookmarked
    .map((id) => problems.find((p) => p.id === id))
    .filter(Boolean) as Problem[];

  return (
    <div className="space-y-8 pb-12">
      {/* Hero Banner */}
      <div className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-blue-900/40 via-indigo-900/30 to-purple-900/20 border border-slate-800 p-6 sm:p-8">
        <div className="absolute -right-12 -bottom-12 w-64 h-64 bg-blue-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 max-w-3xl space-y-4">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-semibold uppercase tracking-wider">
            <Sparkles className="w-3.5 h-3.5" /> Complete DSA Learning & Coding Practice
          </div>
          <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-white leading-tight">
            Master DSA One Problem at a Time
          </h1>
          <p className="text-sm sm:text-base text-slate-300 leading-relaxed">
            A structured roadmap with step-by-step intuition, algorithmic approaches, dry runs, multi-language starter code, progressive hints, and an integrated online compiler with test case evaluation.
          </p>

          <div className="flex items-center gap-3 pt-2 flex-wrap">
            {continueProblem && (
              <button
                onClick={() => onSelectProblem(continueProblem.id)}
                className="flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold text-white bg-blue-600 hover:bg-blue-500 shadow-lg shadow-blue-600/30 transition-all hover:scale-[1.02]"
              >
                <span>Continue Learning</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            )}
            <button
              onClick={() => onNavigate('roadmap')}
              className="flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold text-slate-200 bg-slate-800/80 hover:bg-slate-800 border border-slate-700 transition-all"
            >
              <span>View Full Roadmap</span>
              <BookOpen className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* Progress Metric Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 sm:gap-4">
        <div className="p-4 rounded-2xl bg-slate-900/60 border border-slate-800">
          <div className="text-xs text-slate-400 font-medium">Total Problems</div>
          <div className="text-2xl font-bold text-white mt-1">{totalCount}</div>
          <div className="text-[11px] text-blue-400 mt-0.5">Modules 1–5 Ready</div>
        </div>

        <div className="p-4 rounded-2xl bg-emerald-950/20 border border-emerald-500/20">
          <div className="text-xs text-emerald-400 font-medium flex items-center gap-1">
            <CheckCircle2 className="w-3.5 h-3.5" /> Solved
          </div>
          <div className="text-2xl font-bold text-emerald-300 mt-1">{solvedCount}</div>
          <div className="text-[11px] text-emerald-500 mt-0.5">{overallPercentage}% Completed</div>
        </div>

        <div className="p-4 rounded-2xl bg-blue-950/20 border border-blue-500/20">
          <div className="text-xs text-blue-400 font-medium flex items-center gap-1">
            <Clock className="w-3.5 h-3.5" /> Attempted
          </div>
          <div className="text-2xl font-bold text-blue-300 mt-1">{attemptedCount}</div>
          <div className="text-[11px] text-blue-500 mt-0.5">In Progress</div>
        </div>

        <div className="p-4 rounded-2xl bg-slate-900/60 border border-slate-800">
          <div className="text-xs text-slate-400 font-medium">Remaining</div>
          <div className="text-2xl font-bold text-slate-300 mt-1">{remainingCount}</div>
          <div className="text-[11px] text-slate-500 mt-0.5">To Practice</div>
        </div>

        <div className="p-4 rounded-2xl bg-amber-950/20 border border-amber-500/20">
          <div className="text-xs text-amber-400 font-medium flex items-center gap-1">
            <Bookmark className="w-3.5 h-3.5" /> Bookmarked
          </div>
          <div className="text-2xl font-bold text-amber-300 mt-1">{bookmarked.length}</div>
          <div className="text-[11px] text-amber-500 mt-0.5">Saved for Revisit</div>
        </div>

        <div className="p-4 rounded-2xl bg-purple-950/20 border border-purple-500/20">
          <div className="text-xs text-purple-400 font-medium flex items-center gap-1">
            <TrendingUp className="w-3.5 h-3.5" /> Overall Progress
          </div>
          <div className="text-2xl font-bold text-purple-300 mt-1">{overallPercentage}%</div>
          <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
            <div
              className="bg-purple-500 h-full rounded-full transition-all duration-500"
              style={{ width: `${overallPercentage}%` }}
            />
          </div>
        </div>
      </div>

      {/* Module Progress Section */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-xl font-bold text-white flex items-center gap-2">
              <Layers className="w-5 h-5 text-blue-400" /> Module Learning Progress
            </h2>
            <p className="text-xs text-slate-400">
              Track your mastery across each core data structure and algorithm module.
            </p>
          </div>
          <button
            onClick={() => onNavigate('roadmap')}
            className="text-xs text-blue-400 hover:text-blue-300 flex items-center gap-1 font-semibold"
          >
            All 20 Modules <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {ROADMAP_MODULES.slice(0, 5).map((mod: ModuleInfo) => {
            const modProblems = problems.filter((p) => p.step_id === mod.id);
            const modSolved = modProblems.filter((p) => solved.includes(p.id)).length;
            const modTotal = modProblems.length || 1;
            const percent = Math.round((modSolved / modTotal) * 100);

            return (
              <div
                key={mod.id}
                onClick={() => onNavigate('module-detail', { moduleId: mod.id })}
                className="group p-5 rounded-2xl bg-slate-900/60 hover:bg-slate-900 border border-slate-800 hover:border-slate-700 transition-all cursor-pointer shadow-sm flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs font-mono font-bold text-blue-400 bg-blue-500/10 px-2 py-0.5 rounded border border-blue-500/20">
                      Step {mod.id}
                    </span>
                    <span className="text-xs font-semibold text-slate-400">
                      {modSolved} / {modTotal} solved
                    </span>
                  </div>

                  <h3 className="text-base font-bold text-white group-hover:text-blue-400 transition-colors">
                    {mod.title}
                  </h3>
                  <p className="text-xs text-slate-400 line-clamp-2 mt-1 mb-4">
                    {mod.description}
                  </p>
                </div>

                <div className="space-y-2">
                  <div className="flex items-center justify-between text-xs">
                    <span className="text-slate-400 font-medium">Progress</span>
                    <span className="font-bold text-slate-200">{percent}%</span>
                  </div>
                  <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full transition-all duration-500"
                      style={{ width: `${percent}%` }}
                    />
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Feature Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4 border-t border-slate-800/80">
        <div className="p-5 rounded-2xl bg-slate-900/40 border border-slate-800 space-y-2">
          <div className="w-9 h-9 rounded-xl bg-blue-500/10 text-blue-400 flex items-center justify-center">
            <BookOpen className="w-5 h-5" />
          </div>
          <h4 className="text-sm font-bold text-white">9-Part Deep Editorials</h4>
          <p className="text-xs text-slate-400 leading-relaxed">
            Every problem features Intuition, Brute Force, Better, Optimal, Dry Run, Time/Space Complexity, and Interview Follow-ups.
          </p>
        </div>

        <div className="p-5 rounded-2xl bg-slate-900/40 border border-slate-800 space-y-2">
          <div className="w-9 h-9 rounded-xl bg-emerald-500/10 text-emerald-400 flex items-center justify-center">
            <Terminal className="w-5 h-5" />
          </div>
          <h4 className="text-sm font-bold text-white">Online Sandbox Compiler</h4>
          <p className="text-xs text-slate-400 leading-relaxed">
            Execute real Python code securely in backend sandbox with timing benchmarks and hidden test case verification.
          </p>
        </div>

        <div className="p-5 rounded-2xl bg-slate-900/40 border border-slate-800 space-y-2">
          <div className="w-9 h-9 rounded-xl bg-purple-500/10 text-purple-400 flex items-center justify-center">
            <Sparkles className="w-5 h-5" />
          </div>
          <h4 className="text-sm font-bold text-white">Spaced Revision Mode</h4>
          <p className="text-xs text-slate-400 leading-relaxed">
            Quickly revisit solved and bookmarked problems with guided sequential player mode for efficient interview preparation.
          </p>
        </div>
      </div>

      {/* Recently Solved & Bookmarks Split */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 pt-4 border-t border-slate-800/80">
        {/* Recently Solved */}
        <div className="space-y-3">
          <div className="flex items-center justify-between">
            <h3 className="text-base font-bold text-white flex items-center gap-2">
              <CheckCircle2 className="w-4 h-4 text-emerald-400" /> Recently Solved
            </h3>
            <span className="text-xs text-slate-400">{recentlySolvedProblems.length} problems</span>
          </div>

          {recentlySolvedProblems.length === 0 ? (
            <div className="p-6 rounded-2xl bg-slate-900/30 border border-slate-800/80 text-center text-xs text-slate-500">
              No problems solved yet. Pick a problem and submit your solution!
            </div>
          ) : (
            <div className="space-y-2">
              {recentlySolvedProblems.slice(0, 5).map((p) => (
                <div
                  key={p.id}
                  onClick={() => onSelectProblem(p.id)}
                  className="p-3 rounded-xl bg-slate-900/60 hover:bg-slate-800/80 border border-slate-800 hover:border-slate-700 transition-all cursor-pointer flex items-center justify-between"
                >
                  <div className="truncate pr-2">
                    <div className="text-xs font-semibold text-slate-200 truncate">{p.title}</div>
                    <div className="text-[11px] text-slate-500 truncate">{p.subtopic}</div>
                  </div>
                  <span className="text-xs font-mono text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded shrink-0">
                    Solved
                  </span>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Bookmarked Problems */}
        <div className="space-y-3">
          <div className="flex items-center justify-between">
            <h3 className="text-base font-bold text-white flex items-center gap-2">
              <Bookmark className="w-4 h-4 text-amber-400" /> Bookmarked for Revisit
            </h3>
            <button
              onClick={() => onNavigate('bookmarks')}
              className="text-xs text-blue-400 hover:text-blue-300"
            >
              View All
            </button>
          </div>

          {bookmarkedProblems.length === 0 ? (
            <div className="p-6 rounded-2xl bg-slate-900/30 border border-slate-800/80 text-center text-xs text-slate-500">
              No bookmarked problems yet. Click the bookmark icon on any problem to save it here.
            </div>
          ) : (
            <div className="space-y-2">
              {bookmarkedProblems.slice(0, 5).map((p) => (
                <div
                  key={p.id}
                  onClick={() => onSelectProblem(p.id)}
                  className="p-3 rounded-xl bg-slate-900/60 hover:bg-slate-800/80 border border-slate-800 hover:border-slate-700 transition-all cursor-pointer flex items-center justify-between"
                >
                  <div className="truncate pr-2">
                    <div className="text-xs font-semibold text-slate-200 truncate">{p.title}</div>
                    <div className="text-[11px] text-slate-500 truncate">{p.subtopic}</div>
                  </div>
                  <span className="text-xs font-semibold text-slate-400 bg-slate-800 px-2 py-0.5 rounded shrink-0">
                    {p.difficulty}
                  </span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
