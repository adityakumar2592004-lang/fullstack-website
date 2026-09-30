from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import copy

from models import Problem, RunRequest, RunResponse, TestCase, StepSummary
from problems import PROBLEMS_DB, get_problem_by_id, get_steps_summary, ALL_STEPS_CATALOG
from runner import execute_code

app = FastAPI(
    title="Striver A2Z DSA Compiler & Tester API",
    description="Dedicated coding tester specifically for practicing Striver's A2Z DSA Sheet questions.",
    version="1.0.0"
)

# Enable CORS for Vite frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def sanitize_problem_for_client(problem: Problem) -> Problem:
    """Masks hidden test cases so the client browser never gets preloaded hidden test cases."""
    p_copy = copy.deepcopy(problem)
    sanitized_cases = []
    for tc in p_copy.test_cases:
        if tc.is_hidden:
            # Mask hidden inputs and outputs from client bundle
            sanitized_cases.append(TestCase(
                id=tc.id,
                input_data={},
                expected_output=None,
                is_hidden=True,
                explanation="Hidden Test Case"
            ))
        else:
            sanitized_cases.append(tc)
    p_copy.test_cases = sanitized_cases
    p_copy.step = p_copy.step_title
    return p_copy

@app.get("/api/health")
def health_check():
    return {
        "status": "ok", 
        "message": "DSA Compiler backend is active.",
        "total_problems": len(PROBLEMS_DB)
    }

@app.get("/api/steps", response_model=List[StepSummary])
@app.get("/api/modules", response_model=List[StepSummary])
def list_steps():
    """Return all DSA Roadmap Steps/Modules with problem count and subtopics."""
    return get_steps_summary()

@app.get("/api/problems")
def list_problems(step_id: Optional[int] = None):
    """Return all problems with hidden test cases masked, optionally filtered by step."""
    if step_id is not None:
        filtered = [p for p in PROBLEMS_DB if p.step_id == step_id]
        return [sanitize_problem_for_client(p) for p in filtered]
    return [sanitize_problem_for_client(p) for p in PROBLEMS_DB]

@app.get("/api/problems/{problem_id}")
def get_problem(problem_id: str):
    p = get_problem_by_id(problem_id)
    if not p:
        raise HTTPException(status_code=404, detail="Problem not found")
    return sanitize_problem_for_client(p)

@app.post("/api/run", response_model=RunResponse)
def run_code(req: RunRequest):
    test_cases: List[TestCase] = []
    func_name: str = ""
    comp_mode: str = "exact"

    if req.custom_problem:
        func_name = req.custom_problem.function_name
        comp_mode = req.custom_problem.comparison_mode
        test_cases = req.custom_problem.test_cases
    elif req.problem_id:
        p = get_problem_by_id(req.problem_id)
        if not p:
            raise HTTPException(status_code=404, detail="Selected problem not found")
        func_name = p.function_name
        comp_mode = p.comparison_mode
        test_cases = p.test_cases
    else:
        raise HTTPException(status_code=400, detail="Must provide problem_id or custom_problem")

    if not test_cases:
        raise HTTPException(status_code=400, detail="No test cases found for this problem")

    # Run the code
    response = execute_code(
        code=req.code,
        function_name=func_name,
        test_cases=test_cases,
        comparison_mode=comp_mode,
        mode=req.mode
    )

    # Protect hidden test cases without revealing hidden data
    for res in response.results:
        if res.is_hidden:
            if res.status == "PASS":
                res.input_str = "[Hidden Test Case - Passed]"
                res.expected_str = "[Hidden]"
                res.actual_str = "[Match]"
            else:
                res.input_str = "[Hidden Test Case - Failed]"
                res.expected_str = "[Hidden]"
                res.actual_str = "[Output Hidden]"

    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
