import React, { useState } from 'react';
import type { Problem, ProblemStatus, ModuleInfo, TopicInfo } from '../types';
import { ROADMAP_MODULES } from '../data/modules';
import { ProblemCard } from '../components/problem/ProblemCard';
import { ArrowLeft, Layers, CheckCircle2 } from 'lucide-react';

interface ModuleDetailPageProps {
  moduleId: number;
  problems: Problem[];
  solved: string[];
  bookmarked: string[];
  getStatus: (id: string) => ProblemStatus;
  onToggleBookmark: (id: string) => void;
  onSelectProblem: (id: string) => void;
  onNavigate: (page: string) => void;
}

export const ModuleDetailPage: React.FC<ModuleDetailPageProps> = ({
  moduleId,
  problems,
  solved,
  bookmarked,
  getStatus,
  onToggleBookmark,
  onSelectProblem,
  onNavigate,
}) => {
  const currentModule = ROADMAP_MODULES.find((m: ModuleInfo) => m.id === moduleId) || ROADMAP_MODULES[0];
  const moduleProblems = problems.filter((p) => p.step_id === moduleId);

  const [selectedSubtopic, setSelectedSubtopic] = useState<string>('All');
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('All');

  const solvedCount = moduleProblems.filter((p) => solved.includes(p.id)).length;
  const progressPercent =
    moduleProblems.length > 0 ? Math.round((solvedCount / moduleProblems.length) * 100) : 0;

  // Filter problems within this module
  const filteredProblems = moduleProblems.filter((p) => {
    if (selectedSubtopic !== 'All' && !p.subtopic.includes(selectedSubtopic)) return false;
    if (selectedDifficulty !== 'All' && p.difficulty !== selectedDifficulty) return false;
    return true;
  });

  return (
    <div className="space-y-8 pb-12">
      {/* Back button and Module Header */}
      <div>
        <button
          onClick={() => onNavigate('roadmap')}
          className="inline-flex items-center gap-2 text-xs font-semibold text-slate-400 hover:text-white transition-colors mb-4 group"
        >
          <ArrowLeft className="w-4 h-4 group-hover:-translate-x-1 transition-transform" />
          <span>Back to All Roadmap Modules</span>
        </button>

        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-6 p-6 sm:p-8 rounded-3xl bg-slate-900/80 border border-slate-800 shadow-md">
          <div className="space-y-2 max-w-2xl">
            <div className="flex items-center gap-2">
              <span className="text-xs font-mono font-bold px-2.5 py-0.5 rounded-md bg-blue-500/10 text-blue-400 border border-blue-500/20">
                Step {currentModule.id}
              </span>
              <span className="text-xs font-semibold text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2.5 py-0.5 rounded-full flex items-center gap-1">
                <CheckCircle2 className="w-3.5 h-3.5" /> Fully Implemented
              </span>
            </div>
            <h1 className="text-3xl font-extrabold text-white tracking-tight">
              {currentModule.title}
            </h1>
            <p className="text-sm text-slate-300 leading-relaxed">
              {currentModule.description}
            </p>
          </div>

          <div className="flex flex-col sm:flex-row lg:flex-col items-start lg:items-end justify-between gap-4 p-4 rounded-2xl bg-slate-950/70 border border-slate-800 shrink-0 min-w-[200px]">
            <div>
              <div className="text-xs text-slate-400">Module Completion</div>
              <div className="text-2xl font-bold text-white mt-0.5">
                {solvedCount} / {moduleProblems.length}
              </div>
            </div>
            <div className="w-full sm:w-36 lg:w-full space-y-1">
              <div className="text-[11px] text-right font-semibold text-blue-400">
                {progressPercent}%
              </div>
              <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div
                  className="h-full bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full transition-all duration-500"
                  style={{ width: `${progressPercent}%` }}
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Subtopics Cards Overview */}
      <div className="space-y-3">
        <h2 className="text-sm font-bold text-slate-300 uppercase tracking-wider flex items-center gap-2">
          <Layers className="w-4 h-4 text-blue-400" /> Key Subtopics in this Module
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {currentModule.topics.map((t: TopicInfo) => {
            const topicProblems = moduleProblems.filter((p) => p.subtopic.includes(t.title));
            const topicSolved = topicProblems.filter((p) => solved.includes(p.id)).length;
            const isSelected = selectedSubtopic === t.title;

            return (
              <div
                key={t.id}
                onClick={() => setSelectedSubtopic(isSelected ? 'All' : t.title)}
                className={`p-4 rounded-xl border transition-all cursor-pointer ${
                  isSelected
                    ? 'bg-blue-950/30 border-blue-500 text-white shadow-sm'
                    : 'bg-slate-900/40 hover:bg-slate-900 border-slate-800 text-slate-300'
                }`}
              >
                <div className="flex items-center justify-between text-xs mb-1">
                  <span className="font-bold text-white truncate max-w-[170px]">{t.title}</span>
                  <span className="text-[11px] text-slate-400 font-mono">
                    {topicSolved}/{topicProblems.length}
                  </span>
                </div>
                <p className="text-[11px] text-slate-400 line-clamp-2 leading-relaxed">
                  {t.description}
                </p>
              </div>
            );
          })}
        </div>
      </div>

      {/* Filter and Problem List */}
      <div className="space-y-4 pt-2">
        <div className="flex items-center justify-between flex-wrap gap-3 pb-2 border-b border-slate-800">
          <div className="flex items-center gap-3">
            <h2 className="text-lg font-bold text-white">Problems ({filteredProblems.length})</h2>
            {selectedSubtopic !== 'All' && (
              <button
                onClick={() => setSelectedSubtopic('All')}
                className="text-xs text-blue-400 hover:text-blue-300 font-medium"
              >
                Show all subtopics
              </button>
            )}
          </div>

          <div className="flex items-center gap-2 text-xs">
            <span className="text-slate-400">Difficulty:</span>
            {['All', 'Easy', 'Medium', 'Hard'].map((diff) => (
              <button
                key={diff}
                onClick={() => setSelectedDifficulty(diff)}
                className={`px-2.5 py-1 rounded-md transition-colors ${
                  selectedDifficulty === diff
                    ? 'bg-blue-600 text-white font-semibold'
                    : 'bg-slate-800/80 text-slate-400 hover:text-white'
                }`}
              >
                {diff}
              </button>
            ))}
          </div>
        </div>

        {/* Problems Grid */}
        <div className="grid grid-cols-1 gap-3">
          {filteredProblems.map((prob) => (
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
      </div>
    </div>
  );
};
