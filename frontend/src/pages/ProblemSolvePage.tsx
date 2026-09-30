import React, { useState, useEffect } from 'react';
import type {
  Problem,
  ProblemStatus,
  SupportedLanguage,
  RunResponse,
  TestCase,
} from '../types';
import { ProblemDescription } from '../components/problem/ProblemDescription';
import { ExplanationView } from '../components/problem/ExplanationView';
import { HintAccordion } from '../components/problem/HintAccordion';
import { NotesEditor } from '../components/problem/NotesEditor';
import { CodeEditor } from '../components/editor/CodeEditor';
import { TestConsole } from '../components/editor/TestConsole';
import { executeCode } from '../services/api';
import {
  FileText,
  Lightbulb,
  Sparkles,
  Edit3,
  Bookmark,
  ChevronLeft,
  ChevronRight,
  CheckCircle2,
  Clock,
} from 'lucide-react';

interface ProblemSolvePageProps {
  problem: Problem;
  allProblems: Problem[];
  status: ProblemStatus;
  isBookmarked: boolean;
  onToggleBookmark: () => void;
  onMarkSolved: (problemId: string) => void;
  onMarkAttempted: (problemId: string) => void;
  userNote: string;
  onSaveNote: (problemId: string, title: string, content: string) => void;
  onSelectProblem: (problemId: string) => void;
  onNavigate: (page: string, params?: any) => void;
}

