import React, { useState } from 'react';
import type { RunResponse, TestCaseResult } from '../../types';
import {
  CheckCircle2,
  XCircle,
  AlertTriangle,
  Clock,
  Terminal,
  ShieldAlert,
  ChevronRight,
} from 'lucide-react';

interface TestConsoleProps {
  result: RunResponse | null;
  isRunning: boolean;
  isSubmitting: boolean;
  sampleTestCases: any[];
}

export const TestConsole: React.FC<TestConsoleProps> = ({
  result,
  isRunning,
  isSubmitting,
  sampleTestCases,
}) => {
  const [selectedCaseIndex, setSelectedCaseIndex] = useState(0);

  const getVerdictBadge = (verdict: string) => {
    switch (verdict) {
      case 'ALL TEST CASES PASSED':
        return {
          bg: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30',
          icon: CheckCircle2,
          text: 'Accepted — All Test Cases Passed!',
        };
      case 'SOME TEST CASES FAILED':
        return {
          bg: 'bg-rose-500/10 text-rose-400 border-rose-500/30',
          icon: XCircle,
          text: 'Wrong Answer — Some Test Cases Failed',
        };
      case 'SYNTAX ERROR':
        return {
          bg: 'bg-amber-500/10 text-amber-400 border-amber-500/30',
          icon: AlertTriangle,
          text: 'Compilation / Syntax Error',
        };
      case 'TIME LIMIT EXCEEDED':
        return {
          bg: 'bg-orange-500/10 text-orange-400 border-orange-500/30',
          icon: Clock,
          text: 'Time Limit Exceeded (> 5.0s)',
        };
      case 'RUNTIME ERROR':
      default:
        return {
          bg: 'bg-red-500/10 text-red-400 border-red-500/30',
          icon: ShieldAlert,
          text: 'Runtime / Sandbox Error',
        };
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 flex flex-col space-y-4 shadow-lg text-slate-200">
      {/* Console Header */}
      <div className="flex items-center justify-between pb-3 border-b border-slate-800">
        <div className="flex items-center gap-2">
          <Terminal className="w-4 h-4 text-blue-400" />
          <span className="text-sm font-bold text-slate-100 uppercase tracking-wider">
            Test Results & Console
          </span>
        </div>
        {result && (
          <div className="flex items-center gap-2 text-xs font-mono text-slate-400">
            <Clock className="w-3.5 h-3.5 text-slate-500" />
            <span>{result.total_execution_time_ms} ms</span>
          </div>
        )}
      </div>

      {/* Loading State */}
      {(isRunning || isSubmitting) && (
        <div className="py-8 flex flex-col items-center justify-center space-y-3">
          <div className="w-8 h-8 border-3 border-blue-500/20 border-t-blue-500 rounded-full animate-spin" />
          <p className="text-xs text-slate-400 font-mono">
            {isSubmitting
              ? 'Evaluating against all test cases (including hidden)...'
              : 'Executing test cases in Python sandbox...'}
          </p>
        </div>
      )}

      {/* Empty State before any run */}
      {!result && !isRunning && !isSubmitting && (
        <div className="py-8 text-center space-y-2">
          <Terminal className="w-8 h-8 text-slate-600 mx-auto" />
          <p className="text-xs text-slate-400">
            Write your solution and click <strong className="text-slate-200">Run Code</strong> to evaluate against sample test cases, or <strong className="text-slate-200">Submit</strong> to run against all test cases.
          </p>
          <div className="pt-2 flex items-center justify-center gap-2 text-xs text-slate-500">
            <span>Sample cases available: {sampleTestCases?.length || 0}</span>
          </div>
        </div>
      )}

      {/* Results View */}
      {result && !isRunning && !isSubmitting && (
        <div className="space-y-4">
          {/* Verdict Banner */}
          {(() => {
            const badge = getVerdictBadge(result.verdict);
            const Icon = badge.icon;
            return (
              <div
                className={`p-3.5 rounded-xl border flex items-center justify-between gap-3 ${badge.bg}`}
              >
                <div className="flex items-center gap-2.5">
                  <Icon className="w-5 h-5 shrink-0" />
                  <span className="text-sm font-bold tracking-tight">{badge.text}</span>
                </div>
                <div className="text-xs font-mono font-bold px-2.5 py-1 rounded-md bg-slate-900/60 border border-current/20">
                  {result.passed_cases} / {result.total_cases} Passed
                </div>
              </div>
            );
          })()}

          {/* Global Error Banner */}
          {result.global_error && (
            <div className="p-3.5 rounded-xl bg-red-950/40 border border-red-500/30 text-red-200 text-xs font-mono space-y-1 overflow-x-auto">
              <div className="font-bold flex items-center gap-1.5 text-red-400">
                <AlertTriangle className="w-4 h-4" /> Error Details:
              </div>
              <pre className="whitespace-pre-wrap leading-relaxed text-red-300">
                {result.global_error}
              </pre>
            </div>
          )}

          {/* Test Case Tab Selector */}
          {result.results && result.results.length > 0 && (
            <div className="space-y-3">
              <div className="flex items-center gap-2 overflow-x-auto pb-1 custom-scrollbar">
                {result.results.map((res: TestCaseResult, idx: number) => {
                  const isPassed = res.status === 'PASS';
                  const isSelected = selectedCaseIndex === idx;

                  return (
                    <button
                      key={idx}
                      onClick={() => setSelectedCaseIndex(idx)}
                      className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs font-medium border transition-all whitespace-nowrap ${
                        isSelected
                          ? 'bg-slate-800 text-white border-blue-500 shadow-sm'
                          : 'bg-slate-950/60 text-slate-400 hover:text-slate-200 border-slate-800'
                      }`}
                    >
                      <span
                        className={`w-2 h-2 rounded-full ${
                          isPassed ? 'bg-emerald-400' : 'bg-rose-500'
                        }`}
                      />
                      <span>Case {idx + 1}</span>
                      {res.is_hidden && (
                        <span className="text-[10px] text-slate-500 uppercase font-mono">
                          [Hidden]
                        </span>
                      )}
                    </button>
                  );
                })}
              </div>

              {/* Selected Test Case Inspection */}
              {(() => {
                const currentCase = result.results[selectedCaseIndex];
                if (!currentCase) return null;

                return (
                  <div className="rounded-xl bg-slate-950/70 border border-slate-800 p-4 space-y-3 text-xs font-mono">
                    <div className="flex items-center justify-between pb-2 border-b border-slate-800/80">
                      <span className="font-semibold text-slate-300 flex items-center gap-1.5">
                        <ChevronRight className="w-4 h-4 text-blue-400" />
                        Test Case {selectedCaseIndex + 1} Details
                      </span>
                      <span
                        className={`px-2 py-0.5 rounded font-bold ${
                          currentCase.status === 'PASS'
                            ? 'text-emerald-400 bg-emerald-500/10'
                            : 'text-rose-400 bg-rose-500/10'
                        }`}
                      >
                        {currentCase.status} ({currentCase.execution_time_ms} ms)
                      </span>
                    </div>

                    {/* Input */}
                    <div className="space-y-1">
                      <div className="text-slate-400 text-[11px] font-sans font-medium uppercase">
                        Input:
                      </div>
                      <div className="p-2.5 rounded-lg bg-slate-900 border border-slate-800/80 text-blue-300 break-all">
                        {currentCase.input_str}
                      </div>
                    </div>

                    {/* Expected Output */}
                    <div className="space-y-1">
                      <div className="text-slate-400 text-[11px] font-sans font-medium uppercase">
                        Expected Output:
                      </div>
                      <div className="p-2.5 rounded-lg bg-slate-900 border border-slate-800/80 text-emerald-300 break-all">
                        {currentCase.expected_str}
                      </div>
                    </div>

                    {/* Actual Output */}
                    <div className="space-y-1">
                      <div className="text-slate-400 text-[11px] font-sans font-medium uppercase">
                        Actual Output:
                      </div>
                      <div
                        className={`p-2.5 rounded-lg bg-slate-900 border break-all ${
                          currentCase.status === 'PASS'
                            ? 'border-emerald-500/20 text-emerald-300'
                            : 'border-rose-500/20 text-rose-300'
                        }`}
                      >
                        {currentCase.actual_str !== null && currentCase.actual_str !== undefined
                          ? currentCase.actual_str
                          : '[No return value]'}
                      </div>
                    </div>

                    {/* Stdout if any */}
                    {currentCase.stdout && (
                      <div className="space-y-1 pt-1">
                        <div className="text-slate-400 text-[11px] font-sans font-medium uppercase">
                          Stdout:
                        </div>
                        <div className="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-slate-300 whitespace-pre-wrap">
                          {currentCase.stdout}
                        </div>
                      </div>
                    )}

                    {/* Error message if any */}
                    {currentCase.error_message && (
                      <div className="space-y-1 pt-1">
                        <div className="text-rose-400 text-[11px] font-sans font-medium uppercase">
                          Runtime Error:
                        </div>
                        <div className="p-2.5 rounded-lg bg-red-950/30 border border-red-500/30 text-red-300 whitespace-pre-wrap">
                          {currentCase.error_message}
                        </div>
                      </div>
                    )}
                  </div>
                );
              })()}
            </div>
          )}
        </div>
      )}
    </div>
  );
};
