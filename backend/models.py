from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict, Union

class TestCase(BaseModel):
    id: int
    input_data: Dict[str, Any]
    expected_output: Any
    is_hidden: bool = False
    explanation: Optional[str] = None

class Problem(BaseModel):
    id: str
    title: str
    step_id: int = 1
    step_title: str = "Step 1: Learn the Basics"
    step: Optional[str] = None
    subtopic: str = "1.4: Know Basic Maths"
    difficulty: str = "Easy"  # "Easy", "Medium", "Hard"
    description: str
    input_format: str
    output_format: str
    constraints: List[str]
    function_name: str
    param_names: List[str]
    starter_code: Dict[str, str]
    test_cases: List[TestCase]
    comparison_mode: str = "exact"  # "exact", "unordered", "stdout", "float"
    order: int = 1
    tags: List[str] = Field(default_factory=list)
    hints: List[str] = Field(default_factory=list)
    examples: List[Dict[str, Any]] = Field(default_factory=list)
    explanation: Optional[Dict[str, Any]] = None

    def model_post_init(self, __context: Any) -> None:
        if not self.step:
            self.step = self.step_title

class StepSummary(BaseModel):
    step_id: int
    step_title: str
    total_problems: int
    subtopics: List[str]

class CustomProblemInput(BaseModel):
    title: str
    description: str
    function_name: str
    param_names: List[str]
    comparison_mode: str = "exact"
    test_cases: List[TestCase]

class RunRequest(BaseModel):
    problem_id: Optional[str] = None
    code: str
    language: str = "python"
    mode: str = "submit"  # "sample" or "submit"
    custom_problem: Optional[CustomProblemInput] = None

class TestCaseResult(BaseModel):
    test_case_id: int
    status: str  # "PASS", "FAIL", "ERROR", "TIMEOUT"
    is_hidden: bool
    input_str: str
    expected_str: str
    actual_str: Optional[str] = None
    stdout: Optional[str] = None
    execution_time_ms: float
    error_message: Optional[str] = None

class RunResponse(BaseModel):
    verdict: str  # "ALL TEST CASES PASSED", "SOME TEST CASES FAILED", "SYNTAX ERROR", "RUNTIME ERROR", "TIME LIMIT EXCEEDED"
    total_cases: int
    passed_cases: int
    failed_cases: int
    total_execution_time_ms: float
    results: List[TestCaseResult]
    global_error: Optional[str] = None
