import sys
import os
import json
import time
import io
import copy
import traceback
import math
from collections import Counter, defaultdict, deque
import heapq
import bisect
import itertools
import functools
import typing

# Custom safe builtins dictionary
SAFE_BUILTINS = dict(__builtins__ if isinstance(__builtins__, dict) else __builtins__.__dict__)
# Block harmful builtins from being used in the solution
for dangerous in ["open", "quit", "exit"]:
    if dangerous in SAFE_BUILTINS:
        del SAFE_BUILTINS[dangerous]

def clean_traceback_str(tb_exc: Exception) -> str:
    """Format traceback keeping only frames inside 'solution.py'."""
    lines = []
    tb = tb_exc.__traceback__
    user_frames = []
    while tb:
        frame = tb.tb_frame
        filename = frame.f_code.co_filename
        if "solution.py" in filename or "<string>" in filename:
            user_frames.append(f'  File "solution.py", line {tb.tb_lineno}, in {frame.f_code.co_name}')
        tb = tb.tb_next

    err_name = type(tb_exc).__name__
    err_msg = str(tb_exc)
    if user_frames:
        return "Traceback (most recent call last):\n" + "\n".join(user_frames) + f"\n{err_name}: {err_msg}"
    return f"{err_name}: {err_msg}"

def normalize_compare(actual, expected, mode="exact") -> bool:
    if actual is None and expected is not None:
        return False
    
    # Handle tuple vs list
    if isinstance(actual, tuple) and isinstance(expected, list):
        actual = list(actual)
    if isinstance(actual, list) and isinstance(expected, tuple):
        expected = list(expected)

    # Boolean vs int distinction: in Python, True == 1 is True, but for DSA True must match True
    if isinstance(expected, bool) or isinstance(actual, bool):
        if type(actual) is not type(expected):
            return False
        return actual == expected

    if mode == "unordered":
        if isinstance(actual, list) and isinstance(expected, list):
            if len(actual) != len(expected):
                return False
            try:
                return sorted(actual) == sorted(expected)
            except TypeError:
                return Counter(actual) == Counter(expected)

    if mode == "float":
        try:
            return math.isclose(float(actual), float(expected), rel_tol=1e-5, abs_tol=1e-5)
        except (ValueError, TypeError):
            return False

    # Default exact comparison
    return actual == expected

