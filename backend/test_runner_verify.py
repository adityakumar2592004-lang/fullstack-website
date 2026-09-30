import sys
from problems import get_problem_by_id, PROBLEMS_DB, ALL_STEPS_CATALOG
from models import RunRequest
from main import health_check, list_steps, list_problems, get_problem, run_code

def main():
    print(f"Total problems in DB: {len(PROBLEMS_DB)}")
    print(f"Total roadmap steps: {len(ALL_STEPS_CATALOG)}")
    assert len(PROBLEMS_DB) == 85, f"Expected 85 problems, got {len(PROBLEMS_DB)}"
    assert len(ALL_STEPS_CATALOG) == 20, f"Expected 20 steps, got {len(ALL_STEPS_CATALOG)}"

    # 1. Health check
    health = health_check()
    print("Health check response:", health)
    assert health["status"] == "ok"
    assert health["total_problems"] == 85

    # 2. Steps summary
    steps = list_steps()
    print(f"Steps count: {len(steps)}")
    assert len(steps) == 20

    # 3. List problems
    all_probs = list_problems()
    print(f"Total problems returned by API: {len(all_probs)}")
    assert len(all_probs) == 85
    # Verify hidden test cases are sanitized in listing
    first_prob = all_probs[0]
    hidden_tc = [tc for tc in first_prob.test_cases if tc.is_hidden]
    for h in hidden_tc:
        assert h.input_data == {}, "Client should not receive hidden input_data"
        assert h.expected_output is None, "Client should not receive hidden expected_output"

    # 4. Get individual problem
    prob = get_problem('count-digits')
    print(f"Problem details: {prob.title} | {prob.difficulty} | {prob.subtopic}")
    assert prob.id == 'count-digits'
    assert len(prob.test_cases) == 6
    assert len(prob.hints) >= 2
    assert prob.explanation and prob.explanation.get("optimal_approach") != ""

    # 5. Execute code via run_code endpoint (mode='run')
    code_correct = """class Solution:
    def countDigits(self, n: int) -> int:
        return len(str(abs(n)))
"""
    req_run = RunRequest(
        problem_id="count-digits",
        code=code_correct,
        mode="run"
    )
    res_run = run_code(req_run)
    print("Endpoint run result:", res_run.verdict, f"Passed: {res_run.passed_cases}/{res_run.total_cases}")
    assert res_run.verdict == "ALL TEST CASES PASSED"
    assert res_run.total_cases == 3  # Only sample test cases for mode='run'

    # 6. Execute code via run_code endpoint (mode='submit')
    req_submit = RunRequest(
        problem_id="count-digits",
        code=code_correct,
        mode="submit"
    )
    res_submit = run_code(req_submit)
    print("Endpoint submit result:", res_submit.verdict, f"Passed: {res_submit.passed_cases}/{res_submit.total_cases}")
    assert res_submit.verdict == "ALL TEST CASES PASSED"
    assert res_submit.total_cases == 6  # All 6 test cases

    # Verify hidden test case masking in result
    hidden_results = [r for r in res_submit.results if r.is_hidden]
    assert len(hidden_results) == 3
    for hr in hidden_results:
        assert hr.input_str == "[Hidden Test Case - Passed]", f"Expected masked string, got {hr.input_str}"
        assert hr.expected_str == "[Hidden]", f"Expected masked string, got {hr.expected_str}"
        assert hr.actual_str == "[Match]", f"Expected masked string, got {hr.actual_str}"
    print("Hidden test case masking on submit verified!")

    # 7. Wrong answer submit test
    code_wa = """class Solution:
    def countDigits(self, n: int) -> int:
        return 0
"""
    req_wa = RunRequest(
        problem_id="count-digits",
        code=code_wa,
        mode="submit"
    )
    res_wa = run_code(req_wa)
    print("Endpoint wrong answer result:", res_wa.verdict, f"Passed: {res_wa.passed_cases}/{res_wa.total_cases}")
    assert res_wa.verdict == "SOME TEST CASES FAILED"
    hidden_wa = [r for r in res_wa.results if r.is_hidden]
    for hr in hidden_wa:
        assert hr.input_str == "[Hidden Test Case - Failed]"
        assert hr.expected_str == "[Hidden]"
        assert hr.actual_str == "[Output Hidden]"
    print("Hidden test case masking on failed submit verified!")

    # 8. Security block test
    code_sec = "import os\nprint(os.system('dir'))"
    req_sec = RunRequest(
        problem_id="count-digits",
        code=code_sec,
        mode="run"
    )
    res_sec = run_code(req_sec)
    print("Security block verdict:", res_sec.verdict, "Error:", res_sec.global_error)
    assert res_sec.verdict == "RUNTIME ERROR"
    assert "Security Violation" in (res_sec.global_error or "")

    print("\n==========================================")
    print(">>> ALL BACKEND API TESTS PASSED 100%! <<<")
    print("==========================================")

if __name__ == "__main__":
    main()
