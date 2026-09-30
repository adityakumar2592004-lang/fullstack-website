import sys
import os
import json
import subprocess
import tempfile
from typing import List, Dict, Any, Optional
from models import TestCase, RunResponse, TestCaseResult, Problem
from security import validate_code_security

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
EXECUTOR_SCRIPT = os.path.join(CURRENT_DIR, "executor.py")

def execute_code(
    code: str,
    function_name: str,
    test_cases: List[TestCase],
    comparison_mode: str = "exact",
    mode: str = "submit",
    timeout_sec: float = 5.0
) -> RunResponse:
    # 1. Security Check
    is_safe, sec_error = validate_code_security(code)
    if not is_safe:
        return RunResponse(
            verdict="RUNTIME ERROR",
            total_cases=len(test_cases),
            passed_cases=0,
            failed_cases=len(test_cases),
            total_execution_time_ms=0.0,
            results=[],
            global_error=sec_error
        )

    # 2. Filter test cases based on mode
    cases_to_run = [tc for tc in test_cases if (mode == "submit" or not tc.is_hidden)]
    if not cases_to_run:
        cases_to_run = test_cases

    # 3. Serialize payload
    payload = {
        "code": code,
        "function_name": function_name,
        "comparison_mode": comparison_mode,
        "test_cases": [tc.model_dump() for tc in cases_to_run]
    }

    # 4. Create isolated temp directory for execution
    with tempfile.TemporaryDirectory() as temp_dir:
        payload_file = os.path.join(temp_dir, "payload.json")
        with open(payload_file, "w", encoding="utf-8") as f:
            json.dump(payload, f)

        # Prepare isolated environment
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["PYTHONUNBUFFERED"] = "1"

        try:
            proc = subprocess.Popen(
                [sys.executable, EXECUTOR_SCRIPT, payload_file],
                cwd=temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env,
                text=True,
                encoding="utf-8"
            )

            try:
                stdout, stderr = proc.communicate(timeout=timeout_sec)
            except subprocess.TimeoutExpired:
                proc.kill()
                stdout, stderr = proc.communicate()
                return RunResponse(
                    verdict="TIME LIMIT EXCEEDED",
                    total_cases=len(cases_to_run),
                    passed_cases=0,
                    failed_cases=len(cases_to_run),
                    total_execution_time_ms=round(timeout_sec * 1000, 2),
                    results=[],
                    global_error="Time Limit Exceeded: Execution took longer than 5.0s. Please check for infinite loops or inefficient algorithms (e.g. O(N^2) instead of O(N))."
                )

            if proc.returncode != 0 and not stdout:
                return RunResponse(
                    verdict="RUNTIME ERROR",
                    total_cases=len(cases_to_run),
                    passed_cases=0,
                    failed_cases=len(cases_to_run),
                    total_execution_time_ms=0.0,
                    results=[],
                    global_error=f"Process exited abnormally (code {proc.returncode}):\n{stderr}"
                )

            # Parse JSON output from executor
            try:
                data = json.loads(stdout.strip())
                return RunResponse(**data)
            except json.JSONDecodeError:
                return RunResponse(
                    verdict="RUNTIME ERROR",
                    total_cases=len(cases_to_run),
                    passed_cases=0,
                    failed_cases=len(cases_to_run),
                    total_execution_time_ms=0.0,
                    results=[],
                    global_error=f"Execution failed to produce valid result.\nStdout: {stdout}\nStderr: {stderr}"
                )

        except Exception as e:
            return RunResponse(
                verdict="RUNTIME ERROR",
                total_cases=len(cases_to_run),
                passed_cases=0,
                failed_cases=len(cases_to_run),
                total_execution_time_ms=0.0,
                results=[],
                global_error=f"Internal Runner Exception: {str(e)}"
            )