export const ProblemSolvePage: React.FC<ProblemSolvePageProps> = ({
  problem,
  allProblems,
  status,
  isBookmarked,
  onToggleBookmark,
  onMarkSolved,
  onMarkAttempted,
  userNote,
  onSaveNote,
  onSelectProblem,
  onNavigate,
}) => {
  const [activeTab, setActiveTab] = useState<'problem' | 'explanation' | 'hints' | 'notes'>('problem');
  const [language, setLanguage] = useState<SupportedLanguage>('python');
  const [code, setCode] = useState<string>('');
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [runResult, setRunResult] = useState<RunResponse | null>(null);

  // Initialize starter code when problem or language changes
  useEffect(() => {
    const savedCodeKey = `dsa_code_${problem.id}_${language}`;
    const savedCode = localStorage.getItem(savedCodeKey);
    if (savedCode) {
      setCode(savedCode);
    } else {
      const template = problem.starter_code?.[language] || problem.starter_code?.python || '';
      setCode(template);
    }
    setRunResult(null);
  }, [problem.id, language]);

  // Persist code on change
  const handleCodeChange = (newCode: string) => {
    setCode(newCode);
    try {
      localStorage.setItem(`dsa_code_${problem.id}_${language}`, newCode);
    } catch (e) {
      console.error(e);
    }
  };

  const handleResetCode = () => {
    if (window.confirm('Reset code to original starter template?')) {
      const template = problem.starter_code?.[language] || problem.starter_code?.python || '';
      setCode(template);
      localStorage.removeItem(`dsa_code_${problem.id}_${language}`);
    }
  };

  // Find previous and next problem
  const currentIndex = allProblems.findIndex((p) => p.id === problem.id);
  const prevProblem = currentIndex > 0 ? allProblems[currentIndex - 1] : null;
  const nextProblem = currentIndex < allProblems.length - 1 ? allProblems[currentIndex + 1] : null;

  // Run Code (sample tests only)
  const handleRun = async () => {
    setIsRunning(true);
    onMarkAttempted(problem.id);
    try {
      const resp = await executeCode({
        problem_id: problem.id,
        code,
        language,
        mode: 'sample',
      });
      setRunResult(resp);
    } catch (err: any) {
      setRunResult({
        verdict: 'RUNTIME ERROR',
        total_cases: 0,
        passed_cases: 0,
        failed_cases: 0,
        total_execution_time_ms: 0,
        results: [],
        global_error: err?.message || 'Failed to communicate with compiler backend.',
      });
    } finally {
      setIsRunning(false);
    }
  };

  // Submit Code (sample + hidden test cases)
  const handleSubmit = async () => {
    setIsSubmitting(true);
    onMarkAttempted(problem.id);
    try {
      const resp = await executeCode({
        problem_id: problem.id,
        code,
        language,
        mode: 'submit',
      });
      setRunResult(resp);

      // If all test cases passed, mark as solved!
      if (resp.verdict === 'ALL TEST CASES PASSED') {
        onMarkSolved(problem.id);
      }
    } catch (err: any) {
      setRunResult({
        verdict: 'RUNTIME ERROR',
        total_cases: 0,
        passed_cases: 0,
        failed_cases: 0,
        total_execution_time_ms: 0,
        results: [],
        global_error: err?.message || 'Failed to communicate with compiler backend.',
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  const sampleCases = problem.test_cases?.filter((tc: TestCase) => !tc.is_hidden) || [];

  return (
    <div className="flex flex-col space-y-4 pb-12">
      {/* Top Problem Navigation Bar */}
      <div className="flex items-center justify-between gap-3 p-3.5 rounded-2xl bg-slate-900 border border-slate-800 flex-wrap">
        {/* Left: Module & Sequence Info */}
        <div className="flex items-center gap-3">
          <button
            onClick={() => onNavigate('module-detail', { moduleId: problem.step_id })}
            className="text-xs font-semibold text-blue-400 hover:text-blue-300"
          >
            {problem.step_title}
          </button>
          <span className="text-slate-600 font-mono">/</span>
          <span className="text-xs text-slate-400 truncate max-w-[200px]">
            {problem.title}
          </span>
        </div>

        {/* Right: Prev/Next & Bookmark */}
        <div className="flex items-center gap-2">
          {status === 'Solved' && (
            <span className="hidden sm:flex items-center gap-1 text-xs font-semibold text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2.5 py-1 rounded-full">
              <CheckCircle2 className="w-3.5 h-3.5" /> Solved
            </span>
          )}
          {status === 'Attempted' && (
            <span className="hidden sm:flex items-center gap-1 text-xs font-semibold text-blue-400 bg-blue-500/10 border border-blue-500/20 px-2.5 py-1 rounded-full">
              <Clock className="w-3.5 h-3.5" /> Attempted
            </span>
          )}

          <button
            onClick={onToggleBookmark}
            className={`p-2 rounded-xl border text-xs font-medium flex items-center gap-1.5 transition-colors ${
              isBookmarked
                ? 'text-amber-400 bg-amber-500/10 border-amber-500/30'
                : 'text-slate-400 hover:text-white bg-slate-800 border-slate-700'
            }`}
            title="Bookmark this problem"
          >
            <Bookmark className={`w-4 h-4 ${isBookmarked ? 'fill-amber-400' : ''}`} />
            <span className="hidden md:inline">{isBookmarked ? 'Bookmarked' : 'Bookmark'}</span>
          </button>

          <div className="flex items-center gap-1 border-l border-slate-800 pl-2">
            <button
              onClick={() => prevProblem && onSelectProblem(prevProblem.id)}
              disabled={!prevProblem}
              className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 disabled:opacity-30 disabled:pointer-events-none transition-colors"
              title={prevProblem ? `Previous: ${prevProblem.title}` : 'First Problem'}
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            <button
              onClick={() => nextProblem && onSelectProblem(nextProblem.id)}
              disabled={!nextProblem}
              className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 disabled:opacity-30 disabled:pointer-events-none transition-colors"
              title={nextProblem ? `Next: ${nextProblem.title}` : 'Last Problem'}
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      {/* Main Split Layout: Left Content & Right Code IDE */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
        {/* Left Column: Learning Material Tabs */}
        <div className="lg:col-span-6 flex flex-col bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-lg">
          {/* Tab Selector */}
          <div className="flex items-center border-b border-slate-800 bg-slate-950/80 px-2 pt-2 gap-1 overflow-x-auto custom-scrollbar">
            <button
              onClick={() => setActiveTab('problem')}
              className={`flex items-center gap-2 px-3.5 py-2.5 rounded-t-xl text-xs font-bold transition-colors border-t border-x ${
                activeTab === 'problem'
                  ? 'bg-slate-900 text-blue-400 border-slate-800 border-b-slate-900 -mb-px'
                  : 'text-slate-400 hover:text-slate-200 border-transparent hover:bg-slate-900/40'
              }`}
            >
              <FileText className="w-3.5 h-3.5" /> Problem
            </button>

            <button
              onClick={() => setActiveTab('explanation')}
              className={`flex items-center gap-2 px-3.5 py-2.5 rounded-t-xl text-xs font-bold transition-colors border-t border-x ${
                activeTab === 'explanation'
                  ? 'bg-slate-900 text-amber-400 border-slate-800 border-b-slate-900 -mb-px'
                  : 'text-slate-400 hover:text-slate-200 border-transparent hover:bg-slate-900/40'
              }`}
            >
              <Lightbulb className="w-3.5 h-3.5" /> Editorial
            </button>

            <button
              onClick={() => setActiveTab('hints')}
              className={`flex items-center gap-2 px-3.5 py-2.5 rounded-t-xl text-xs font-bold transition-colors border-t border-x ${
                activeTab === 'hints'
                  ? 'bg-slate-900 text-indigo-400 border-slate-800 border-b-slate-900 -mb-px'
                  : 'text-slate-400 hover:text-slate-200 border-transparent hover:bg-slate-900/40'
              }`}
            >
              <Sparkles className="w-3.5 h-3.5" /> Hints ({problem.hints?.length || 3})
            </button>

            <button
              onClick={() => setActiveTab('notes')}
              className={`flex items-center gap-2 px-3.5 py-2.5 rounded-t-xl text-xs font-bold transition-colors border-t border-x ${
                activeTab === 'notes'
                  ? 'bg-slate-900 text-emerald-400 border-slate-800 border-b-slate-900 -mb-px'
                  : 'text-slate-400 hover:text-slate-200 border-transparent hover:bg-slate-900/40'
              }`}
            >
              <Edit3 className="w-3.5 h-3.5" /> Notes
            </button>
          </div>

          {/* Tab Content Container */}
          <div className="p-5 overflow-y-auto max-h-[calc(100vh-14rem)] custom-scrollbar">
            {activeTab === 'problem' && <ProblemDescription problem={problem} />}
            {activeTab === 'explanation' && (
              <ExplanationView explanation={problem.explanation} />
            )}
            {activeTab === 'hints' && <HintAccordion hints={problem.hints || []} />}
            {activeTab === 'notes' && (
              <NotesEditor
                problemId={problem.id}
                problemTitle={problem.title}
                initialNote={userNote}
                onSave={onSaveNote}
              />
            )}
          </div>
        </div>

        {/* Right Column: Code Editor + Test Console */}
        <div className="lg:col-span-6 space-y-4">
          {/* Monaco Editor */}
          <div className="h-[460px]">
            <CodeEditor
              language={language}
              onLanguageChange={setLanguage}
              code={code}
              onCodeChange={handleCodeChange}
              onResetCode={handleResetCode}
              onRun={handleRun}
              onSubmit={handleSubmit}
              isRunning={isRunning}
              isSubmitting={isSubmitting}
            />
          </div>

          {/* Test Case & Result Console */}
          <TestConsole
            result={runResult}
            isRunning={isRunning}
            isSubmitting={isSubmitting}
            sampleTestCases={sampleCases}
          />
        </div>
      </div>
    </div>
  );
};
