import React, { useState, useEffect } from 'react';
import { FileEdit, Check, Sparkles } from 'lucide-react';

interface NotesEditorProps {
  problemId: string;
  problemTitle: string;
  initialNote: string;
  onSave: (problemId: string, title: string, content: string) => void;
}

export const NotesEditor: React.FC<NotesEditorProps> = ({
  problemId,
  problemTitle,
  initialNote,
  onSave,
}) => {
  const [content, setContent] = useState(initialNote);
  const [isSaved, setIsSaved] = useState(true);

  useEffect(() => {
    setContent(initialNote);
  }, [problemId, initialNote]);

  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setContent(e.target.value);
    setIsSaved(false);
  };

  const handleSave = () => {
    onSave(problemId, problemTitle, content);
    setIsSaved(true);
  };

  const addTemplate = (text: string) => {
    setContent((prev) => (prev ? `${prev}\n\n${text}` : text));
    setIsSaved(false);
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between pb-2 border-b border-slate-800">
        <div className="flex items-center gap-2">
          <FileEdit className="w-5 h-5 text-blue-400" />
          <div>
            <h2 className="text-base font-bold text-white">Personal Learning Notes</h2>
            <p className="text-xs text-slate-400">
              Save key insights, tricky edge cases, and personal takeaways. Persisted locally.
            </p>
          </div>
        </div>

        <button
          onClick={handleSave}
          disabled={isSaved}
          className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
            isSaved
              ? 'bg-slate-800 text-slate-400 cursor-default'
              : 'bg-blue-600 hover:bg-blue-500 text-white shadow-md shadow-blue-600/20'
          }`}
        >
          <Check className="w-3.5 h-3.5" />
          {isSaved ? 'Saved' : 'Save Notes'}
        </button>
      </div>

      {/* Quick Prompt Templates */}
      <div className="flex items-center gap-2 flex-wrap text-xs">
        <span className="text-slate-500 font-medium flex items-center gap-1">
          <Sparkles className="w-3 h-3 text-amber-400" /> Quick Templates:
        </span>
        <button
          onClick={() => addTemplate('💡 **Key Insight / Pattern:**\n')}
          className="px-2.5 py-1 rounded-md bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition-colors"
        >
          + Key Insight
        </button>
        <button
          onClick={() => addTemplate('⚠️ **My Mistake & Pitfall:**\n')}
          className="px-2.5 py-1 rounded-md bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition-colors"
        >
          + My Mistake
        </button>
        <button
          onClick={() => addTemplate('🔄 **Revise for Interviews:**\n')}
          className="px-2.5 py-1 rounded-md bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition-colors"
        >
          + Revisit Note
        </button>
      </div>

      {/* Textarea */}
      <div className="relative">
        <textarea
          value={content}
          onChange={handleChange}
          rows={12}
          placeholder="Write your personal notes, learnings, mistakes, or interview reflections here..."
          className="w-full p-4 rounded-xl bg-slate-950/80 border border-slate-800 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 text-slate-200 placeholder-slate-500 text-sm leading-relaxed font-mono focus:outline-none transition-all resize-y"
        />
        {!isSaved && (
          <span className="absolute bottom-3 right-3 text-[11px] text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">
            Unsaved changes
          </span>
        )}
      </div>
    </div>
  );
};
