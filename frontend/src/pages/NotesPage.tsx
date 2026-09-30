import React, { useState } from 'react';
import type { UserNote } from '../types';
import { FileEdit, Search, ArrowRight, Calendar, BookOpen } from 'lucide-react';

interface NotesPageProps {
  notes: Record<string, UserNote>;
  onSelectProblem: (problemId: string) => void;
  onNavigate: (page: string) => void;
}

export const NotesPage: React.FC<NotesPageProps> = ({
  notes,
  onSelectProblem,
  onNavigate,
}) => {
  const [searchQuery, setSearchQuery] = useState('');

  const notesList = Object.values(notes).filter((n) => n.content.trim() !== '');

  const filteredNotes = notesList.filter((n) => {
    if (!searchQuery.trim()) return true;
    const q = searchQuery.toLowerCase().trim();
    return (
      n.problemTitle.toLowerCase().includes(q) ||
      n.content.toLowerCase().includes(q)
    );
  });

  const formatDate = (isoString: string) => {
    try {
      const d = new Date(isoString);
      return d.toLocaleDateString(undefined, {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      });
    } catch {
      return 'Recently';
    }
  };

  return (
    <div className="space-y-6 pb-12">
      {/* Header */}
      <div className="border-b border-slate-800 pb-5">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-semibold uppercase tracking-wider mb-2">
          <FileEdit className="w-3.5 h-3.5" /> Personal Learning Journal
        </div>
        <h1 className="text-3xl font-extrabold text-white tracking-tight">
          Problem Notes & Reflections
        </h1>
        <p className="text-sm text-slate-400 mt-1">
          Review your personal insights, algorithmic observations, and debugging notes saved across problems.
        </p>
      </div>

      {/* Search Input */}
      {notesList.length > 0 && (
        <div className="relative max-w-md">
          <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search within your notes and takeaways..."
            className="w-full pl-10 pr-4 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 focus:outline-none focus:border-blue-500 transition-colors"
          />
        </div>
      )}

      {notesList.length === 0 ? (
        <div className="p-12 text-center rounded-2xl bg-slate-900/40 border border-slate-800 space-y-4 max-w-lg mx-auto">
          <div className="w-12 h-12 rounded-2xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-center mx-auto">
            <FileEdit className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">No notes written yet</h3>
            <p className="text-xs text-slate-400 mt-1 leading-relaxed">
              When solving problems, switch to the <strong>Notes</strong> tab in the left pane to record your thoughts, patterns, and mistakes.
            </p>
          </div>
          <button
            onClick={() => onNavigate('problems')}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold text-white bg-blue-600 hover:bg-blue-500 transition-colors shadow-md"
          >
            <BookOpen className="w-4 h-4" /> Go to Problems
          </button>
        </div>
      ) : filteredNotes.length === 0 ? (
        <div className="p-8 text-center text-xs text-slate-500 bg-slate-900/30 rounded-xl border border-slate-800">
          No notes match your search &ldquo;{searchQuery}&rdquo;.
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {filteredNotes.map((note) => (
            <div
              key={note.problemId}
              onClick={() => onSelectProblem(note.problemId)}
              className="p-5 rounded-2xl bg-slate-900/60 hover:bg-slate-900 border border-slate-800 hover:border-blue-500/40 transition-all cursor-pointer shadow-sm group flex flex-col justify-between space-y-3"
            >
              <div>
                <div className="flex items-center justify-between text-xs text-slate-400 mb-2">
                  <span className="flex items-center gap-1.5 font-mono text-[11px] text-slate-500">
                    <Calendar className="w-3.5 h-3.5" />
                    {formatDate(note.updatedAt)}
                  </span>
                  <div className="flex items-center gap-1 text-blue-400 group-hover:translate-x-0.5 transition-transform font-semibold text-[11px]">
                    <span>Open Problem</span>
                    <ArrowRight className="w-3 h-3" />
                  </div>
                </div>

                <h3 className="text-sm font-bold text-white group-hover:text-blue-400 transition-colors truncate">
                  {note.problemTitle}
                </h3>

                <p className="text-xs text-slate-300 font-mono bg-slate-950/80 p-3 rounded-xl border border-slate-800/80 mt-2 line-clamp-4 whitespace-pre-wrap leading-relaxed">
                  {note.content}
                </p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
