from models import Problem, TestCase

MODULE_5_PROBLEMS = [
    Problem(
        id="binary-search-iterative",
        title="Standard Binary Search on Sorted Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Easy",
        description="Given an array of integers arr sorted in ascending order and an integer target, write a function to search target in arr. If target exists, return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.",
        input_format="A sorted list of integers arr and integer target.",
        output_format="Return the 0-based index or -1.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i], target <= 10^9", "All elements in arr are unique."],
        function_name="search",
        param_names=["arr", "target"],
        starter_code={
            "python": "class Solution:\n    def search(self, arr: list[int], target: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int search(vector<int>& arr, int target) {\n        return -1;\n    }\n};",
            "java": "class Solution {\n    public int search(int[] arr, int target) {\n        return -1;\n    }\n}",
            "javascript": "class Solution {\n    search(arr, target) {\n        return -1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [-1, 0, 3, 5, 9, 12], "target": 9}, expected_output=4, is_hidden=False),
            TestCase(id=2, input_data={"arr": [-1, 0, 3, 5, 9, 12], "target": 2}, expected_output=-1, is_hidden=False),
            TestCase(id=3, input_data={"arr": [5], "target": 5}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"arr": [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], "target": 23}, expected_output=5, is_hidden=True),
        ],
        comparison_mode="exact",
        order=66,
        tags=["Binary Search", "Divide and Conquer", "Basics"],
        hints=[
            "Maintain search space pointers: low = 0, high = len(arr) - 1.",
            "Calculate mid = low + (high - low) // 2.",
            "If arr[mid] == target return mid. If arr[mid] < target, search right (low = mid + 1). Else search left (high = mid - 1)."
        ],
        examples=[
            {"input": "arr = [-1, 0, 3, 5, 9, 12], target = 9", "output": "4", "explanation": "9 exists at index 4."},
            {"input": "arr = [-1, 0, 3, 5, 9, 12], target = 2", "output": "-1", "explanation": "2 does not exist."}
        ],
        explanation={
            "intuition": "Halving the search space at each comparison enables finding an element in logarithmic time.",
            "brute_force": "Linear search in O(N).",
            "optimal_approach": "low = 0, high = len(arr)-1. While low <= high: mid = (low + high) // 2. If arr[mid] == target: return mid. Elif arr[mid] < target: low = mid + 1. Else: high = mid - 1. Return -1.",
            "dry_run": "arr = [-1, 0, 3, 5, 9, 12], target = 9:\nlow=0, high=5 -> mid=2, arr[2]=3 < 9 -> low=3\nlow=3, high=5 -> mid=4, arr[4]=9 == 9 -> return 4.",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Overflowing integer mid calculation in C++/Java (use low + (high - low) / 2).",
            "interview_questions": "How does binary search behave on an infinite stream of sorted data? (Exponential search followed by binary search)."
        }
    ),
    Problem(
        id="lower-bound-binary-search",
        title="Implement Lower Bound in Sorted Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Easy",
        description="Given a sorted array of integers arr and a target value x, find the lower bound of x. The lower bound is the smallest index idx such that arr[idx] >= x. If all elements are smaller than x, return len(arr).",
        input_format="A sorted list of integers arr and integer target x.",
        output_format="Return the lower bound index as an integer.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i], x <= 10^9"],
        function_name="lowerBound",
        param_names=["arr", "x"],
        starter_code={
            "python": "class Solution:\n    def lowerBound(self, arr: list[int], x: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int lowerBound(vector<int>& arr, int x) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int lowerBound(int[] arr, int x) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    lowerBound(arr, x) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 8, 10, 11, 12, 19], "x": 0}, expected_output=0, is_hidden=False),
            TestCase(id=2, input_data={"arr": [1, 2, 8, 10, 11, 12, 19], "x": 5}, expected_output=2, is_hidden=False, explanation="arr[2] = 8 is the smallest element >= 5."),
            TestCase(id=3, input_data={"arr": [1, 2, 8, 10, 11, 12, 19], "x": 20}, expected_output=7, is_hidden=False),
            TestCase(id=4, input_data={"arr": [3, 5, 8, 15, 19], "x": 8}, expected_output=2, is_hidden=True),
        ],
        comparison_mode="exact",
        order=67,
        tags=["Binary Search", "Bounds"],
        hints=[
            "Condition to look for: arr[mid] >= x.",
            "If arr[mid] >= x, this mid is a potential answer, but there could be an even smaller valid index to the left! Record ans = mid and shrink right: high = mid - 1.",
            "If arr[mid] < x, search right: low = mid + 1."
        ],
        examples=[
            {"input": "arr = [1, 2, 8, 10, 11, 12, 19], x = 5", "output": "2", "explanation": "arr[2] = 8 >= 5."},
            {"input": "arr = [1, 2, 3], x = 4", "output": "3", "explanation": "No element >= 4, returns len(arr) = 3."}
        ],
        explanation={
            "intuition": "Lower bound finds the first insertion point that maintains sorted order for an element.",
            "brute_force": "Linear scan finding first index with arr[i] >= x in O(N).",
            "optimal_approach": "low = 0, high = len(arr)-1, ans = len(arr). While low <= high: mid = (low+high)//2. If arr[mid] >= x: ans = mid; high = mid - 1. Else: low = mid + 1. Return ans.",
            "dry_run": "[1, 2, 8, 10], x = 5:\nlow=0, high=3 -> mid=1, arr[1]=2 < 5 -> low=2\nlow=2, high=3 -> mid=2, arr[2]=8 >= 5 -> ans=2, high=1\nLoop ends. Return ans = 2.",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Returning -1 when x is greater than all elements instead of len(arr).",
            "interview_questions": "How does lower bound relate to C++ std::lower_bound or Python bisect_left?"
        }
    ),
    Problem(
        id="upper-bound-binary-search",
        title="Implement Upper Bound in Sorted Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Easy",
        description="Given a sorted array of integers arr and a target value x, find the upper bound of x. The upper bound is the smallest index idx such that arr[idx] > x. If no such element exists, return len(arr).",
        input_format="A sorted list of integers arr and integer x.",
        output_format="Return the upper bound index as an integer.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i], x <= 10^9"],
        function_name="upperBound",
        param_names=["arr", "x"],
        starter_code={
            "python": "class Solution:\n    def upperBound(self, arr: list[int], x: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int upperBound(vector<int>& arr, int x) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int upperBound(int[] arr, int x) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    upperBound(arr, x) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [2, 3, 6, 7, 8, 8, 11, 11, 12], "x": 6}, expected_output=3, is_hidden=False, explanation="arr[3] = 7 is the first element strictly > 6."),
            TestCase(id=2, input_data={"arr": [2, 3, 6, 7, 8, 8, 11, 11, 12], "x": 11}, expected_output=8, is_hidden=False, explanation="arr[8] = 12 is first element strictly > 11."),
            TestCase(id=3, input_data={"arr": [1, 2, 3], "x": 5}, expected_output=3, is_hidden=False),
            TestCase(id=4, input_data={"arr": [5, 5, 5], "x": 2}, expected_output=0, is_hidden=True),
        ],
        comparison_mode="exact",
        order=68,
        tags=["Binary Search", "Bounds"],
        hints=[
            "Condition: arr[mid] > x (strictly greater).",
            "If arr[mid] > x, this mid is a candidate. Record ans = mid and search left: high = mid - 1.",
            "If arr[mid] <= x, search right: low = mid + 1."
        ],
        examples=[
            {"input": "arr = [2, 3, 6, 7, 8], x = 6", "output": "3", "explanation": "arr[3] = 7 > 6."},
            {"input": "arr = [1, 2, 3], x = 3", "output": "3", "explanation": "No element strictly > 3."}
        ],
        explanation={
            "intuition": "Upper bound finds the first element strictly greater than x, which corresponds to bisect_right.",
            "brute_force": "Linear scan for arr[i] > x in O(N).",
            "optimal_approach": "low = 0, high = len(arr)-1, ans = len(arr). While low <= high: mid = (low+high)//2. If arr[mid] > x: ans = mid; high = mid - 1. Else: low = mid + 1. Return ans.",
            "dry_run": "[2, 6, 7], x = 6:\nlow=0, high=2 -> mid=1, arr[1]=6 <= 6 -> low=2\nlow=2, high=2 -> mid=2, arr[2]=7 > 6 -> ans=2, high=1. Return 2.",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Using >= instead of > (that would be lower bound).",
            "interview_questions": "How do you count occurrences of x in sorted array using upper_bound and lower_bound? (count = upper_bound(x) - lower_bound(x))."
        }
    ),
    Problem(
        id="search-insert-position",
        title="Search Insert Position in Sorted Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Easy",
        description="Given a sorted array of distinct integers arr and a target value target, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.",
        input_format="A sorted list of integers arr and integer target.",
        output_format="Return the index as an integer.",
        constraints=["1 <= len(arr) <= 10^5", "-10^4 <= arr[i], target <= 10^4"],
        function_name="searchInsert",
        param_names=["arr", "target"],
        starter_code={
            "python": "class Solution:\n    def searchInsert(self, arr: list[int], target: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int searchInsert(vector<int>& arr, int target) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int searchInsert(int[] arr, int target) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    searchInsert(arr, target) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 3, 5, 6], "target": 5}, expected_output=2, is_hidden=False),
            TestCase(id=2, input_data={"arr": [1, 3, 5, 6], "target": 2}, expected_output=1, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, 3, 5, 6], "target": 7}, expected_output=4, is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 3, 5, 6], "target": 0}, expected_output=0, is_hidden=True),
        ],
        comparison_mode="exact",
        order=69,
        tags=["Binary Search", "Bounds"],
        hints=[
            "Notice that search insert position is identical to finding the Lower Bound of target!",
            "Find the smallest index where arr[mid] >= target.",
            "If target is larger than all elements, the insert position is len(arr)."
        ],
        examples=[
            {"input": "arr = [1, 3, 5, 6], target = 5", "output": "2", "explanation": "5 found at index 2."},
            {"input": "arr = [1, 3, 5, 6], target = 2", "output": "1", "explanation": "2 would be inserted at index 1."}
        ],
        explanation={
            "intuition": "The insert position for target is precisely the first index where arr[i] >= target, which is lower bound.",
            "brute_force": "Linear scan in O(N).",
            "optimal_approach": "low = 0, high = len(arr) - 1, ans = len(arr). While low <= high: mid = (low + high) // 2. If arr[mid] >= target: ans = mid; high = mid - 1. Else: low = mid + 1. Return ans.",
            "dry_run": "[1, 3, 5, 6], target = 2:\nmid=1, arr[1]=3 >= 2 -> ans=1, high=0\nmid=0, arr[0]=1 < 2 -> low=1. Loop terminates, return 1.",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Not returning len(arr) when target > arr[-1].",
            "interview_questions": "What happens if there are duplicate elements? (Lower bound returns the position before any duplicate)."
        }
    ),
    Problem(
        id="floor-and-ceil-sorted",
        title="Floor and Ceil in Sorted Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Easy",
        description="Given a sorted array of integers arr and a value x, find the floor and ceil of x in the array. The floor is the largest element <= x, and ceil is the smallest element >= x. Return a list [floor, ceil]. If either does not exist, use -1.",
        input_format="A sorted list of integers arr and integer x.",
        output_format="Return a list [floor, ceil].",
        constraints=["1 <= len(arr) <= 10^5", "1 <= arr[i], x <= 10^9"],
        function_name="getFloorAndCeil",
        param_names=["arr", "x"],
        starter_code={
            "python": "class Solution:\n    def getFloorAndCeil(self, arr: list[int], x: int) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> getFloorAndCeil(vector<int>& arr, int x) {\n        return {-1, -1};\n    }\n};",
            "java": "class Solution {\n    public int[] getFloorAndCeil(int[] arr, int x) {\n        return new int[]{-1, -1};\n    }\n}",
            "javascript": "class Solution {\n    getFloorAndCeil(arr, x) {\n        return [-1, -1];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [3, 4, 4, 7, 8, 10], "x": 5}, expected_output=[4, 7], is_hidden=False),
            TestCase(id=2, input_data={"arr": [3, 4, 4, 7, 8, 10], "x": 2}, expected_output=[-1, 3], is_hidden=False),
            TestCase(id=3, input_data={"arr": [3, 4, 4, 7, 8, 10], "x": 12}, expected_output=[10, -1], is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 2, 8, 10], "x": 8}, expected_output=[8, 8], is_hidden=True),
        ],
        comparison_mode="exact",
        order=70,
        tags=["Binary Search", "Floor", "Ceil"],
        hints=[
            "Floor: largest element in arr <= x. Search right whenever arr[mid] <= x.",
            "Ceil: smallest element in arr >= x (lower bound value). Search left whenever arr[mid] >= x.",
            "Both can be calculated via two independent binary search routines or in one pass."
        ],
        examples=[
            {"input": "arr = [3, 4, 4, 7, 8, 10], x = 5", "output": "[4, 7]", "explanation": "4 is largest <= 5; 7 is smallest >= 5."},
            {"input": "arr = [3, 4, 7], x = 2", "output": "[-1, 3]", "explanation": "No element <= 2, so floor is -1."}
        ],
        explanation={
            "intuition": "Floor requires maximizing arr[mid] <= x, while Ceil requires minimizing arr[mid] >= x.",
            "brute_force": "Linear scan tracking floor and ceil in O(N).",
            "optimal_approach": "Binary search for floor (if arr[mid] <= x: floor = arr[mid], low = mid + 1 else: high = mid - 1). Binary search for ceil (if arr[mid] >= x: ceil = arr[mid], high = mid - 1 else: low = mid + 1). Return [floor, ceil].",
            "dry_run": "[3, 4, 7], x = 5:\nFloor BS: mid=1 (4) <= 5 -> floor=4, low=2. mid=2 (7) > 5 -> high=1. Floor = 4.\nCeil BS: mid=1 (4) < 5 -> low=2. mid=2 (7) >= 5 -> ceil=7, high=1. Ceil = 7.\nReturn [4, 7].",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Returning indices instead of element values.",
            "interview_questions": "How is floor/ceil used in continuous time query systems like financial tick data?"
        }
    ),
    Problem(
        id="first-and-last-occurrence",
        title="First and Last Position of Element in Sorted Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Medium",
        description="Given an array of integers arr sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.",
        input_format="A sorted list of integers arr and integer target.",
        output_format="Return a list of two integers [first_pos, last_pos].",
        constraints=["0 <= len(arr) <= 10^5", "-10^9 <= arr[i], target <= 10^9"],
        function_name="searchRange",
        param_names=["arr", "target"],
        starter_code={
            "python": "class Solution:\n    def searchRange(self, arr: list[int], target: int) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> searchRange(vector<int>& arr, int target) {\n        return {-1, -1};\n    }\n};",
            "java": "class Solution {\n    public int[] searchRange(int[] arr, int target) {\n        return new int[]{-1, -1};\n    }\n}",
            "javascript": "class Solution {\n    searchRange(arr, target) {\n        return [-1, -1];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [5, 7, 7, 8, 8, 10], "target": 8}, expected_output=[3, 4], is_hidden=False),
            TestCase(id=2, input_data={"arr": [5, 7, 7, 8, 8, 10], "target": 6}, expected_output=[-1, -1], is_hidden=False),
            TestCase(id=3, input_data={"arr": [], "target": 0}, expected_output=[-1, -1], is_hidden=False),
            TestCase(id=4, input_data={"arr": [1], "target": 1}, expected_output=[0, 0], is_hidden=True),
            TestCase(id=5, input_data={"arr": [2, 2, 2, 2, 2], "target": 2}, expected_output=[0, 4], is_hidden=True),
        ],
        comparison_mode="exact",
        order=71,
        tags=["Binary Search", "Bounds", "Occurrences"],
        hints=[
            "Find the first position using lower bound: first index where arr[mid] == target (continue searching left).",
            "Find the last position by searching right whenever arr[mid] == target.",
            "If target is not found in the first search, you can immediately return [-1, -1]."
        ],
        examples=[
            {"input": "arr = [5, 7, 7, 8, 8, 10], target = 8", "output": "[3, 4]", "explanation": "8 starts at index 3 and ends at index 4."},
            {"input": "arr = [5, 7, 7, 8, 8, 10], target = 6", "output": "[-1, -1]", "explanation": "6 is not in array."}
        ],
        explanation={
            "intuition": "Two separate binary searches: one biased to the left to find the first occurrence, one biased to the right to find the last occurrence.",
            "brute_force": "Linear scan finding first and last matches in O(N).",
            "optimal_approach": "Helper find_first: when arr[mid] == target, ans = mid, high = mid - 1. Helper find_last: when arr[mid] == target, ans = mid, low = mid + 1. Return [find_first(), find_last()].",
            "dry_run": "[5, 7, 7, 8, 8, 10], target = 8:\nfind_first: mid=2 (7) < 8 -> low=3. mid=4 (8) == 8 -> ans=4, high=3. mid=3 (8) == 8 -> ans=3, high=2 -> returns 3.\nfind_last: returns 4. Output [3, 4].",
            "time_complexity": "2 * O(log N) = O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Expanding linearly from a found target (degrades to O(N) if all elements are equal).",
            "interview_questions": "How can you count the total occurrences using these two indices? (count = last - first + 1)."
        }
    ),
    Problem(
        id="count-occurrences-sorted",
        title="Count Occurrences of Number in Sorted Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Easy",
        description="Given a sorted array of integers arr and a target integer target, count the number of occurrences of target in arr in O(log n) time.",
        input_format="A sorted list of integers arr and integer target.",
        output_format="Return the integer count of occurrences.",
        constraints=["0 <= len(arr) <= 10^5", "-10^9 <= arr[i], target <= 10^9"],
        function_name="countOccurrences",
        param_names=["arr", "target"],
        starter_code={
            "python": "class Solution:\n    def countOccurrences(self, arr: list[int], target: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int countOccurrences(vector<int>& arr, int target) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int countOccurrences(int[] arr, int target) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    countOccurrences(arr, target) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 1, 2, 2, 2, 2, 3], "target": 2}, expected_output=4, is_hidden=False),
            TestCase(id=2, input_data={"arr": [1, 1, 2, 2, 2, 2, 3], "target": 4}, expected_output=0, is_hidden=False),
            TestCase(id=3, input_data={"arr": [], "target": 1}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"arr": [7, 7, 7, 7, 7], "target": 7}, expected_output=5, is_hidden=True),
        ],
        comparison_mode="exact",
        order=72,
        tags=["Binary Search", "Counting"],
        hints=[
            "Find the first occurrence index using binary search.",
            "If target does not exist, return 0.",
            "Find the last occurrence index. The answer is (last - first + 1)."
        ],
        examples=[
            {"input": "arr = [1, 1, 2, 2, 2, 2, 3], target = 2", "output": "4", "explanation": "2 appears 4 times at indices 2, 3, 4, 5."},
            {"input": "arr = [1, 2, 3], target = 5", "output": "0", "explanation": "5 is not present."}
        ],
        explanation={
            "intuition": "In a sorted array, all occurrences of target are contiguous. Finding the start and end of this block gives the count in O(log N).",
            "brute_force": "Linear count in O(N).",
            "optimal_approach": "Find first position using binary search. If -1, return 0. Find last position using binary search. Return (last - first + 1).",
            "dry_run": "[1, 2, 2, 3], target = 2:\nfirst = 1, last = 2. count = 2 - 1 + 1 = 2.",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Searching linearly after binary search hits target.",
            "interview_questions": "Can this be written using upper_bound(target) - lower_bound(target)? (Yes, precisely)."
        }
    ),
    Problem(
        id="search-rotated-sorted-array",
        title="Search in Rotated Sorted Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Medium",
        description="There is an integer array arr sorted in ascending order with distinct values. Prior to being passed to your function, arr is possibly rotated at an unknown pivot index. Given array arr and target, return the index of target if it is in arr, or -1 if it is not in arr. You must write an algorithm with O(log n) runtime complexity.",
        input_format="A list of integers arr and integer target.",
        output_format="Return the 0-based index or -1.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i], target <= 10^9", "All elements in arr are unique."],
        function_name="searchRotated",
        param_names=["arr", "target"],
        starter_code={
            "python": "class Solution:\n    def searchRotated(self, arr: list[int], target: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int searchRotated(vector<int>& arr, int target) {\n        return -1;\n    }\n};",
            "java": "class Solution {\n    public int searchRotated(int[] arr, int target) {\n        return -1;\n    }\n}",
            "javascript": "class Solution {\n    searchRotated(arr, target) {\n        return -1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [4, 5, 6, 7, 0, 1, 2], "target": 0}, expected_output=4, is_hidden=False),
            TestCase(id=2, input_data={"arr": [4, 5, 6, 7, 0, 1, 2], "target": 3}, expected_output=-1, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1], "target": 0}, expected_output=-1, is_hidden=False),
            TestCase(id=4, input_data={"arr": [5, 1, 3], "target": 5}, expected_output=0, is_hidden=True),
            TestCase(id=5, input_data={"arr": [4, 5, 6, 7, 8, 1, 2], "target": 8}, expected_output=4, is_hidden=True),
        ],
        comparison_mode="exact",
        order=73,
        tags=["Binary Search", "Rotated Array"],
        hints=[
            "Notice that if you split a rotated sorted array at mid, at least one half (either left or right) is ALWAYS sorted!",
            "Identify which half is sorted: if arr[low] <= arr[mid], the left half is sorted; otherwise the right half is sorted.",
            "Check if target falls within the bounds of the sorted half. If yes, search that half; otherwise search the other half."
        ],
        examples=[
            {"input": "arr = [4, 5, 6, 7, 0, 1, 2], target = 0", "output": "4", "explanation": "0 is at index 4."},
            {"input": "arr = [4, 5, 6, 7, 0, 1, 2], target = 3", "output": "-1", "explanation": "3 is not present."}
        ],
        explanation={
            "intuition": "In any rotated sorted array, splitting at mid always yields at least one perfectly sorted subarray.",
            "brute_force": "Linear search in O(N).",
            "optimal_approach": "low = 0, high = len(arr)-1. While low <= high: mid = (low+high)//2. If arr[mid] == target: return mid. If left half is sorted (arr[low] <= arr[mid]): if arr[low] <= target < arr[mid]: high = mid - 1 else: low = mid + 1. Else (right half sorted): if arr[mid] < target <= arr[high]: low = mid + 1 else: high = mid - 1. Return -1.",
            "dry_run": "[4, 5, 6, 7, 0, 1, 2], target = 0:\nlow=0, high=6 -> mid=3, arr[3]=7.\nLeft half [4..7] is sorted (4 <= 7). Is 0 in [4, 7)? No -> search right: low = 4.\nlow=4, high=6 -> mid=5, arr[5]=1.\nRight half [1..2] sorted. Is 0 in (1, 2]? No -> search left: high = 4.\nlow=4, high=4 -> mid=4, arr[4]=0 == target -> return 4.",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Forgetting the equality conditions when checking range bounds.",
            "interview_questions": "How does this algorithm break down when duplicate elements are allowed?"
        }
    ),
    Problem(
        id="search-rotated-sorted-duplicates",
        title="Search in Rotated Sorted Array with Duplicates",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Medium",
        description="Given an integer array arr sorted in ascending order (not necessarily with distinct values) that has been rotated at an unknown pivot, and an integer target, return True if target is in arr, or False if it is not.",
        input_format="A list of integers arr and integer target.",
        output_format="Return True or False.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i], target <= 10^9"],
        function_name="searchRotatedDuplicates",
        param_names=["arr", "target"],
        starter_code={
            "python": "class Solution:\n    def searchRotatedDuplicates(self, arr: list[int], target: int) -> bool:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    bool searchRotatedDuplicates(vector<int>& arr, int target) {\n        return false;\n    }\n};",
            "java": "class Solution {\n    public boolean searchRotatedDuplicates(int[] arr, int target) {\n        return false;\n    }\n}",
            "javascript": "class Solution {\n    searchRotatedDuplicates(arr, target) {\n        return false;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [2, 5, 6, 0, 0, 1, 2], "target": 0}, expected_output=True, is_hidden=False),
            TestCase(id=2, input_data={"arr": [2, 5, 6, 0, 0, 1, 2], "target": 3}, expected_output=False, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, 0, 1, 1, 1], "target": 0}, expected_output=True, is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 1, 1, 1, 1, 1, 1], "target": 2}, expected_output=False, is_hidden=True),
        ],
        comparison_mode="exact",
        order=74,
        tags=["Binary Search", "Rotated Array", "Duplicates"],
        hints=[
            "When arr[low] == arr[mid] == arr[high], it is impossible to determine which half is sorted.",
            "In that ambiguous case, simply shrink the search space: low += 1 and high -= 1.",
            "Otherwise, apply the standard rotated binary search logic."
        ],
        examples=[
            {"input": "arr = [2, 5, 6, 0, 0, 1, 2], target = 0", "output": "True", "explanation": "0 is present."},
            {"input": "arr = [2, 5, 6, 0, 0, 1, 2], target = 3", "output": "False", "explanation": "3 is not present."}
        ],
        explanation={
            "intuition": "Duplicate values at boundaries can cause arr[low] == arr[mid] == arr[high]. Trimming duplicates restores the ability to identify the sorted half.",
            "brute_force": "Linear search in O(N).",
            "optimal_approach": "While low <= high: mid = (low+high)//2. If arr[mid] == target: return True. If arr[low] == arr[mid] == arr[high]: low += 1; high -= 1; continue. Apply rotated search on left vs right sorted portion.",
            "dry_run": "[1, 0, 1, 1, 1], target = 0:\nlow=0, high=4 -> arr[0]=arr[2]=arr[4]=1 -> low=1, high=3.\nNow arr[1]=0, arr[2]=1, arr[3]=1 -> mid=2 (1). Left sorted: arr[1]=0 <= target 0 <= arr[2]=1 -> high=1. Next mid=1 (arr[1]=0 == target) -> True.",
            "time_complexity": "Average: O(log N). Worst Case: O(N) when all elements are identical.",
            "space_complexity": "O(1)",
            "common_mistakes": "Not checking arr[low] == arr[mid] == arr[high] before deciding which half is sorted.",
            "interview_questions": "Why does the worst-case runtime become O(N)? (Because shrinking boundaries one element at a time takes N/2 steps for all-identical arrays)."
        }
    ),
    Problem(
        id="find-min-rotated-sorted",
        title="Find Minimum in Rotated Sorted Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Medium",
        description="Suppose an array of length n sorted in ascending order with unique elements is rotated between 1 and n times. Find the minimum element of this array in O(log n) time.",
        input_format="A list of unique integers arr.",
        output_format="Return the minimum integer.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="findMin",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def findMin(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int findMin(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int findMin(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    findMin(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [3, 4, 5, 1, 2]}, expected_output=1, is_hidden=False),
            TestCase(id=2, input_data={"arr": [4, 5, 6, 7, 0, 1, 2]}, expected_output=0, is_hidden=False),
            TestCase(id=3, input_data={"arr": [11, 13, 15, 17]}, expected_output=11, is_hidden=False),
            TestCase(id=4, input_data={"arr": [2, 1]}, expected_output=1, is_hidden=True),
            TestCase(id=5, input_data={"arr": [1]}, expected_output=1, is_hidden=True),
        ],
        comparison_mode="exact",
        order=75,
        tags=["Binary Search", "Rotated Array", "Extrema"],
        hints=[
            "Compare arr[mid] with arr[high].",
            "If arr[mid] > arr[high], the inflection (minimum) point must lie strictly to the right: low = mid + 1.",
            "If arr[mid] <= arr[high], the minimum could be arr[mid] or to the left: high = mid."
        ],
        examples=[
            {"input": "arr = [3, 4, 5, 1, 2]", "output": "1", "explanation": "The minimum element is 1."},
            {"input": "arr = [11, 13, 15, 17]", "output": "11", "explanation": "Array is already in sorted order."}
        ],
        explanation={
            "intuition": "Comparing mid with the rightmost boundary high indicates whether the inflection pivot point is in the right half or left half.",
            "brute_force": "Linear scan in O(N).",
            "optimal_approach": "low = 0, high = len(arr)-1. While low < high: mid = (low+high)//2. If arr[mid] > arr[high]: low = mid + 1. Else: high = mid. Return arr[low].",
            "dry_run": "[4, 5, 6, 7, 0, 1, 2]:\nlow=0, high=6 -> mid=3, arr[3]=7 > arr[6]=2 -> low=4.\nlow=4, high=6 -> mid=5, arr[5]=1 < arr[6]=2 -> high=5.\nlow=4, high=5 -> mid=4, arr[4]=0 < arr[5]=1 -> high=4.\nlow == high (4) -> return arr[4] = 0.",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Setting high = mid - 1 when arr[mid] <= arr[high], which could discard the minimum element itself.",
            "interview_questions": "How does this problem relate to finding how many times the array has been rotated? (The index of the minimum element equals the rotation count)."
        }
    ),
    Problem(
        id="single-element-sorted-array",
        title="Single Element in a Sorted Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Medium",
        description="You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find and return this single element that appears only once in O(log n) time and O(1) space.",
        input_format="A sorted list of integers arr.",
        output_format="Return the single integer.",
        constraints=["1 <= len(arr) <= 10^5", "arr length is odd", "-10^9 <= arr[i] <= 10^9"],
        function_name="singleNonDuplicate",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def singleNonDuplicate(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int singleNonDuplicate(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int singleNonDuplicate(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    singleNonDuplicate(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 1, 2, 3, 3, 4, 4, 8, 8]}, expected_output=2, is_hidden=False),
            TestCase(id=2, input_data={"arr": [3, 3, 7, 7, 10, 11, 11]}, expected_output=10, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1]}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 1, 2]}, expected_output=2, is_hidden=True),
        ],
        comparison_mode="exact",
        order=76,
        tags=["Binary Search", "Index Parity"],
        hints=[
            "Observe the indices of pairs before the single element: (0, 1), (2, 3), (4, 5)... (even, odd).",
            "After the single element, the pairing pattern shifts to (odd, even)!",
            "If mid is even and arr[mid] == arr[mid+1], the single element is to the right. Otherwise it is at or to the left."
        ],
        examples=[
            {"input": "arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]", "output": "2", "explanation": "2 appears only once."},
            {"input": "arr = [3, 3, 7, 7, 10, 11, 11]", "output": "10", "explanation": "10 appears once."}
        ],
        explanation={
            "intuition": "The single element disrupts the alternating (even, odd) parity pattern of identical element pairs.",
            "brute_force": "XOR all elements in O(N).",
            "optimal_approach": "low = 0, high = len(arr) - 1. While low < high: mid = (low + high) // 2. If mid % 2 == 1: mid -= 1. If arr[mid] == arr[mid + 1]: low = mid + 2 else: high = mid. Return arr[low].",
            "dry_run": "[1, 1, 2, 3, 3]:\nlow=0, high=4 -> mid=2 (even). arr[2]=2 != arr[3]=3 -> high=2.\nlow=0, high=2 -> mid=1 -> mid=0. arr[0]=1 == arr[1]=1 -> low=2.\nlow == high (2) -> return arr[2] = 2.",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Not ensuring mid is normalized to an even index.",
            "interview_questions": "How does the bitwise trick `mid ^ 1` automatically handle both even and odd index pair matching?"
        }
    ),
    Problem(
        id="find-peak-element",
        title="Find Peak Element in Array",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.1: BS on 1D Arrays",
        difficulty="Medium",
        description="A peak element is an element that is strictly greater than its neighbors. Given an integer array arr, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may imagine that arr[-1] = arr[n] = -infinity. You must write an algorithm that runs in O(log n) time.",
        input_format="A list of integers arr.",
        output_format="Return the 0-based index of any peak.",
        constraints=["1 <= len(arr) <= 10^5", "-2^31 <= arr[i] <= 2^31 - 1", "arr[i] != arr[i + 1] for all valid i."],
        function_name="findPeakElement",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def findPeakElement(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int findPeakElement(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int findPeakElement(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    findPeakElement(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 3, 1]}, expected_output=2, is_hidden=False),
            TestCase(id=2, input_data={"arr": [1, 2, 1, 3, 5, 6, 4]}, expected_output=5, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1]}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 2]}, expected_output=1, is_hidden=True),
        ],
        comparison_mode="exact",
        order=77,
        tags=["Binary Search", "Peak Element"],
        hints=[
            "Compare arr[mid] with arr[mid + 1].",
            "If arr[mid] < arr[mid + 1], you are on an upward slope. A peak is guaranteed to exist to the right (low = mid + 1).",
            "Otherwise, you are on a downward slope; a peak exists at mid or to the left (high = mid)."
        ],
        examples=[
            {"input": "arr = [1, 2, 3, 1]", "output": "2", "explanation": "3 is peak at index 2."},
            {"input": "arr = [1, 2, 1, 3, 5, 6, 4]", "output": "5", "explanation": "6 is peak at index 5."}
        ],
        explanation={
            "intuition": "Following the upward gradient always leads to a local maximum, because boundaries are -infinity.",
            "brute_force": "Scan linearly checking arr[i] > arr[i-1] and arr[i] > arr[i+1] in O(N).",
            "optimal_approach": "low = 0, high = len(arr) - 1. While low < high: mid = (low + high) // 2. If arr[mid] < arr[mid + 1]: low = mid + 1 else: high = mid. Return low.",
            "dry_run": "[1, 2, 3, 1]:\nlow=0, high=3 -> mid=1, arr[1]=2 < arr[2]=3 -> low=2.\nlow=2, high=3 -> mid=2, arr[2]=3 > arr[3]=1 -> high=2.\nlow == high (2) -> return 2.",
            "time_complexity": "O(log N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Accessing arr[mid+1] when mid is at the last index (use low < high condition).",
            "interview_questions": "How to extend this to 2D matrices (finding peak in N x M matrix in O(N log M))?"
        }
    ),
    Problem(
        id="integer-square-root",
        title="Square Root of an Integer Using Binary Search",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.2: BS on Answers",
        difficulty="Easy",
        description="Given a non-negative integer x, compute and return the integer square root of x, which is floor(sqrt(x)). You must not use any built-in exponent function or operator (like pow(x, 0.5) or x ** 0.5).",
        input_format="A non-negative integer x.",
        output_format="Return the integer floor square root.",
        constraints=["0 <= x <= 2^31 - 1"],
        function_name="mySqrt",
        param_names=["x"],
        starter_code={
            "python": "class Solution:\n    def mySqrt(self, x: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int mySqrt(int x) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int mySqrt(int x) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    mySqrt(x) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"x": 4}, expected_output=2, is_hidden=False),
            TestCase(id=2, input_data={"x": 8}, expected_output=2, is_hidden=False, explanation="sqrt(8) is 2.82842..., floor is 2."),
            TestCase(id=3, input_data={"x": 0}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"x": 1}, expected_output=1, is_hidden=False),
            TestCase(id=5, input_data={"x": 2147395599}, expected_output=46339, is_hidden=True),
        ],
        comparison_mode="exact",
        order=78,
        tags=["Binary Search", "Maths", "BS on Answer"],
        hints=[
            "The answer lies within the range [0, x].",
            "Use binary search on this answer range.",
            "If mid * mid <= x, mid is a candidate; search right (low = mid + 1). Else search left (high = mid - 1)."
        ],
        examples=[
            {"input": "x = 4", "output": "2", "explanation": "2 * 2 = 4."},
            {"input": "x = 8", "output": "2", "explanation": "floor(sqrt(8)) = 2."}
        ],
        explanation={
            "intuition": "f(m) = m * m is monotonically increasing for m >= 0, so binary search is directly applicable.",
            "brute_force": "Linear test from 1 upwards until m*m > x in O(sqrt(X)).",
            "optimal_approach": "low = 0, high = x, ans = 0. While low <= high: mid = (low+high)//2. If mid * mid <= x: ans = mid; low = mid + 1 else: high = mid - 1. Return ans.",
            "dry_run": "x = 8:\nlow=0, high=8 -> mid=4: 16 > 8 -> high=3\nlow=0, high=3 -> mid=1: 1 <= 8 -> ans=1, low=2\nlow=2, high=3 -> mid=2: 4 <= 8 -> ans=2, low=3\nlow=3, high=3 -> mid=3: 9 > 8 -> high=2\nReturn 2.",
            "time_complexity": "O(log X)",
            "space_complexity": "O(1)",
            "common_mistakes": "Integer overflow when calculating mid * mid in 32-bit types (use mid <= x // mid).",
            "interview_questions": "How does Newton-Raphson method compare to binary search for square roots?"
        }
    ),
    Problem(
        id="nth-root-integer",
        title="Nth Root of an Integer Using Binary Search",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.2: BS on Answers",
        difficulty="Medium",
        description="Given two numbers n and m, find the integer nth root of m (i.e. x such that x^n = m). If the exact nth root is not an integer, return -1.",
        input_format="Two positive integers n and m.",
        output_format="Return the exact integer root or -1.",
        constraints=["1 <= n <= 30", "1 <= m <= 10^9"],
        function_name="nthRoot",
        param_names=["n", "m"],
        starter_code={
            "python": "class Solution:\n    def nthRoot(self, n: int, m: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int nthRoot(int n, int m) {\n        return -1;\n    }\n};",
            "java": "class Solution {\n    public int nthRoot(int n, int m) {\n        return -1;\n    }\n}",
            "javascript": "class Solution {\n    nthRoot(n, m) {\n        return -1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"n": 3, "m": 27}, expected_output=3, is_hidden=False, explanation="3^3 = 27."),
            TestCase(id=2, input_data={"n": 4, "m": 69}, expected_output=-1, is_hidden=False, explanation="No integer raised to 4th power equals 69."),
            TestCase(id=3, input_data={"n": 1, "m": 14}, expected_output=14, is_hidden=False),
            TestCase(id=4, input_data={"n": 2, "m": 16}, expected_output=4, is_hidden=True),
        ],
        comparison_mode="exact",
        order=79,
        tags=["Binary Search", "Maths", "BS on Answer"],
        hints=[
            "Search range for root is [1, m].",
            "Binary search for mid in [1, m].",
            "Compute mid^n carefully. If mid^n == m return mid. If mid^n < m search right, else search left."
        ],
        examples=[
            {"input": "n = 3, m = 27", "output": "3", "explanation": "3^3 = 27."},
            {"input": "n = 4, m = 69", "output": "-1", "explanation": "Not an exact integer power."}
        ],
        explanation={
            "intuition": "f(x) = x^n is strictly monotonic. Binary search finds exact x in O(n log m).",
            "brute_force": "Linear test from 1 to m in O(m).",
            "optimal_approach": "low = 1, high = m. While low <= high: mid = (low+high)//2; val = mid ** n; if val == m: return mid; elif val < m: low = mid + 1; else: high = mid - 1. Return -1.",
            "dry_run": "n=3, m=27: low=1, high=27 -> mid=14 (14^3 > 27) -> high=13... narrows to mid=3 (3^3 = 27) -> return 3.",
            "time_complexity": "O(log(M) * log(N))",
            "space_complexity": "O(1)",
            "common_mistakes": "Large powers mid^n overflowing in languages without arbitrary precision integers.",
            "interview_questions": "How to stop power multiplication early to prevent 64-bit integer overflow?"
        }
    ),
    Problem(
        id="koko-eating-bananas-speed",
        title="Minimum Eating Speed (Binary Search on Answer)",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.2: BS on Answers",
        difficulty="Medium",
        description="Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards will come back in h hours. Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile and eats k bananas from it. If the pile has less than k bananas, she eats all of them and will not eat any more bananas during this hour. Return the minimum integer k such that she can eat all the bananas within h hours.",
        input_format="A list of integers piles and integer h.",
        output_format="Return the minimum integer speed k.",
        constraints=["1 <= len(piles) <= 10^5", "len(piles) <= h <= 10^9", "1 <= piles[i] <= 10^9"],
        function_name="minEatingSpeed",
        param_names=["piles", "h"],
        starter_code={
            "python": "class Solution:\n    def minEatingSpeed(self, piles: list[int], h: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int minEatingSpeed(vector<int>& piles, int h) {\n        return 1;\n    }\n};",
            "java": "class Solution {\n    public int minEatingSpeed(int[] piles, int h) {\n        return 1;\n    }\n}",
            "javascript": "class Solution {\n    minEatingSpeed(piles, h) {\n        return 1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"piles": [3, 6, 7, 11], "h": 8}, expected_output=4, is_hidden=False),
            TestCase(id=2, input_data={"piles": [30, 11, 23, 4, 20], "h": 5}, expected_output=30, is_hidden=False),
            TestCase(id=3, input_data={"piles": [30, 11, 23, 4, 20], "h": 6}, expected_output=23, is_hidden=False),
            TestCase(id=4, input_data={"piles": [1000000000], "h": 2}, expected_output=500000000, is_hidden=True),
        ],
        comparison_mode="exact",
        order=80,
        tags=["Binary Search", "BS on Answer", "Greedy"],
        hints=[
            "What is the minimum possible eating speed? 1.",
            "What is the maximum necessary speed? max(piles).",
            "For a test speed k, hours required for a pile is ceil(pile / k) = (pile + k - 1) // k. If total hours <= h, k is feasible: try smaller speeds (search left)."
        ],
        examples=[
            {"input": "piles = [3, 6, 7, 11], h = 8", "output": "4", "explanation": "At speed 4: ceil(3/4)=1, ceil(6/4)=2, ceil(7/4)=2, ceil(11/4)=3. Total hours = 1+2+2+3 = 8 <= 8."},
            {"input": "piles = [30, 11, 23, 4, 20], h = 5", "output": "30", "explanation": "Speed 30 required to eat each pile in 1 hour."}
        ],
        explanation={
            "intuition": "Total hours required decreases monotonically as eating speed increases. Binary search on answer range [1, max(piles)].",
            "brute_force": "Linear test speeds k = 1, 2... in O(max(piles) * N).",
            "optimal_approach": "low = 1, high = max(piles), ans = high. While low <= high: mid = (low+high)//2. Hours = sum((p + mid - 1)//mid for p in piles). If hours <= h: ans = mid; high = mid - 1. Else: low = mid + 1. Return ans.",
            "dry_run": "piles = [3, 6, 7, 11], h = 8: low=1, high=11. mid=6: hours=1+1+2+2=6 <= 8 -> ans=6, high=5. mid=3: hours=1+2+3+4=10 > 8 -> low=4. mid=4: hours=1+2+2+3=8 <= 8 -> ans=4, high=3. Return 4.",
            "time_complexity": "O(N log(max(piles)))",
            "space_complexity": "O(1)",
            "common_mistakes": "Using float division with math.ceil which can suffer floating point precision issues for 10^9.",
            "interview_questions": "How does this pattern generalize to Ship Packages within D Days?"
        }
    ),
    Problem(
        id="minimum-days-make-bouquets",
        title="Minimum Days to Make M Bouquets",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.2: BS on Answers",
        difficulty="Medium",
        description="You are given an integer array bloomDay, an integer m and an integer k. You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden. The garden consists of n flowers, where the ith flower will bloom in the bloomDay[i] day. Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible, return -1.",
        input_format="A list of integers bloomDay, integer m, integer k.",
        output_format="Return the minimum days as an integer, or -1.",
        constraints=["1 <= len(bloomDay) <= 10^5", "1 <= m <= 10^6", "1 <= k <= len(bloomDay)", "1 <= bloomDay[i] <= 10^9"],
        function_name="minDaysBouquets",
        param_names=["bloomDay", "m", "k"],
        starter_code={
            "python": "class Solution:\n    def minDaysBouquets(self, bloomDay: list[int], m: int, k: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int minDaysBouquets(vector<int>& bloomDay, int m, int k) {\n        return -1;\n    }\n};",
            "java": "class Solution {\n    public int minDaysBouquets(int[] bloomDay, int m, int k) {\n        return -1;\n    }\n}",
            "javascript": "class Solution {\n    minDaysBouquets(bloomDay, m, k) {\n        return -1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"bloomDay": [1, 10, 3, 10, 2], "m": 3, "k": 1}, expected_output=3, is_hidden=False),
            TestCase(id=2, input_data={"bloomDay": [1, 10, 3, 10, 2], "m": 3, "k": 2}, expected_output=-1, is_hidden=False, explanation="Need 3 * 2 = 6 flowers, but only 5 flowers exist."),
            TestCase(id=3, input_data={"bloomDay": [7, 7, 7, 7, 12, 7, 7], "m": 2, "k": 3}, expected_output=12, is_hidden=False),
            TestCase(id=4, input_data={"bloomDay": [1000000000, 1000000000], "m": 1, "k": 1}, expected_output=1000000000, is_hidden=True),
        ],
        comparison_mode="exact",
        order=81,
        tags=["Binary Search", "BS on Answer"],
        hints=[
            "If m * k > len(bloomDay), there aren't enough flowers in total, return -1 immediately.",
            "Days search space: [min(bloomDay), max(bloomDay)].",
            "For a given day d, traverse bloomDay: count consecutive flowers bloomed (bloomDay[i] <= d). Every time count reaches k, increment bouquets count and reset count to 0."
        ],
        examples=[
            {"input": "bloomDay = [1, 10, 3, 10, 2], m = 3, k = 1", "output": "3", "explanation": "On day 3, flowers at indices 0, 2, 4 are bloomed, giving 3 bouquets of 1 flower."},
            {"input": "bloomDay = [1, 2, 3], m = 2, k = 2", "output": "-1", "explanation": "Need 4 flowers, only 3 available."}
        ],
        explanation={
            "intuition": "More days mean more flowers bloomed, making the bouquet formation check monotonic. Binary search on day range [min, max].",
            "brute_force": "Linear test every possible day.",
            "optimal_approach": "If m * k > len(bloomDay): return -1. Helper can_make(d): bouquets = 0, flowers = 0; for b in bloomDay: if b <= d: flowers += 1; if flowers == k: bouquets += 1; flowers = 0 else: flowers = 0; return bouquets >= m. Binary search low=min(bloomDay), high=max(bloomDay).",
            "dry_run": "[1, 10, 3, 10, 2], m=3, k=1: low=1, high=10. mid=5: bloomed indices 0, 2, 4 -> 3 bouquets >= 3. ans=5, high=4. mid=2: 2 bouquets < 3 -> low=3. mid=3: 3 bouquets >= 3 -> ans=3, high=2. Return 3.",
            "time_complexity": "O(N log(max_day - min_day))",
            "space_complexity": "O(1)",
            "common_mistakes": "Not checking if m * k > len(bloomDay) upfront (prevents unnecessary search).",
            "interview_questions": "How does non-adjacent flower selection change the problem complexity?"
        }
    ),
    Problem(
        id="find-smallest-divisor-threshold",
        title="Find the Smallest Divisor Given a Threshold",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.2: BS on Answers",
        difficulty="Medium",
        description="Given an array of integers nums and an integer threshold, choose a positive integer divisor, divide all the array by it, and sum the result of the division (each division result is rounded up to the nearest integer). Find the smallest divisor such that the sum is less than or equal to threshold.",
        input_format="A list of integers nums and integer threshold.",
        output_format="Return the smallest divisor as an integer.",
        constraints=["1 <= len(nums) <= 5 * 10^4", "len(nums) <= threshold <= 10^6", "1 <= nums[i] <= 10^6"],
        function_name="smallestDivisor",
        param_names=["nums", "threshold"],
        starter_code={
            "python": "class Solution:\n    def smallestDivisor(self, nums: list[int], threshold: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int smallestDivisor(vector<int>& nums, int threshold) {\n        return 1;\n    }\n};",
            "java": "class Solution {\n    public int smallestDivisor(int[] nums, int threshold) {\n        return 1;\n    }\n}",
            "javascript": "class Solution {\n    smallestDivisor(nums, threshold) {\n        return 1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"nums": [1, 2, 5, 9], "threshold": 6}, expected_output=5, is_hidden=False),
            TestCase(id=2, input_data={"nums": [44, 22, 33, 11, 1], "threshold": 5}, expected_output=44, is_hidden=False),
            TestCase(id=3, input_data={"nums": [21212, 10101, 12121], "threshold": 1000000}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"nums": [2, 3, 5, 7, 11], "threshold": 11}, expected_output=3, is_hidden=True),
        ],
        comparison_mode="exact",
        order=82,
        tags=["Binary Search", "BS on Answer"],
        hints=[
            "Search range for divisor is [1, max(nums)].",
            "As divisor increases, the sum of ceil(num / divisor) monotonically decreases.",
            "If sum <= threshold at divisor d, d is a valid candidate. Search left for a smaller divisor (high = d - 1)."
        ],
        examples=[
            {"input": "nums = [1, 2, 5, 9], threshold = 6", "output": "5", "explanation": "Divisor 5: ceil(1/5)+ceil(2/5)+ceil(5/5)+ceil(9/5) = 1+1+1+2 = 5 <= 6."},
            {"input": "nums = [44, 22, 33, 11, 1], threshold = 5", "output": "44", "explanation": "Divisor 44 yields 1+1+1+1+1 = 5."}
        ],
        explanation={
            "intuition": "The quotient sum is monotonically decreasing with respect to divisor. Binary search on divisor range [1, max(nums)].",
            "brute_force": "Linear search divisor from 1 upwards.",
            "optimal_approach": "low = 1, high = max(nums), ans = high. While low <= high: mid = (low+high)//2; s = sum((x + mid - 1)//mid for x in nums); if s <= threshold: ans = mid; high = mid - 1 else: low = mid + 1. Return ans.",
            "dry_run": "nums = [1, 2, 5, 9], threshold = 6: low=1, high=9. mid=5: s = 1+1+1+2 = 5 <= 6 -> ans=5, high=4. mid=2: s = 1+1+3+5 = 10 > 6 -> low=3. mid=3: s = 1+1+2+3 = 7 > 6 -> low=4. mid=4: s = 1+1+2+3 = 7 > 6 -> low=5. Return 5.",
            "time_complexity": "O(N log(max(nums)))",
            "space_complexity": "O(1)",
            "common_mistakes": "Ceil division formula: (x + d - 1) // d.",
            "interview_questions": "Why is the lower search bound 1 and not 0? (Division by zero)."
        }
    ),
    Problem(
        id="capacity-to-ship-packages",
        title="Capacity to Ship Packages Within D Days",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.2: BS on Answers",
        difficulty="Medium",
        description="A conveyor belt has packages that must be shipped from one port to another within days days. The ith package has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt in the given order. We cannot load more weight than the maximum weight capacity of the ship. Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.",
        input_format="A list of integers weights and integer days.",
        output_format="Return the minimum ship capacity as an integer.",
        constraints=["1 <= len(weights) <= 5 * 10^4", "1 <= days <= len(weights)", "1 <= weights[i] <= 500"],
        function_name="shipWithinDays",
        param_names=["weights", "days"],
        starter_code={
            "python": "class Solution:\n    def shipWithinDays(self, weights: list[int], days: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int shipWithinDays(vector<int>& weights, int days) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int shipWithinDays(int[] weights, int days) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    shipWithinDays(weights, days) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"weights": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "days": 5}, expected_output=15, is_hidden=False),
            TestCase(id=2, input_data={"weights": [3, 2, 2, 4, 1, 4], "days": 3}, expected_output=6, is_hidden=False),
            TestCase(id=3, input_data={"weights": [1, 2, 3, 1, 1], "days": 4}, expected_output=3, is_hidden=False),
            TestCase(id=4, input_data={"weights": [10], "days": 1}, expected_output=10, is_hidden=True),
        ],
        comparison_mode="exact",
        order=83,
        tags=["Binary Search", "BS on Answer", "Greedy"],
        hints=[
            "The ship must be able to carry the heaviest package: low = max(weights).",
            "The upper bound capacity ships everything in 1 day: high = sum(weights).",
            "For a test capacity C, greedily pack items on current day; when adding next package exceeds C, increment day count."
        ],
        examples=[
            {"input": "weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5", "output": "15", "explanation": "Capacity 15 ships: 1st day (1..5), 2nd day (6,7), 3rd day (8), 4th day (9), 5th day (10)."},
            {"input": "weights = [3, 2, 2, 4, 1, 4], days = 3", "output": "6", "explanation": "Ships in 3 days with capacity 6."}
        ],
        explanation={
            "intuition": "Capacity is monotonic: higher capacity requires fewer or equal days. Binary search on [max(weights), sum(weights)].",
            "brute_force": "Linear test capacity from max(weights) to sum(weights).",
            "optimal_approach": "low = max(weights), high = sum(weights), ans = high. While low <= high: mid = (low+high)//2; d = 1; curr = 0; for w in weights: if curr + w > mid: d += 1; curr = w else: curr += w. If d <= days: ans = mid; high = mid - 1 else: low = mid + 1. Return ans.",
            "dry_run": "weights=[1,2,3,4,5,6,7,8,9,10], days=5: low=10, high=55. mid=32 -> fits in 2 days <= 5 -> ans=32, high=31... narrows down to 15.",
            "time_complexity": "O(N log(sum(weights) - max(weights)))",
            "space_complexity": "O(1)",
            "common_mistakes": "Setting low lower than max(weights), which makes it impossible to ship the heaviest package.",
            "interview_questions": "How does this problem relate to the Split Array Largest Sum problem? (They are identical formulations)."
        }
    ),
    Problem(
        id="aggressive-cows-distance",
        title="Aggressive Cows (Maximize Minimum Distance)",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.2: BS on Answers",
        difficulty="Hard",
        description="You are given an array stalls representing coordinates of stalls on a straight line and an integer k representing the number of aggressive cows. Assign stalls to k cows such that the minimum distance between any two of them is as large as possible. Return that maximum possible minimum distance.",
        input_format="A list of integers stalls and integer k.",
        output_format="Return the maximum minimum distance as an integer.",
        constraints=["2 <= len(stalls) <= 10^5", "2 <= k <= len(stalls)", "0 <= stalls[i] <= 10^9"],
        function_name="aggressiveCows",
        param_names=["stalls", "k"],
        starter_code={
            "python": "class Solution:\n    def aggressiveCows(self, stalls: list[int], k: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int aggressiveCows(vector<int>& stalls, int k) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int aggressiveCows(int[] stalls, int k) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    aggressiveCows(stalls, k) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"stalls": [1, 2, 8, 4, 9], "k": 3}, expected_output=3, is_hidden=False),
            TestCase(id=2, input_data={"stalls": [0, 3, 4, 7, 10, 9], "k": 4}, expected_output=3, is_hidden=False),
            TestCase(id=3, input_data={"stalls": [1, 10], "k": 2}, expected_output=9, is_hidden=False),
            TestCase(id=4, input_data={"stalls": [5, 17, 100, 11], "k": 2}, expected_output=95, is_hidden=True),
        ],
        comparison_mode="exact",
        order=84,
        tags=["Binary Search", "BS on Answer", "Greedy"],
        hints=[
            "First, sort the stalls array so positions are sequential.",
            "Distance range is [1, stalls[-1] - stalls[0]].",
            "For a candidate distance d, place the first cow at stalls[0]. For subsequent cows, place at the next stall with position >= last_placed + d. If you can place >= k cows, d is achievable!"
        ],
        examples=[
            {"input": "stalls = [1, 2, 8, 4, 9], k = 3", "output": "3", "explanation": "Sorted stalls: [1, 2, 4, 8, 9]. Place cows at 1, 4, 8. Minimum distance is min(3, 4) = 3."},
            {"input": "stalls = [1, 10], k = 2", "output": "9", "explanation": "Place at 1 and 10, distance is 9."}
        ],
        explanation={
            "intuition": "If a distance d is feasible, any distance smaller than d is also feasible. This monotonicity allows binary searching on the answer distance.",
            "brute_force": "Linear test distances from 1 to max possible in O(max_dist * N).",
            "optimal_approach": "stalls.sort(). low = 1, high = stalls[-1] - stalls[0], ans = 1. While low <= high: mid = (low+high)//2; cows = 1; last = stalls[0]; for pos in stalls[1:]: if pos - last >= mid: cows += 1; last = pos. If cows >= k: ans = mid; low = mid + 1 else: high = mid - 1. Return ans.",
            "dry_run": "[1, 2, 4, 8, 9], k = 3:\nlow=1, high=8 -> mid=4: place 1, 8 -> 2 cows < 3 -> high=3.\nmid=2: place 1, 4, 8 -> 3 cows >= 3 -> ans=2, low=3.\nmid=3: place 1, 4, 8 -> 3 cows >= 3 -> ans=3, low=4 -> terminates. Return 3.",
            "time_complexity": "O(N log N + N log(max_distance))",
            "space_complexity": "O(1)",
            "common_mistakes": "Forgetting to sort stalls array before applying the greedy placement check.",
            "interview_questions": "How does this formulate as a max-min optimization problem?"
        }
    ),
    Problem(
        id="book-allocation-problem",
        title="Allocate Minimum Number of Pages",
        step_id=5,
        step_title="Step 5: Binary Search",
        subtopic="5.2: BS on Answers",
        difficulty="Hard",
        description="Given an array arr of integers where arr[i] denotes the number of pages in the ith book, and an integer m representing students. Allocate all books to m students such that:\n1. Each student gets at least one book.\n2. Each book is allocated to exactly one student.\n3. Book allocation is contiguous.\nAllocate books such that the maximum number of pages assigned to any student is minimized. If allocation is impossible, return -1.",
        input_format="A list of integers arr and integer m.",
        output_format="Return the minimized maximum pages as an integer, or -1.",
        constraints=["1 <= len(arr) <= 10^5", "1 <= m <= 10^5", "1 <= arr[i] <= 10^9"],
        function_name="allocateBooks",
        param_names=["arr", "m"],
        starter_code={
            "python": "class Solution:\n    def allocateBooks(self, arr: list[int], m: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int allocateBooks(vector<int>& arr, int m) {\n        return -1;\n    }\n};",
            "java": "class Solution {\n    public int allocateBooks(int[] arr, int m) {\n        return -1;\n    }\n}",
            "javascript": "class Solution {\n    allocateBooks(arr, m) {\n        return -1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [12, 34, 67, 90], "m": 2}, expected_output=113, is_hidden=False, explanation="Allocate [12, 34, 67] (113 pages) and [90] (90 pages). Max is 113."),
            TestCase(id=2, input_data={"arr": [25, 46, 28, 49, 24], "m": 4}, expected_output=71, is_hidden=False),
            TestCase(id=3, input_data={"arr": [10, 20], "m": 3}, expected_output=-1, is_hidden=False, explanation="More students than books."),
            TestCase(id=4, input_data={"arr": [5, 17, 100, 11], "m": 4}, expected_output=100, is_hidden=True),
        ],
        comparison_mode="exact",
        order=85,
        tags=["Binary Search", "BS on Answer", "Allocation"],
        hints=[
            "If m > len(arr), it is impossible to give each student at least one book, return -1.",
            "Lower bound for pages is max(arr), upper bound is sum(arr).",
            "Greedily count how many students are needed when no student gets more than mid pages. If students <= m, search left."
        ],
        examples=[
            {"input": "arr = [12, 34, 67, 90], m = 2", "output": "113", "explanation": "Student 1: 12+34+67 = 113. Student 2: 90. Max pages = 113."},
            {"input": "arr = [10, 20], m = 3", "output": "-1", "explanation": "Only 2 books for 3 students."}
        ],
        explanation={
            "intuition": "Minimizing the maximum contiguous partition sum is monotonic with respect to partition ceiling. Binary search on answer range [max(arr), sum(arr)].",
            "brute_force": "Try all possible partition combinations in exponential time.",
            "optimal_approach": "If m > len(arr): return -1. low = max(arr), high = sum(arr), ans = high. While low <= high: mid = (low+high)//2; students = 1; pages = 0; for x in arr: if pages + x > mid: students += 1; pages = x else: pages += x. If students <= m: ans = mid; high = mid - 1 else: low = mid + 1. Return ans.",
            "dry_run": "[12, 34, 67, 90], m=2: low=90, high=203. mid=146 -> students=2 <= 2 -> ans=146, high=145... narrows to ans=113.",
            "time_complexity": "O(N log(sum(arr) - max(arr)))",
            "space_complexity": "O(1)",
            "common_mistakes": "Forgetting to return -1 when m > len(arr).",
            "interview_questions": "How is this problem identical to Painter's Partition and Split Array Largest Sum?"
        }
    ),
]
