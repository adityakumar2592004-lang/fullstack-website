from models import Problem, TestCase

MODULE_3_PROBLEMS = [
    Problem(
        id="largest-element-array",
        title="Find the Largest Element in an Array",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Easy",
        description="Given an array of integers arr, find and return the maximum element present in the array.",
        input_format="A list of integers arr.",
        output_format="Return the maximum integer.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="findLargest",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def findLargest(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int findLargest(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int findLargest(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    findLargest(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [2, 5, 1, 3, 0]}, expected_output=5, is_hidden=False),
            TestCase(id=2, input_data={"arr": [8, 10, 5, 7, 9]}, expected_output=10, is_hidden=False),
            TestCase(id=3, input_data={"arr": [-3, -1, -5]}, expected_output=-1, is_hidden=False),
            TestCase(id=4, input_data={"arr": [42]}, expected_output=42, is_hidden=True),
            TestCase(id=5, input_data={"arr": [1000000000, 999999999]}, expected_output=1000000000, is_hidden=True),
        ],
        comparison_mode="exact",
        order=26,
        tags=["Arrays", "Basics"],
        hints=[
            "Initialize a variable max_val with the first element of the array.",
            "Traverse the remaining elements from index 1 to n-1.",
            "Whenever an element is greater than max_val, update max_val."
        ],
        examples=[
            {"input": "arr = [2, 5, 1, 3, 0]", "output": "5", "explanation": "5 is the largest element."},
            {"input": "arr = [-3, -1, -5]", "output": "-1", "explanation": "-1 is larger than -3 and -5."}
        ],
        explanation={
            "intuition": "Scanning every element once and tracking the maximum seen so far is optimal because any element could potentially be the maximum.",
            "brute_force": "Sort the array in O(N log N) and pick arr[-1].",
            "optimal_approach": "Initialize max_val = arr[0]. Loop x in arr: if x > max_val: max_val = x. Return max_val.",
            "dry_run": "arr = [2, 5, 1]: max_val=2. 5 > 2 -> max_val=5. 1 < 5 -> max_val=5. Return 5.",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Initializing max_val to 0 instead of arr[0], which fails when all numbers are negative.",
            "interview_questions": "Can you find the maximum in fewer than N-1 comparisons? (No, finding maximum of N elements requires at least N-1 comparisons by adversary argument)."
        }
    ),
    Problem(
        id="second-largest-element",
        title="Find Second Largest Without Sorting",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Easy",
        description="Given an array of integers arr, find the second largest distinct element. If no second largest distinct element exists, return -1.",
        input_format="A list of integers arr.",
        output_format="Return the second largest distinct integer, or -1.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="findSecondLargest",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def findSecondLargest(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int findSecondLargest(vector<int>& arr) {\n        return -1;\n    }\n};",
            "java": "class Solution {\n    public int findSecondLargest(int[] arr) {\n        return -1;\n    }\n}",
            "javascript": "class Solution {\n    findSecondLargest(arr) {\n        return -1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [12, 35, 1, 10, 34, 1]}, expected_output=34, is_hidden=False),
            TestCase(id=2, input_data={"arr": [10, 10, 10]}, expected_output=-1, is_hidden=False),
            TestCase(id=3, input_data={"arr": [5, 2]}, expected_output=2, is_hidden=False),
            TestCase(id=4, input_data={"arr": [-10, -5, -2, -20]}, expected_output=-5, is_hidden=True),
            TestCase(id=5, input_data={"arr": [7]}, expected_output=-1, is_hidden=True),
        ],
        comparison_mode="exact",
        order=27,
        tags=["Arrays", "Single Pass"],
        hints=[
            "Maintain two variables: largest and second_largest.",
            "If an element is strictly greater than largest, second_largest takes the old largest, and largest takes the new element.",
            "If an element is between largest and second_largest, update only second_largest."
        ],
        examples=[
            {"input": "arr = [12, 35, 1, 10, 34, 1]", "output": "34", "explanation": "Largest is 35, second largest distinct is 34."},
            {"input": "arr = [10, 10]", "output": "-1", "explanation": "All elements are equal, no second distinct largest exists."}
        ],
        explanation={
            "intuition": "In a single pass, whenever a new peak is found, the previous peak becomes the candidate for second largest.",
            "brute_force": "Sort array and find the first element strictly smaller than arr[-1]. Takes O(N log N).",
            "optimal_approach": "Initialize largest = -inf, second = -inf. For x in arr: if x > largest: second = largest; largest = x. Elif x > second and x < largest: second = x. Return second if second != -inf else -1.",
            "dry_run": "[12, 35, 34]:\n12: largest=12, second=-inf\n35: second=12, largest=35\n34: 34 < 35 and 34 > 12 -> second=34\nReturn 34.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(1)",
            "common_mistakes": "Forgetting strict inequality x < largest, which incorrectly sets second_largest equal to duplicate largests.",
            "interview_questions": "How would you extend this to find the k-th largest element in O(N)? (Use QuickSelect or min-heap of size k)."
        }
    ),
    Problem(
        id="remove-duplicates-sorted",
        title="Remove Duplicates from Sorted Array",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Easy",
        description="Given an integer array arr sorted in non-decreasing order, remove duplicates in-place such that each unique element appears only once. Return the number of unique elements k.",
        input_format="A list of integers arr sorted in non-decreasing order.",
        output_format="Return the integer count of unique elements k.",
        constraints=["1 <= len(arr) <= 10^5", "-10^4 <= arr[i] <= 10^4"],
        function_name="removeDuplicates",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def removeDuplicates(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int removeDuplicates(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int removeDuplicates(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    removeDuplicates(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 1, 2]}, expected_output=2, is_hidden=False),
            TestCase(id=2, input_data={"arr": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]}, expected_output=5, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1]}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 2, 3, 4]}, expected_output=4, is_hidden=True),
            TestCase(id=5, input_data={"arr": [5, 5, 5, 5, 5]}, expected_output=1, is_hidden=True),
        ],
        comparison_mode="exact",
        order=28,
        tags=["Arrays", "Two Pointers", "In-place"],
        hints=[
            "Since the array is sorted, all duplicate elements are contiguous.",
            "Use a slow pointer i tracking the position of unique elements.",
            "Scan with fast pointer j: whenever arr[j] != arr[i], increment i and copy arr[i] = arr[j]."
        ],
        examples=[
            {"input": "arr = [1, 1, 2]", "output": "2", "explanation": "Unique elements are [1, 2], count is 2."},
            {"input": "arr = [0, 0, 1, 1, 2]", "output": "3", "explanation": "Unique elements are [0, 1, 2]."}
        ],
        explanation={
            "intuition": "Because duplicates are grouped together in sorted order, we can overwrite duplicates in-place using two pointers.",
            "brute_force": "Use an extra hash set or list, copy unique elements back. Takes O(N) extra space.",
            "optimal_approach": "Pointer i = 0. For j from 1 to len(arr)-1: if arr[j] != arr[i]: i += 1; arr[i] = arr[j]. Return i + 1.",
            "dry_run": "[1, 1, 2]: i=0.\nj=1: arr[1] == arr[0] (1==1) -> skip.\nj=2: arr[2] != arr[0] (2!=1) -> i=1, arr[1]=2.\nEnd. Return i + 1 = 2.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(1) in-place.",
            "common_mistakes": "Returning i instead of i + 1 as count of elements.",
            "interview_questions": "What if at most two occurrences of each element are allowed? (Compare with arr[i-1] instead of arr[i])."
        }
    ),
    Problem(
        id="rotate-array-left-k",
        title="Rotate Array Left by K Positions",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Medium",
        description="Given an array of integers arr and a non-negative integer k, rotate the array to the left by k steps in-place and return the rotated array.",
        input_format="A list of integers arr and an integer k.",
        output_format="Return the rotated list of integers.",
        constraints=["1 <= len(arr) <= 10^5", "0 <= k <= 10^9", "-10^9 <= arr[i] <= 10^9"],
        function_name="rotateLeft",
        param_names=["arr", "k"],
        starter_code={
            "python": "class Solution:\n    def rotateLeft(self, arr: list[int], k: int) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> rotateLeft(vector<int>& arr, int k) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] rotateLeft(int[] arr, int k) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    rotateLeft(arr, k) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 3, 4, 5], "k": 2}, expected_output=[3, 4, 5, 1, 2], is_hidden=False),
            TestCase(id=2, input_data={"arr": [1, 2, 3, 4, 5, 6, 7], "k": 3}, expected_output=[4, 5, 6, 7, 1, 2, 3], is_hidden=False),
            TestCase(id=3, input_data={"arr": [10, 20], "k": 0}, expected_output=[10, 20], is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 2, 3], "k": 4}, expected_output=[2, 3, 1], is_hidden=True),
            TestCase(id=5, input_data={"arr": [5], "k": 100}, expected_output=[5], is_hidden=True),
        ],
        comparison_mode="exact",
        order=29,
        tags=["Arrays", "Rotation", "Two Pointers"],
        hints=[
            "First, reduce k using modulo: k = k % len(arr).",
            "Rotating left by k moves the first k elements to the end.",
            "Can you reverse parts of the array? Reverse arr[0..k-1], reverse arr[k..n-1], then reverse the whole array arr[0..n-1]!"
        ],
        examples=[
            {"input": "arr = [1, 2, 3, 4, 5], k = 2", "output": "[3, 4, 5, 1, 2]", "explanation": "Elements 1 and 2 move to the back."},
            {"input": "arr = [1, 2, 3], k = 4", "output": "[2, 3, 1]", "explanation": "k % 3 = 1 left rotation."}
        ],
        explanation={
            "intuition": "The reversal algorithm achieves in-place rotation in linear time without extra buffer memory.",
            "brute_force": "Rotate one step left k times in O(N * K) time, or use a temporary array of size k.",
            "optimal_approach": "k = k % n. Reverse arr[0..k-1], reverse arr[k..n-1], and reverse entire arr[0..n-1].",
            "dry_run": "[1, 2, 3, 4, 5], k = 2:\n1. Reverse arr[0..1]: [2, 1, 3, 4, 5]\n2. Reverse arr[2..4]: [2, 1, 5, 4, 3]\n3. Reverse entire: [3, 4, 5, 1, 2].",
            "time_complexity": "O(N)",
            "space_complexity": "O(1) in-place.",
            "common_mistakes": "Forgetting k = k % n when k > len(arr).",
            "interview_questions": "How does left rotation differ from right rotation by k? (Right rotation by k is equivalent to left rotation by (n - k % n))."
        }
    ),
    Problem(
        id="move-zeroes-to-end",
        title="Move All Zeroes to the End of Array",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Easy",
        description="Given an integer array arr, move all 0's to the end of it while maintaining the relative order of the non-zero elements. You must do this in-place without making a copy of the array.",
        input_format="A list of integers arr.",
        output_format="Return the modified array.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="moveZeroes",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def moveZeroes(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> moveZeroes(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] moveZeroes(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    moveZeroes(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [0, 1, 0, 3, 12]}, expected_output=[1, 3, 12, 0, 0], is_hidden=False),
            TestCase(id=2, input_data={"arr": [0]}, expected_output=[0], is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, 2, 3]}, expected_output=[1, 2, 3], is_hidden=False),
            TestCase(id=4, input_data={"arr": [0, 0, 0, 1]}, expected_output=[1, 0, 0, 0], is_hidden=True),
            TestCase(id=5, input_data={"arr": [4, 0, 5, 0, 0, 6]}, expected_output=[4, 5, 6, 0, 0, 0], is_hidden=True),
        ],
        comparison_mode="exact",
        order=30,
        tags=["Arrays", "Two Pointers", "In-place"],
        hints=[
            "Keep a pointer for where the next non-zero element should go.",
            "Iterate through the array; whenever you see a non-zero element, swap it with the position at the pointer.",
            "Increment the pointer after each non-zero element is positioned."
        ],
        examples=[
            {"input": "arr = [0, 1, 0, 3, 12]", "output": "[1, 3, 12, 0, 0]", "explanation": "Non-zero values 1, 3, 12 maintain relative order; zeroes pushed to end."},
            {"input": "arr = [0]", "output": "[0]", "explanation": "Only zero present."}
        ],
        explanation={
            "intuition": "Use a two-pointer approach: pointer insert_pos tracks the destination for the next non-zero number.",
            "brute_force": "Collect all non-zeros in an auxiliary list, count zeroes, and combine. Requires O(N) space.",
            "optimal_approach": "insert_pos = 0. For i in range(len(arr)): if arr[i] != 0: arr[insert_pos], arr[i] = arr[i], arr[insert_pos]; insert_pos += 1. Return arr.",
            "dry_run": "[0, 1, 0, 3]:\ni=0: arr[0]=0, skip.\ni=1: arr[1]=1 != 0 -> swap(arr[0], arr[1]) -> [1, 0, 0, 3], insert_pos=1.\ni=2: arr[2]=0, skip.\ni=3: arr[3]=3 != 0 -> swap(arr[1], arr[3]) -> [1, 3, 0, 0], insert_pos=2.\nReturn [1, 3, 0, 0].",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(1) in-place.",
            "common_mistakes": "Overwriting non-zeros with zeroes before reading them.",
            "interview_questions": "Can you minimize the total number of write operations when there are no zeroes? (Check if i != insert_pos before swapping)."
        }
    ),
    Problem(
        id="linear-search",
        title="Linear Search in Array",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Easy",
        description="Given an array of integers arr and an integer target, perform linear search to find the first index where target occurs. Return the 0-based index, or -1 if target is not found.",
        input_format="A list of integers arr and an integer target.",
        output_format="Return the 0-based index or -1.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= target, arr[i] <= 10^9"],
        function_name="linearSearch",
        param_names=["arr", "target"],
        starter_code={
            "python": "class Solution:\n    def linearSearch(self, arr: list[int], target: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int linearSearch(vector<int>& arr, int target) {\n        return -1;\n    }\n};",
            "java": "class Solution {\n    public int linearSearch(int[] arr, int target) {\n        return -1;\n    }\n}",
            "javascript": "class Solution {\n    linearSearch(arr, target) {\n        return -1;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 3, 4, 5], "target": 3}, expected_output=2, is_hidden=False),
            TestCase(id=2, input_data={"arr": [5, 4, 3, 2, 1], "target": 6}, expected_output=-1, is_hidden=False),
            TestCase(id=3, input_data={"arr": [10], "target": 10}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"arr": [4, 2, 4, 4], "target": 4}, expected_output=0, is_hidden=True),
            TestCase(id=5, input_data={"arr": [-5, 0, 7, 12], "target": 12}, expected_output=3, is_hidden=True),
        ],
        comparison_mode="exact",
        order=31,
        tags=["Arrays", "Search", "Basics"],
        hints=[
            "Traverse from index 0 to len(arr) - 1.",
            "Compare arr[i] with target at each index.",
            "Return the first index i where arr[i] == target. If loop completes, return -1."
        ],
        examples=[
            {"input": "arr = [1, 2, 3, 4, 5], target = 3", "output": "2", "explanation": "3 is located at index 2."},
            {"input": "arr = [5, 4, 3], target = 6", "output": "-1", "explanation": "6 is not in the array."}
        ],
        explanation={
            "intuition": "For unsorted arrays, sequentially checking every element until a match is found is the standard search method.",
            "brute_force": "Linear search is O(N).",
            "optimal_approach": "for i in range(len(arr)): if arr[i] == target: return i; return -1.",
            "dry_run": "arr = [1, 2, 3], target = 2:\ni=0: arr[0]=1 != 2\ni=1: arr[1]=2 == 2 -> return 1.",
            "time_complexity": "O(N) in worst case.",
            "space_complexity": "O(1)",
            "common_mistakes": "Returning target value instead of its index.",
            "interview_questions": "Under what condition can search be faster than O(N)? (When the array is sorted, Binary Search runs in O(log N))."
        }
    ),
    Problem(
        id="union-two-sorted-arrays",
        title="Union of Two Sorted Arrays",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Easy",
        description="Given two sorted integer arrays a and b, return a sorted list containing the union of both arrays with all duplicate elements removed.",
        input_format="Two sorted integer lists a and b.",
        output_format="Return the sorted union list without duplicates.",
        constraints=["1 <= len(a), len(b) <= 10^5", "-10^9 <= a[i], b[j] <= 10^9"],
        function_name="findUnion",
        param_names=["a", "b"],
        starter_code={
            "python": "class Solution:\n    def findUnion(self, a: list[int], b: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> findUnion(vector<int>& a, vector<int>& b) {\n        return {};\n    }\n};",
            "java": "class Solution {\n    public List<Integer> findUnion(int[] a, int[] b) {\n        return new ArrayList<>();\n    }\n}",
            "javascript": "class Solution {\n    findUnion(a, b) {\n        return [];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"a": [1, 2, 3, 4, 5], "b": [1, 2, 3, 6, 7]}, expected_output=[1, 2, 3, 4, 5, 6, 7], is_hidden=False),
            TestCase(id=2, input_data={"a": [2, 2, 3, 4, 5], "b": [1, 1, 2, 3, 4]}, expected_output=[1, 2, 3, 4, 5], is_hidden=False),
            TestCase(id=3, input_data={"a": [1, 1, 1], "b": [2, 2, 2]}, expected_output=[1, 2], is_hidden=False),
            TestCase(id=4, input_data={"a": [10, 20, 30], "b": [5, 15, 25]}, expected_output=[5, 10, 15, 20, 25, 30], is_hidden=True),
        ],
        comparison_mode="exact",
        order=32,
        tags=["Arrays", "Two Pointers", "Union"],
        hints=[
            "Both arrays are already sorted.",
            "Use two pointers i and j to merge elements just like in merge sort.",
            "Only add an element if the output list is empty or the last added element is different from the current candidate."
        ],
        examples=[
            {"input": "a = [1, 2, 3, 4, 5], b = [1, 2, 3, 6, 7]", "output": "[1, 2, 3, 4, 5, 6, 7]", "explanation": "Combines elements from both arrays with duplicates omitted."},
            {"input": "a = [1, 1], b = [2, 2]", "output": "[1, 2]", "explanation": "Unique union elements."}
        ],
        explanation={
            "intuition": "Leverage sorted order of both arrays using two pointers to merge in O(N + M) time while filtering adjacent duplicates.",
            "brute_force": "Insert all elements into a Set and sort. Takes O((N+M) log(N+M)).",
            "optimal_approach": "Pointers i=0, j=0. Compare a[i] and b[j]. Take smaller (or either if equal). Append to union if union is empty or union[-1] != val. Advance pointers. Process remaining elements.",
            "dry_run": "a=[1, 2], b=[2, 3]:\ncompare 1, 2 -> take 1, union=[1], i=1.\ncompare 2, 2 -> take 2, union=[1, 2], i=2, j=1.\nremaining in b is 3 -> take 3, union=[1, 2, 3].",
            "time_complexity": "O(N + M)",
            "space_complexity": "O(N + M) for result.",
            "common_mistakes": "Adding duplicates from the same array into union.",
            "interview_questions": "How would you find the intersection of two sorted arrays? (Advance both pointers and only add when a[i] == b[j])."
        }
    ),
    Problem(
        id="find-missing-number",
        title="Find Missing Number in Range 1 to N",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Easy",
        description="Given an array arr containing n-1 distinct integers in the range 1 to n, find and return the one missing number.",
        input_format="A list of integers arr and integer n.",
        output_format="Return the missing integer.",
        constraints=["2 <= n <= 10^5", "len(arr) == n - 1", "1 <= arr[i] <= n"],
        function_name="findMissingNumber",
        param_names=["arr", "n"],
        starter_code={
            "python": "class Solution:\n    def findMissingNumber(self, arr: list[int], n: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int findMissingNumber(vector<int>& arr, int n) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int findMissingNumber(int[] arr, int n) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    findMissingNumber(arr, n) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 4, 5], "n": 5}, expected_output=3, is_hidden=False),
            TestCase(id=2, input_data={"arr": [1, 3], "n": 3}, expected_output=2, is_hidden=False),
            TestCase(id=3, input_data={"arr": [2], "n": 2}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 2, 3, 4, 5, 6, 7, 8, 10], "n": 10}, expected_output=9, is_hidden=True),
        ],
        comparison_mode="exact",
        order=33,
        tags=["Arrays", "Maths", "Bit Manipulation"],
        hints=[
            "The expected sum of numbers from 1 to n is n * (n + 1) // 2.",
            "Subtract the sum of elements in arr from the expected sum.",
            "Alternatively, XOR all numbers from 1 to n with all numbers in arr; identical pairs cancel out!"
        ],
        examples=[
            {"input": "arr = [1, 2, 4, 5], n = 5", "output": "3", "explanation": "The sequence from 1 to 5 is missing 3."},
            {"input": "arr = [1, 3], n = 3", "output": "2", "explanation": "Missing 2."}
        ],
        explanation={
            "intuition": "Sum or XOR of the complete sequence 1..n minus or XORed with the present elements immediately isolates the missing number.",
            "brute_force": "Search for each number from 1 to n in arr in O(N^2).",
            "optimal_approach": "Method 1 (Sum): return (n * (n + 1) // 2) - sum(arr).\nMethod 2 (XOR): xor_all = 0; for i in 1..n: xor_all ^= i; for x in arr: xor_all ^= x; return xor_all. Prevents integer overflow.",
            "dry_run": "arr = [1, 2, 4, 5], n = 5:\nExpected sum = 5 * 6 // 2 = 15.\nArray sum = 1 + 2 + 4 + 5 = 12.\nMissing = 15 - 12 = 3.",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Potential integer overflow in 32-bit languages if n is around 10^5 (sum can exceed 2*10^9).",
            "interview_questions": "Why is the XOR approach preferable to the sum approach in C++ or Java? (XOR avoids integer overflow entirely)."
        }
    ),
    Problem(
        id="max-consecutive-ones",
        title="Maximum Consecutive Ones",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Easy",
        description="Given a binary array arr consisting only of 0s and 1s, find the maximum number of consecutive 1s in the array.",
        input_format="A list of integers arr consisting of 0s and 1s.",
        output_format="Return the maximum consecutive count as an integer.",
        constraints=["1 <= len(arr) <= 10^5", "arr[i] in {0, 1}"],
        function_name="findMaxConsecutiveOnes",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def findMaxConsecutiveOnes(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int findMaxConsecutiveOnes(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int findMaxConsecutiveOnes(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    findMaxConsecutiveOnes(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 1, 0, 1, 1, 1]}, expected_output=3, is_hidden=False),
            TestCase(id=2, input_data={"arr": [1, 0, 1, 1, 0, 1]}, expected_output=2, is_hidden=False),
            TestCase(id=3, input_data={"arr": [0, 0, 0]}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 1, 1, 1]}, expected_output=4, is_hidden=True),
            TestCase(id=5, input_data={"arr": [0, 1]}, expected_output=1, is_hidden=True),
        ],
        comparison_mode="exact",
        order=34,
        tags=["Arrays", "Counting", "Sliding Window"],
        hints=[
            "Keep a current count of consecutive 1s and a max_count.",
            "When you see 1, increment current count and update max_count.",
            "When you see 0, reset current count to 0."
        ],
        examples=[
            {"input": "arr = [1, 1, 0, 1, 1, 1]", "output": "3", "explanation": "The last three digits are consecutive 1s."},
            {"input": "arr = [0, 0]", "output": "0", "explanation": "No 1s present."}
        ],
        explanation={
            "intuition": "A continuous run of 1s continues until interrupted by a 0.",
            "brute_force": "For every index i with 1, scan forward to count consecutive 1s in O(N^2).",
            "optimal_approach": "Single pass: max_cnt = 0, curr = 0. For x in arr: if x == 1: curr += 1; max_cnt = max(max_cnt, curr) else: curr = 0. Return max_cnt.",
            "dry_run": "[1, 1, 0, 1]:\n1: curr=1, max=1\n1: curr=2, max=2\n0: curr=0\n1: curr=1, max=2\nReturn 2.",
            "time_complexity": "O(N)",
            "space_complexity": "O(1)",
            "common_mistakes": "Forgetting to update max_count if the longest sequence is at the very end of the array.",
            "interview_questions": "What if you are allowed to flip at most k zeroes to 1s? (Sliding window problem)."
        }
    ),
    Problem(
        id="single-number-finder",
        title="Find the Number That Appears Only Once",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Easy",
        description="Given a non-empty array of integers arr where every element appears exactly twice except for one unique element which appears only once, find and return that single element.",
        input_format="A list of integers arr.",
        output_format="Return the single integer.",
        constraints=["1 <= len(arr) <= 10^5", "arr length is odd", "-10^9 <= arr[i] <= 10^9"],
        function_name="findSingleNumber",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def findSingleNumber(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int findSingleNumber(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int findSingleNumber(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    findSingleNumber(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [2, 2, 1]}, expected_output=1, is_hidden=False),
            TestCase(id=2, input_data={"arr": [4, 1, 2, 1, 2]}, expected_output=4, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1]}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"arr": [-1, -1, -2]}, expected_output=-2, is_hidden=True),
            TestCase(id=5, input_data={"arr": [10, 20, 30, 20, 10]}, expected_output=30, is_hidden=True),
        ],
        comparison_mode="exact",
        order=35,
        tags=["Arrays", "Bit Manipulation", "XOR"],
        hints=[
            "Can you count frequencies using a hash map? That takes O(N) space.",
            "Can you do it in O(1) space?",
            "Use XOR: x ^ x = 0 and x ^ 0 = x. If you XOR all elements together, identical pairs cancel out!"
        ],
        examples=[
            {"input": "arr = [4, 1, 2, 1, 2]", "output": "4", "explanation": "1 and 2 appear twice, 4 appears once."},
            {"input": "arr = [2, 2, 1]", "output": "1", "explanation": "1 appears once."}
        ],
        explanation={
            "intuition": "XOR is associative, commutative, and self-inverse: a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b.",
            "brute_force": "Count frequencies using Counter / Hash Map in O(N) time and O(N) space.",
            "optimal_approach": "ans = 0. For num in arr: ans ^= num. Return ans.",
            "dry_run": "[4, 1, 2, 1, 2]: ans = 0 ^ 4 = 4 -> 4 ^ 1 -> (4 ^ 1) ^ 2 -> 4 ^ (1 ^ 1) ^ 2 = 4 ^ 2 -> (4 ^ 2) ^ 2 = 4.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(1) auxiliary space.",
            "common_mistakes": "Assuming array is sorted (it is unsorted).",
            "interview_questions": "What if every element appears three times except one which appears once? (Count bit frequencies modulo 3)."
        }
    ),
    Problem(
        id="longest-subarray-sum-k",
        title="Longest Subarray with Sum K (Positives & Zeroes)",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.1: Easy",
        difficulty="Medium",
        description="Given an array arr of non-negative integers and an integer k, find the length of the longest contiguous subarray whose elements sum up to exactly k. Return 0 if no such subarray exists.",
        input_format="A list of non-negative integers arr and integer k.",
        output_format="Return the maximum length as an integer.",
        constraints=["1 <= len(arr) <= 10^5", "0 <= arr[i] <= 10^6", "1 <= k <= 10^9"],
        function_name="longestSubarray",
        param_names=["arr", "k"],
        starter_code={
            "python": "class Solution:\n    def longestSubarray(self, arr: list[int], k: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int longestSubarray(vector<int>& arr, int k) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int longestSubarray(int[] arr, int k) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    longestSubarray(arr, k) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 3, 1, 1, 1, 1, 4, 2, 3], "k": 3}, expected_output=3, is_hidden=False),
            TestCase(id=2, input_data={"arr": [2, 3, 5], "k": 5}, expected_output=2, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, 1, 1], "k": 5}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"arr": [10, 5, 2, 7, 1, 9], "k": 15}, expected_output=4, is_hidden=True),
        ],
        comparison_mode="exact",
        order=36,
        tags=["Arrays", "Two Pointers", "Sliding Window"],
        hints=[
            "Since elements are non-negative, extending the right pointer monotonically increases window sum.",
            "If current window sum exceeds k, shrink from the left pointer.",
            "When current window sum equals k, update max_len = max(max_len, right - left + 1)."
        ],
        examples=[
            {"input": "arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3], k = 3", "output": "3", "explanation": "Subarray [1, 1, 1] sums to 3 with length 3."},
            {"input": "arr = [2, 3, 5], k = 5", "output": "2", "explanation": "[2, 3] sums to 5 with length 2."}
        ],
        explanation={
            "intuition": "Because there are no negative numbers, the two-pointer sliding window is monotonic and gives optimal O(N) time with O(1) space.",
            "brute_force": "Check all subarray sums in O(N^2).",
            "optimal_approach": "left = 0, current_sum = 0, max_len = 0. For right in range(len(arr)): current_sum += arr[right]; while current_sum > k and left <= right: current_sum -= arr[left]; left += 1. If current_sum == k: max_len = max(max_len, right - left + 1). Return max_len.",
            "dry_run": "arr = [2, 3, 5], k = 5:\nright=0: sum=2\nright=1: sum=5 == k -> max_len = max(0, 1-0+1) = 2\nright=2: sum=10 > 5 -> shrink left=0 (sum=8), shrink left=1 (sum=5 == k) -> len=1. max_len=2.",
            "time_complexity": "O(N) - each element is visited at most twice.",
            "space_complexity": "O(1)",
            "common_mistakes": "Using two-pointer when array contains negative numbers (requires prefix hash map).",
            "interview_questions": "How does this solution change if the array contains negative numbers? (Must use prefix sum with HashMap in O(N) space)."
        }
    ),
    Problem(
        id="two-sum-sorted-pairs",
        title="Two Sum - Target Sum Pair Indices",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Medium",
        description="Given an array of integers arr and an integer target, find two distinct indices [i, j] such that arr[i] + arr[j] == target. Return the 0-based indices [i, j] in ascending order. If no such pair exists, return [-1, -1].",
        input_format="A list of integers arr and an integer target.",
        output_format="Return a list of two indices [i, j].",
        constraints=["2 <= len(arr) <= 10^5", "-10^9 <= target, arr[i] <= 10^9"],
        function_name="twoSum",
        param_names=["arr", "target"],
        starter_code={
            "python": "class Solution:\n    def twoSum(self, arr: list[int], target: int) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> twoSum(vector<int>& arr, int target) {\n        return {-1, -1};\n    }\n};",
            "java": "class Solution {\n    public int[] twoSum(int[] arr, int target) {\n        return new int[]{-1, -1};\n    }\n}",
            "javascript": "class Solution {\n    twoSum(arr, target) {\n        return [-1, -1];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [2, 7, 11, 15], "target": 9}, expected_output=[0, 1], is_hidden=False),
            TestCase(id=2, input_data={"arr": [3, 2, 4], "target": 6}, expected_output=[1, 2], is_hidden=False),
            TestCase(id=3, input_data={"arr": [3, 3], "target": 6}, expected_output=[0, 1], is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 2, 3], "target": 10}, expected_output=[-1, -1], is_hidden=True),
            TestCase(id=5, input_data={"arr": [-3, 4, 3, 90], "target": 0}, expected_output=[0, 2], is_hidden=True),
        ],
        comparison_mode="exact",
        order=37,
        tags=["Arrays", "Hash Map", "Two Sum"],
        hints=[
            "For each element arr[i], the complementary required value is target - arr[i].",
            "Can you store seen elements and their indices in a hash map as you traverse?",
            "If complement is found in map, you have found the pair!"
        ],
        examples=[
            {"input": "arr = [2, 7, 11, 15], target = 9", "output": "[0, 1]", "explanation": "arr[0] + arr[1] = 2 + 7 = 9."},
            {"input": "arr = [3, 2, 4], target = 6", "output": "[1, 2]", "explanation": "arr[1] + arr[2] = 2 + 4 = 6."}
        ],
        explanation={
            "intuition": "Instead of checking all pairs, store visited numbers in a dictionary. Looking up complement takes O(1) on average.",
            "brute_force": "Nested loops checking every pair (i, j) in O(N^2) time.",
            "optimal_approach": "seen = {}. For i, x in enumerate(arr): comp = target - x. If comp in seen: return [seen[comp], i]. seen[x] = i. Return [-1, -1].",
            "dry_run": "arr = [2, 7, 11, 15], target = 9:\ni=0, x=2: comp = 7 not in seen -> seen[2]=0.\ni=1, x=7: comp = 2 is in seen -> return [seen[2], 1] = [0, 1].",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(N) for hash map.",
            "common_mistakes": "Using the same element twice (e.g. 3 + 3 = 6 when only one 3 is in array).",
            "interview_questions": "How would you solve this if the array is already sorted and O(1) extra space is required? (Two-pointer technique from ends)."
        }
    ),
    Problem(
        id="majority-element-n2",
        title="Majority Element (> N/2 times using Boyer-Moore)",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Medium",
        description="Given an array of integers arr of size n, find the majority element. The majority element is the element that appears more than floor(n / 2) times. You may assume that the majority element always exists in the array.",
        input_format="A list of integers arr.",
        output_format="Return the majority integer.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="majorityElement",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def majorityElement(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int majorityElement(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int majorityElement(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    majorityElement(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [3, 2, 3]}, expected_output=3, is_hidden=False),
            TestCase(id=2, input_data={"arr": [2, 2, 1, 1, 1, 2, 2]}, expected_output=2, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1]}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"arr": [6, 5, 5]}, expected_output=5, is_hidden=True),
            TestCase(id=5, input_data={"arr": [7, 7, 7, 7, 1, 2, 3]}, expected_output=7, is_hidden=True),
        ],
        comparison_mode="exact",
        order=38,
        tags=["Arrays", "Boyer-Moore", "Voting"],
        hints=[
            "A hash map counts frequencies in O(N) space.",
            "Can you solve it in O(1) space?",
            "Use Boyer-Moore Voting Algorithm: maintain candidate and count. If count == 0, select current element. If same, increment count, else decrement."
        ],
        examples=[
            {"input": "arr = [3, 2, 3]", "output": "3", "explanation": "3 appears 2 times, which is > 3 // 2 = 1."},
            {"input": "arr = [2, 2, 1, 1, 1, 2, 2]", "output": "2", "explanation": "2 appears 4 times out of 7."}
        ],
        explanation={
            "intuition": "Since the majority element occurs > N/2 times, pairing different elements off against each other still leaves the majority element standing.",
            "brute_force": "Count occurrences of every element in O(N^2) or sort and pick arr[N//2] in O(N log N).",
            "optimal_approach": "Boyer-Moore Voting Algorithm: candidate = None, count = 0. For x in arr: if count == 0: candidate = x. Count += (1 if x == candidate else -1). Return candidate.",
            "dry_run": "[2, 2, 1, 1, 1, 2, 2]:\n2: cand=2, cnt=1\n2: cand=2, cnt=2\n1: cand=2, cnt=1\n1: cand=2, cnt=0\n1: cand=1, cnt=1\n2: cand=1, cnt=0\n2: cand=2, cnt=1\nResult: 2.",
            "time_complexity": "O(N)",
            "space_complexity": "O(1) auxiliary space.",
            "common_mistakes": "Assuming Boyer-Moore works when majority element is not guaranteed without a verification pass.",
            "interview_questions": "How does this generalize to finding elements appearing > N/3 times? (Maintain 2 candidates and 2 counters)."
        }
    ),
    Problem(
        id="maximum-subarray-sum-kadane",
        title="Maximum Subarray Sum (Kadane's Algorithm)",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Medium",
        description="Given an integer array arr, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.",
        input_format="A list of integers arr.",
        output_format="Return the maximum sum as an integer.",
        constraints=["1 <= len(arr) <= 10^5", "-10^4 <= arr[i] <= 10^4"],
        function_name="maxSubArray",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def maxSubArray(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int maxSubArray(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int maxSubArray(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    maxSubArray(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [-2, 1, -3, 4, -1, 2, 1, -5, 4]}, expected_output=6, is_hidden=False),
            TestCase(id=2, input_data={"arr": [1]}, expected_output=1, is_hidden=False),
            TestCase(id=3, input_data={"arr": [5, 4, -1, 7, 8]}, expected_output=23, is_hidden=False),
            TestCase(id=4, input_data={"arr": [-1, -2, -3]}, expected_output=-1, is_hidden=True),
            TestCase(id=5, input_data={"arr": [-5, 10, -2, 3]}, expected_output=11, is_hidden=True),
        ],
        comparison_mode="exact",
        order=39,
        tags=["Arrays", "Kadane's Algorithm", "Dynamic Programming"],
        hints=[
            "If your current running sum becomes negative, carrying it forward only hurts subsequent subarray sums.",
            "Whenever running sum drops below 0, reset it to 0.",
            "Maintain max_sum initialized to arr[0] (or -infinity) to handle arrays with all negative numbers."
        ],
        examples=[
            {"input": "arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]", "output": "6", "explanation": "Subarray [4, -1, 2, 1] has the largest sum = 6."},
            {"input": "arr = [1]", "output": "1", "explanation": "Single element."}
        ],
        explanation={
            "intuition": "Kadane's algorithm observes that a prefix subarray with negative sum will never contribute positively to any longer contiguous subarray.",
            "brute_force": "Compute sum of all possible subarrays in O(N^2) or O(N^3).",
            "optimal_approach": "max_so_far = arr[0], curr_max = arr[0]. For x in arr[1:]: curr_max = max(x, curr_max + x); max_so_far = max(max_so_far, curr_max). Return max_so_far.",
            "dry_run": "[-2, 1, -3, 4]:\ncurr = -2, max = -2\nx=1: curr = max(1, -2+1) = 1, max = 1\nx=-3: curr = max(-3, 1-3) = -2, max = 1\nx=4: curr = max(4, -2+4) = 4, max = 4. Return 4.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(1)",
            "common_mistakes": "Initializing max_sum to 0, which fails when all numbers in the array are negative.",
            "interview_questions": "How can you modify Kadane's to also return the starting and ending indices of the maximum subarray?"
        }
    ),
    Problem(
        id="stock-buy-sell-max-profit",
        title="Best Time to Buy and Sell Stock",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Easy",
        description="You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.",
        input_format="A list of non-negative integers prices.",
        output_format="Return the maximum profit integer.",
        constraints=["1 <= len(prices) <= 10^5", "0 <= prices[i] <= 10^4"],
        function_name="maxProfit",
        param_names=["prices"],
        starter_code={
            "python": "class Solution:\n    def maxProfit(self, prices: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int maxProfit(vector<int>& prices) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int maxProfit(int[] prices) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    maxProfit(prices) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"prices": [7, 1, 5, 3, 6, 4]}, expected_output=5, is_hidden=False),
            TestCase(id=2, input_data={"prices": [7, 6, 4, 3, 1]}, expected_output=0, is_hidden=False),
            TestCase(id=3, input_data={"prices": [1, 2]}, expected_output=1, is_hidden=False),
            TestCase(id=4, input_data={"prices": [2, 4, 1]}, expected_output=2, is_hidden=True),
            TestCase(id=5, input_data={"prices": [3, 8, 1, 5]}, expected_output=5, is_hidden=True),
        ],
        comparison_mode="exact",
        order=40,
        tags=["Arrays", "Dynamic Programming", "Greedy"],
        hints=[
            "To maximize profit selling on day i, you should have bought at the minimum price on days 0 through i-1.",
            "Maintain min_price seen so far as you iterate through prices.",
            "Potential profit selling today is prices[i] - min_price. Update max_profit accordingly."
        ],
        examples=[
            {"input": "prices = [7, 1, 5, 3, 6, 4]", "output": "5", "explanation": "Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5."},
            {"input": "prices = [7, 6, 4, 3, 1]", "output": "0", "explanation": "Prices continuously drop, no profit possible."}
        ],
        explanation={
            "intuition": "Every day you sell, the optimal buy day was the day with the minimum price before today.",
            "brute_force": "Compare every buy day i and sell day j > i in O(N^2).",
            "optimal_approach": "min_price = infinity, max_prof = 0. For p in prices: if p < min_price: min_price = p. Elif p - min_price > max_prof: max_prof = p - min_price. Return max_prof.",
            "dry_run": "[7, 1, 5, 3, 6]:\n7: min=7, prof=0\n1: min=1, prof=0\n5: prof = max(0, 5-1=4) = 4\n3: prof = max(4, 3-1=2) = 4\n6: prof = max(4, 6-1=5) = 5\nReturn 5.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(1)",
            "common_mistakes": "Trying to sell before buying (j < i).",
            "interview_questions": "What if you can buy and sell multiple times? (Greedy: capture every positive difference prices[i] - prices[i-1])."
        }
    ),
    Problem(
        id="rearrange-array-alternating",
        title="Rearrange Array Elements by Alternating Signs",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Medium",
        description="You are given an array arr of even length n containing an equal number of positive and negative integers. Rearrange the elements such that every consecutive pair has opposite signs, starting with a positive integer (i.e. positive, negative, positive, negative...). The relative order among positives and negatives must be preserved.",
        input_format="A list of integers arr containing equal positive and negative numbers.",
        output_format="Return the rearranged list.",
        constraints=["2 <= len(arr) <= 10^5", "len(arr) is even", "arr[i] != 0", "-10^5 <= arr[i] <= 10^5"],
        function_name="rearrangeArray",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def rearrangeArray(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> rearrangeArray(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] rearrangeArray(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    rearrangeArray(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [3, 1, -2, -5, 2, -4]}, expected_output=[3, -2, 1, -5, 2, -4], is_hidden=False),
            TestCase(id=2, input_data={"arr": [-1, 1]}, expected_output=[1, -1], is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, 2, 3, -1, -2, -3]}, expected_output=[1, -1, 2, -2, 3, -3], is_hidden=False),
            TestCase(id=4, input_data={"arr": [2, -3, 4, -5]}, expected_output=[2, -3, 4, -5], is_hidden=True),
        ],
        comparison_mode="exact",
        order=41,
        tags=["Arrays", "Two Pointers", "Rearrangement"],
        hints=[
            "Positives will end up at even indices: 0, 2, 4...",
            "Negatives will end up at odd indices: 1, 3, 5...",
            "Initialize an output array of size n. Use pos_idx = 0 and neg_idx = 1 to place elements in a single pass."
        ],
        examples=[
            {"input": "arr = [3, 1, -2, -5, 2, -4]", "output": "[3, -2, 1, -5, 2, -4]", "explanation": "Positives [3, 1, 2] placed at indices 0, 2, 4; Negatives [-2, -5, -4] at indices 1, 3, 5."},
            {"input": "arr = [-1, 1]", "output": "[1, -1]", "explanation": "Positive first, then negative."}
        ],
        explanation={
            "intuition": "Directly place each element into its designated parity index in the output array in a single traversal.",
            "brute_force": "Filter positives and negatives into two separate lists, then interleave them.",
            "optimal_approach": "ans = [0] * len(arr); pos = 0, neg = 1. For x in arr: if x > 0: ans[pos] = x; pos += 2; else: ans[neg] = x; neg += 2. Return ans.",
            "dry_run": "[3, 1, -2, -5]:\n3 (>0): ans[0]=3, pos=2\n1 (>0): ans[2]=1, pos=4\n-2 (<0): ans[1]=-2, neg=3\n-5 (<0): ans[3]=-5, neg=5\nResult: [3, -2, 1, -5].",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(N) for output array.",
            "common_mistakes": "Modifying in-place without auxiliary space loses relative ordering.",
            "interview_questions": "What if the number of positive and negative elements is not equal? (Append leftover elements to the end)."
        }
    ),
    Problem(
        id="next-permutation",
        title="Next Lexicographical Permutation",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Medium",
        description="A permutation of an array of integers is an arrangement of its members into a sequence. Given an array arr, rearrange it into the lexicographically next greater permutation in-place. If no such next greater permutation is possible, rearrange it into the lowest possible order (i.e. sorted in ascending order).",
        input_format="A list of integers arr.",
        output_format="Return the modified array.",
        constraints=["1 <= len(arr) <= 10^5", "-100 <= arr[i] <= 100"],
        function_name="nextPermutation",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def nextPermutation(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> nextPermutation(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] nextPermutation(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    nextPermutation(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 3]}, expected_output=[1, 3, 2], is_hidden=False),
            TestCase(id=2, input_data={"arr": [3, 2, 1]}, expected_output=[1, 2, 3], is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, 1, 5]}, expected_output=[1, 5, 1], is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 3, 2]}, expected_output=[2, 1, 3], is_hidden=True),
            TestCase(id=5, input_data={"arr": [2, 3, 1, 3, 3]}, expected_output=[2, 3, 3, 1, 3], is_hidden=True),
        ],
        comparison_mode="exact",
        order=42,
        tags=["Arrays", "Two Pointers", "Permutation"],
        hints=[
            "Find the first dip from the right: find largest index i such that arr[i] < arr[i+1].",
            "If no such dip exists, the array is strictly descending, so reverse the entire array.",
            "Otherwise, find the smallest element from the right that is strictly greater than arr[i], swap them, and reverse the subarray from index i+1 to end."
        ],
        examples=[
            {"input": "arr = [1, 2, 3]", "output": "[1, 3, 2]", "explanation": "Next permutation after [1, 2, 3] is [1, 3, 2]."},
            {"input": "arr = [3, 2, 1]", "output": "[1, 2, 3]", "explanation": "Largest permutation wraps around to smallest."}
        ],
        explanation={
            "intuition": "To make the next lexicographical permutation, we must change the suffix as far right as possible with the smallest possible increase.",
            "brute_force": "Generate all permutations, sort lexicographically, and find next permutation in O(N! * N).",
            "optimal_approach": "1. Find break-point i from right where arr[i] < arr[i+1]. 2. If i == -1, reverse arr. 3. Find j from right where arr[j] > arr[i]. 4. Swap arr[i], arr[j]. 5. Reverse arr[i+1:].",
            "dry_run": "[1, 3, 2]:\nDip: i=0 (1 < 3).\nj from right > 1: index 2 (val 2).\nSwap arr[0], arr[2] -> [2, 3, 1].\nReverse arr[1:] -> [2, 1, 3].",
            "time_complexity": "O(N) time.",
            "space_complexity": "O(1) in-place.",
            "common_mistakes": "Forgetting duplicate values (using >= instead of >).",
            "interview_questions": "How would you find the previous permutation? (Invert the comparison directions: find arr[i] > arr[i+1] from right)."
        }
    ),
    Problem(
        id="array-leaders",
        title="Find Leaders in an Array",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Easy",
        description="An element of an array is called a leader if it is greater than or equal to all the elements to its right. The rightmost element is always a leader. Given array arr, find all the leaders and return them in the order of their appearance from left to right.",
        input_format="A list of integers arr.",
        output_format="Return a list of leader integers in original left-to-right order.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="findLeaders",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def findLeaders(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> findLeaders(vector<int>& arr) {\n        return {};\n    }\n};",
            "java": "class Solution {\n    public List<Integer> findLeaders(int[] arr) {\n        return new ArrayList<>();\n    }\n}",
            "javascript": "class Solution {\n    findLeaders(arr) {\n        return [];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [16, 17, 4, 3, 5, 2]}, expected_output=[17, 5, 2], is_hidden=False),
            TestCase(id=2, input_data={"arr": [1, 2, 3, 4, 0]}, expected_output=[4, 0], is_hidden=False),
            TestCase(id=3, input_data={"arr": [5]}, expected_output=[5], is_hidden=False),
            TestCase(id=4, input_data={"arr": [10, 20, 30]}, expected_output=[30], is_hidden=True),
            TestCase(id=5, input_data={"arr": [7, 7, 7]}, expected_output=[7, 7, 7], is_hidden=True),
        ],
        comparison_mode="exact",
        order=43,
        tags=["Arrays", "Prefix/Suffix"],
        hints=[
            "Checking elements to the right of each element takes O(N^2) if done naively from left to right.",
            "What if you traverse the array from right to left?",
            "Maintain max_from_right. An element is a leader if arr[i] >= max_from_right."
        ],
        examples=[
            {"input": "arr = [16, 17, 4, 3, 5, 2]", "output": "[17, 5, 2]", "explanation": "17 >= all to its right (4,3,5,2); 5 >= 2; 2 has no elements to its right."},
            {"input": "arr = [1, 2, 3, 4, 0]", "output": "[4, 0]", "explanation": "4 and 0 are leaders."}
        ],
        explanation={
            "intuition": "Traversing backwards from right to left allows us to know the maximum element to the right of any index in O(1).",
            "brute_force": "For every i, loop j from i+1 to n-1 and check if arr[i] >= arr[j]. Takes O(N^2).",
            "optimal_approach": "leaders = []; max_right = -infinity. Loop i from n-1 down to 0: if arr[i] >= max_right: leaders.append(arr[i]); max_right = arr[i]. Reverse leaders and return.",
            "dry_run": "[16, 17, 4, 3, 5, 2]:\n2: >= -inf -> leader, max=2\n5: >= 2 -> leader, max=5\n3: < 5\n4: < 5\n17: >= 5 -> leader, max=17\n16: < 17\nCollected [2, 5, 17] -> reversed [17, 5, 2].",
            "time_complexity": "O(N) linear time.",
            "space_complexity": "O(N) to store leaders.",
            "common_mistakes": "Forgetting to reverse the collected leaders back to original left-to-right order.",
            "interview_questions": "Can this be solved using a monotonic stack? (Yes, monotonic decreasing stack)."
        }
    ),
    Problem(
        id="longest-consecutive-sequence-array",
        title="Longest Consecutive Sequence in Array",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Medium",
        description="Given an unsorted array of integers arr, return the length of the longest consecutive elements sequence (elements can appear in any order in the array). You must write an algorithm that runs in O(n) time.",
        input_format="A list of integers arr.",
        output_format="Return the integer length of the longest consecutive sequence.",
        constraints=["0 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="longestConsecutive",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def longestConsecutive(self, arr: list[int]) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int longestConsecutive(vector<int>& arr) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int longestConsecutive(int[] arr) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    longestConsecutive(arr) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [100, 4, 200, 1, 3, 2]}, expected_output=4, is_hidden=False),
            TestCase(id=2, input_data={"arr": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]}, expected_output=9, is_hidden=False),
            TestCase(id=3, input_data={"arr": []}, expected_output=0, is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 2, 0, 1]}, expected_output=3, is_hidden=True),
            TestCase(id=5, input_data={"arr": [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]}, expected_output=7, is_hidden=True),
        ],
        comparison_mode="exact",
        order=44,
        tags=["Arrays", "Hash Set", "Consecutive"],
        hints=[
            "Insert all numbers into a Hash Set for O(1) existence lookup.",
            "Only start counting a sequence if num - 1 is NOT in the set (this ensures we only start from sequence heads).",
            "While current_num + 1 is in the set, increment current sequence length."
        ],
        examples=[
            {"input": "arr = [100, 4, 200, 1, 3, 2]", "output": "4", "explanation": "The longest consecutive sequence is [1, 2, 3, 4], length = 4."},
            {"input": "arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]", "output": "9", "explanation": "Sequence 0 through 8 has length 9."}
        ],
        explanation={
            "intuition": "By only initiating a counting chain at the starting element of a sequence (when num - 1 is not in set), each element is visited at most twice.",
            "brute_force": "Sort array in O(N log N) and count consecutive runs.",
            "optimal_approach": "num_set = set(arr); longest = 0. For num in num_set: if (num - 1) not in num_set: curr = num; streak = 1; while (curr + 1) in num_set: curr += 1; streak += 1; longest = max(longest, streak). Return longest.",
            "dry_run": "{100, 4, 200, 1, 3, 2}:\n100: 99 not in set -> streak=1\n4: 3 in set -> skip\n200: 199 not in set -> streak=1\n1: 0 not in set -> 2,3,4 in set -> streak=4\nLongest = 4.",
            "time_complexity": "O(N) linear time.",
            "space_complexity": "O(N) for Hash Set.",
            "common_mistakes": "Checking sequence for every number instead of only heads (leads to O(N^2) worst case).",
            "interview_questions": "Can this be solved using Union-Find? (Yes, union contiguous elements and find size of largest component)."
        }
    ),
    Problem(
        id="set-matrix-zeroes",
        title="Set Matrix Zeroes",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Medium",
        description="Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.",
        input_format="A 2D list of integers matrix.",
        output_format="Return the modified 2D list.",
        constraints=["1 <= m, n <= 200", "-2^31 <= matrix[i][j] <= 2^31 - 1"],
        function_name="setZeroes",
        param_names=["matrix"],
        starter_code={
            "python": "class Solution:\n    def setZeroes(self, matrix: list[list[int]]) -> list[list[int]]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<vector<int>> setZeroes(vector<vector<int>>& matrix) {\n        return matrix;\n    }\n};",
            "java": "class Solution {\n    public int[][] setZeroes(int[][] matrix) {\n        return matrix;\n    }\n}",
            "javascript": "class Solution {\n    setZeroes(matrix) {\n        return matrix;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"matrix": [[1, 1, 1], [1, 0, 1], [1, 1, 1]]}, expected_output=[[1, 0, 1], [0, 0, 0], [1, 0, 1]], is_hidden=False),
            TestCase(id=2, input_data={"matrix": [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]}, expected_output=[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], is_hidden=False),
            TestCase(id=3, input_data={"matrix": [[1]]}, expected_output=[[1]], is_hidden=False),
            TestCase(id=4, input_data={"matrix": [[0]]}, expected_output=[[0]], is_hidden=True),
        ],
        comparison_mode="exact",
        order=45,
        tags=["Matrix", "Arrays", "In-place"],
        hints=[
            "If you set zeroes immediately during first pass, newly created zeroes will mistakenly cause other rows and columns to become zero.",
            "Can you use the first row and first column of the matrix itself as marker arrays?",
            "Use two extra booleans to record whether the first row and first column themselves initially contained a zero."
        ],
        examples=[
            {"input": "matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]", "output": "[[1, 0, 1], [0, 0, 0], [1, 0, 1]]", "explanation": "Row 1 and Column 1 are zeroed out."},
            {"input": "matrix = [[0, 1], [1, 1]]", "output": "[[0, 0], [0, 1]]", "explanation": "Row 0 and Col 0 set to 0."}
        ],
        explanation={
            "intuition": "Use row 0 and column 0 as markers to indicate which rows and columns must be zeroed, achieving O(1) extra space.",
            "brute_force": "Use two boolean arrays rows[m] and cols[n] in O(M + N) space.",
            "optimal_approach": "Track first_row_has_zero and first_col_has_zero. Use matrix[i][0] and matrix[0][j] as markers. Update matrix body from markers. Finally update first row and col.",
            "dry_run": "[[1,1,1],[1,0,1],[1,1,1]]: matrix[1][1]==0 sets matrix[1][0]=0 and matrix[0][1]=0. Updating body makes row 1 zero and col 1 zero.",
            "time_complexity": "O(M * N)",
            "space_complexity": "O(1) auxiliary space.",
            "common_mistakes": "Overwriting first row/col markers before using them to zero the inner cells.",
            "interview_questions": "How would you handle this if matrix is stored row-by-row on disk?"
        }
    ),
    Problem(
        id="rotate-matrix-90",
        title="Rotate Matrix 90 Degrees Clockwise",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Medium",
        description="You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees clockwise in-place.",
        input_format="An n x n 2D list of integers matrix.",
        output_format="Return the rotated matrix.",
        constraints=["1 <= n <= 100", "-1000 <= matrix[i][j] <= 1000"],
        function_name="rotateMatrix",
        param_names=["matrix"],
        starter_code={
            "python": "class Solution:\n    def rotateMatrix(self, matrix: list[list[int]]) -> list[list[int]]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<vector<int>> rotateMatrix(vector<vector<int>>& matrix) {\n        return matrix;\n    }\n};",
            "java": "class Solution {\n    public int[][] rotateMatrix(int[][] matrix) {\n        return matrix;\n    }\n}",
            "javascript": "class Solution {\n    rotateMatrix(matrix) {\n        return matrix;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}, expected_output=[[7, 4, 1], [8, 5, 2], [9, 6, 3]], is_hidden=False),
            TestCase(id=2, input_data={"matrix": [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]}, expected_output=[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]], is_hidden=False),
            TestCase(id=3, input_data={"matrix": [[1]]}, expected_output=[[1]], is_hidden=False),
            TestCase(id=4, input_data={"matrix": [[1, 2], [3, 4]]}, expected_output=[[3, 1], [4, 2]], is_hidden=True),
        ],
        comparison_mode="exact",
        order=46,
        tags=["Matrix", "Geometry", "In-place"],
        hints=[
            "Observe the relationship: element at (i, j) moves to (j, n - 1 - i).",
            "Can you achieve this in two simple matrix transformations?",
            "Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i]). Step 2: Reverse each row!"
        ],
        examples=[
            {"input": "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]", "output": "[[7, 4, 1], [8, 5, 2], [9, 6, 3]]", "explanation": "Clockwise 90-degree rotation."},
            {"input": "matrix = [[1, 2], [3, 4]]", "output": "[[3, 1], [4, 2]]", "explanation": "2x2 rotation."}
        ],
        explanation={
            "intuition": "Rotating a matrix 90 degrees clockwise is mathematically identical to transposing the matrix across its main diagonal, followed by reversing each row horizontally.",
            "brute_force": "Allocate a new n x n matrix and copy ans[j][n-1-i] = matrix[i][j]. Takes O(N^2) space.",
            "optimal_approach": "1. Transpose: for i in 0..n-1: for j in i+1..n-1: swap matrix[i][j], matrix[j][i]. 2. Reverse rows: for row in matrix: row.reverse(). Return matrix.",
            "dry_run": "[[1,2],[3,4]] -> Transpose: [[1,3],[2,4]] -> Reverse rows: [[3,1],[4,2]].",
            "time_complexity": "O(N^2)",
            "space_complexity": "O(1) in-place.",
            "common_mistakes": "Transposing twice or running j from 0 to n-1 which undoes swaps.",
            "interview_questions": "How would you rotate 90 degrees counter-clockwise? (Reverse each row first, then transpose)."
        }
    ),
    Problem(
        id="spiral-matrix-traversal",
        title="Spiral Traversal of Matrix",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Medium",
        description="Given an m x n matrix, return all elements of the matrix in spiral order (starting from top-left, going right, down, left, up).",
        input_format="A 2D list of integers matrix.",
        output_format="Return a list of integers in spiral order.",
        constraints=["1 <= m, n <= 100", "-100 <= matrix[i][j] <= 100"],
        function_name="spiralOrder",
        param_names=["matrix"],
        starter_code={
            "python": "class Solution:\n    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> spiralOrder(vector<vector<int>>& matrix) {\n        return {};\n    }\n};",
            "java": "class Solution {\n    public List<Integer> spiralOrder(int[][] matrix) {\n        return new ArrayList<>();\n    }\n}",
            "javascript": "class Solution {\n    spiralOrder(matrix) {\n        return [];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}, expected_output=[1, 2, 3, 6, 9, 8, 7, 4, 5], is_hidden=False),
            TestCase(id=2, input_data={"matrix": [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]}, expected_output=[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], is_hidden=False),
            TestCase(id=3, input_data={"matrix": [[1]]}, expected_output=[1], is_hidden=False),
            TestCase(id=4, input_data={"matrix": [[1, 2], [3, 4]]}, expected_output=[1, 2, 4, 3], is_hidden=True),
        ],
        comparison_mode="exact",
        order=47,
        tags=["Matrix", "Simulation", "Spiral"],
        hints=[
            "Maintain four boundaries: top, bottom, left, right.",
            "Traverse: 1. left to right on 'top' row, then top += 1. 2. top to bottom on 'right' column, then right -= 1.",
            "3. right to left on 'bottom' row (if top <= bottom), then bottom -= 1. 4. bottom to top on 'left' column (if left <= right), then left += 1."
        ],
        examples=[
            {"input": "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]", "output": "[1, 2, 3, 6, 9, 8, 7, 4, 5]", "explanation": "Spiral path: 1->2->3->6->9->8->7->4->5."},
            {"input": "matrix = [[1, 2], [3, 4]]", "output": "[1, 2, 4, 3]", "explanation": "Spiral traversal."}
        ],
        explanation={
            "intuition": "Simulate the spiral layer by layer, contracting the active rectangle boundaries (top, bottom, left, right) after each direction traverse.",
            "brute_force": "Track visited matrix cells with boolean visited table.",
            "optimal_approach": "top=0, bottom=m-1, left=0, right=n-1. While top <= bottom and left <= right: traverse top row -> top++; traverse right col -> right--; if top<=bottom: traverse bottom row -> bottom--; if left<=right: traverse left col -> left++. Return ans.",
            "dry_run": "[[1,2],[3,4]]:\nRight: 1, 2 (top=1)\nDown: 4 (right=0)\nLeft: 3 (bottom=0)\nUp: none (left=1 > right=0). Result: [1, 2, 4, 3].",
            "time_complexity": "O(M * N) visits every cell once.",
            "space_complexity": "O(1) auxiliary space (excluding result).",
            "common_mistakes": "Missing the top <= bottom or left <= right checks before traversing left and up in non-square matrices.",
            "interview_questions": "How would you generate an N x N matrix filled in spiral order from 1 to N^2?"
        }
    ),
    Problem(
        id="count-subarrays-with-given-sum",
        title="Count Subarrays with Sum Equals K",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.2: Medium",
        difficulty="Medium",
        description="Given an array of integers arr and an integer k, return the total number of continuous subarrays whose sum equals to k.",
        input_format="A list of integers arr and integer k.",
        output_format="Return the integer count of subarrays.",
        constraints=["1 <= len(arr) <= 10^5", "-1000 <= arr[i] <= 1000", "-10^7 <= k <= 10^7"],
        function_name="subarraySumCount",
        param_names=["arr", "k"],
        starter_code={
            "python": "class Solution:\n    def subarraySumCount(self, arr: list[int], k: int) -> int:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    int subarraySumCount(vector<int>& arr, int k) {\n        return 0;\n    }\n};",
            "java": "class Solution {\n    public int subarraySumCount(int[] arr, int k) {\n        return 0;\n    }\n}",
            "javascript": "class Solution {\n    subarraySumCount(arr, k) {\n        return 0;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 1, 1], "k": 2}, expected_output=2, is_hidden=False),
            TestCase(id=2, input_data={"arr": [1, 2, 3], "k": 3}, expected_output=2, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, -1, 0], "k": 0}, expected_output=3, is_hidden=False),
            TestCase(id=4, input_data={"arr": [3, 4, 7, 2, -3, 1, 4, 2], "k": 7}, expected_output=4, is_hidden=True),
        ],
        comparison_mode="exact",
        order=48,
        tags=["Arrays", "Prefix Sum", "Hash Map"],
        hints=[
            "Since elements can be negative, two-pointer sliding window does NOT work.",
            "Subarray sum between indices i and j is prefix_sum[j] - prefix_sum[i-1] == k.",
            "Therefore, prefix_sum[i-1] == prefix_sum[j] - k. Use a hash map to store frequencies of prefix sums!"
        ],
        examples=[
            {"input": "arr = [1, 1, 1], k = 2", "output": "2", "explanation": "[arr[0..1]] and [arr[1..2]] both sum to 2."},
            {"input": "arr = [1, 2, 3], k = 3", "output": "2", "explanation": "[1, 2] and [3] sum to 3."}
        ],
        explanation={
            "intuition": "Prefix sum property: if prefix_sum - k was seen m times previously, then there are m valid subarrays ending at the current index.",
            "brute_force": "Compute sum of every subarray with nested loops in O(N^2).",
            "optimal_approach": "prefix_counts = {0: 1}; curr_sum = 0; ans = 0. For x in arr: curr_sum += x; if (curr_sum - k) in prefix_counts: ans += prefix_counts[curr_sum - k]; prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1. Return ans.",
            "dry_run": "[1, 1, 1], k = 2:\nprefix_counts = {0: 1}\nx=1: sum=1, sum-k=-1 (not in map), counts={0:1, 1:1}\nx=1: sum=2, sum-k=0 (in map: +1), ans=1, counts={0:1, 1:1, 2:1}\nx=1: sum=3, sum-k=1 (in map: +1), ans=2, counts={...}\nReturn 2.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(N) for hash map.",
            "common_mistakes": "Forgetting to initialize prefix_counts with {0: 1} for subarrays starting at index 0.",
            "interview_questions": "Can you use this pattern to find subarrays whose length is divisible by k? (Prefix sum with modulo arithmetic)."
        }
    ),
    Problem(
        id="pascal-triangle-generator",
        title="Generate Pascal's Triangle Rows",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.3: Hard",
        difficulty="Easy",
        description="Given an integer numRows, generate and return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it.",
        input_format="An integer numRows.",
        output_format="Return a list of lists of integers.",
        constraints=["1 <= numRows <= 30"],
        function_name="generatePascal",
        param_names=["numRows"],
        starter_code={
            "python": "class Solution:\n    def generatePascal(self, numRows: int) -> list[list[int]]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<vector<int>> generatePascal(int numRows) {\n        return {};\n    }\n};",
            "java": "class Solution {\n    public List<List<Integer>> generatePascal(int numRows) {\n        return new ArrayList<>();\n    }\n}",
            "javascript": "class Solution {\n    generatePascal(numRows) {\n        return [];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"numRows": 5}, expected_output=[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], is_hidden=False),
            TestCase(id=2, input_data={"numRows": 1}, expected_output=[[1]], is_hidden=False),
            TestCase(id=3, input_data={"numRows": 3}, expected_output=[[1], [1, 1], [1, 2, 1]], is_hidden=False),
            TestCase(id=4, input_data={"numRows": 4}, expected_output=[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]], is_hidden=True),
        ],
        comparison_mode="exact",
        order=49,
        tags=["Arrays", "Maths", "Combinatorics"],
        hints=[
            "Row 0 is [1]. Row 1 is [1, 1].",
            "For row i, the first and last elements are always 1.",
            "Each middle element row[i][j] = prev_row[j - 1] + prev_row[j]."
        ],
        examples=[
            {"input": "numRows = 5", "output": "[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]", "explanation": "Standard 5 rows of Pascal's triangle."},
            {"input": "numRows = 1", "output": "[[1]]", "explanation": "First row only."}
        ],
        explanation={
            "intuition": "Pascal's triangle elements correspond to combinations C(n, k). Each row is formed from adjacent sums of the previous row.",
            "brute_force": "Compute combinations factorial formula for every cell in O(numRows^3).",
            "optimal_approach": "triangle = []; for i in range(numRows): row = [1] * (i + 1); for j in range(1, i): row[j] = triangle[i-1][j-1] + triangle[i-1][j]; triangle.append(row). Return triangle.",
            "dry_run": "numRows = 3:\ni=0: [1]\ni=1: [1, 1]\ni=2: row = [1, 1, 1]; j=1 -> row[1] = 1 + 1 = 2 -> [1, 2, 1].",
            "time_complexity": "O(numRows^2) total elements generated.",
            "space_complexity": "O(numRows^2) to store the triangle.",
            "common_mistakes": "Index out of bounds on middle elements.",
            "interview_questions": "How can you generate only the k-th row directly in O(k) time? (Using C(k, i) = C(k, i-1) * (k - i + 1) // i)."
        }
    ),
    Problem(
        id="merge-overlapping-intervals",
        title="Merge Overlapping Intervals",
        step_id=3,
        step_title="Step 3: Arrays",
        subtopic="3.3: Hard",
        difficulty="Medium",
        description="Given an array of intervals intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.",
        input_format="A list of 2-element integer lists intervals.",
        output_format="Return a list of merged 2-element integer lists.",
        constraints=["1 <= len(intervals) <= 10^5", "intervals[i].length == 2", "0 <= start_i <= end_i <= 10^5"],
        function_name="mergeIntervals",
        param_names=["intervals"],
        starter_code={
            "python": "class Solution:\n    def mergeIntervals(self, intervals: list[list[int]]) -> list[list[int]]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals) {\n        return {};\n    }\n};",
            "java": "class Solution {\n    public int[][] mergeIntervals(int[][] intervals) {\n        return new int[0][0];\n    }\n}",
            "javascript": "class Solution {\n    mergeIntervals(intervals) {\n        return [];\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"intervals": [[1, 3], [2, 6], [8, 10], [15, 18]]}, expected_output=[[1, 6], [8, 10], [15, 18]], is_hidden=False),
            TestCase(id=2, input_data={"intervals": [[1, 4], [4, 5]]}, expected_output=[[1, 5]], is_hidden=False),
            TestCase(id=3, input_data={"intervals": [[1, 4], [2, 3]]}, expected_output=[[1, 4]], is_hidden=False),
            TestCase(id=4, input_data={"intervals": [[6, 8], [1, 9], [2, 4]]}, expected_output=[[1, 9]], is_hidden=True),
        ],
        comparison_mode="exact",
        order=50,
        tags=["Arrays", "Sorting", "Intervals"],
        hints=[
            "First sort intervals based on their start times.",
            "Once sorted, any overlapping intervals will be adjacent.",
            "If current interval's start <= merged[-1]'s end, merge them: merged[-1][1] = max(merged[-1][1], current[1])."
        ],
        examples=[
            {"input": "intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]", "output": "[[1, 6], [8, 10], [15, 18]]", "explanation": "[1, 3] and [2, 6] overlap into [1, 6]."},
            {"input": "intervals = [[1, 4], [4, 5]]", "output": "[[1, 5]]", "explanation": "Intervals touching at boundary 4 merge into [1, 5]."}
        ],
        explanation={
            "intuition": "Sorting by start time guarantees that intervals can only overlap with their immediate predecessor in the merged list.",
            "brute_force": "Compare every interval with every other interval repeatedly in O(N^2).",
            "optimal_approach": "Sort intervals by x[0]. merged = [intervals[0]]. For interval in intervals[1:]: if interval[0] <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], interval[1]) else: merged.append(interval). Return merged.",
            "dry_run": "[[1,3],[2,6],[8,10]]: sorted.\n[1,3]: merged = [[1,3]]\n[2,6]: 2 <= 3 -> merged[-1][1] = max(3, 6) = 6 -> [[1,6]]\n[8,10]: 8 > 6 -> merged.append([8,10]) -> [[1,6],[8,10]].",
            "time_complexity": "O(N log N) dominated by sorting.",
            "space_complexity": "O(N) for output.",
            "common_mistakes": "Forgetting that an interval can be completely contained inside another (need max(merged[-1][1], interval[1])).",
            "interview_questions": "How would you solve the 'Insert Interval' problem where a new interval is added to already sorted non-overlapping intervals in O(N)?"
        }
    ),
]
