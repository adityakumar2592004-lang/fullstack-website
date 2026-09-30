import type { Problem, StepSummary, RunResponse, SupportedLanguage } from '../types';

const API_BASE = '/api';

export async function fetchHealth(): Promise<{ status: string; message: string; total_problems: number }> {
  const res = await fetch(`${API_BASE}/health`);
  if (!res.ok) {
    throw new Error(`Health check failed with status ${res.status}`);
  }
  return res.json();
}

export async function fetchSteps(): Promise<StepSummary[]> {
  const res = await fetch(`${API_BASE}/steps`);
  if (!res.ok) {
    throw new Error(`Failed to fetch steps: ${res.statusText}`);
  }
  return res.json();
}

export async function fetchProblems(stepId?: number): Promise<Problem[]> {
  const url = stepId ? `${API_BASE}/problems?step_id=${stepId}` : `${API_BASE}/problems`;
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Failed to fetch problems: ${res.statusText}`);
  }
  return res.json();
}

export async function fetchProblemById(problemId: string): Promise<Problem> {
  const res = await fetch(`${API_BASE}/problems/${problemId}`);
  if (!res.ok) {
    throw new Error(`Problem not found: ${problemId}`);
  }
  return res.json();
}

export async function executeCode(payload: {
  problem_id: string;
  code: string;
  language?: SupportedLanguage;
  mode?: 'sample' | 'submit';
}): Promise<RunResponse> {
  const res = await fetch(`${API_BASE}/run`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      problem_id: payload.problem_id,
      code: payload.code,
      language: payload.language || 'python',
      mode: payload.mode || 'submit',
    }),
  });

  if (!res.ok) {
    const errorText = await res.text();
    try {
      const parsed = JSON.parse(errorText);
      throw new Error(parsed.detail || parsed.message || 'Execution error');
    } catch {
      throw new Error(errorText || `Execution failed with HTTP status ${res.status}`);
    }
  }

  return res.json();
}