def format_val(val) -> str:
    if isinstance(val, str):
        return f'"{val}"'
    return json.dumps(val, default=str)

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No payload file provided"}))
        sys.exit(1)

    payload_path = sys.argv[1]
    with open(payload_path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    user_code = payload["code"]
    function_name = payload["function_name"]
    comparison_mode = payload.get("comparison_mode", "exact")
    test_cases = payload["test_cases"]

    # Global namespace for execution
    user_namespace = {
        "__builtins__": SAFE_BUILTINS,
        "math": math,
        "collections": collections if "collections" in globals() else None,
        "Counter": Counter,
        "defaultdict": defaultdict,
        "deque": deque,
        "heapq": heapq,
        "bisect": bisect,
        "itertools": itertools,
        "functools": functools,
        "typing": typing,
        "List": typing.List,
        "Dict": typing.Dict,
        "Set": typing.Set,
        "Tuple": typing.Tuple,
        "Optional": typing.Optional,
    }

    # 1. Compile user code
    try:
        compiled = compile(user_code, "solution.py", "exec")
    except SyntaxError as e:
        err_msg = f"SyntaxError: {e.msg} (line {e.lineno})"
        if e.text:
            err_msg += f"\n  {e.text.strip()}\n  {' ' * max(0, (e.offset or 1) - 1)}^"
        output = {
            "verdict": "SYNTAX ERROR",
            "global_error": err_msg,
            "total_cases": len(test_cases),
            "passed_cases": 0,
            "failed_cases": 0,
            "total_execution_time_ms": 0.0,
            "results": []
        }
        print(json.dumps(output))
        return

    # 2. Execute user code definitions
    try:
        exec(compiled, user_namespace)
    except Exception as e:
        tb_str = clean_traceback_str(e)
        output = {
            "verdict": "RUNTIME ERROR",
            "global_error": f"Error during script initialization:\n{tb_str}",
            "total_cases": len(test_cases),
            "passed_cases": 0,
            "failed_cases": 0,
            "total_execution_time_ms": 0.0,
            "results": []
        }
        print(json.dumps(output))
        return

    # 3. Locate entrypoint
    entry_callable = None
    if "Solution" in user_namespace and isinstance(user_namespace["Solution"], type):
        try:
            sol_instance = user_namespace["Solution"]()
            if hasattr(sol_instance, function_name):
                entry_callable = getattr(sol_instance, function_name)
            else:
                # Fallback: check if Solution has only one custom method
                methods = [m for m in dir(sol_instance) if not m.startswith("_") and callable(getattr(sol_instance, m))]
                if len(methods) == 1:
                    entry_callable = getattr(sol_instance, methods[0])
        except Exception as e:
            tb_str = clean_traceback_str(e)
            output = {
                "verdict": "RUNTIME ERROR",
                "global_error": f"Failed to instantiate Solution class:\n{tb_str}",
                "total_cases": len(test_cases),
                "passed_cases": 0,
                "failed_cases": 0,
                "total_execution_time_ms": 0.0,
                "results": []
            }
            print(json.dumps(output))
            return

    if not entry_callable:
        if function_name in user_namespace and callable(user_namespace[function_name]):
            entry_callable = user_namespace[function_name]
        elif "solve" in user_namespace and callable(user_namespace["solve"]):
            entry_callable = user_namespace["solve"]

    if not entry_callable:
        output = {
            "verdict": "RUNTIME ERROR",
            "global_error": f"Could not find function '{function_name}' or class Solution with method '{function_name}'. Please ensure your function name matches the problem requirement.",
            "total_cases": len(test_cases),
            "passed_cases": 0,
            "failed_cases": 0,
            "total_execution_time_ms": 0.0,
            "results": []
        }
        print(json.dumps(output))
        return

    # 4. Run test cases
    results = []
    passed_count = 0
    failed_count = 0
    total_time_ms = 0.0
    crashed = False
    first_crash_error = None

    for tc in test_cases:
        tc_id = tc["id"]
        is_hidden = tc.get("is_hidden", False)
        input_data = tc["input_data"]
        expected = tc["expected_output"]

        # Render input string cleanly
        if isinstance(input_data, dict):
            input_str = ", ".join(f"{k} = {format_val(v)}" for k, v in input_data.items())
        else:
            input_str = str(input_data)

        expected_str = format_val(expected)

        if crashed:
            # Skip subsequent cases if code crashed with runtime error
            continue

        # Prepare deep copies of input so mutations don't leak
        input_copy = copy.deepcopy(input_data)

        # Redirect stdout
        stdout_buf = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = stdout_buf

        start_time = time.perf_counter()
        actual = None
        error_msg = None
        status = "FAIL"

        try:
            if isinstance(input_copy, dict):
                try:
                    actual = entry_callable(**input_copy)
                except TypeError:
                    # In case user named parameters differently: call positionally
                    actual = entry_callable(*input_copy.values())
            else:
                actual = entry_callable(input_copy)

            # Check if function modified first argument in-place and returned None
            if actual is None and isinstance(input_copy, dict):
                first_key = next(iter(input_copy))
                if isinstance(input_copy[first_key], list) and isinstance(expected, list):
                    actual = input_copy[first_key]

        except Exception as e:
            error_msg = clean_traceback_str(e)
            status = "ERROR"
            crashed = True
            first_crash_error = f"Runtime Error on test case {tc_id}:\n{error_msg}"
        finally:
            end_time = time.perf_counter()
            sys.stdout = old_stdout

        elapsed_ms = round((end_time - start_time) * 1000, 2)
        total_time_ms += elapsed_ms
        captured_stdout = stdout_buf.getvalue()

        if status != "ERROR":
            if normalize_compare(actual, expected, mode=comparison_mode):
                status = "PASS"
                passed_count += 1
            else:
                status = "FAIL"
                failed_count += 1
        else:
            failed_count += 1

        actual_str = format_val(actual) if actual is not None else None

        results.append({
            "test_case_id": tc_id,
            "status": status,
            "is_hidden": is_hidden,
            "input_str": input_str,
            "expected_str": expected_str,
            "actual_str": actual_str,
            "stdout": captured_stdout if captured_stdout else None,
            "execution_time_ms": elapsed_ms,
            "error_message": error_msg
        })

    total_time_ms = round(total_time_ms, 2)

    if crashed:
        verdict = "RUNTIME ERROR"
    elif failed_count == 0 and passed_count == len(test_cases):
        verdict = "ALL TEST CASES PASSED"
    else:
        verdict = "SOME TEST CASES FAILED"

    output = {
        "verdict": verdict,
        "total_cases": len(test_cases),
        "passed_cases": passed_count,
        "failed_cases": failed_count,
        "total_execution_time_ms": total_time_ms,
        "results": results,
        "global_error": first_crash_error
    }
    print(json.dumps(output))

if __name__ == "__main__":
    main()
