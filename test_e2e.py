import urllib.request
import json

def test_api(name, payload):
    req = urllib.request.Request(
        'http://localhost:5173/api/run',
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print(f"=== {name} ===")
        print("Verdict:", data['verdict'])
        print(f"Cases: {data['passed_cases']} / {data['total_cases']} passed, {data['failed_cases']} failed")
        print(f"Execution time: {data['total_execution_time_ms']} ms")
        if data.get('global_error'):
            print("Global Error:\n", data['global_error'])
        if data['results']:
            print("Test cases summary:")
            for r in data['results']:
                hidden_tag = "[HIDDEN]" if r['is_hidden'] else "[VISIBLE]"
                print(f"  Case {r['test_case_id']} {hidden_tag}: {r['status']} | In: {r['input_str']} | Exp: {r['expected_str']} | Act: {r['actual_str']}")
        print()

# 1. Sample Run (visible only)
test_api('1. Sample Run (Count Digits Correct)', {
    'problem_id': 'count-digits',
    'code': 'class Solution:\n    def countDigits(self, n: int) -> int:\n        return len(str(n))\n',
    'mode': 'sample'
})

# 2. Submit Run (visible + hidden)
test_api('2. Submit Run (Count Digits Correct)', {
    'problem_id': 'count-digits',
    'code': 'class Solution:\n    def countDigits(self, n: int) -> int:\n        return len(str(n))\n',
    'mode': 'submit'
})

# 3. Submit Run with Wrong Answer
test_api('3. Submit Run (Count Digits Wrong Answer)', {
    'problem_id': 'count-digits',
    'code': 'class Solution:\n    def countDigits(self, n: int) -> int:\n        return 999\n',
    'mode': 'submit'
})

# 4. Syntax Error
test_api('4. Syntax Error Detection', {
    'problem_id': 'count-digits',
    'code': 'class Solution:\n    def countDigits(self, n: int) -> int:\n        return (\n',
    'mode': 'submit'
})

# 5. Security Policy Sandbox Test
test_api('5. Security Sandbox Block', {
    'problem_id': 'count-digits',
    'code': 'import os\nclass Solution:\n    def countDigits(self, n: int) -> int:\n        return 1\n',
    'mode': 'submit'
})
