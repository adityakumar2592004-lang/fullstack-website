from models import Problem, TestCase

MODULE_2_PROBLEMS = [
    Problem(
        id="selection-sort",
        title="Selection Sort Algorithm",
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        subtopic="2.1: Sorting-I",
        difficulty="Easy",
        description="Given an array of integers arr, sort the array in ascending order using the Selection Sort algorithm and return the sorted array.",
        input_format="A list of integers arr.",
        output_format="Return the sorted list of integers.",
        constraints=["1 <= len(arr) <= 1000", "-10^5 <= arr[i] <= 10^5"],
        function_name="selectionSort",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def selectionSort(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> selectionSort(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] selectionSort(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    selectionSort(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [64, 25, 12, 22, 11]}, expected_output=[11, 12, 22, 25, 64], is_hidden=False),
            TestCase(id=2, input_data={"arr": [5, 4, 3, 2, 1]}, expected_output=[1, 2, 3, 4, 5], is_hidden=False),
            TestCase(id=3, input_data={"arr": [1]}, expected_output=[1], is_hidden=False),
            TestCase(id=4, input_data={"arr": [3, 3, 1, 2, 1]}, expected_output=[1, 1, 2, 3, 3], is_hidden=True),
            TestCase(id=5, input_data={"arr": [-10, 0, 5, -2, 8]}, expected_output=[-10, -2, 0, 5, 8], is_hidden=True),
        ],
        comparison_mode="exact",
        order=16,
        tags=["Sorting", "Algorithms", "Selection Sort"],
        hints=[
            "Divide the array into a sorted part and an unsorted part.",
            "In each step, scan the unsorted portion to find the minimum element.",
            "Swap this minimum element with the first element of the unsorted portion."
        ],
        examples=[
            {"input": "arr = [64, 25, 12, 22, 11]", "output": "[11, 12, 22, 25, 64]", "explanation": "Smallest element 11 moves to index 0, followed by 12 to index 1, etc."},
            {"input": "arr = [5, 4, 3, 2, 1]", "output": "[1, 2, 3, 4, 5]", "explanation": "Sorted in non-decreasing order."}
        ],
        explanation={
            "intuition": "Repeatedly find the minimum element from the unsorted part and place it at the beginning of the unsorted part.",
            "brute_force": "Selection sort inherently makes N*(N-1)/2 comparisons.",
            "optimal_approach": "Loop i from 0 to n-1: find min_idx in range i to n-1. Swap arr[i] with arr[min_idx]. Return arr.",
            "dry_run": "arr = [3, 1, 2]:\ni=0: min is 1 at index 1 -> swap arr[0], arr[1] -> [1, 3, 2]\ni=1: min is 2 at index 2 -> swap arr[1], arr[2] -> [1, 2, 3]\nDone.",
            "time_complexity": "O(N^2) for best, average, and worst cases.",
            "space_complexity": "O(1) in-place.",
            "common_mistakes": "Selection sort is not a stable sort by default because swapping can change relative order of identical elements.",
            "interview_questions": "When would you prefer Selection Sort over Quick Sort? (When memory writes are extremely expensive, as Selection Sort performs at most O(N) swaps)."
        }
    ),
    Problem(
        id="bubble-sort",
        title="Bubble Sort with Early Stopping",
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        subtopic="2.1: Sorting-I",
        difficulty="Easy",
        description="Given an array of integers arr, sort the array in ascending order using Bubble Sort with early stopping (optimized flag) and return the sorted array.",
        input_format="A list of integers arr.",
        output_format="Return the sorted list.",
        constraints=["1 <= len(arr) <= 1000", "-10^5 <= arr[i] <= 10^5"],
        function_name="bubbleSort",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def bubbleSort(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> bubbleSort(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] bubbleSort(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    bubbleSort(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [5, 1, 4, 2, 8]}, expected_output=[1, 2, 4, 5, 8], is_hidden=False),
            TestCase(id=2, input_data={"arr": [1, 2, 3, 4, 5]}, expected_output=[1, 2, 3, 4, 5], is_hidden=False),
            TestCase(id=3, input_data={"arr": [2, 1]}, expected_output=[1, 2], is_hidden=False),
            TestCase(id=4, input_data={"arr": [10, -1, 3, 8, 2]}, expected_output=[-1, 2, 3, 8, 10], is_hidden=True),
            TestCase(id=5, input_data={"arr": [0, 0, 0]}, expected_output=[0, 0, 0], is_hidden=True),
        ],
        comparison_mode="exact",
        order=17,
        tags=["Sorting", "Algorithms", "Bubble Sort"],
        hints=[
            "Compare adjacent elements arr[j] and arr[j+1]. If arr[j] > arr[j+1], swap them.",
            "After pass i, the largest element among the remaining unsorted prefix bubbles to the end.",
            "Use a boolean flag swapped: if no swaps occur during a pass, the array is already sorted, so break early."
        ],
        examples=[
            {"input": "arr = [5, 1, 4, 2, 8]", "output": "[1, 2, 4, 5, 8]", "explanation": "Adjacent inversions are swapped until sorted."},
            {"input": "arr = [1, 2, 3]", "output": "[1, 2, 3]", "explanation": "Already sorted, terminates in 1 pass."}
        ],
        explanation={
            "intuition": "Lighter elements 'bubble' to their correct position through pairwise adjacent swaps.",
            "brute_force": "Standard bubble sort runs all N passes regardless of sorted state in O(N^2).",
            "optimal_approach": "Add a swapped flag. If a full pass completes without any swaps, break immediately to achieve O(N) best case.",
            "dry_run": "arr = [5, 1, 4, 2]:\nPass 1: (5,1)->swap [1,5,4,2] -> (5,4)->swap [1,4,5,2] -> (5,2)->swap [1,4,2,5]. 5 is in place.\nPass 2: (1,4) ok -> (4,2) swap [1,2,4,5]. 4 is in place.\nPass 3: no swaps. Break early.",
            "time_complexity": "Best Case: O(N) when already sorted. Worst/Average: O(N^2).",
            "space_complexity": "O(1) in-place.",
            "common_mistakes": "Forgetting the inner loop upper limit n - 1 - i.",
            "interview_questions": "Is Bubble Sort stable? (Yes, adjacent elements are only swapped when arr[j] > arr[j+1], never when equal)."
        }
    ),
    Problem(
        id="insertion-sort",
        title="Insertion Sort Algorithm",
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        subtopic="2.1: Sorting-I",
        difficulty="Easy",
        description="Given an array of integers arr, sort the array in ascending order using Insertion Sort and return the sorted array.",
        input_format="A list of integers arr.",
        output_format="Return the sorted list.",
        constraints=["1 <= len(arr) <= 1000", "-10^5 <= arr[i] <= 10^5"],
        function_name="insertionSort",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def insertionSort(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> insertionSort(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] insertionSort(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    insertionSort(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [12, 11, 13, 5, 6]}, expected_output=[5, 6, 11, 12, 13], is_hidden=False),
            TestCase(id=2, input_data={"arr": [4, 3, 2, 10, 12, 1, 5, 6]}, expected_output=[1, 2, 3, 4, 5, 6, 10, 12], is_hidden=False),
            TestCase(id=3, input_data={"arr": [1]}, expected_output=[1], is_hidden=False),
            TestCase(id=4, input_data={"arr": [9, 8, 7, 6]}, expected_output=[6, 7, 8, 9], is_hidden=True),
            TestCase(id=5, input_data={"arr": [-3, -1, -4, -2]}, expected_output=[-4, -3, -2, -1], is_hidden=True),
        ],
        comparison_mode="exact",
        order=18,
        tags=["Sorting", "Algorithms", "Insertion Sort"],
        hints=[
            "Imagine sorting playing cards in your hand.",
            "Take element arr[i] as key, and shift all elements in arr[0..i-1] that are greater than key one position to the right.",
            "Insert key into its correct vacant position."
        ],
        examples=[
            {"input": "arr = [12, 11, 13, 5, 6]", "output": "[5, 6, 11, 12, 13]", "explanation": "Elements are sequentially inserted into sorted prefix."},
            {"input": "arr = [3, 1, 2]", "output": "[1, 2, 3]", "explanation": "Sorted result."}
        ],
        explanation={
            "intuition": "Build a sorted array prefix one element at a time by sliding larger predecessors to the right.",
            "brute_force": "Insertion sort itself runs in O(N^2) worst case.",
            "optimal_approach": "For i from 1 to n-1: key = arr[i]; j = i - 1; while j >= 0 and arr[j] > key: arr[j+1] = arr[j]; j -= 1; arr[j+1] = key. Return arr.",
            "dry_run": "arr = [12, 11, 13]:\ni=1: key=11. 12 > 11 -> arr[1]=12, arr[0]=11 -> [11, 12, 13]\ni=2: key=13. 12 <= 13 -> no shifts. Final: [11, 12, 13].",
            "time_complexity": "Best Case: O(N) when sorted. Worst/Average: O(N^2).",
            "space_complexity": "O(1) in-place.",
            "common_mistakes": "Forgetting the j >= 0 boundary check while shifting.",
            "interview_questions": "Why is Insertion Sort preferred for small arrays or nearly sorted data? (It has very low constant factor overhead and O(N) best case)."
        }
    ),
    Problem(
        id="merge-sort",
        title="Merge Sort (Divide and Conquer)",
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        subtopic="2.2: Sorting-II",
        difficulty="Medium",
        description="Given an array of integers arr, sort the array in ascending order using the Merge Sort algorithm and return the sorted array.",
        input_format="A list of integers arr.",
        output_format="Return the sorted list.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="mergeSort",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def mergeSort(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> mergeSort(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] mergeSort(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    mergeSort(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [38, 27, 43, 3, 9, 82, 10]}, expected_output=[3, 9, 10, 27, 38, 43, 82], is_hidden=False),
            TestCase(id=2, input_data={"arr": [5, 2, 3, 1]}, expected_output=[1, 2, 3, 5], is_hidden=False),
            TestCase(id=3, input_data={"arr": [1]}, expected_output=[1], is_hidden=False),
            TestCase(id=4, input_data={"arr": [10, -5, 20, -15, 0]}, expected_output=[-15, -5, 0, 10, 20], is_hidden=True),
            TestCase(id=5, input_data={"arr": [4, 2, 2, 8, 3, 3, 1]}, expected_output=[1, 2, 2, 3, 3, 4, 8], is_hidden=True),
        ],
        comparison_mode="exact",
        order=19,
        tags=["Sorting", "Divide and Conquer", "Merge Sort"],
        hints=[
            "Divide the array into two halves around the midpoint.",
            "Recursively sort the left and right halves.",
            "Merge the two sorted halves using a two-pointer technique into a combined sorted array."
        ],
        examples=[
            {"input": "arr = [38, 27, 43, 3, 9, 82, 10]", "output": "[3, 9, 10, 27, 38, 43, 82]", "explanation": "Divide recursively until size 1, then merge back up in order."},
            {"input": "arr = [5, 2, 3, 1]", "output": "[1, 2, 3, 5]", "explanation": "Sorted."}
        ],
        explanation={
            "intuition": "Divide-and-conquer paradigm. Splitting the problem into halves log(N) times and doing linear merges gives guaranteed O(N log N) runtime.",
            "brute_force": "O(N^2) comparison-based sorts.",
            "optimal_approach": "Divide array at mid = len(arr)//2. Left = mergeSort(arr[:mid]), Right = mergeSort(arr[mid:]). Merge left and right using two pointers: i, j. Append remaining elements.",
            "dry_run": "[4, 2, 1, 3] -> split [4,2] and [1,3] -> [4],[2] merged to [2,4]; [1],[3] merged to [1,3] -> merge [2,4] & [1,3]: compare (2,1)->1, (2,3)->2, (4,3)->3, 4 -> [1,2,3,4].",
            "time_complexity": "O(N log N) in all cases (best, average, worst).",
            "space_complexity": "O(N) auxiliary space for merging.",
            "common_mistakes": "Off-by-one errors when setting mid or merging unequal half lengths.",
            "interview_questions": "Is Merge Sort stable? (Yes, if during merge we pick from left array on equal elements: left[i] <= right[j])."
        }
    ),
    Problem(
        id="quick-sort",
        title="Quick Sort Algorithm",
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        subtopic="2.2: Sorting-II",
        difficulty="Medium",
        description="Given an array of integers arr, sort the array in ascending order using Quick Sort and return the sorted array.",
        input_format="A list of integers arr.",
        output_format="Return the sorted list.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="quickSort",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def quickSort(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> quickSort(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] quickSort(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    quickSort(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [10, 7, 8, 9, 1, 5]}, expected_output=[1, 5, 7, 8, 9, 10], is_hidden=False),
            TestCase(id=2, input_data={"arr": [4, 5, 1, 2, 3]}, expected_output=[1, 2, 3, 4, 5], is_hidden=False),
            TestCase(id=3, input_data={"arr": [2, 2, 2]}, expected_output=[2, 2, 2], is_hidden=False),
            TestCase(id=4, input_data={"arr": [-3, 4, -1, 0, 2]}, expected_output=[-3, -1, 0, 2, 4], is_hidden=True),
            TestCase(id=5, input_data={"arr": [100]}, expected_output=[100], is_hidden=True),
        ],
        comparison_mode="exact",
        order=20,
        tags=["Sorting", "Quick Sort", "Divide and Conquer"],
        hints=[
            "Pick an element as pivot (e.g. the last element or middle element).",
            "Partition the array such that elements smaller than pivot are on the left, and elements greater are on the right.",
            "Recursively apply quicksort to the left and right sub-arrays."
        ],
        examples=[
            {"input": "arr = [10, 7, 8, 9, 1, 5]", "output": "[1, 5, 7, 8, 9, 10]", "explanation": "Pivot partitioning places each element in its final sorted position."},
            {"input": "arr = [4, 5, 1, 2, 3]", "output": "[1, 2, 3, 4, 5]", "explanation": "Sorted."}
        ],
        explanation={
            "intuition": "Partitioning places the pivot element at its exact final sorted index, splitting the problem into two independent sub-problems.",
            "brute_force": "O(N^2) sorting methods.",
            "optimal_approach": "Partition with pivot: elements < pivot go left, elements > pivot go right. Recursively sort left and right partitions.",
            "dry_run": "arr = [4, 1, 3, 2], pivot = 2:\nPartition -> [1], 2, [4, 3].\nLeft [1] is base case.\nRight [4, 3] with pivot 3 -> [3], 4.\nCombined -> [1, 2, 3, 4].",
            "time_complexity": "Average: O(N log N). Worst Case: O(N^2) if pivot selection is unbalanced.",
            "space_complexity": "O(log N) recursion stack on average.",
            "common_mistakes": "Handling duplicate elements equal to the pivot incorrectly, causing infinite recursion.",
            "interview_questions": "How can you prevent Quick Sort's worst case O(N^2) on sorted arrays? (Use randomized pivot selection or median-of-three)."
        }
    ),
    Problem(
        id="recursive-bubble-sort",
        title="Recursive Bubble Sort Implementation",
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        subtopic="2.2: Sorting-II",
        difficulty="Easy",
        description="Implement Bubble Sort recursively. Given an array arr of integers, sort it in ascending order using recursion instead of an outer iterative loop.",
        input_format="A list of integers arr.",
        output_format="Return the sorted list.",
        constraints=["1 <= len(arr) <= 500", "-10^4 <= arr[i] <= 10^4"],
        function_name="recursiveBubbleSort",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def recursiveBubbleSort(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> recursiveBubbleSort(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] recursiveBubbleSort(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    recursiveBubbleSort(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [64, 34, 25, 12, 22, 11, 90]}, expected_output=[11, 12, 22, 25, 34, 64, 90], is_hidden=False),
            TestCase(id=2, input_data={"arr": [5, 1, 4, 2]}, expected_output=[1, 2, 4, 5], is_hidden=False),
            TestCase(id=3, input_data={"arr": [1]}, expected_output=[1], is_hidden=False),
            TestCase(id=4, input_data={"arr": [3, 2, 1]}, expected_output=[1, 2, 3], is_hidden=True),
        ],
        comparison_mode="exact",
        order=21,
        tags=["Sorting", "Recursion", "Bubble Sort"],
        hints=[
            "Base case: if array length n <= 1, return arr.",
            "Do one full pass of adjacent swaps up to n-1 to bubble the largest element to index n-1.",
            "Recursively call the function for size n-1."
        ],
        examples=[
            {"input": "arr = [5, 1, 4, 2]", "output": "[1, 2, 4, 5]", "explanation": "Recursively bubbles largest elements to end."},
            {"input": "arr = [3, 2, 1]", "output": "[1, 2, 3]", "explanation": "Sorted."}
        ],
        explanation={
            "intuition": "In iterative bubble sort, the outer loop runs N times. Replace the outer loop with a recursive function that decrements the active array boundary n.",
            "brute_force": "Iterative bubble sort.",
            "optimal_approach": "Helper solve(n): if n == 1 return; for j in range(n-1): if arr[j] > arr[j+1]: swap. solve(n-1). Call solve(len(arr)).",
            "dry_run": "[3, 2, 1]:\npass 1 (n=3): [2, 1, 3] -> calls solve(2)\npass 2 (n=2): [1, 2, 3] -> calls solve(1)\npass 3 (n=1): base case hit, returns.",
            "time_complexity": "O(N^2)",
            "space_complexity": "O(N) call stack.",
            "common_mistakes": "Exceeding recursion depth limit if input size is too large.",
            "interview_questions": "What is the overhead of recursive bubble sort compared to iterative? (Function call frames on the stack consume O(N) memory)."
        }
    ),
    Problem(
        id="recursive-insertion-sort",
        title="Recursive Insertion Sort Implementation",
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        subtopic="2.2: Sorting-II",
        difficulty="Easy",
        description="Implement Insertion Sort recursively. Given an array arr, sort it in ascending order by recursively sorting the first n-1 elements and then inserting the nth element into its correct position.",
        input_format="A list of integers arr.",
        output_format="Return the sorted list.",
        constraints=["1 <= len(arr) <= 500", "-10^4 <= arr[i] <= 10^4"],
        function_name="recursiveInsertionSort",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def recursiveInsertionSort(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> recursiveInsertionSort(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] recursiveInsertionSort(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    recursiveInsertionSort(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [9, 5, 1, 4, 3]}, expected_output=[1, 3, 4, 5, 9], is_hidden=False),
            TestCase(id=2, input_data={"arr": [2, 1]}, expected_output=[1, 2], is_hidden=False),
            TestCase(id=3, input_data={"arr": [1]}, expected_output=[1], is_hidden=False),
            TestCase(id=4, input_data={"arr": [10, -2, 5, 3]}, expected_output=[-2, 3, 5, 10], is_hidden=True),
        ],
        comparison_mode="exact",
        order=22,
        tags=["Sorting", "Recursion", "Insertion Sort"],
        hints=[
            "Base case: if n <= 1, the first element is already sorted.",
            "Recursively sort the first n-1 elements.",
            "Insert the nth element arr[n-1] into the sorted subarray arr[0..n-2]."
        ],
        examples=[
            {"input": "arr = [9, 5, 1, 4, 3]", "output": "[1, 3, 4, 5, 9]", "explanation": "Sorted recursively."},
            {"input": "arr = [2, 1]", "output": "[1, 2]", "explanation": "Sorted."}
        ],
        explanation={
            "intuition": "Assume arr[0..n-2] is sorted by the recursive step. We only need to insert arr[n-1] into its appropriate position in that sorted prefix.",
            "brute_force": "Standard iterative insertion sort.",
            "optimal_approach": "Helper(n): if n <= 1: return; helper(n-1); last = arr[n-1]; j = n-2; while j >= 0 and arr[j] > last: arr[j+1] = arr[j]; j -= 1; arr[j+1] = last. Return arr.",
            "dry_run": "[3, 1, 2]: helper(3) calls helper(2) calls helper(1) [3].\nThen insert 1 into [3] -> [1, 3].\nThen insert 2 into [1, 3] -> [1, 2, 3].",
            "time_complexity": "O(N^2)",
            "space_complexity": "O(N) call stack.",
            "common_mistakes": "Inserting into the prefix before the recursive call returns.",
            "interview_questions": "How does this compare to inductive reasoning in mathematics?"
        }
    ),
    Problem(
        id="check-array-sorted",
        title="Check if Array is Sorted",
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        subtopic="2.1: Sorting-I",
        difficulty="Easy",
        description="Given an array of integers arr, determine whether it is sorted in non-decreasing order (arr[i] <= arr[i+1] for all valid i). Return True if sorted, otherwise False.",
        input_format="A list of integers arr.",
        output_format="Return True if sorted, False otherwise.",
        constraints=["1 <= len(arr) <= 10^5", "-10^9 <= arr[i] <= 10^9"],
        function_name="isSorted",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def isSorted(self, arr: list[int]) -> bool:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    bool isSorted(vector<int>& arr) {\n        return true;\n    }\n};",
            "java": "class Solution {\n    public boolean isSorted(int[] arr) {\n        return true;\n    }\n}",
            "javascript": "class Solution {\n    isSorted(arr) {\n        return true;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [1, 2, 3, 4, 5]}, expected_output=True, is_hidden=False),
            TestCase(id=2, input_data={"arr": [5, 4, 3, 2, 1]}, expected_output=False, is_hidden=False),
            TestCase(id=3, input_data={"arr": [1, 2, 2, 3]}, expected_output=True, is_hidden=False),
            TestCase(id=4, input_data={"arr": [10]}, expected_output=True, is_hidden=False),
            TestCase(id=5, input_data={"arr": [1, 3, 2, 4]}, expected_output=False, is_hidden=True),
            TestCase(id=6, input_data={"arr": [-5, -2, -1, 0, 7]}, expected_output=True, is_hidden=True),
        ],
        comparison_mode="exact",
        order=23,
        tags=["Arrays", "Sorting", "Basics"],
        hints=[
            "Compare each adjacent pair arr[i] and arr[i-1].",
            "If arr[i] < arr[i-1] for any index i >= 1, the array cannot be sorted.",
            "If the loop finishes without violations, the array is sorted."
        ],
        examples=[
            {"input": "arr = [1, 2, 2, 3]", "output": "True", "explanation": "Every element is greater than or equal to its predecessor."},
            {"input": "arr = [1, 3, 2]", "output": "False", "explanation": "3 > 2 at index 1 and 2, which violates non-decreasing order."}
        ],
        explanation={
            "intuition": "A single inversion where arr[i] > arr[i+1] is sufficient to disprove that the array is sorted.",
            "brute_force": "Compare all pairs (i, j) with i < j to ensure arr[i] <= arr[j] in O(N^2).",
            "optimal_approach": "Single linear pass: for i in range(1, len(arr)): if arr[i] < arr[i-1]: return False. Return True.",
            "dry_run": "arr = [1, 3, 2]:\ni=1: arr[1] (3) >= arr[0] (1) -> ok\ni=2: arr[2] (2) < arr[1] (3) -> violation! Return False.",
            "time_complexity": "O(N) time with early exit.",
            "space_complexity": "O(1) auxiliary space.",
            "common_mistakes": "Using strictly less than (<) instead of <= for duplicates.",
            "interview_questions": "How can you check if an array was originally sorted but then rotated? (Check if number of drop points arr[i] > arr[i+1] is <= 1)."
        }
    ),
    Problem(
        id="sort-by-parity",
        title="Sort Array by Parity",
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        subtopic="2.1: Sorting-I",
        difficulty="Easy",
        description="Given an array of integers arr, rearrange the elements such that all even integers appear before all odd integers. The relative order within evens and odds does not matter. Return the modified array.",
        input_format="A list of integers arr.",
        output_format="Return the partitioned list.",
        constraints=["1 <= len(arr) <= 10^5", "0 <= arr[i] <= 10^9"],
        function_name="sortByParity",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def sortByParity(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> sortByParity(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] sortByParity(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    sortByParity(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [3, 1, 2, 4]}, expected_output=[4, 2, 1, 3], is_hidden=False),
            TestCase(id=2, input_data={"arr": [0]}, expected_output=[0], is_hidden=False),
            TestCase(id=3, input_data={"arr": [2, 4, 6]}, expected_output=[2, 4, 6], is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 3, 5]}, expected_output=[1, 3, 5], is_hidden=True),
        ],
        comparison_mode="unordered",  # Parity partition allows any relative order as long as parity condition holds
        order=24,
        tags=["Two Pointers", "Sorting", "Parity"],
        hints=[
            "Can you use a two-pointer approach similar to quicksort partitioning?",
            "Pointer left at start, pointer right at end.",
            "If left is odd and right is even, swap them and move both inward."
        ],
        examples=[
            {"input": "arr = [3, 1, 2, 4]", "output": "[4, 2, 1, 3]", "explanation": "Evens [4, 2] come before odds [1, 3]."},
            {"input": "arr = [0]", "output": "[0]", "explanation": "Single even element."}
        ],
        explanation={
            "intuition": "This is a two-way partition problem where the condition is (x % 2 == 0).",
            "brute_force": "Filter all evens into one list, odds into another, and concatenate.",
            "optimal_approach": "Two pointers left=0, right=n-1. While left < right: if left is odd and right is even, swap arr[left], arr[right]. Increment left if even, decrement right if odd.",
            "dry_run": "[3, 1, 2, 4]: left=0 (3, odd), right=3 (4, even) -> swap -> [4, 1, 2, 3]. left=1 (1, odd), right=2 (2, even) -> swap -> [4, 2, 1, 3]. Done.",
            "time_complexity": "O(N) single pass.",
            "space_complexity": "O(1) in-place.",
            "common_mistakes": "Incrementing both pointers when only one meets its parity condition.",
            "interview_questions": "What if you must preserve the original relative order of elements? (Requires O(N) extra space or stable partitioning in O(N log N))."
        }
    ),
    Problem(
        id="sort-colors-three-pointers",
        title="Sort Array of 0s, 1s, and 2s (Dutch National Flag)",
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        subtopic="2.2: Sorting-II",
        difficulty="Medium",
        description="Given an array arr containing only numbers 0, 1, and 2, sort the array in-place in ascending order without using library sort functions.",
        input_format="A list of integers arr containing only 0, 1, and 2.",
        output_format="Return the sorted list.",
        constraints=["1 <= len(arr) <= 10^5", "arr[i] in {0, 1, 2}"],
        function_name="sortColors",
        param_names=["arr"],
        starter_code={
            "python": "class Solution:\n    def sortColors(self, arr: list[int]) -> list[int]:\n        # Write your code here\n        pass\n",
            "cpp": "class Solution {\npublic:\n    vector<int> sortColors(vector<int>& arr) {\n        return arr;\n    }\n};",
            "java": "class Solution {\n    public int[] sortColors(int[] arr) {\n        return arr;\n    }\n}",
            "javascript": "class Solution {\n    sortColors(arr) {\n        return arr;\n    }\n}"
        },
        test_cases=[
            TestCase(id=1, input_data={"arr": [2, 0, 2, 1, 1, 0]}, expected_output=[0, 0, 1, 1, 2, 2], is_hidden=False),
            TestCase(id=2, input_data={"arr": [2, 0, 1]}, expected_output=[0, 1, 2], is_hidden=False),
            TestCase(id=3, input_data={"arr": [0]}, expected_output=[0], is_hidden=False),
            TestCase(id=4, input_data={"arr": [1, 1, 0, 2, 0, 1, 2]}, expected_output=[0, 0, 1, 1, 1, 2, 2], is_hidden=True),
            TestCase(id=5, input_data={"arr": [2, 2, 1, 1, 0, 0]}, expected_output=[0, 0, 1, 1, 2, 2], is_hidden=True),
        ],
        comparison_mode="exact",
        order=25,
        tags=["Sorting", "Two Pointers", "Dutch National Flag"],
        hints=[
            "A counting approach counts occurrences of 0, 1, 2 and overwrites array in 2 passes.",
            "Can you do it in a single pass with O(1) space?",
            "Use three pointers: low, mid, and high. Keep 0s before low, 1s between low and mid, and 2s after high."
        ],
        examples=[
            {"input": "arr = [2, 0, 2, 1, 1, 0]", "output": "[0, 0, 1, 1, 2, 2]", "explanation": "All 0s first, then 1s, then 2s."},
            {"input": "arr = [2, 0, 1]", "output": "[0, 1, 2]", "explanation": "Sorted."}
        ],
        explanation={
            "intuition": "Dijkstra's Dutch National Flag algorithm partitions the array into three sections [0..low-1] for 0s, [low..mid-1] for 1s, [mid..high] unprocessed, [high+1..n-1] for 2s.",
            "brute_force": "Counting sort with 2 passes: count frequencies of 0, 1, and 2, then write them back.",
            "optimal_approach": "Maintain low=0, mid=0, high=len(arr)-1. While mid <= high: if arr[mid] == 0: swap(arr[low], arr[mid]); low += 1; mid += 1. Elif arr[mid] == 1: mid += 1. Else (arr[mid] == 2): swap(arr[mid], arr[high]); high -= 1. Return arr.",
            "dry_run": "arr = [2, 0, 1]: low=0, mid=0, high=2.\nmid=0, arr[0]=2: swap(0, 2) -> [1, 0, 2], high=1.\nmid=0, arr[0]=1: mid=1.\nmid=1, arr[1]=0: swap(low=0, mid=1) -> [0, 1, 2], low=1, mid=2.\nmid > high (2 > 1) -> terminate. Result: [0, 1, 2].",
            "time_complexity": "O(N) strictly one single pass.",
            "space_complexity": "O(1) in-place.",
            "common_mistakes": "Incrementing mid when swapping with high (the swapped element from high has not yet been processed).",
            "interview_questions": "How does Dutch National Flag generalize to 3-way QuickSort with duplicate elements?"
        }
    ),
]
