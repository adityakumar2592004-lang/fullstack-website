import type { Problem } from '../types';
import rawData from './problemsData.json';

export const INITIAL_PROBLEMS: Problem[] = rawData as unknown as Problem[];

export const PROBLEM_MAP: Record<string, Problem> = INITIAL_PROBLEMS.reduce((acc, p) => {
  acc[p.id] = p;
  return acc;
}, {} as Record<string, Problem>);
