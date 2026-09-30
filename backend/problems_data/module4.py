from models import Problem, TestCase

MODULE_4_PROBLEMS = [
    Problem(
        id="element-frequency-counter",
        title="Count Frequencies of Elements in Array",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.1: Frequency Counting",
        difficulty="Easy",
        description="Given an array of integers arr, calculate the frequency of each unique element. Return a dictionary mapping each integer to its frequency.",
        input_format="A list of integers arr.",
        output_format="Return a dictionary mapping integer to frequency.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="countFrequencies",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def countFrequencies(self, arr: list[int]) -> dict[int, int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    unordered_map<int, int> countFrequencies(vector<int>& arr) {\n        unordered_map<int, int> freq;\n        return freq;\n    }\n};",
            "java": "class Solution {\n    public Map<Integer, Integer> countFrequencies(int[] arr) {\n        return new HashMap<>();\n    }\n}",
            "javascript": "class Solution {\n    countFrequencies(arr) {\n        return {};\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 2, 3, 1, 4]}, expected_output={1: 2, 2: 2, 3: 1, 4: 1}, is_hidden=False),
            TestCase(id=2, input_data={"arr": [5, 5, 5, 5]}, expected_output={5: 4}, is_hidden=False),
            TestCase(id=3, input_data={"arr": [10]}, expected_output={10: 1}, is_hidden=False),
            TestCase(id=4, input_data={"arr": [-1, -2, -1, 0]}, expected_output={-1: 2, -2: 1, 0: 1}, is_hidden=True),
        ],
        comparison_mode="exact",
        order=51,
        tags=["Hashing", "Frequency", "Hash Map"],
        hints=[
            "Initialize an empty hash table (dictionary).",
            "Iterate through the array. For each element x, if it exists in the table, increment its count by 1.",
            "If it does not exist, insert it with count 1."
        ],
        examples=[
            {"input": "arr = [1, 2, 2, 3, 1, 4]", "output": "{1: 2, 2: 2, 3: 1, 4: 1}", "explanation": "1 appears twice, 2 appears twice, 3 and 4 appear once."},
            {"input": "arr = [5, 5]", "output": "{5: 2}", "explanation": "5 has frequency 2."}
        ],
        explanation={
            "intuition": "Hash tables provide average O(1) time complexity for insertions and lookups, making them the standard choice for frequency tracking.",
            "brute_force": "For each distinct element, loop through entire array to count occurrences in O(N^2).",
            "optimal_approach": "freq = {}; for x in arr: freq[x] = freq.get(x, 0) + 1; return freq.",
            "dry_run": "[1, 2, 1]:\nx=1: freq={1:1}\nx=2: freq={1:1, 2:1}\nx=1: freq={1:2, 2:1}. Return freq.",
            "time_complexity": "O(N) on average.",
            "space_complexity": "O(U) where U is number of unique elements.",
            "common_mistakes": "Key errors when accessing uninitialized dictionary keys without get() or default.",
            "interview_questions": "How does a hash map handle hash collisions internally? (Chaining with linked lists/red-black trees, or open addressing like linear probing)."
        }
    ),
    Problem(
        id="character-frequency-counter",
        title="Count Character Frequencies in String",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.1: Frequency Counting",
        difficulty="Easy",
        description="Given a string s, count the frequency of each character. Return a dictionary mapping each character to its occurrence count.",
        input_format="A string s.",
        output_format="Return a dictionary mapping character to frequency.",
        constraints=["1 <= len(s) <= 10^5"],
        function_name="charFrequency",
        param_names=["s"],
        starter_code={
            "python": "class Solution:\n    def charFrequency(self, s: str) -> dict[str, int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    unordered_map<char, int> charFrequency(string s) {\n        unordered_map<char, int> freq;\n        return freq;\n    }\n};",
            "java": "class Solution {\n    public Map<Character, Integer> charFrequency(String s) {\n        return new HashMap<>();\n    }\n}",
            "javascript": "class Solution {\n    charFrequency(s) {\n        return {};\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"s": "hello"}, expected_output={"h": 1, "e": 1, "l": 2, "o": 1}, is_hidden=False),
            TestCase(id=2, input_data={"s": "banana"}, expected_output={"b": 1, "a": 3, "n": 2}, is_hidden=False),
            TestCase(id=3, input_data={"s": "z"}, expected_output={"z": 1}, is_hidden=False),
            TestCase(id=4, input_data={"s": "aabbcc"}, expected_output={"a": 2, "b": 2, "c": 2}, is_hidden=True),
        ],
        comparison_mode="exact",
        order=52,
        tags=["Hashing", "Strings", "Hash Map"],
        hints=[
            "Traverse each character in the string.",
            "Use a hash map or an array of size 26 if string is limited to lowercase English letters.",
            "Increment character counts in O(1) time per character."
        ],
        examples=[
            {"input": "s = 'banana'", "output": "{'b': 1, 'a': 3, 'n': 2}", "explanation": "'a' occurs 3 times, 'n' occurs 2 times, 'b' occurs once."},
            {"input": "s = 'hi'", "output": "{'h': 1, 'i': 1}", "explanation": "Both characters occur once."}
        ],
        explanation={
            "intuition": "Iterating over characters and updating a frequency dictionary gives linear runtime.",
            "brute_force": "For each character, count its occurrences using string scan O(N^2).",
            "optimal_approach": "freq = {}; for ch in s: freq[ch] = freq.get(ch, 0) + 1; return freq.",
            "dry_run": "s = 'aba':\nch='a': {a:1}\nch='b': {a:1, b:1}\nch='a': {a:2, b:1}.",
            "time_complexity": "O(N)",
            "space_complexity": "O(K) where K is alphabet size (at most 256 for ASCII).",
            "common_mistakes": "Case-sensitivity confusion (e.g. 'A' vs 'a').",
            "interview_questions": "How can you implement this in C/C++ without a hash table? (Use a fixed-size integer array of length 26: count[ch - 'a']++)."
        }
    ),
    Problem(
        id="most-frequent-element",
        title="Find Highest and Lowest Frequency Elements",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.1: Frequency Counting",
        difficulty="Easy",
        description="Given an array of integers arr, find the element with the highest frequency and the element with the lowest frequency. If there is a tie, return the smaller element. Return a list [highest_freq_elem, lowest_freq_elem].",
        input_format="A list of integers arr.",
        output_format="Return a list of two integers [highest_freq_elem, lowest_freq_elem].",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="mostAndLeastFrequent",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def mostAndLeastFrequent(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> mostAndLeastFrequent(vector<int>& arr) {\n        return {0, 0};\n    }\n};",
            "java": "class Solution {\n    public int[] mostAndLeastFrequent(int[] arr) {\n        return new int[]{0, 0};\n    }\n}",
            "javascript": "class Solution {\n    mostAndLeastFrequent(arr) {\n        return [0, 0];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 3, 1, 1, 4]}, expected_output=[1, 2], is_hidden=False, explanation="1 has highest freq (3). 2, 3, 4 all have lowest freq (1); smaller element is 2."),
            TestCase(id=2, input_data={"arr": [10, 5, 10, 15, 10, 5]}, expected_output=[10, 15], is_hidden=False),
            TestCase(id=3, input_data={"arr": [7]}, expected_output=[7, 7], is_hidden=False),
            TestCase(id=4, input_data={"arr": [4, 4, 2, 2]}, expected_output=[2, 2], is_hidden=True),
        ],
        comparison_mode="exact",
        order=53,
        tags=["Hashing", "Frequency", "Hash Map"],
        hints=[
            "First, build a frequency hash map for all elements.",
            "Track max_freq, max_elem, min_freq, and min_elem.",
            "Break ties by choosing the smaller element when frequencies are identical."
        ],
        examples=[
            {"input": "arr = [1, 2, 3, 1, 1, 4]", "output": "[1, 2]", "explanation": "Highest frequency element is 1 (occurs 3 times). Lowest frequency elements are 2, 3, 4; 2 is the smallest."},
            {"input": "arr = [10, 5, 10, 15, 10, 5]", "output": "[10, 15]", "explanation": "10 occurs 3 times (highest); 15 occurs 1 time (lowest)."}
        ],
        explanation={
            "intuition": "Count frequencies using a hash map in first pass, then iterate over unique elements to identify extrema while handling tie-breaking rules.",
            "brute_force": "Nested loops to count frequencies for every element in O(N^2).",
            "optimal_approach": "Build frequency map. Sort unique keys (to handle smaller-element ties first). Track max_freq, min_freq and their corresponding elements. Return [max_elem, min_elem].",
            "dry_run": "[1, 2, 3, 1, 1, 4]: counts={1:3, 2:1, 3:1, 4:1}. Max freq is 3 (elem 1). Min freq is 1; smallest among {2, 3, 4} is 2. Result: [1, 2].",
            "time_complexity": "O(N + U log U) where U is distinct elements count.",
            "space_complexity": "O(U) for frequency map.",
            "common_mistakes": "Not breaking ties in favor of the smaller element value.",
            "interview_questions": "How can you find the top K frequent elements? (Using Bucket Sort in O(N) or a Min-Heap of size K in O(N log K))."
        }
    ),
    Problem(
        id="count-distinct-elements",
        title="Count Distinct Elements in an Array",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.2: Hash Set",
        difficulty="Easy",
        description="Given an array of integers arr, calculate and return the total number of unique (distinct) elements present in the array.",
        input_format="A list of integers arr.",
        output_format="Return the integer count of distinct elements.",
        constraints=["0 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="countDistinct",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def countDistinct(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int countDistinct(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int countDistinct(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    countDistinct(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [5, 10, 15, 5, 4, 5]}, expected_output=4, is_hidden=False, explanation="Unique elements are {4, 5, 10, 15}, total 4."),
            TestCase(id=2, input_data={"arr": [1, 1, 1, 1]}, expected_output=1, is_hidden=False),
            TestCase(id=3, input_data={"arr": []}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 2, 3, 4, 5]}, expected_output=5, is_hidden=True),
        ],
        comparison_mode="exact",
        order=54,
        tags=["Hashing", "Hash Set", "Basics"],
        hints=[
            "A Hash Set inherently rejects duplicates.",
            "Insert all elements from the array into a set.",
            "The size of the set equals the count of distinct elements."
        ],
        examples=[
            {"input": "arr = [5, 10, 15, 5, 4, 5]", "output": "4", "explanation": "4 distinct elements: 5, 10, 15, 4."},
            {"input": "arr = [1, 1, 1]", "output": "1", "explanation": "Only one distinct number."}
        ],
        explanation={
            "intuition": "A Hash Set data structure stores unique keys. Its size directly gives the distinct element count.",
            "brute_force": "Nested loops to check if arr[i] appeared earlier in O(N^2).",
            "optimal_approach": "return len(set(arr)).",
            "dry_run": "[5, 10, 5]: set contains {5, 10}. len is 2.",
            "time_complexity": "O(N) on average.",
            "space_complexity": "O(N) for set storage.",
            "common_mistakes": "Forgetting empty array edge case.",
            "interview_questions": "How can you count distinct elements in sliding windows of size k? (Maintain a sliding window frequency hash map)."
        }
    ),
    Problem(
        id="intersection-two-arrays-hash",
        title="Intersection of Two Arrays Using Hash Set",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.2: Hash Set",
        difficulty="Easy",
        description="Given two integer arrays nums1 and nums2, return an array of their intersection in sorted order. Each element in the result must be unique.",
        input_format="Two lists of integers nums1 and nums2.",
        output_format="Return a sorted list of unique intersecting integers.",
        constraints=["1 <= len(nums1), len(nums2) <= 10^5", "0 <= nums1[i], nums2[i] <= 10^5"],
        function_name="intersection",
        param_names=["nums1", "nums2"],
        starter_code={
            "python": "class Solution:\n    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {\n        return {};\n    }\n};",
            "java": "class Solution {\n    public int[] intersection(int[] nums1, int[] nums2) {\n        return new int[0];\n    }\n}",
            "javascript": "class Solution {\n    intersection(nums1, nums2) {\n        return [];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"nums1": [1, 2, 2, 1], "nums2": [2, 2]}, expected_output=[2], is_hidden=False),
            TestCase(id=2, input_data={"nums1": [4, 9, 5], "nums2": [9, 4, 9, 8, 4]}, expected_output=[4, 9], is_hidden=False),
            TestCase(id=3, input_data={"nums1": [1, 3, 5], "nums2": [2, 4, 6]}, expected_output=[], is_hidden=False),
            TestCase(id=4, input_data={"nums1": [1, 2, 3], "nums2": [1, 2, 3]}, expected_output=[1, 2, 3], is_hidden=True),
        ],
        comparison_mode="exact",
        order=55,
        tags=["Hashing", "Hash Set", "Intersection"],
        hints=[
            "Convert nums1 into a Hash Set set1 for O(1) membership check.",
            "Iterate through nums2; if element is in set1, add it to result set.",
            "Return the sorted unique results."
        ],
        examples=[
            {"input": "nums1 = [1, 2, 2, 1], nums2 = [2, 2]", "output": "[2]", "explanation": "2 is the only common element."},
            {"input": "nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]", "output": "[4, 9]", "explanation": "4 and 9 are present in both."}
        ],
        explanation={
            "intuition": "Using a hash set allows O(1) verification of common elements between two collections.",
            "brute_force": "Compare every element of nums1 with every element of nums2 in O(N * M).",
            "optimal_approach": "s1 = set(nums1); res = {x for x in nums2 if x in s1}; return sorted(list(res)).",
            "dry_run": "nums1=[4, 9, 5], nums2=[9, 4]: s1={4, 5, 9}. 9 is in s1 -> add 9. 4 is in s1 -> add 4. Sorted: [4, 9].",
            "time_complexity": "O(N + M + K log K) where K is intersection size.",
            "space_complexity": "O(N + K)",
            "common_mistakes": "Returning duplicate elements in the intersection.",
            "interview_questions": "What if both arrays are already sorted on disk? (Use two pointers with O(1) extra memory)."
        }
    ),
    Problem(
        id="first-repeating-element",
        title="Find the First Repeating Element in Array",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.2: Hash Set",
        difficulty="Easy",
        description="Given an array of integers arr, find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest among all repeating elements. Return the 0-based index of this first repeating element. If no element repeats, return -1.",
        input_format="A list of integers arr.",
        output_format="Return the 0-based index or -1.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="firstRepeatingElement",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def firstRepeatingElement(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int firstRepeatingElement(vector<int>& arr) {\n        return -1;\n    }\n};",
            "java": "class Solution {\n    public int firstRepeatingElement(int[] arr) {\n        return -1;\n    }\n}",
            "javascript": "class Solution {\n    firstRepeatingElement(arr) {\n        return -1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [10, 5, 3, 4, 3, 5, 6]}, expected_output=1, is_hidden=False, explanation="5 repeats and its first occurrence is at index 1 (earlier than 3 at index 2)."),
            TestCase(id=2, input_data={"arr": [1, 2, 3, 4]}, expected_output=-1, is_hidden=False),
            TestCase(id=3, input_data={"arr": [6, 10, 5, 4, 9, 120, 4, 6, 10]}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"arr": [2, 2]}, expected_output=0, is_hidden=True),
        ],
        comparison_mode="exact",
        order=56,
        tags=["Hashing", "Hash Set", "Search"],
        hints=[
            "Notice the requirement: smallest first occurrence index among all repeating numbers.",
            "Can you traverse from right to left while maintaining a hash set of seen elements?",
            "Whenever you see an element already in the set, update min_index to current index i."
        ],
        examples=[
            {"input": "arr = [10, 5, 3, 4, 3, 5, 6]", "output": "1", "explanation": "5 first appears at index 1 and repeats at index 5."},
            {"input": "arr = [1, 2, 3]", "output": "-1", "explanation": "No repeating elements."}
        ],
        explanation={
            "intuition": "Traversing backwards from right to left ensures that the last time we see a duplicate element as we move left, it is at its earliest appearance in the array.",
            "brute_force": "For each index i, check if arr[i] appears again at any j > i in O(N^2).",
            "optimal_approach": "seen = set(); min_idx = -1. Loop i from len(arr)-1 down to 0: if arr[i] in seen: min_idx = i else: seen.add(arr[i]). Return min_idx.",
            "dry_run": "[10, 5, 3, 4, 3, 5, 6]:\nRight to left: 6, 5, 3, 4 added.\nNext is 3 (in seen): min_idx = 2.\nNext is 5 (in seen): min_idx = 1.\nNext is 10 (not in seen): added.\nReturn min_idx = 1.",
            "time_complexity": "O(N) single reverse pass.",
            "space_complexity": "O(N) for set.",
            "common_mistakes": "Traversing left-to-right and picking the element that repeats earliest in second encounter rather than earliest first appearance.",
            "interview_questions": "How does traversing backwards simplify finding the earliest occurrence?"
        }
    ),
    Problem(
        id="first-non-repeating-char",
        title="First Non-Repeating Character in String",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.1: Frequency Counting",
        difficulty="Easy",
        description="Given a string s, find the first non-repeating character and return it. If every character repeats or the string is empty, return an empty string \"\".",
        input_format="A string s.",
        output_format="Return the single character string, or \"\".",
        constraints=["0 <= len(s) <= 10^5"],
        function_name="firstNonRepeatingChar",
        param_names=["s"],
        starter_code={
            "python": "class Solution:\n    def firstNonRepeatingChar(self, s: str) -> str:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    string firstNonRepeatingChar(string s) {\n        return \"\";\n    }\n};",
            "java": "class Solution {\n    public String firstNonRepeatingChar(String s) {\n        return \"\";\n    }\n}",
            "javascript": "class Solution {\n    firstNonRepeatingChar(s) {\n        return \"\";\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"s": "swiss"}, expected_output="w", is_hidden=False, explanation="'s' repeats, first unique character is 'w'."),
            TestCase(id=2, input_data={"s": "aabb"}, expected_output="", is_hidden=False),
            TestCase(id=3, input_data={"s": "loveleetcode"}, expected_output="v", is_hidden=False),
            TestCase(id=4, input_data={"s": "z"}, expected_output="z", is_hidden=True),
            TestCase(id=5, input_data={"s": ""}, expected_output="", is_hidden=True),
        ],
        comparison_mode="exact",
        order=57,
        tags=["Hashing", "Strings", "Frequency"],
        hints=[
            "First pass: build a frequency dictionary of all characters in s.",
            "Second pass: iterate through characters of s in original order.",
            "Return the first character whose recorded frequency is 1."
        ],
        examples=[
            {"input": "s = 'swiss'", "output": "'w'", "explanation": "'w' occurs once at index 1."},
            {"input": "s = 'aabb'", "output": "''", "explanation": "All characters repeat."}
        ],
        explanation={
            "intuition": "Frequency mapping tells us how many times each character exists. A second sequential pass finds the earliest candidate with frequency exactly 1.",
            "brute_force": "For each character, scan string to verify count == 1 in O(N^2).",
            "optimal_approach": "counts = Counter(s). For ch in s: if counts[ch] == 1: return ch. Return ''.",
            "dry_run": "s = 'swiss': counts = {s:3, w:1, i:1}.\nch='s' (count 3 != 1)\nch='w' (count 1 == 1) -> return 'w'.",
            "time_complexity": "O(N) two linear passes.",
            "space_complexity": "O(K) where K <= 256 for character set.",
            "common_mistakes": "Iterating over hash map keys directly instead of the original string s (which may lose insertion order in some languages).",
            "interview_questions": "How would you solve this in a real-time data stream of characters? (Use a queue alongside the hash map to track candidates)."
        }
    ),
    Problem(
        id="two-sum-hashmap",
        title="Check if Pair Exists with Target Sum",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.3: Hash Map",
        difficulty="Easy",
        description="Given an array of integers arr and an integer target, determine whether there exist two distinct indices i and j such that arr[i] + arr[j] == target. Return True if such a pair exists, otherwise False.",
        input_format="A list of integers arr and integer target.",
        output_format="Return True or False.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= target, arr[i] <= 10^9"],
        function_name="twoSumHash",
        param_names=["arr", "target"],
        starter_code={
            "python": "class Solution:\n    def twoSumHash(self, arr: list[int], target: int) -> bool:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    bool twoSumHash(vector<int>& arr, int target) {\n        return false;\n    }\n};",
            "java": "class Solution {\n    public boolean twoSumHash(int[] arr, int target) {\n        return false;\n    }\n}",
            "javascript": "class Solution {\n    twoSumHash(arr, target) {\n        return false;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [0, -1, 2, -3, 1], "target": -2}, expected_output=True, is_hidden=False, explanation="-3 + 1 = -2."),
            TestCase(id=2, input_data={"arr": [1, -2, 1, 0, 5], "target": 0}, expected_output=False, is_hidden=False),
            TestCase(id=3, input_data={"arr": [5], "target": 10}, expected_output=False, is_hidden=False),
            TestCase(id=4, input_data={"arr": [3, 3], "target": 6}, expected_output=True, is_hidden=True),
        ],
        comparison_mode="exact",
        order=58,
        tags=["Hashing", "Hash Set", "Two Sum"],
        hints=[
            "Use a Hash Set to remember numbers you have inspected so far.",
            "For each number x in arr, check if (target - x) is present in the set.",
            "If yes, return True. If not, add x to the set."
        ],
        examples=[
            {"input": "arr = [0, -1, 2, -3, 1], target = -2", "output": "True", "explanation": "(-3) + 1 = -2."},
            {"input": "arr = [1, 2, 3], target = 10", "output": "False", "explanation": "No two numbers sum to 10."}
        ],
        explanation={
            "intuition": "As we scan through the array, the required matching complement is (target - x). Checking presence in a hash set takes O(1).",
            "brute_force": "Two nested loops checking all pairs in O(N^2).",
            "optimal_approach": "seen = set(); for x in arr: if (target - x) in seen: return True; seen.add(x); return False.",
            "dry_run": "[0, -1, 2, -3, 1], target = -2:\nx=0: -2 not in seen, add 0\nx=-1: -1 not in seen, add -1\nx=2: -4 not in seen, add 2\nx=-3: 1 not in seen, add -3\nx=1: -3 is in seen! Return True.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(N) for set.",
            "common_mistakes": "Checking complement after adding current element to the set (can match element with itself).",
            "interview_questions": "How does this compare with the sorting + two-pointer approach? (Hash set is O(N) time and O(N) space; Two-pointer is O(N log N) time and O(1) space)."
        }
    ),
    Problem(
        id="pair-with-given-difference",
        title="Find Pair with Given Difference",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.3: Hash Map",
        difficulty="Easy",
        description="Given an array of integers arr and a non-negative integer diff, determine if there exists a pair of distinct indices (i, j) such that arr[i] - arr[j] == diff. Return True if such a pair exists, otherwise False.",
        input_format="A list of integers arr and an integer diff.",
        output_format="Return True or False.",
        constraints=["2 <= len(arr) <= 10^5", "0 <= diff <= 10^9", "-10^9 <= arr[i] <= 10^9"],
        function_name="hasPairWithDifference",
        param_names=["arr", "diff"],
        starter_code={
            "python": "class Solution:\n    def hasPairWithDifference(self, arr: list[int], diff: int) -> bool:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    bool hasPairWithDifference(vector<int>& arr, int diff) {\n        return false;\n    }\n};",
            "java": "class Solution {\n    public boolean hasPairWithDifference(int[] arr, int diff) {\n        return false;\n    }\n}",
            "javascript": "class Solution {\n    hasPairWithDifference(arr, diff) {\n        return false;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [5, 20, 3, 2, 50, 80], "diff": 78}, expected_output=True, is_hidden=False, explanation="80 - 2 = 78."),
            TestCase(id=2, input_data={"arr": [90, 70, 20, 80, 50], "diff": 45}, expected_output=False, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, 2, 3], "diff": 0}, expected_output=False, is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 1, 3], "diff": 0}, expected_output=True, is_hidden=True),
        ],
        comparison_mode="exact",
        order=59,
        tags=["Hashing", "Hash Set", "Difference"],
        hints=[
            "For each element x, we are looking for either (x + diff) or (x - diff).",
            "Be careful when diff == 0: we need at least two occurrences of the same number.",
            "Use a frequency hash map or a set while carefully distinguishing distinct indices."
        ],
        examples=[
            {"input": "arr = [5, 20, 3, 2, 50, 80], diff = 78", "output": "True", "explanation": "80 - 2 = 78."},
            {"input": "arr = [1, 2, 3], diff = 0", "output": "False", "explanation": "No duplicate elements to make difference 0."}
        ],
        explanation={
            "intuition": "If arr[i] - arr[j] = diff, then arr[i] = arr[j] + diff. Looking up (x - diff) or (x + diff) in a hash set achieves O(1) matching.",
            "brute_force": "Compare all pairs (i, j) with i != j in O(N^2).",
            "optimal_approach": "seen = set(). If diff == 0: count frequencies; return True if any count >= 2. Else: for x in arr: if (x - diff) in seen or (x + diff) in seen: return True; seen.add(x). Return False.",
            "dry_run": "[5, 20, 80, 2], diff=78:\nx=5: add 5\nx=20: add 20\nx=80: 80 - 78 = 2 (not seen), 80 + 78 (not seen), add 80\nx=2: 2 + 78 = 80 (seen!). Return True.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(N) for set.",
            "common_mistakes": "Returning True for diff = 0 on an array with only unique elements.",
            "interview_questions": "How can this be solved using two pointers after sorting?"
        }
    ),
    Problem(
        id="longest-consecutive-sequence-hash",
        title="Longest Consecutive Sequence Using Hash Set",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.2: Hash Set",
        difficulty="Medium",
        description="Given an unsorted array of integers arr, return the length of the longest consecutive elements sequence using a Hash Set in O(n) time.",
        input_format="A list of integers arr.",
        output_format="Return the maximum sequence length as an integer.",
        constraints=["0 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="longestConsecutiveSet",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def longestConsecutiveSet(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int longestConsecutiveSet(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int longestConsecutiveSet(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    longestConsecutiveSet(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [100, 4, 200, 1, 3, 2]}, expected_output=4, is_hidden=False),
            TestCase(id=2, input_data={"arr": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]}, expected_output=9, is_hidden=False),
            TestCase(id=3, input_data={"arr": []}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"arr": [5]}, expected_output=1, is_hidden=True),
        ],
        comparison_mode="exact",
        order=60,
        tags=["Hashing", "Hash Set", "Consecutive"],
        hints=[
            "Insert all elements into a Hash Set.",
            "An element x is the START of a consecutive sequence if (x - 1) is NOT in the set.",
            "For each starting element, count how many successive elements (x+1, x+2...) exist in the set."
        ],
        examples=[
            {"input": "arr = [100, 4, 200, 1, 3, 2]", "output": "4", "explanation": "Consecutive sequence is [1, 2, 3, 4]."},
            {"input": "arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]", "output": "9", "explanation": "Sequence 0..8 has length 9."}
        ],
        explanation={
            "intuition": "Every consecutive sequence has a unique minimum element. Identifying and expanding only from sequence starts guarantees O(N) overall time.",
            "brute_force": "Sort array in O(N log N).",
            "optimal_approach": "s = set(arr); max_len = 0. For x in s: if (x - 1) not in s: curr = x; length = 1; while (curr + 1) in s: curr += 1; length += 1; max_len = max(max_len, length). Return max_len.",
            "dry_run": "[100, 4, 200, 1, 3, 2]: set={1,2,3,4,100,200}.\n1 has no 0 in set: counts 1,2,3,4 -> len 4.\n100 has no 99: len 1.\n200 has no 199: len 1.\nMax is 4.",
            "time_complexity": "O(N) linear time.",
            "space_complexity": "O(N) for Hash Set.",
            "common_mistakes": "Expanding sequences from every element instead of only sequence heads.",
            "interview_questions": "Why does checking `(x - 1) not in s` ensure linear time complexity?"
        }
    ),
    Problem(
        id="zero-sum-subarray-exists",
        title="Check if Subarray with Zero Sum Exists",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.4: Prefix Hashing",
        difficulty="Easy",
        description="Given an array of integers arr, determine if there exists a contiguous subarray with sum equal to 0. Return True if found, otherwise False.",
        input_format="A list of integers arr.",
        output_format="Return True or False.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="hasZeroSumSubarray",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def hasZeroSumSubarray(self, arr: list[int]) -> bool:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    bool hasZeroSumSubarray(vector<int>& arr) {\n        return false;\n    }\n};",
            "java": "class Solution {\n    public boolean hasZeroSumSubarray(int[] arr) {\n        return false;\n    }\n}",
            "javascript": "class Solution {\n    hasZeroSumSubarray(arr) {\n        return false;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [4, 2, -3, 1, 6]}, expected_output=True, is_hidden=False, explanation="Subarray [2, -3, 1] sums to 0."),
            TestCase(id=2, input_data={"arr": [4, 2, 0, 1, 6]}, expected_output=True, is_hidden=False, explanation="Subarray [0] has sum 0."),
            TestCase(id=3, input_data={"arr": [1, 2, 3]}, expected_output=False, is_hidden=False),
            TestCase(id=4, input_data={"arr": [-3, 2, 3, 1, 6]}, expected_output=False, is_hidden=True),
        ],
        comparison_mode="exact",
        order=61,
        tags=["Hashing", "Prefix Sum", "Subarrays"],
        hints=[
            "Compute prefix sums as you iterate through the array.",
            "If current prefix sum is 0, or if this prefix sum has been seen before in our set, then the subarray between the two identical prefix sum indices has sum 0!",
            "Store seen prefix sums in a Hash Set."
        ],
        examples=[
            {"input": "arr = [4, 2, -3, 1, 6]", "output": "True", "explanation": "[2, -3, 1] sums to 0."},
            {"input": "arr = [1, 2, 3]", "output": "False", "explanation": "No subarray sums to 0."}
        ],
        explanation={
            "intuition": "If prefix_sum[j] == prefix_sum[i], then the sum of elements from index i+1 to j is prefix_sum[j] - prefix_sum[i] = 0.",
            "brute_force": "Compute sum of all subarrays in O(N^2).",
            "optimal_approach": "prefix_set = {0}; curr = 0; for x in arr: curr += x; if curr in prefix_set: return True; prefix_set.add(curr); return False.",
            "dry_run": "[4, 2, -3, 1, 6]:\nprefix_set = {0}\nx=4: sum=4, add 4\nx=2: sum=6, add 6\nx=-3: sum=3, add 3\nx=1: sum=4 -> 4 is in prefix_set! Return True.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(N) for set.",
            "common_mistakes": "Forgetting that a single 0 element is itself a valid zero-sum subarray.",
            "interview_questions": "How can you find the length of the largest subarray with 0 sum? (Store first occurrence index of each prefix sum)."
        }
    ),
    Problem(
        id="longest-subarray-sum-k-hashing",
        title="Longest Subarray with Sum K (Including Negatives)",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.4: Prefix Hashing",
        difficulty="Medium",
        description="Given an array arr containing both positive and negative integers, find the length of the longest contiguous subarray whose sum is equal to k. If no such subarray exists, return 0.",
        input_format="A list of integers arr and integer k.",
        output_format="Return the maximum length as an integer.",
        constraints=["1 <= len(arr) <= 10^5", "-10^5 <= arr[i] <= 10^5", "-10^9 <= k <= 10^9"],
        function_name="longestSubarrayWithSumK",
        param_names=["arr", "k"],
        starter_code={
            "python": "class Solution:\n    def longestSubarrayWithSumK(self, arr: list[int], k: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int longestSubarrayWithSumK(vector<int>& arr, int k) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int longestSubarrayWithSumK(int[] arr, int k) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    longestSubarrayWithSumK(arr, k) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [10, 5, 2, 7, 1, 9], "k": 15}, expected_output=4, is_hidden=False, explanation="Subarray [5, 2, 7, 1] has sum 15, length 4."),
            TestCase(id=2, input_data={"arr": [-1, 2, 3], "k": 6}, expected_output=0, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, -1, 1, -1, 1], "k": 0}, expected_output=4, is_hidden=False),
            TestCase(id=4, input_data={"arr": [2, 0, 0, 3], "k": 3}, expected_output=3, is_hidden=True),
        ],
        comparison_mode="exact",
        order=62,
        tags=["Hashing", "Prefix Sum", "Hash Map"],
        hints=[
            "Maintain a running prefix sum.",
            "If prefix_sum == k, subarray from 0 to i has length i + 1.",
            "Otherwise, if (prefix_sum - k) is in hash map, length is i - map[prefix_sum - k]. Store only the EARLIEST index for each prefix sum to maximize length!"
        ],
        examples=[
            {"input": "arr = [10, 5, 2, 7, 1, 9], k = 15", "output": "4", "explanation": "[5, 2, 7, 1] has sum 15 with length 4."},
            {"input": "arr = [1, -1, 1, -1], k = 0", "output": "4", "explanation": "Entire array sums to 0."}
        ],
        explanation={
            "intuition": "By recording only the first index at which each prefix sum is encountered, we ensure the distance i - first_seen[prefix - k] is as large as possible.",
            "brute_force": "Test all subarray spans in O(N^2).",
            "optimal_approach": "first_seen = {}; curr_sum = 0; max_len = 0. For i, x in enumerate(arr): curr_sum += x; if curr_sum == k: max_len = i + 1; rem = curr_sum - k; if rem in first_seen: max_len = max(max_len, i - first_seen[rem]); if curr_sum not in first_seen: first_seen[curr_sum] = i. Return max_len.",
            "dry_run": "[10, 5, 2, 7, 1], k = 15:\ni=0 (10): sum=10, map={10:0}\ni=1 (5): sum=15 == k -> max_len=2, map={10:0, 15:1}\ni=2 (2): sum=17, rem=2 (not in map), map={..., 17:2}\ni=3 (7): sum=24, rem=9 (not in map), map={..., 24:3}\ni=4 (1): sum=25, rem=10 -> in map at idx 0! len = 4 - 0 = 4. max_len = max(2, 4) = 4.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(N) for hash map.",
            "common_mistakes": "Overwriting existing prefix sum indices in the hash map (which shrinks subarray lengths).",
            "interview_questions": "Why is this preferable over the two-pointer sliding window when negative numbers are present?"
        }
    ),
    Problem(
        id="count-subarrays-xor-k",
        title="Count Subarrays with Given XOR K",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.4: Prefix Hashing",
        difficulty="Medium",
        description="Given an array of integers arr and an integer k, find the total number of continuous subarrays having bitwise XOR of their elements equal to k.",
        input_format="A list of integers arr and integer k.",
        output_format="Return the count of subarrays as an integer.",
        constraints=["1 <= len(arr) <= 10^5", "0 <= arr[i], k <= 10^9"],
        function_name="countSubarraysWithXorK",
        param_names=["arr", "k"],
        starter_code={
            "python": "class Solution:\n    def countSubarraysWithXorK(self, arr: list[int], k: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int countSubarraysWithXorK(vector<int>& arr, int k) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int countSubarraysWithXorK(int[] arr, int k) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    countSubarraysWithXorK(arr, k) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [4, 2, 2, 6, 4], "k": 6}, expected_output=4, is_hidden=False),
            TestCase(id=2, input_data={"arr": [5, 6, 7, 8, 9], "k": 5}, expected_output=2, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, 1, 1], "k": 1}, expected_output=4, is_hidden=False),
            TestCase(id=4, input_data={"arr": [0, 0, 0], "k": 0}, expected_output=6, is_hidden=True),
        ],
        comparison_mode="exact",
        order=63,
        tags=["Hashing", "Bit Manipulation", "Prefix XOR"],
        hints=[
            "Prefix XOR behaves identically to prefix sum.",
            "If prefix_xor[i..j] == k, then (pref[j] ^ pref[i-1]) == k.",
            "XORing both sides by k gives pref[i-1] = pref[j] ^ k. Use a frequency map of prefix XORs!"
        ],
        examples=[
            {"input": "arr = [4, 2, 2, 6, 4], k = 6", "output": "4", "explanation": "The 4 valid subarrays are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]."},
            {"input": "arr = [5, 6, 7, 8, 9], k = 5", "output": "2", "explanation": "Subarrays [5] and [5, 6, 7, 8, 9] (5^6^7^8^9 = 5)."}
        ],
        explanation={
            "intuition": "XOR property: If X ^ Y = K, then X ^ K = Y. We store counts of prefix XORs in a hash map.",
            "brute_force": "Check XOR of all O(N^2) subarrays.",
            "optimal_approach": "xor_counts = {0: 1}; curr_xor = 0; ans = 0. For x in arr: curr_xor ^= x; target = curr_xor ^ k; if target in xor_counts: ans += xor_counts[target]; xor_counts[curr_xor] = xor_counts.get(curr_xor, 0) + 1. Return ans.",
            "dry_run": "[4, 2, 2, 6, 4], k = 6:\ninit: {0: 1}\nx=4: curr=4, target=4^6=2 (0), {0:1, 4:1}\nx=2: curr=6, target=6^6=0 (in map: +1), ans=1, {0:1, 4:1, 6:1}\nContinues to find all 4 subarrays.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(N) for frequency map.",
            "common_mistakes": "Forgetting to initialize map with {0: 1}.",
            "interview_questions": "How does prefix XOR cancellation relate to prefix sums?"
        }
    ),
    Problem(
        id="group-anagrams-hash",
        title="Group Anagrams Using Hashing",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.3: Hash Map",
        difficulty="Medium",
        description="Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase.",
        input_format="A list of strings strs.",
        output_format="Return a list of grouped lists of strings.",
        constraints=["1 <= len(strs) <= 10^4", "0 <= len(strs[i]) <= 100", "strs[i] consists of lowercase English letters."],
        function_name="groupAnagrams",
        param_names=["strs"],
        starter_code={
            "python": "class Solution:\n    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<vector<string>> groupAnagrams(vector<string>& strs) {\n        return {};\n    }\n};",
            "java": "class Solution {\n    public List<List<String>> groupAnagrams(String[] strs) {\n        return new ArrayList<>();\n    }\n}",
            "javascript": "class Solution {\n    groupAnagrams(strs) {\n        return [];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"strs": ["eat", "tea", "tan", "ate", "nat", "bat"]}, expected_output=[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]], is_hidden=False),
            TestCase(id=2, input_data={"strs": [""]}, expected_output=[[""]], is_hidden=False),
            TestCase(id=3, input_data={"strs": ["a"]}, expected_output=[["a"]], is_hidden=False),
            TestCase(id=4, input_data={"strs": ["listen", "silent", "enlist"]}, expected_output=[["listen", "silent", "enlist"]], is_hidden=True),
        ],
        comparison_mode="unordered",
        order=64,
        tags=["Hashing", "Strings", "Anagrams"],
        hints=[
            "Two strings are anagrams if and only if their sorted versions are identical.",
            "Can you use the sorted string as a hash map key?",
            "Alternatively, use a 26-element character frequency tuple as the key to avoid sorting."
        ],
        examples=[
            {"input": "strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']", "output": "[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]", "explanation": "Anagrams share identical character counts."},
            {"input": "strs = ['a']", "output": "[['a']]", "explanation": "Single word."}
        ],
        explanation={
            "intuition": "Anagrams map to the same canonical representation. We can group them by mapping canonical representation -> list of words.",
            "brute_force": "Compare every pair of strings to check if they are anagrams in O(N^2 * L).",
            "optimal_approach": "groups = defaultdict(list). For word in strs: key = ''.join(sorted(word)); groups[key].append(word). Return list(groups.values()).",
            "dry_run": "'eat', 'tea': sorted('eat') = 'aet', sorted('tea') = 'aet' -> both grouped under 'aet'.",
            "time_complexity": "O(N * L log L) where L is max word length.",
            "space_complexity": "O(N * L)",
            "common_mistakes": "Using mutable lists as dictionary keys instead of strings or tuples.",
            "interview_questions": "How to achieve O(N * L) without sorting? (Use a 26-tuple of character counts as the dictionary key)."
        }
    ),
    Problem(
        id="isomorphic-strings-hash",
        title="Check if Two Strings are Isomorphic",
        step_id=4,
        step_title="Step 4: Hashing",
        subtopic="4.3: Hash Map",
        difficulty="Easy",
        description="Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t, with a 1-to-1 bijection: no two characters may map to the same character, but a character may map to itself.",
        input_format="Two strings s and t of equal length.",
        output_format="Return True if isomorphic, False otherwise.",
        constraints=["1 <= len(s) == len(t) <= 10^5"],
        function_name="isIsomorphic",
        param_names=["s", "t"],
        starter_code={
            "python": "class Solution:\n    def isIsomorphic(self, s: str, t: str) -> bool:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    bool isIsomorphic(string s, string t) {\n        return false;\n    }\n};",
            "java": "class Solution {\n    public boolean isIsomorphic(String s, String t) {\n        return false;\n    }\n}",
            "javascript": "class Solution {\n    isIsomorphic(s, t) {\n        return false;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"s": "egg", "t": "add"}, expected_output=True, is_hidden=False, explanation="'e'->'a', 'g'->'d'."),
            TestCase(id=2, input_data={"s": "foo", "t": "bar"}, expected_output=False, is_hidden=False, explanation="'o' cannot map to both 'a' and 'r'."),
            TestCase(id=3, input_data={"s": "paper", "t": "title"}, expected_output=True, is_hidden=False),
            TestCase(id=4, input_data={"s": "badc", "t": "baba"}, expected_output=False, is_hidden=True, explanation="'d' and 'b' both try to map to 'b'."),
        ],
        comparison_mode="exact",
        order=65,
        tags=["Hashing", "Strings", "Mapping"],
        hints=[
            "The mapping must be a two-way bijection (s -> t and t -> s).",
            "Maintain two dictionaries: map_s_to_t and map_t_to_s.",
            "If s[i] was already mapped to a different char in t, or vice versa, return False."
        ],
        examples=[
            {"input": "s = 'egg', t = 'add'", "output": "True", "explanation": "Consistent mapping: e->a, g->d."},
            {"input": "s = 'foo', t = 'bar'", "output": "False", "explanation": "'o' maps to both 'a' and 'r'."}
        ],
        explanation={
            "intuition": "Every character in s must map uniquely to a character in t, and no two characters in s can map to the same character in t.",
            "brute_force": "Check transformation consistency for each character position.",
            "optimal_approach": "s2t = {}; t2s = {}. For c1, c2 in zip(s, t): if (c1 in s2t and s2t[c1] != c2) or (c2 in t2s and t2s[c2] != c1): return False; s2t[c1] = c2; t2s[c2] = c1. Return True.",
            "dry_run": "s='egg', t='add':\ne->a (t2s: a->e)\ng->d (t2s: d->g)\ng->d (matches existing mapping). Return True.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(K) where K is character set size.",
            "common_mistakes": "Checking only one direction mapping (s -> t) without checking reverse (t -> s).",
            "interview_questions": "How does this relate to the Word Pattern problem?"
        }
    ),
]
