import React from 'react';
import type { Problem, ModuleInfo, TopicInfo } from '../types';
import { ROADMAP_MODULES } from '../data/modules';
import { Map, ArrowRight, Lock, CheckCircle2 } from 'lucide-react';

interface RoadmapPageProps {
  problems: Problem[];
  solved: string[];
  onNavigate: (page: string, params?: any) => void;
}

export const RoadmapPage: React.FC<RoadmapPageProps> = ({
  problems,
  solved,
  onNavigate,
}) => {
  return (
    <div className="space-y-8 pb-12">
      {/* Header */}
      <div className="border-b border-slate-800 pb-6">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-xs font-semibold uppercase tracking-wider mb-2">
          <Map className="w-3.5 h-3.5" /> Structured Learning Path
        </div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">
          DSA Roadmap
        </h1>
        <p className="text-sm text-slate-400 mt-1 max-w-2xl">
          A step-by-step master roadmap covering 20 essential DSA domains. Practice foundational to advanced algorithmic patterns with verified editorials.
        </p>
      </div>

      {/* Grid of All 20 Modules */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {ROADMAP_MODULES.map((mod: ModuleInfo) => {
          const isAvailable = !mod.isComingSoon;
          const modProblems = problems.filter((p) => p.step_id === mod.id);
          const solvedInMod = modProblems.filter((p) => solved.includes(p.id)).length;
          const totalInMod = modProblems.length;
          const progress = totalInMod > 0 ? Math.round((solvedInMod / totalInMod) * 100) : 0;

          return (
            <div
              key={mod.id}
              onClick={() => {
                if (isAvailable) {
                  onNavigate('module-detail', { moduleId: mod.id });
                }
              }}
              className={`rounded-2xl border transition-all duration-200 flex flex-col justify-between p-5 relative overflow-hidden ${
                isAvailable
                  ? 'bg-slate-900/70 hover:bg-slate-900 border-slate-800 hover:border-blue-500/50 cursor-pointer shadow-sm hover:shadow-md group'
                  : 'bg-slate-950/40 border-slate-800/60 opacity-80 cursor-default'
              }`}
            >
              <div>
                {/* Header status */}
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-2">
                    <span
                      className={`text-xs font-mono font-bold px-2.5 py-0.5 rounded-md border ${
                        isAvailable
                          ? 'text-blue-400 bg-blue-500/10 border-blue-500/20'
                          : 'text-slate-500 bg-slate-800/60 border-slate-700/60'
                      }`}
                    >
                      Step {mod.id.toString().padStart(2, '0')}
                    </span>
                    {isAvailable ? (
                      <span className="text-[11px] font-semibold text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2 py-0.5 rounded-full flex items-center gap-1">
                        <CheckCircle2 className="w-3 h-3" /> Live
                      </span>
                    ) : (
                      <span className="text-[11px] font-semibold text-amber-400 bg-amber-500/10 border border-amber-500/20 px-2 py-0.5 rounded-full flex items-center gap-1">
                        <Lock className="w-3 h-3" /> Coming Soon
                      </span>
                    )}
                  </div>

                  {isAvailable && (
                    <span className="text-xs font-bold text-slate-300">
                      {solvedInMod} / {totalInMod}
                    </span>
                  )}
                </div>

                {/* Title & Description */}
                <h3
                  className={`text-lg font-bold tracking-tight mb-1.5 transition-colors ${
                    isAvailable ? 'text-white group-hover:text-blue-400' : 'text-slate-400'
                  }`}
                >
                  {mod.title}
                </h3>
                <p className="text-xs text-slate-400 line-clamp-2 leading-relaxed mb-4">
                  {mod.description}
                </p>

                {/* Subtopic pill tags */}
                <div className="space-y-1.5 mb-5">
                  <div className="text-[11px] font-medium text-slate-500 uppercase tracking-wider">
                    {mod.topics.length} Key Topics:
                  </div>
                  <div className="flex flex-wrap gap-1.5">
                    {mod.topics.slice(0, 3).map((topic: TopicInfo, i: number) => (
                      <span
                        key={i}
                        className="text-[11px] font-medium text-slate-400 bg-slate-950 px-2 py-0.5 rounded border border-slate-800 truncate max-w-[190px]"
                      >
                        {topic.title}
                      </span>
                    ))}
                    {mod.topics.length > 3 && (
                      <span className="text-[10px] text-slate-500 self-center">
                        +{mod.topics.length - 3} more
                      </span>
                    )}
                  </div>
                </div>
              </div>

              {/* Bottom action / progress */}
              {isAvailable ? (
                <div className="pt-3 border-t border-slate-800/80 space-y-2">
                  <div className="flex items-center justify-between text-xs">
                    <span className="text-slate-400">Mastery</span>
                    <span className="font-semibold text-slate-200">{progress}%</span>
                  </div>
                  <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full transition-all duration-500"
                      style={{ width: `${progress}%` }}
                    />
                  </div>

                  <div className="pt-2 flex items-center justify-between text-xs font-semibold text-blue-400 group-hover:text-blue-300">
                    <span>Explore {totalInMod} Problems</span>
                    <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                  </div>
                </div>
              ) : (
                <div className="pt-3 border-t border-slate-800/60 flex items-center justify-between text-xs text-slate-500">
                  <span>Advanced Module</span>
                  <span className="italic">In development</span>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
