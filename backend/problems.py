from typing import List, Optional, Dict
from models import Problem, StepSummary

from problems_data.module1 import MODULE_1_PROBLEMS
from problems_data.module2 import MODULE_2_PROBLEMS
from problems_data.module3 import MODULE_3_PROBLEMS
from problems_data.module4 import MODULE_4_PROBLEMS
from problems_data.module5 import MODULE_5_PROBLEMS

# Combine all 85 problems for Modules 1-5
PROBLEMS_DB: List[Problem] = (
    MODULE_1_PROBLEMS +
    MODULE_2_PROBLEMS +
    MODULE_3_PROBLEMS +
    MODULE_4_PROBLEMS +
    MODULE_5_PROBLEMS
)

# Lookup dictionary for fast O(1) retrieval
_PROBLEMS_BY_ID: Dict[str, Problem] = {p.id: p for p in PROBLEMS_DB}

def get_problem_by_id(problem_id: str) -> Optional[Problem]:
    return _PROBLEMS_BY_ID.get(problem_id)

# Full 20 Steps Catalog according to roadmap
ALL_STEPS_CATALOG: List[StepSummary] = [
    StepSummary(
        step_id=1,
        step_title="Step 1: Beginner Problems",
        total_problems=len(MODULE_1_PROBLEMS),
        subtopics=[
            "1.1: Basic Input and Output",
            "1.2: Conditional Statements",
            "1.3: Pattern Problems",
            "1.4: Know Basic Maths",
            "1.5: Functions",
            "1.6: Time and Space Complexity"
        ]
    ),
    StepSummary(
        step_id=2,
        step_title="Step 2: Sorting Techniques",
        total_problems=len(MODULE_2_PROBLEMS),
        subtopics=[
            "2.1: Sorting-I",
            "2.2: Sorting-II"
        ]
    ),
    StepSummary(
        step_id=3,
        step_title="Step 3: Arrays",
        total_problems=len(MODULE_3_PROBLEMS),
        subtopics=[
            "3.1: Easy",
            "3.2: Medium",
            "3.3: Hard"
        ]
    ),
    StepSummary(
        step_id=4,
        step_title="Step 4: Hashing",
        total_problems=len(MODULE_4_PROBLEMS),
        subtopics=[
            "4.1: Frequency Counting",
            "4.2: Hash Set",
            "4.3: Hash Map",
            "4.4: Prefix Hashing"
        ]
    ),
    StepSummary(
        step_id=5,
        step_title="Step 5: Binary Search",
        total_problems=len(MODULE_5_PROBLEMS),
        subtopics=[
            "5.1: BS on 1D Arrays",
            "5.2: BS on Answers",
            "5.3: BS on 2D Arrays"
        ]
    ),
    StepSummary(step_id=6, step_title="Step 6: Strings", total_problems=0, subtopics=["6.1: Basic Strings", "6.2: Medium Strings"]),
    StepSummary(step_id=7, step_title="Step 7: Recursion", total_problems=0, subtopics=["7.1: Recursion Basics", "7.2: Subsequences Pattern"]),
    StepSummary(step_id=8, step_title="Step 8: Linked List", total_problems=0, subtopics=["8.1: Singly Linked List", "8.2: Doubly Linked List"]),
    StepSummary(step_id=9, step_title="Step 9: Bit Manipulation", total_problems=0, subtopics=["9.1: Bit Tricks", "9.2: Advanced Bits"]),
    StepSummary(step_id=10, step_title="Step 10: Greedy", total_problems=0, subtopics=["10.1: Easy Greedy", "10.2: Medium/Hard Greedy"]),
    StepSummary(step_id=11, step_title="Step 11: Sliding Window / Two Pointer", total_problems=0, subtopics=["11.1: Constant Window", "11.2: Dynamic Window"]),
    StepSummary(step_id=12, step_title="Step 12: Stack / Queue", total_problems=0, subtopics=["12.1: Monotonic Stack", "12.2: Implementation"]),
    StepSummary(step_id=13, step_title="Step 13: Binary Trees", total_problems=0, subtopics=["13.1: Traversals", "13.2: Medium Problems"]),
    StepSummary(step_id=14, step_title="Step 14: Binary Search Tree", total_problems=0, subtopics=["14.1: Concept", "14.2: Practice Problems"]),
    StepSummary(step_id=15, step_title="Step 15: Heaps", total_problems=0, subtopics=["15.1: Priority Queue", "15.2: K-Way Merging"]),
    StepSummary(step_id=16, step_title="Step 16: Graphs", total_problems=0, subtopics=["16.1: BFS/DFS", "16.2: Shortest Path"]),
    StepSummary(step_id=17, step_title="Step 17: Dynamic Programming", total_problems=0, subtopics=["17.1: 1D DP", "17.2: 2D/3D DP", "17.3: DP on Strings"]),
    StepSummary(step_id=18, step_title="Step 18: Tries", total_problems=0, subtopics=["18.1: Trie Operations", "18.2: Bitwise Trie"]),
    StepSummary(step_id=19, step_title="Step 19: Advanced Strings", total_problems=0, subtopics=["19.1: KMP Algorithm", "19.2: Z-Algorithm"]),
    StepSummary(step_id=20, step_title="Step 20: Maths", total_problems=0, subtopics=["20.1: Prime Sieve", "20.2: Combinatorics"])
]

def get_steps_summary() -> List[StepSummary]:
    return ALL_STEPS_CATALOG
