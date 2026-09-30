from models import Problem, TestCase

MODULE_1_PROBLEMS = [
    Problem(
        id="count-digits",
        title="Count Digits in an Integer",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.4: Know Basic Maths",
        difficulty="Easy",
        description="Given an integer n, calculate and return the total number of digits present in n.",
        input_format="A single positive or zero integer n.",
        output_format="Return an integer representing the count of digits.",
        constraints=["0 <= n <= 10^9"],
        function_name="countDigits",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def countDigits(self, n: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int countDigits(int n) {\n        // Write your code here\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int countDigits(int n) {\n        // Write your code here\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    /**\n     * @param {number} n\n     * @return {number}\n     */\n    countDigits(n) {\n        // Write your code here\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 12345}, expected_output=5, is_hidden=False, explanation="12345 has 5 digits."),
            TestCase(id=2, input_data={"n": 7}, expected_output=1, is_hidden=False, explanation="7 has 1 digit."),
            TestCase(id=3, input_data={"n": 0}, expected_output=1, is_hidden=False, explanation="0 has 1 digit."),
            TestCase(id=4, input_data={"n": 1000000000}, expected_output=10, is_hidden=True),
            TestCase(id=5, input_data={"n": 9999}, expected_output=4, is_hidden=True),
            TestCase(id=6, input_data={"n": 405060}, expected_output=6, is_hidden=True),
        ],
        comparison_mode="exact",
        order=1,
        tags=["Maths", "Basic Coding", "Numbers"],
        hints=[
            "Think about how dividing a number by 10 repeatedly truncates its last digit.",
            "Can you use a loop that divides n by 10 until n becomes 0, counting each division step?",
            "Remember the special edge case: when n is 0, the digit count is 1, not 0."
        ],
        examples=[
            {"input": "n = 12345", "output": "5", "explanation": "12345 consists of five digits: 1, 2, 3, 4, 5."},
            {"input": "n = 9", "output": "1", "explanation": "9 is a single digit number."}
        ],
        explanation={
            "intuition": "Each decimal place represents a power of 10. Successively stripping the least significant digit by integer division by 10 gives us the total count.",
            "brute_force": "Convert the integer to a string and return the length of the string: len(str(n)).",
            "optimal_approach": "While n > 0, increment count and update n = n // 10. Handle n == 0 explicitly as a base case returning 1.",
            "dry_run": "For n = 123:\n1. count = 0, n = 123\n2. n > 0 -> count = 1, n = 12\n3. n > 0 -> count = 2, n = 1\n4. n > 0 -> count = 3, n = 0\n5. n == 0 -> loop ends, return 3.",
            "time_complexity": "O(log10(N)) - The number of iterations equals the number of digits in N.",
            "space_complexity": "O(1) - Only a few primitive integer counters are used.",
            "common_mistakes": "Forgetting that 0 has 1 digit, or using float division instead of integer floor division.",
            "interview_questions": "Can you do this in O(1) time using logarithms? (Yes, int(math.log10(n)) + 1 for n > 0)."
        }
    ),
    Problem(
        id="reverse-number",
        title="Reverse an Integer",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.4: Know Basic Maths",
        difficulty="Easy",
        description="Given a non-negative integer n, reverse its digits and return the resulting integer without leading zeroes.",
        input_format="A single non-negative integer n.",
        output_format="Return the reversed integer.",
        constraints=["0 <= n <= 10^9"],
        function_name="reverseNumber",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def reverseNumber(self, n: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int reverseNumber(int n) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int reverseNumber(int n) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    reverseNumber(n) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 1234}, expected_output=4321, is_hidden=False),
            TestCase(id=2, input_data={"n": 500}, expected_output=5, is_hidden=False),
            TestCase(id=3, input_data={"n": 0}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"n": 10002}, expected_output=20001, is_hidden=True),
            TestCase(id=5, input_data={"n": 987654321}, expected_output=123456789, is_hidden=True),
        ],
        comparison_mode="exact",
        order=2,
        tags=["Maths", "Modulo", "Numbers"],
        hints=[
            "How do you extract the last digit? Using the modulo operator: n % 10.",
            "How do you push a digit to the right of an existing accumulated number? multiply by 10 and add the digit.",
            "Maintain reversed_num = reversed_num * 10 + (n % 10), then n = n // 10."
        ],
        examples=[
            {"input": "n = 1234", "output": "4321", "explanation": "Reversing 1234 gives 4321."},
            {"input": "n = 500", "output": "5", "explanation": "Reversing 500 gives 005, which is 5."}
        ],
        explanation={
            "intuition": "Extract the last digit using modulo 10 and append it to our accumulating result multiplied by 10.",
            "brute_force": "Convert integer to string, reverse the string, and parse back to integer: int(str(n)[::-1]).",
            "optimal_approach": "Iterate while n > 0: rev = rev * 10 + (n % 10); n = n // 10. Return rev.",
            "dry_run": "n = 123, rev = 0:\n1. digit = 3, rev = 0*10 + 3 = 3, n = 12\n2. digit = 2, rev = 3*10 + 2 = 32, n = 1\n3. digit = 1, rev = 32*10 + 1 = 321, n = 0\nReturn 321.",
            "time_complexity": "O(log10(N)) - Proportional to number of digits.",
            "space_complexity": "O(1) - Constant extra space.",
            "common_mistakes": "Overflowing 32-bit signed integer limits in languages like C++/Java if not checking boundaries.",
            "interview_questions": "How would you handle negative numbers? (Preserve the negative sign, reverse abs(n), and reapply)."
        }
    ),
    Problem(
        id="palindrome-number",
        title="Check if Number is Palindrome",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.4: Know Basic Maths",
        difficulty="Easy",
        description="Determine whether a given non-negative integer n is a palindrome. A number is a palindrome when it reads the same backwards as forwards.",
        input_format="A single non-negative integer n.",
        output_format="Return True if n is a palindrome, otherwise False.",
        constraints=["0 <= n <= 10^9"],
        function_name="isPalindrome",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def isPalindrome(self, n: int) -> bool:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    bool isPalindrome(int n) {\n        return false;\n    }\n};",
            "java": "class Solution {\n    public boolean isPalindrome(int n) {\n        return false;\n    }\n}",
            "javascript": "class Solution {\n    isPalindrome(n) {\n        return false;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 121}, expected_output=True, is_hidden=False),
            TestCase(id=2, input_data={"n": 123}, expected_output=False, is_hidden=False),
            TestCase(id=3, input_data={"n": 0}, expected_output=True, is_hidden=False),
            TestCase(id=4, input_data={"n": 1221}, expected_output=True, is_hidden=True),
            TestCase(id=5, input_data={"n": 1000021}, expected_output=False, is_hidden=True),
        ],
        comparison_mode="exact",
        order=3,
        tags=["Maths", "Palindrome"],
        hints=[
            "If a number is equal to its reversed representation, it is a palindrome.",
            "Keep a copy of original n, compute reversed number, and compare original == reversed.",
            "Single digit numbers (0-9) are always palindromes."
        ],
        examples=[
            {"input": "n = 121", "output": "True", "explanation": "121 read backwards is 121, so it is a palindrome."},
            {"input": "n = 123", "output": "False", "explanation": "123 read backwards is 321, which does not equal 123."}
        ],
        explanation={
            "intuition": "A palindrome reads identical in forward and backward sequence. Reversing the digits and comparing against the initial value answers this directly.",
            "brute_force": "Convert number to string and check if s == s[::-1].",
            "optimal_approach": "Store original = n, reverse digits mathematically into rev, then return original == rev.",
            "dry_run": "n = 121, original = 121, rev = 121. Since original == rev, return True.",
            "time_complexity": "O(log10(N))",
            "space_complexity": "O(1)",
            "common_mistakes": "Modifying n directly without saving its initial value in a temporary variable.",
            "interview_questions": "Can you check palindrome by only reversing half of the number to prevent potential 32-bit integer overflow?"
        }
    ),
    Problem(
        id="armstrong-number",
        title="Armstrong Number Verification",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.4: Know Basic Maths",
        difficulty="Easy",
        description="An Armstrong number (or narcissistic number) is a number that is the sum of its own digits each raised to the power of the number of digits. Determine if integer n is an Armstrong number.",
        input_format="A single positive integer n.",
        output_format="Return True if n is an Armstrong number, else False.",
        constraints=["1 <= n <= 10^9"],
        function_name="isArmstrong",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def isArmstrong(self, n: int) -> bool:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    bool isArmstrong(int n) {\n        return false;\n    }\n};",
            "java": "class Solution {\n    public boolean isArmstrong(int n) {\n        return false;\n    }\n}",
            "javascript": "class Solution {\n    isArmstrong(n) {\n        return false;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 153}, expected_output=True, is_hidden=False, explanation="1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153."),
            TestCase(id=2, input_data={"n": 370}, expected_output=True, is_hidden=False),
            TestCase(id=3, input_data={"n": 123}, expected_output=False, is_hidden=False),
            TestCase(id=4, input_data={"n": 1634}, expected_output=True, is_hidden=True, explanation="1^4 + 6^4 + 3^4 + 4^4 = 1634."),
            TestCase(id=5, input_data={"n": 9474}, expected_output=True, is_hidden=True),
        ],
        comparison_mode="exact",
        order=4,
        tags=["Maths", "Numbers"],
        hints=[
            "First find the number of digits k in n.",
            "Then iterate through each digit d and add d^k to an accumulator sum.",
            "Compare sum with the initial value of n."
        ],
        examples=[
            {"input": "n = 153", "output": "True", "explanation": "Number of digits = 3. 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153."},
            {"input": "n = 120", "output": "False", "explanation": "1^3 + 2^3 + 0^3 = 9 != 120."}
        ],
        explanation={
            "intuition": "Count total digits k. Then extract every digit, raise to power k, accumulate, and verify equality with n.",
            "brute_force": "Calculate k = len(str(n)), iterate through string chars, raise int(char)**k, sum, and compare.",
            "optimal_approach": "Mathematically count digits with temp = n; while temp: k += 1; temp //= 10. Then repeat modulo extraction to compute sum of powers.",
            "dry_run": "For 153: k = 3. digits are 3, 5, 1. Sum = 3^3 (27) + 5^3 (125) + 1^3 (1) = 153 == 153 -> True.",
            "time_complexity": "O(log10(N))",
            "space_complexity": "O(1)",
            "common_mistakes": "Assuming the power is always 3 instead of dynamically matching the number of digits k.",
            "interview_questions": "What is the maximum number of digits an Armstrong number can have in base 10? (Max is 39 digits)."
        }
    ),
    Problem(
        id="gcd-lcm",
        title="Greatest Common Divisor (GCD)",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.4: Know Basic Maths",
        difficulty="Easy",
        description="Given two non-negative integers a and b, compute and return their Greatest Common Divisor (GCD), also known as the Highest Common Factor (HCF).",
        input_format="Two integers a and b.",
        output_format="Return the integer GCD.",
        constraints=["1 <= a, b <= 10^9"],
        function_name="findGCD",
        param_names=["a", "b"],
        starter_code={
            "python": "class Solution:\n    def findGCD(self, a: int, b: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int findGCD(int a, int b) {\n        return 1;\n    }\n};",
            "java": "class Solution {\n    public int findGCD(int a, int b) {\n        return 1;\n    }\n}",
            "javascript": "class Solution {\n    findGCD(a, b) {\n        return 1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"a": 20, "b": 15}, expected_output=5, is_hidden=False),
            TestCase(id=2, input_data={"a": 9, "b": 12}, expected_output=3, is_hidden=False),
            TestCase(id=3, input_data={"a": 7, "b": 13}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"a": 100, "b": 2000}, expected_output=100, is_hidden=True),
            TestCase(id=5, input_data={"a": 48, "b": 18}, expected_output=6, is_hidden=True),
        ],
        comparison_mode="exact",
        order=5,
        tags=["Maths", "Euclidean Algorithm", "GCD"],
        hints=[
            "The brute force checks all numbers from min(a,b) down to 1.",
            "Can we do much better? Recall Euclidean algorithm: gcd(a, b) = gcd(b, a % b).",
            "Continue until b reaches 0; then a is the GCD."
        ],
        examples=[
            {"input": "a = 20, b = 15", "output": "5", "explanation": "Factors of 20 are 1,2,4,5,10,20. Factors of 15 are 1,3,5,15. Highest common is 5."},
            {"input": "a = 7, b = 13", "output": "1", "explanation": "Both are prime numbers with no common factors other than 1."}
        ],
        explanation={
            "intuition": "If a divisor divides both a and b, it must also divide the remainder of a divided by b.",
            "brute_force": "Loop from min(a, b) down to 1. Return the first number that divides both a and b evenly. O(min(A, B)).",
            "optimal_approach": "Use Euclidean algorithm: while b != 0: a, b = b, a % b. Return a.",
            "dry_run": "a = 20, b = 15:\n1. a = 15, b = 20 % 15 = 5\n2. a = 5, b = 15 % 5 = 0\nb is 0, return a = 5.",
            "time_complexity": "O(log(min(A, B)))",
            "space_complexity": "O(1)",
            "common_mistakes": "Forgetting that modulo is much faster than repeated subtraction.",
            "interview_questions": "How do you calculate LCM using GCD? (LCM(a, b) = (a * b) // GCD(a, b))."
        }
    ),
    Problem(
        id="print-divisors",
        title="Find All Divisors of a Number",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.4: Know Basic Maths",
        difficulty="Easy",
        description="Given an integer n, find and return all of its positive divisors in strictly ascending sorted order.",
        input_format="A single positive integer n.",
        output_format="Return a sorted list of integer divisors.",
        constraints=["1 <= n <= 10^7"],
        function_name="getAllDivisors",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def getAllDivisors(self, n: int) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> getAllDivisors(int n) {\n        return {};\n    }\n};",
            "java": "class Solution {\n    public List<Integer> getAllDivisors(int n) {\n        return new ArrayList<>();\n    }\n}",
            "javascript": "class Solution {\n    getAllDivisors(n) {\n        return [];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 36}, expected_output=[1, 2, 3, 4, 6, 9, 12, 18, 36], is_hidden=False),
            TestCase(id=2, input_data={"n": 7}, expected_output=[1, 7], is_hidden=False),
            TestCase(id=3, input_data={"n": 1}, expected_output=[1], is_hidden=False),
            TestCase(id=4, input_data={"n": 100}, expected_output=[1, 2, 4, 5, 10, 20, 25, 50, 100], is_hidden=True),
            TestCase(id=5, input_data={"n": 49}, expected_output=[1, 7, 49], is_hidden=True),
        ],
        comparison_mode="exact",
        order=6,
        tags=["Maths", "Divisors", "Square Root"],
        hints=[
            "Checking every number from 1 to n takes O(N) time which is slow for large N.",
            "Divisors always appear in complementary pairs (i, n / i).",
            "Iterate only up to sqrt(n). If i divides n, both i and n // i are divisors (avoid duplicate if i == n // i)."
        ],
        examples=[
            {"input": "n = 36", "output": "[1, 2, 3, 4, 6, 9, 12, 18, 36]", "explanation": "These are all integers dividing 36 with 0 remainder."},
            {"input": "n = 7", "output": "[1, 7]", "explanation": "7 is prime so only 1 and 7 divide it."}
        ],
        explanation={
            "intuition": "If d is a divisor of n, then (n / d) is also a divisor. One factor is always <= sqrt(n).",
            "brute_force": "Loop i from 1 to n; if n % i == 0 append i. Takes O(N) time.",
            "optimal_approach": "Loop i from 1 up to int(sqrt(n)). If n % i == 0, add i, and if i != n // i add n // i. Finally sort the collected divisors.",
            "dry_run": "n = 36: sqrt(36) = 6.\ni=1: add 1, 36\ni=2: add 2, 18\ni=3: add 3, 12\ni=4: add 4, 9\ni=5: not factor\ni=6: add 6 (single instance)\nSorted: [1, 2, 3, 4, 6, 9, 12, 18, 36].",
            "time_complexity": "O(sqrt(N) + D log D) where D is number of divisors.",
            "space_complexity": "O(D) to hold the output list.",
            "common_mistakes": "Adding i twice when i * i == n (like 6 for 36).",
            "interview_questions": "How many total divisors does a highly composite number around 10^9 have? (Usually at most 1344)."
        }
    ),
    Problem(
        id="check-prime",
        title="Check for Prime Number",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.4: Know Basic Maths",
        difficulty="Easy",
        description="Given an integer n, determine whether it is a prime number. A prime number is a natural number strictly greater than 1 that has no positive divisors other than 1 and itself.",
        input_format="A single positive integer n.",
        output_format="Return True if n is prime, else False.",
        constraints=["1 <= n <= 10^9"],
        function_name="isPrime",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def isPrime(self, n: int) -> bool:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    bool isPrime(int n) {\n        return false;\n    }\n};",
            "java": "class Solution {\n    public boolean isPrime(int n) {\n        return false;\n    }\n}",
            "javascript": "class Solution {\n    isPrime(n) {\n        return false;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 2}, expected_output=True, is_hidden=False),
            TestCase(id=2, input_data={"n": 11}, expected_output=True, is_hidden=False),
            TestCase(id=3, input_data={"n": 4}, expected_output=False, is_hidden=False),
            TestCase(id=4, input_data={"n": 1}, expected_output=False, is_hidden=False),
            TestCase(id=5, input_data={"n": 997}, expected_output=True, is_hidden=True),
            TestCase(id=6, input_data={"n": 1000000000}, expected_output=False, is_hidden=True),
        ],
        comparison_mode="exact",
        order=7,
        tags=["Maths", "Primes", "Square Root"],
        hints=[
            "1 is neither prime nor composite, return False for n <= 1.",
            "2 is the only even prime number.",
            "You only need to check divisibility up to sqrt(n)."
        ],
        examples=[
            {"input": "n = 11", "output": "True", "explanation": "11 is divisible only by 1 and 11."},
            {"input": "n = 1", "output": "False", "explanation": "1 is not a prime number by definition."}
        ],
        explanation={
            "intuition": "If n is composite, it must have a factor d <= sqrt(n). If no such factor exists, n must be prime.",
            "brute_force": "Check all integers from 2 to n-1. If any divides n, return False. O(N) time.",
            "optimal_approach": "If n <= 1 return False. If n <= 3 return True. If n % 2 == 0 or n % 3 == 0 return False. Check i from 5 to sqrt(n) stepping by 6 (checking i and i+2).",
            "dry_run": "n = 11: sqrt(11) ~ 3.31. Test i = 2 (11%2!=0), i = 3 (11%3!=0). No factors <= sqrt(11). Return True.",
            "time_complexity": "O(sqrt(N))",
            "space_complexity": "O(1)",
            "common_mistakes": "Classifying 1 as prime, or forgetting 2 as prime.",
            "interview_questions": "How do you find all primes up to N? (Sieve of Eratosthenes in O(N log log N))."
        }
    ),
    Problem(
        id="sum-of-n-numbers",
        title="Sum of First N Natural Numbers",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.1: Basic Input and Output",
        difficulty="Easy",
        description="Given an integer n, calculate the sum of the first n positive natural numbers (1 + 2 + 3 + ... + n).",
        input_format="A single positive integer n.",
        output_format="Return the total integer sum.",
        constraints=["1 <= n <= 10^6"],
        function_name="sumOfFirstN",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def sumOfFirstN(self, n: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    long long sumOfFirstN(int n) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public long sumOfFirstN(int n) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    sumOfFirstN(n) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 5}, expected_output=15, is_hidden=False, explanation="1 + 2 + 3 + 4 + 5 = 15."),
            TestCase(id=2, input_data={"n": 10}, expected_output=55, is_hidden=False),
            TestCase(id=3, input_data={"n": 1}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"n": 1000}, expected_output=500500, is_hidden=True),
            TestCase(id=5, input_data={"n": 1000000}, expected_output=500000500000, is_hidden=True),
        ],
        comparison_mode="exact",
        order=8,
        tags=["Maths", "Formulas", "Loops"],
        hints=[
            "A simple loop can iterate from 1 to n and add each number.",
            "Can you compute this in O(1) time without looping?",
            "Use Gauss's formula: n * (n + 1) // 2."
        ],
        examples=[
            {"input": "n = 5", "output": "15", "explanation": "1 + 2 + 3 + 4 + 5 = 15."},
            {"input": "n = 3", "output": "6", "explanation": "1 + 2 + 3 = 6."}
        ],
        explanation={
            "intuition": "Pairing first and last numbers (1+n, 2+(n-1)...) shows that every pair sums to (n+1). There are n/2 such pairs.",
            "brute_force": "Initialize s = 0. Loop i from 1 to n, s += i. Takes O(N) time.",
            "optimal_approach": "Direct formula: return (n * (n + 1)) // 2 in O(1) time.",
            "dry_run": "n = 5: 5 * (5 + 1) // 2 = 30 // 2 = 15.",
            "time_complexity": "O(1) using formula, or O(N) with loop.",
            "space_complexity": "O(1)",
            "common_mistakes": "Integer overflow in languages like C++/Java if using 32-bit int for large n.",
            "interview_questions": "How does Gauss formula generalize to sum of squares or sum of cubes? (Sum of squares = n(n+1)(2n+1)/6)."
        }
    ),
    Problem(
        id="factorial-number",
        title="Factorial of a Number",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.4: Know Basic Maths",
        difficulty="Easy",
        description="Given a non-negative integer n, compute and return n! (n factorial), where n! = 1 * 2 * 3 * ... * n and 0! = 1.",
        input_format="A non-negative integer n.",
        output_format="Return the factorial value.",
        constraints=["0 <= n <= 20"],
        function_name="factorial",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def factorial(self, n: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    long long factorial(int n) {\n        return 1;\n    }\n};",
            "java": "class Solution {\n    public long factorial(int n) {\n        return 1;\n    }\n}",
            "javascript": "class Solution {\n    factorial(n) {\n        return 1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 5}, expected_output=120, is_hidden=False),
            TestCase(id=2, input_data={"n": 0}, expected_output=1, is_hidden=False),
            TestCase(id=3, input_data={"n": 1}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"n": 10}, expected_output=3628800, is_hidden=True),
            TestCase(id=5, input_data={"n": 15}, expected_output=1307674368000, is_hidden=True),
        ],
        comparison_mode="exact",
        order=9,
        tags=["Maths", "Recursion", "Loops"],
        hints=[
            "Base case: 0! is 1 by mathematical convention.",
            "Multiply result sequentially from 1 up to n.",
            "Factorial grows extremely quickly, so test with 64-bit integers."
        ],
        examples=[
            {"input": "n = 5", "output": "120", "explanation": "5! = 5 * 4 * 3 * 2 * 1 = 120."},
            {"input": "n = 0", "output": "1", "explanation": "0! is defined as 1."}
        ],
        explanation={
            "intuition": "Factorial is the product of all positive integers less than or equal to n.",
            "brute_force": "Iterative loop: ans = 1; for i in range(1, n+1): ans *= i; return ans.",
            "optimal_approach": "Iterative multiplication O(N) time and O(1) space. Avoid recursion to save call stack overhead.",
            "dry_run": "n = 4: ans = 1 -> ans = 1*1 = 1 -> ans = 1*2 = 2 -> ans = 2*3 = 6 -> ans = 6*4 = 24.",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Returning 0 for n = 0 instead of 1.",
            "interview_questions": "How many trailing zeros does N! have? (Count factors of 5: floor(N/5) + floor(N/25) + ...)."
        }
    ),
    Problem(
        id="even-odd-count",
        title="Count Even and Odd Elements in an Array",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.2: Conditional Statements",
        difficulty="Easy",
        description="Given an array of integers arr, count how many elements are even and how many are odd. Return a list [even_count, odd_count].",
        input_format="A list of integers arr.",
        output_format="Return a list of two integers [even_count, odd_count].",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="countEvenOdd",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def countEvenOdd(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> countEvenOdd(vector<int>& arr) {\n        return {0, 0};\n    }\n};",
            "java": "class Solution {\n    public int[] countEvenOdd(int[] arr) {\n        return new int[]{0, 0};\n    }\n}",
            "javascript": "class Solution {\n    countEvenOdd(arr) {\n        return [0, 0];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 3, 4, 5]}, expected_output=[2, 3], is_hidden=False),
            TestCase(id=2, input_data={"arr": [2, 4, 6, 8]}, expected_output=[4, 0], is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, 3, 5]}, expected_output=[0, 3], is_hidden=False),
            TestCase(id=4, input_data={"arr": [0, -2, -3, 7]}, expected_output=[2, 2], is_hidden=True),
            TestCase(id=5, input_data={"arr": [100]}, expected_output=[1, 0], is_hidden=True),
        ],
        comparison_mode="exact",
        order=10,
        tags=["Arrays", "Conditionals", "Basics"],
        hints=[
            "An integer x is even if x % 2 == 0.",
            "Be mindful of negative integers: in some languages x % 2 can yield -1.",
            "Traverse the array once while maintaining two counters."
        ],
        examples=[
            {"input": "arr = [1, 2, 3, 4, 5]", "output": "[2, 3]", "explanation": "Even numbers are 2, 4 (count=2). Odd numbers are 1, 3, 5 (count=3)."},
            {"input": "arr = [2, 4, 6]", "output": "[3, 0]", "explanation": "All numbers are even."}
        ],
        explanation={
            "intuition": "Iterate through each number in the array. Check divisibility by 2 to determine parity.",
            "brute_force": "Single pass iteration checking num % 2 == 0.",
            "optimal_approach": "Loop through arr: if num % 2 == 0: even += 1 else: odd += 1. Return [even, odd].",
            "dry_run": "arr = [1, 2, 3]:\n1: odd -> odd=1\n2: even -> even=1\n3: odd -> odd=2\nResult: [1, 2].",
            "time_complexity": "O(N) - One pass through the array.",
            "space_complexity": "O(1) - Only two counters.",
            "common_mistakes": "Forgetting that 0 is an even number (0 % 2 == 0).",
            "interview_questions": "Can you check parity without modulo? (Using bitwise AND: if (x & 1) == 0 then even)."
        }
    ),
    Problem(
        id="fibonacci-number",
        title="Nth Fibonacci Number",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.5: Functions",
        difficulty="Easy",
        description="The Fibonacci numbers form a sequence where F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n >= 2. Given integer n, calculate F(n).",
        input_format="A single non-negative integer n.",
        output_format="Return the nth Fibonacci number.",
        constraints=["0 <= n <= 30"],
        function_name="fibonacci",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def fibonacci(self, n: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int fibonacci(int n) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int fibonacci(int n) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    fibonacci(n) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 2}, expected_output=1, is_hidden=False),
            TestCase(id=2, input_data={"n": 3}, expected_output=2, is_hidden=False),
            TestCase(id=3, input_data={"n": 4}, expected_output=3, is_hidden=False),
            TestCase(id=4, input_data={"n": 0}, expected_output=0, is_hidden=False),
            TestCase(id=5, input_data={"n": 10}, expected_output=55, is_hidden=True),
            TestCase(id=6, input_data={"n": 20}, expected_output=6765, is_hidden=True),
        ],
        comparison_mode="exact",
        order=11,
        tags=["Maths", "DP", "Functions"],
        hints=[
            "Base cases: F(0) = 0, F(1) = 1.",
            "Naive recursion computes the same subproblems repeatedly leading to O(2^N) time.",
            "Keep two variables for previous two Fibonacci values and update them iteratively."
        ],
        examples=[
            {"input": "n = 4", "output": "3", "explanation": "F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3."},
            {"input": "n = 2", "output": "1", "explanation": "F(2) = F(1) + F(0) = 1 + 0 = 1."}
        ],
        explanation={
            "intuition": "Every term is the sum of the two preceding terms. We only need the latest two values at any step.",
            "brute_force": "Recursive fib(n) = fib(n-1) + fib(n-2) with O(2^N) exponential time.",
            "optimal_approach": "Iterate from 2 to n maintaining a = 0, b = 1. In each step, new_val = a + b; a = b; b = new_val. Return b.",
            "dry_run": "n = 4: a=0, b=1.\ni=2: c = 0+1=1, a=1, b=1\ni=3: c = 1+1=2, a=1, b=2\ni=4: c = 1+2=3, a=2, b=3. Return 3.",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Forgetting the base cases for n=0 or n=1.",
            "interview_questions": "Can you compute F(N) in O(log N) time? (Yes, using matrix exponentiation or Binet formula)."
        }
    ),
    Problem(
        id="character-case-check",
        title="Determine Character Case and Type",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.2: Conditional Statements",
        difficulty="Easy",
        description="Given a single character string ch, determine its type. Return 'uppercase' if it is an uppercase English letter ('A'-'Z'), 'lowercase' if it is a lowercase English letter ('a'-'z'), 'digit' if it is a digit ('0'-'9'), and 'other' for any other character.",
        input_format="A string of length 1 containing character ch.",
        output_format="Return 'uppercase', 'lowercase', 'digit', or 'other'.",
        constraints=["len(ch) == 1"],
        function_name="checkCharType",
        param_names=["ch"],
        starter_code={
            "python": "class Solution:\n    def checkCharType(self, ch: str) -> str:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    string checkCharType(char ch) {\n        return \"\";\n    }\n};",
            "java": "class Solution {\n    public String checkCharType(char ch) {\n        return \"\";\n    }\n}",
            "javascript": "class Solution {\n    checkCharType(ch) {\n        return \"\";\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"ch": "A"}, expected_output="uppercase", is_hidden=False),
            TestCase(id=2, input_data={"ch": "z"}, expected_output="lowercase", is_hidden=False),
            TestCase(id=3, input_data={"ch": "7"}, expected_output="digit", is_hidden=False),
            TestCase(id=4, input_data={"ch": "#"}, expected_output="other", is_hidden=False),
            TestCase(id=5, input_data={"ch": "M"}, expected_output="uppercase", is_hidden=True),
            TestCase(id=6, input_data={"ch": "@"}, expected_output="other", is_hidden=True),
        ],
        comparison_mode="exact",
        order=12,
        tags=["Strings", "Conditionals", "ASCII"],
        hints=[
            "Check character range using ASCII comparison or built-in methods.",
            "'A' <= ch <= 'Z' defines uppercase.",
            "'a' <= ch <= 'z' defines lowercase, and '0' <= ch <= '9' defines digit."
        ],
        examples=[
            {"input": "ch = 'G'", "output": "'uppercase'", "explanation": "'G' is an uppercase letter."},
            {"input": "ch = '5'", "output": "'digit'", "explanation": "'5' is a numeric digit."}
        ],
        explanation={
            "intuition": "Characters have underlying ASCII numeric codes where uppercase, lowercase, and digits lie in contiguous ranges.",
            "brute_force": "Check if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'...",
            "optimal_approach": "Use range comparison: if 'A' <= ch <= 'Z' return 'uppercase', elif 'a' <= ch <= 'z' return 'lowercase', elif '0' <= ch <= '9' return 'digit', else 'other'.",
            "dry_run": "ch = 'z': Not between 'A' and 'Z'. Is between 'a' and 'z' -> return 'lowercase'.",
            "time_complexity": "O(1)",
            "space_complexity": "O(1)",
            "common_mistakes": "Checking uppercase after converting character, which mutates the input state.",
            "interview_questions": "How does ASCII differ from Unicode when checking character classes?"
        }
    ),
    Problem(
        id="pattern-right-triangle",
        title="Right-Angled Number Triangle Pattern",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.3: Pattern Problems",
        difficulty="Easy",
        description="Given an integer n, generate a right-angled number triangle pattern of n rows. Row i (1-indexed) contains numbers from 1 up to i concatenated as a string. Return a list of strings representing the rows.",
        input_format="A single positive integer n.",
        output_format="Return a list of strings representing the n rows.",
        constraints=["1 <= n <= 20"],
        function_name="generateNumberTriangle",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def generateNumberTriangle(self, n: int) -> list[str]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<string> generateNumberTriangle(int n) {\n        return {};\n    }\n};",
            "java": "class Solution {\n    public List<String> generateNumberTriangle(int n) {\n        return new ArrayList<>();\n    }\n}",
            "javascript": "class Solution {\n    generateNumberTriangle(n) {\n        return [];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 3}, expected_output=["1", "12", "123"], is_hidden=False),
            TestCase(id=2, input_data={"n": 1}, expected_output=["1"], is_hidden=False),
            TestCase(id=3, input_data={"n": 5}, expected_output=["1", "12", "123", "1234", "12345"], is_hidden=False),
            TestCase(id=4, input_data={"n": 4}, expected_output=["1", "12", "123", "1234"], is_hidden=True),
        ],
        comparison_mode="exact",
        order=13,
        tags=["Patterns", "Nested Loops", "Strings"],
        hints=[
            "The pattern consists of n rows.",
            "Row 1 has '1', Row 2 has '12', Row i has digits from 1 to i.",
            "Use an outer loop for rows from 1 to n, and build string for each row."
        ],
        examples=[
            {"input": "n = 3", "output": "['1', '12', '123']", "explanation": "Row 1 is '1', row 2 is '12', row 3 is '123'."},
            {"input": "n = 2", "output": "['1', '12']", "explanation": "Two rows created."}
        ],
        explanation={
            "intuition": "For each row i from 1 to n, append numbers 1 through i into a string, then collect in a list.",
            "brute_force": "Nested loop: outer loop i from 1 to n; inner loop j from 1 to i; concatenate string.",
            "optimal_approach": "Loop i from 1 to n: row = ''.join(str(j) for j in range(1, i+1)); append to result list.",
            "dry_run": "n = 3:\ni = 1: '1'\ni = 2: '12'\ni = 3: '123'\nResult: ['1', '12', '123'].",
            "time_complexity": "O(N^2) total characters generated.",
            "space_complexity": "O(N^2) to hold output strings.",
            "common_mistakes": "1-indexing vs 0-indexing discrepancies in loop ranges.",
            "interview_questions": "How would you modify this to print characters ('A', 'AB', 'ABC') instead?"
        }
    ),
    Problem(
        id="pattern-inverted-pyramid",
        title="Inverted Star Pyramid Pattern",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.3: Pattern Problems",
        difficulty="Easy",
        description="Given an integer n, generate an inverted star pyramid pattern of n lines. Line 0 has 2*n - 1 stars, line 1 has 2*n - 3 stars preceded by 1 space, line i has (2*(n-i) - 1) stars preceded by i spaces. Return the lines as a list of strings.",
        input_format="A single positive integer n.",
        output_format="Return a list of strings representing the inverted pyramid rows.",
        constraints=["1 <= n <= 20"],
        function_name="generateInvertedStars",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def generateInvertedStars(self, n: int) -> list[str]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<string> generateInvertedStars(int n) {\n        return {};\n    }\n};",
            "java": "class Solution {\n    public List<String> generateInvertedStars(int n) {\n        return new ArrayList<>();\n    }\n}",
            "javascript": "class Solution {\n    generateInvertedStars(n) {\n        return [];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 3}, expected_output=["*****", " ***", "  *"], is_hidden=False),
            TestCase(id=2, input_data={"n": 1}, expected_output=["*"], is_hidden=False),
            TestCase(id=3, input_data={"n": 4}, expected_output=["*******", " *****", "  ***", "   *"], is_hidden=False),
            TestCase(id=4, input_data={"n": 2}, expected_output=["***", " *"], is_hidden=True),
        ],
        comparison_mode="exact",
        order=14,
        tags=["Patterns", "Strings", "Geometry"],
        hints=[
            "For row i (from 0 to n-1), how many leading spaces are there? Exactly i spaces.",
            "How many stars are in row i? (2 * (n - i) - 1) stars.",
            "Concatenate i spaces followed by the stars."
        ],
        examples=[
            {"input": "n = 3", "output": "['*****', ' ***', '  *']", "explanation": "Row 0 has 0 spaces and 5 stars. Row 1 has 1 space and 3 stars. Row 2 has 2 spaces and 1 star."},
            {"input": "n = 1", "output": "['*']", "explanation": "Single star row."}
        ],
        explanation={
            "intuition": "Break down each row into its components: leading spaces and stars. As row index i increases from 0 to n-1, spaces increase by 1 and stars decrease by 2.",
            "brute_force": "Build each line using string repetition: (' ' * i) + ('*' * (2 * (n - i) - 1)).",
            "optimal_approach": "Loop i from 0 to n-1: construct (' ' * i) + ('*' * (2*(n-i)-1)), append to result list.",
            "dry_run": "n = 3:\ni=0: spaces=0, stars=5 -> '*****'\ni=1: spaces=1, stars=3 -> ' ***'\ni=2: spaces=2, stars=1 -> '  *'.",
            "time_complexity": "O(N^2) characters rendered.",
            "space_complexity": "O(N^2) for the returned array of strings.",
            "common_mistakes": "Adding trailing spaces after the stars.",
            "interview_questions": "How do you combine upright and inverted pyramids to make a diamond pattern?"
        }
    ),
    Problem(
        id="time-complexity-estimation",
        title="Count Nested Loop Iterations",
        step_id=1,
        step_title="Step 1: Beginner Problems",
        subtopic="1.6: Time and Space Complexity",
        difficulty="Easy",
        description="Consider two nested loops: an outer loop running for i from 0 to n-1, and an inner loop running for j from i to n-1. In each step of the inner loop, a counter increments by 1. Given integer n, calculate the final value of the counter without running the loops explicitly.",
        input_format="A single positive integer n.",
        output_format="Return the total count of iterations as an integer.",
        constraints=["1 <= n <= 10^6"],
        function_name="countNestedIterations",
        param_names=["n"],
        starter_code={
            "python": "class Solution:\n    def countNestedIterations(self, n: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    long long countNestedIterations(int n) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public long countNestedIterations(int n) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    countNestedIterations(n) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 3}, expected_output=6, is_hidden=False, explanation="i=0: j in 0..2 (3 steps); i=1: j in 1..2 (2 steps); i=2: j in 2..2 (1 step). Total = 3 + 2 + 1 = 6."),
            TestCase(id=2, input_data={"n": 4}, expected_output=10, is_hidden=False),
            TestCase(id=3, input_data={"n": 1}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"n": 100}, expected_output=5050, is_hidden=True),
            TestCase(id=5, input_data={"n": 1000000}, expected_output=500000500000, is_hidden=True),
        ],
        comparison_mode="exact",
        order=15,
        tags=["Complexity", "Maths", "Loops"],
        hints=[
            "When i = 0, inner loop executes n times.",
            "When i = 1, inner loop executes n - 1 times.",
            "The sum of n + (n-1) + ... + 1 is given by n * (n + 1) // 2."
        ],
        examples=[
            {"input": "n = 3", "output": "6", "explanation": "3 + 2 + 1 = 6."},
            {"input": "n = 4", "output": "10", "explanation": "4 + 3 + 2 + 1 = 10."}
        ],
        explanation={
            "intuition": "Understanding how nested loop bounds translate to summation series is the cornerstone of Big-O complexity analysis.",
            "brute_force": "Run the nested loop with counter += 1. For n = 10^6, this takes 10^12 operations and will TLE.",
            "optimal_approach": "Recognize the arithmetic progression sum: n + (n-1) + ... + 1 = n * (n + 1) // 2. Compute in O(1) time.",
            "dry_run": "n = 3: 3 * 4 // 2 = 6.",
            "time_complexity": "O(1)",
            "space_complexity": "O(1)",
            "common_mistakes": "Simulating the loop for large n instead of using the closed-form math formula.",
            "interview_questions": "What Big-O notation does this loop pattern belong to? (O(N^2))."
        }
    ),
]
