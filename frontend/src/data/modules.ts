import type { ModuleInfo } from '../types';

export const ROADMAP_MODULES: ModuleInfo[] = [
  {
    id: 1,
    title: "Beginner Problems",
    description: "Master fundamentals: Input/Output, conditionals, loops, functions, basic number maths, and patterns.",
    isComingSoon: false,
    topics: [
      { id: "1.1", title: "1.1: Basic Input and Output", description: "Standard IO, types, and arithmetic." },
      { id: "1.2", title: "1.2: Conditional Statements", description: "If-else branch decisions and parity logic." },
      { id: "1.3", title: "1.3: Pattern Problems", description: "Triangles, pyramids, and nested loop reasoning." },
      { id: "1.4", title: "1.4: Know Basic Maths", description: "Digits extraction, reversing, GCD, primes, and Armstrong numbers." },
      { id: "1.5", title: "1.5: Functions", description: "Parameters, return types, and sequence generators." },
      { id: "1.6", title: "1.6: Time and Space Complexity", description: "Analyzing Big-O growth and loop iterations." },
    ]
  },
  {
    id: 2,
    title: "Sorting",
    description: "Learn essential comparison and divide-and-conquer sorting algorithms with in-depth time complexity.",
    isComingSoon: false,
    topics: [
      { id: "2.1", title: "2.1: Sorting-I", description: "Selection sort, Bubble sort, Insertion sort, and parity sorting." },
      { id: "2.2", title: "2.2: Sorting-II", description: "Merge sort, Quick sort, recursive implementations, and 3-way partition." },
    ]
  },
  {
    id: 3,
    title: "Arrays",
    description: "Core array manipulations, sliding window, two-pointer techniques, Kadane's algorithm, and 2D matrix problems.",
    isComingSoon: false,
    topics: [
      { id: "3.1", title: "3.1: Easy", description: "Largest/second largest, duplicates removal, rotation, union, missing number, consecutive ones." },
      { id: "3.2", title: "3.2: Medium", description: "Two Sum, Kadane's maximum subarray, stock profit, next permutation, leaders, matrix rotation." },
      { id: "3.3", title: "3.3: Hard", description: "Pascal's triangle, merge intervals, and subarray sums." },
    ]
  },
  {
    id: 4,
    title: "Hashing",
    description: "Harness Hash Maps and Hash Sets for O(1) lookups, frequency counting, and prefix sum/XOR subarray tracking.",
    isComingSoon: false,
    topics: [
      { id: "4.1", title: "4.1: Frequency Counting", description: "Element and character counters, most/least frequent elements." },
      { id: "4.2", title: "4.2: Hash Set", description: "Distinct elements, set intersection, first repeating element, and longest consecutive sequences." },
      { id: "4.3", title: "4.3: Hash Map", description: "Two Sum, pairs with difference, anagram grouping, and isomorphic strings." },
      { id: "4.4", title: "4.4: Prefix Hashing", description: "Zero-sum subarrays, longest subarray with sum K, and prefix XOR counters." },
    ]
  },
  {
    id: 5,
    title: "Binary Search",
    description: "Search in sorted space, lower/upper bounds, rotated arrays, peak elements, and monotonic search on answers.",
    isComingSoon: false,
    topics: [
      { id: "5.1", title: "5.1: BS on 1D Arrays", description: "Binary search, lower/upper bound, insert position, rotated array search, single non-duplicate, and peaks." },
      { id: "5.2", title: "5.2: BS on Answers", description: "Square root, Nth root, Koko eating bananas, bouqet blooming, ship packages, and aggressive cows." },
      { id: "5.3", title: "5.3: BS on 2D Arrays", description: "Search in 2D sorted matrices and matrix median." },
    ]
  },
  {
    id: 6,
    title: "Strings",
    description: "String matching, palindromes, roman numerals, and substring problems.",
    isComingSoon: true,
    topics: [
      { id: "6.1", title: "6.1: Basic Strings", description: "Reversals, rotations, and anagram checks." },
      { id: "6.2", title: "6.2: Medium Strings", description: "Roman numerals, string to integer (atoi), and nesting depth." },
    ]
  },
  {
    id: 7,
    title: "Recursion",
    description: "Recursion tree mechanics, subsets, combinations, permutations, and backtracking.",
    isComingSoon: true,
    topics: [
      { id: "7.1", title: "7.1: Recursion Basics", description: "Print sequences, power function, and stack unwinding." },
      { id: "7.2", title: "7.2: Subsequences Pattern", description: "Subsets, combination sum, and subsets with duplicates." },
    ]
  },
  {
    id: 8,
    title: "Linked List",
    description: "Singly and doubly linked lists, fast/slow pointer cycle detection, reversals, and merges.",
    isComingSoon: true,
    topics: [
      { id: "8.1", title: "8.1: Singly Linked List", description: "Insert, delete, length, and search in linked lists." },
      { id: "8.2", title: "8.2: Doubly Linked List", description: "Bidirectional pointers, delete nodes, and reverse DLL." },
    ]
  },
  {
    id: 9,
    title: "Bit Manipulation",
    description: "Bitwise operators, masks, power of two, bit flipping, and single numbers.",
    isComingSoon: true,
    topics: [
      { id: "9.1", title: "9.1: Bit Tricks", description: "Check i-th bit set, set/clear bit, and count set bits." },
      { id: "9.2", title: "9.2: Advanced Bits", description: "Two odd numbers, power set using bits, and division." },
    ]
  },
  {
    id: 10,
    title: "Greedy",
    description: "Locally optimal choice strategies, activity selection, fractional knapsack, and jump game.",
    isComingSoon: true,
    topics: [
      { id: "10.1", title: "10.1: Easy Greedy", description: "Assign cookies, lemonaded change, and fractional knapsack." },
      { id: "10.2", title: "10.2: Medium/Hard Greedy", description: "N meetings in one room, minimum platforms, and job sequencing." },
    ]
  },
  {
    id: 11,
    title: "Sliding Window / Two Pointer",
    description: "Constant and variable size windows, maximum fruits, longest substring without repeats.",
    isComingSoon: true,
    topics: [
      { id: "11.1", title: "11.1: Constant Window", description: "Maximum sum subarray of size k." },
      { id: "11.2", title: "11.2: Dynamic Window", description: "Longest substring without repeating characters, fruit into baskets." },
    ]
  },
  {
    id: 12,
    title: "Stack / Queue",
    description: "LIFO and FIFO data structures, next greater element, balanced parentheses, and min-stack.",
    isComingSoon: true,
    topics: [
      { id: "12.1", title: "12.1: Implementation", description: "Stack using array/queue, balanced brackets, min-stack." },
      { id: "12.2", title: "12.2: Monotonic Stack", description: "Next greater element, next smaller element, largest rectangle." },
    ]
  },
  {
    id: 13,
    title: "Binary Trees",
    description: "Hierarchical trees, in-order/pre-order/post-order traversals, height, diameter, and views.",
    isComingSoon: true,
    topics: [
      { id: "13.1", title: "13.1: Traversals", description: "DFS (pre/in/post) and BFS level order traversal." },
      { id: "13.2", title: "13.2: Medium Problems", description: "Maximum depth, check balanced, diameter, identical trees." },
    ]
  },
  {
    id: 14,
    title: "Binary Search Tree",
    description: "Binary search tree invariants, search, insert, delete, LCA, and BST iterator.",
    isComingSoon: true,
    topics: [
      { id: "14.1", title: "14.1: Concept", description: "Search in BST, floor/ceil, insert, and delete node." },
      { id: "14.2", title: "14.2: Practice Problems", description: "Kth smallest element, check if tree is BST, LCA in BST." },
    ]
  },
  {
    id: 15,
    title: "Heaps",
    description: "Binary heaps, priority queues, min/max heaps, K-th largest, and median in a data stream.",
    isComingSoon: true,
    topics: [
      { id: "15.1", title: "15.1: Priority Queue", description: "Heapify, push, pop, check if array is binary heap." },
      { id: "15.2", title: "15.2: K-Way Merging", description: "Merge K sorted lists, find median from data stream." },
    ]
  },
  {
    id: 16,
    title: "Graphs",
    description: "Vertices and edges, adjacency representations, BFS, DFS, cycle detection, topological sort, and Dijkstra.",
    isComingSoon: true,
    topics: [
      { id: "16.1", title: "16.1: BFS/DFS", description: "Graph traversals, number of islands, connected components." },
      { id: "16.2", title: "16.2: Shortest Path", description: "Dijkstra's algorithm, Bellman-Ford, and Floyd-Warshall." },
    ]
  },
  {
    id: 17,
    title: "Dynamic Programming",
    description: "Overlapping subproblems, optimal substructure, memoization, tabulation, and state space optimization.",
    isComingSoon: true,
    topics: [
      { id: "17.1", title: "17.1: 1D DP", description: "Climbing stairs, frog jump, house robber." },
      { id: "17.2", title: "17.2: 2D/3D DP", description: "Grid unique paths, minimum path sum, triangle." },
      { id: "17.3", title: "17.3: DP on Strings", description: "Longest common subsequence, edit distance." },
    ]
  },
  {
    id: 18,
    title: "Tries",
    description: "Prefix tree data structure, word search, prefix autocomplete, and maximum XOR with Trie.",
    isComingSoon: true,
    topics: [
      { id: "18.1", title: "18.1: Trie Operations", description: "Insert word, search word, startsWith prefix." },
      { id: "18.2", title: "18.2: Bitwise Trie", description: "Maximum XOR of two numbers in an array." },
    ]
  },
  {
    id: 19,
    title: "Advanced Strings",
    description: "Pattern matching algorithms: Knuth-Morris-Pratt (KMP), Rabin-Karp, and Z-Algorithm.",
    isComingSoon: true,
    topics: [
      { id: "19.1", title: "19.1: KMP Algorithm", description: "LPS array construction and linear string matching." },
      { id: "19.2", title: "19.2: Z-Algorithm", description: "Z-array prefix matching and string factorization." },
    ]
  },
  {
    id: 20,
    title: "Maths",
    description: "Advanced number theory, modular arithmetic, prime factorization, and combinatorics.",
    isComingSoon: true,
    topics: [
      { id: "20.1", title: "20.1: Prime Sieve", description: "Sieve of Eratosthenes, prime factorization in O(log N)." },
      { id: "20.2", title: "20.2: Combinatorics", description: "Modular inverse, nCr calculation, power exponentiation." },
    ]
  }
];
