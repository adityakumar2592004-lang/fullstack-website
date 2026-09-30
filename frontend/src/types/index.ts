export type Difficulty = 'Easy' | 'Medium' | 'Hard';
export type ProblemStatus = 'Not Started' | 'Attempted' | 'Solved';

export interface Example {
  input: string;
  output: string;
  explanation?: string;
}

export interface Explanation {
  intuition: string;
  brute_force: string;
  better_approach?: string;
  optimal_approach: string;
  dry_run: string;
  time_complexity: string;
  space_complexity: string;
  common_mistakes: string;
  interview_questions: string;
}

export interface TestCase {
  id: number;
  input_data: Record<string, any>;
  expected_output: any;
  is_hidden: boolean;
  explanation?: string;
}

export interface Problem {
  id: string;
  title: string;
  step_id: number;
  step_title: string;
  subtopic: string;
  difficulty: Difficulty;
  description: string;
  input_format: string;
  output_format: string;
  constraints: string[];
  function_name: string;
  param_names: string[];
  starter_code: Record<string, string>;
  test_cases: TestCase[];
  comparison_mode?: string;
  order: number;
  tags: string[];
  hints: string[];
  examples: Example[];
  explanation: Explanation;
}

export interface StepSummary {
  step_id: number;
  step_title: string;
  total_problems: number;
  subtopics: string[];
}

export interface TopicInfo {
  id: string;
  title: string;
  description: string;
}

export interface ModuleInfo {
  id: number;
  title: string;
  description: string;
  isComingSoon: boolean;
  topics: TopicInfo[];
}

export interface TestCaseResult {
  test_case_id: number;
  status: 'PASS' | 'FAIL' | 'ERROR' | 'TIMEOUT';
  is_hidden: boolean;
  input_str: string;
  expected_str: string;
  actual_str?: string | null;
  stdout?: string | null;
  execution_time_ms: number;
  error_message?: string | null;
}

export interface RunResponse {
  verdict: 'ALL TEST CASES PASSED' | 'SOME TEST CASES FAILED' | 'SYNTAX ERROR' | 'RUNTIME ERROR' | 'TIME LIMIT EXCEEDED';
  total_cases: number;
  passed_cases: number;
  failed_cases: number;
  total_execution_time_ms: number;
  results: TestCaseResult[];
  global_error?: string | null;
}

export interface UserNote {
  problemId: string;
  problemTitle: string;
  content: string;
  updatedAt: string;
}

export type SupportedLanguage = 'python' | 'cpp' | 'java' | 'javascript';
