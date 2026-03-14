# DSA Practice — Python

> Pattern-by-pattern interview preparation · 14 Topics

---

## Folder Structure

```
dsa-practice/
│
├── README.md
│
├── arrays_strings/
│   ├── README.md              ← patterns, notes, tips
│   ├── two_pointers/
│   ├── sliding_window/
│   ├── prefix_sum/
│   ├── kadanes/
│   └── hashmap/
│
├── binary_search/
│   ├── README.md
│   ├── classic/
│   ├── rotated_array/
│   ├── search_on_answer/
│   └── bisect_patterns/
│
├── sorting/
│   └── README.md
│
├── stacks_queues/
│   ├── README.md
│   ├── matching_validity/
│   ├── monotonic_stack/
│   └── queue_deque/
│
├── linked_lists/
│   ├── README.md
│   ├── fast_slow_pointers/
│   ├── reversal/
│   ├── merge_sort/
│   └── hashmap/
│
├── trees/
│   ├── README.md
│   ├── dfs_recursive/
│   ├── bfs_level_order/
│   ├── bst/
│   └── construction/
│
├── graphs/
│   ├── README.md
│   ├── bfs/
│   ├── dfs/
│   ├── topological_sort/
│   ├── union_find/
│   └── dijkstra/
│
├── dynamic_programming/
│   ├── README.md
│   ├── 1d_dp/
│   ├── 2d_dp/
│   ├── knapsack/
│   └── interval_dp/
│
├── tries/           └── README.md
├── heaps/           └── README.md
├── backtracking/    └── README.md
├── bit_manipulation/└── README.md
├── math/            └── README.md
├── intervals/       └── README.md
│
├── templates/
│   ├── binary_search.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── union_find.py
│   ├── dijkstra.py
│   ├── trie.py
│   └── merge_sort.py
│
└── notes/
    └── DSA_Interview_Prep.pdf
```

---

## Topics

| # | Topic | Patterns | README |
|---|-------|----------|--------|
| 1 | 📦 Arrays & Strings | Two Pointers · Sliding Window · Prefix Sum · Kadane's · HashMap | [arrays_strings/README.md](./arrays_strings/README.md) |
| 2 | 🔍 Binary Search | Classic · Rotated Array · Search on Answer · bisect | [binary_search/README.md](./binary_search/README.md) |
| 3 | 📊 Sorting | Merge · Quick · Heap · Counting · Radix | [sorting/README.md](./sorting/README.md) |
| 4 | 📚 Stacks & Queues | Matching · Monotonic Stack · Queue & Deque | [stacks_queues/README.md](./stacks_queues/README.md) |
| 5 | 🔗 Linked Lists | Fast & Slow · Reversal · Merge & Sort · HashMap | [linked_lists/README.md](./linked_lists/README.md) |
| 6 | 🌳 Trees | DFS · BFS · BST · Construction | [trees/README.md](./trees/README.md) |
| 7 | 🕸️ Graphs | BFS · DFS · Topo Sort · Union-Find · Dijkstra | [graphs/README.md](./graphs/README.md) |
| 8 | 💡 Dynamic Programming | 1D · 2D · Knapsack · Interval DP | [dynamic_programming/README.md](./dynamic_programming/README.md) |
| 9 | 📝 Tries | Insert · Search · Prefix Match · Bitwise Trie | [tries/README.md](./tries/README.md) |
| 10 | ⛏️ Heaps | Top K · K-way Merge · Two Heaps · Greedy+Heap | [heaps/README.md](./heaps/README.md) |
| 11 | 🔄 Backtracking | Subsets · Permutations · Combinations · Constraints | [backtracking/README.md](./backtracking/README.md) |
| 12 | ⚡ Bit Manipulation | XOR Tricks · Bitmask DP · Count Bits · Power of 2 | [bit_manipulation/README.md](./bit_manipulation/README.md) |
| 13 | 📐 Math & Number Theory | GCD & Primes · Modular Arithmetic · Combinatorics | [math/README.md](./math/README.md) |
| 14 | 📅 Intervals | Merge · Insert · Non-overlapping · Meeting Rooms | [intervals/README.md](./intervals/README.md) |

---

## Progress Tracker

Mark `✅` when solved, `🔁` when needs review.

### 📦 Arrays & Strings

#### Two Pointers
| Problem | LC # | Difficulty | Status |
|---------|------|-----------|--------|
| Two Sum II — Input Array Is Sorted | #167 | 🟢 | ⬜ |
| Remove Duplicates from Sorted Array | #26 | 🟢 | ⬜ |
| Move Zeroes | #283 | 🟢 | ⬜ |
| Valid Palindrome | #125 | 🟢 | ⬜ |
| Reverse String | #344 | 🟢 | ⬜ |
| 3Sum | #15 | 🟡 | ⬜ |
| Container With Most Water | #11 | 🟡 | ⬜ |
| Two Sum Less Than K | #1099 | 🟡 | ⬜ |
| Trapping Rain Water | #42 | 🔴 | ⬜ |

#### Sliding Window
| Problem | LC # | Difficulty | Status |
|---------|------|-----------|--------|
| Best Time to Buy and Sell Stock | #121 | 🟢 | ⬜ |
| Maximum Average Subarray I | #643 | 🟢 | ⬜ |
| Longest Substring Without Repeating Characters | #3 | 🟡 | ⬜ |
| Minimum Size Subarray Sum | #209 | 🟡 | ⬜ |
| Longest Repeating Character Replacement | #424 | 🟡 | ⬜ |
| Permutation in String | #567 | 🟡 | ⬜ |
| Fruit Into Baskets | #904 | 🟡 | ⬜ |
| Minimum Window Substring | #76 | 🔴 | ⬜ |
| Sliding Window Maximum | #239 | 🔴 | ⬜ |

#### Prefix Sum
| Problem | LC # | Difficulty | Status |
|---------|------|-----------|--------|
| Running Sum of 1D Array | #1480 | 🟢 | ⬜ |
| Find Pivot Index | #724 | 🟢 | ⬜ |
| Subarray Sum Equals K | #560 | 🟡 | ⬜ |
| Product of Array Except Self | #238 | 🟡 | ⬜ |
| Encode and Decode Strings | #271 | 🟡 | ⬜ |
| Continuous Subarray Sum | #523 | 🟡 | ⬜ |
| Subarray Sums Divisible by K | #974 | 🟡 | ⬜ |

#### Kadane's
| Problem | LC # | Difficulty | Status |
|---------|------|-----------|--------|
| Maximum Subarray | #53 | 🟡 | ⬜ |
| Maximum Product Subarray | #152 | 🟡 | ⬜ |
| Maximum Sum Circular Subarray | #918 | 🟡 | ⬜ |
| Longest Turbulent Subarray | #978 | 🟡 | ⬜ |

#### HashMap / Frequency
| Problem | LC # | Difficulty | Status |
|---------|------|-----------|--------|
| Two Sum | #1 | 🟢 | ⬜ |
| Contains Duplicate | #217 | 🟢 | ⬜ |
| Valid Anagram | #242 | 🟢 | ⬜ |
| Majority Element | #169 | 🟢 | ⬜ |
| First Unique Character in a String | #387 | 🟢 | ⬜ |
| Top K Frequent Elements | #347 | 🟡 | ⬜ |
| Group Anagrams | #49 | 🟡 | ⬜ |
| Longest Consecutive Sequence | #128 | 🟡 | ⬜ |
| Longest Palindromic Substring | #5 | 🟡 | ⬜ |

#### Combined
| Problem | LC # | Difficulty | Status |
|---------|------|-----------|--------|
| 4Sum | #18 | 🟡 | ⬜ |
| Min Ops to Reduce X to Zero | #1658 | 🟡 | ⬜ |
| Longest Substring with At Most K Distinct | #340 | 🟡 | ⬜ |
| Find All Anagrams in a String | #438 | 🟡 | ⬜ |
| Subarray Sums Divisible by K | #974 | 🟡 | ⬜ |
| Minimum Window Substring | #76 | 🔴 | ⬜ |
| Max Sum of 3 Non-Overlapping Subarrays | #689 | 🔴 | ⬜ |

---

### 🔍 Binary Search
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Binary Search | #704 | 🟢 | Classic | ⬜ |
| Search Insert Position | #35 | 🟢 | Classic | ⬜ |
| Find First and Last Position | #34 | 🟡 | Classic | ⬜ |
| Find Minimum in Rotated Array | #153 | 🟡 | Rotated | ⬜ |
| Search in Rotated Sorted Array | #33 | 🟡 | Rotated | ⬜ |
| Koko Eating Bananas | #875 | 🟡 | Search on Answer | ⬜ |
| Capacity to Ship Packages | #1011 | 🟡 | Search on Answer | ⬜ |
| Split Array Largest Sum | #410 | 🔴 | Search on Answer | ⬜ |
| Longest Increasing Subsequence | #300 | 🟡 | bisect | ⬜ |

---

### 📚 Stacks & Queues
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Valid Parentheses | #20 | 🟢 | Matching | ⬜ |
| Min Stack | #155 | 🟡 | Matching | ⬜ |
| Evaluate Reverse Polish Notation | #150 | 🟡 | Matching | ⬜ |
| Basic Calculator II | #227 | 🟡 | Matching | ⬜ |
| Next Greater Element I | #496 | 🟢 | Monotonic Stack | ⬜ |
| Daily Temperatures | #739 | 🟡 | Monotonic Stack | ⬜ |
| Online Stock Span | #901 | 🟡 | Monotonic Stack | ⬜ |
| Remove K Digits | #402 | 🟡 | Monotonic Stack | ⬜ |
| Largest Rectangle in Histogram | #84 | 🔴 | Monotonic Stack | ⬜ |
| Implement Queue Using Stacks | #232 | 🟢 | Queue & Deque | ⬜ |
| Design Circular Queue | #622 | 🟡 | Queue & Deque | ⬜ |
| Sliding Window Maximum | #239 | 🔴 | Queue & Deque | ⬜ |
| LRU Cache | #146 | 🟡 | Queue & Deque | ⬜ |

---

### 🔗 Linked Lists
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Linked List Cycle | #141 | 🟢 | Fast & Slow | ⬜ |
| Middle of the Linked List | #876 | 🟢 | Fast & Slow | ⬜ |
| Linked List Cycle II | #142 | 🟡 | Fast & Slow | ⬜ |
| Reverse Linked List | #206 | 🟢 | Reversal | ⬜ |
| Palindrome Linked List | #234 | 🟢 | Reversal | ⬜ |
| Reverse Linked List II | #92 | 🟡 | Reversal | ⬜ |
| Reorder List | #143 | 🟡 | Reversal | ⬜ |
| Merge Two Sorted Lists | #21 | 🟢 | Merge | ⬜ |
| Sort List | #148 | 🟡 | Merge | ⬜ |
| Merge K Sorted Lists | #23 | 🔴 | Merge | ⬜ |
| Copy List with Random Pointer | #138 | 🟡 | HashMap | ⬜ |
| Remove Nth Node from End | #19 | 🟡 | HashMap | ⬜ |

---

### 🌳 Trees
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Maximum Depth of Binary Tree | #104 | 🟢 | DFS | ⬜ |
| Invert Binary Tree | #226 | 🟢 | DFS | ⬜ |
| Diameter of Binary Tree | #543 | 🟢 | DFS | ⬜ |
| Path Sum | #112 | 🟢 | DFS | ⬜ |
| Binary Tree Max Path Sum | #124 | 🔴 | DFS | ⬜ |
| Binary Tree Level Order Traversal | #102 | 🟡 | BFS | ⬜ |
| Binary Tree Right Side View | #199 | 🟡 | BFS | ⬜ |
| Validate BST | #98 | 🟡 | BST | ⬜ |
| Kth Smallest in BST | #230 | 🟡 | BST | ⬜ |
| LCA of BST | #235 | 🟢 | BST | ⬜ |
| Build Tree from Preorder + Inorder | #105 | 🟡 | Construction | ⬜ |
| Serialize and Deserialize BT | #297 | 🔴 | Construction | ⬜ |

---

### 🕸️ Graphs
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Number of Islands | #200 | 🟡 | BFS/DFS | ⬜ |
| Rotting Oranges | #994 | 🟡 | BFS | ⬜ |
| Word Ladder | #127 | 🔴 | BFS | ⬜ |
| Clone Graph | #133 | 🟡 | DFS | ⬜ |
| Pacific Atlantic Water Flow | #417 | 🟡 | DFS | ⬜ |
| Course Schedule | #207 | 🟡 | Topo Sort | ⬜ |
| Course Schedule II | #210 | 🟡 | Topo Sort | ⬜ |
| Number of Connected Components | #323 | 🟡 | Union-Find | ⬜ |
| Redundant Connection | #684 | 🟡 | Union-Find | ⬜ |
| Network Delay Time | #743 | 🟡 | Dijkstra | ⬜ |
| Cheapest Flights Within K Stops | #787 | 🟡 | Dijkstra | ⬜ |

---

### 💡 Dynamic Programming
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Climbing Stairs | #70 | 🟢 | 1D DP | ⬜ |
| House Robber | #198 | 🟡 | 1D DP | ⬜ |
| House Robber II | #213 | 🟡 | 1D DP | ⬜ |
| Coin Change | #322 | 🟡 | 1D DP | ⬜ |
| Word Break | #139 | 🟡 | 1D DP | ⬜ |
| Unique Paths | #62 | 🟡 | 2D DP | ⬜ |
| Minimum Path Sum | #64 | 🟡 | 2D DP | ⬜ |
| Longest Common Subsequence | #1143 | 🟡 | 2D DP | ⬜ |
| Edit Distance | #72 | 🔴 | 2D DP | ⬜ |
| Partition Equal Subset Sum | #416 | 🟡 | Knapsack | ⬜ |
| Target Sum | #494 | 🟡 | Knapsack | ⬜ |
| Longest Increasing Subsequence | #300 | 🟡 | Interval DP | ⬜ |
| Burst Balloons | #312 | 🔴 | Interval DP | ⬜ |

---

## Solution File Template

```python
"""
Problem: <Problem Name> (#<number>)
Difficulty: Easy / Medium / Hard
Pattern: <pattern name>
Link: https://leetcode.com/problems/<slug>/

Approach:
- <step 1>
- <step 2>

Time:  O(?)
Space: O(?)
"""

def solution(args):
    pass


# ── Alternative / Optimised solution ────────────────────────────
# def solution_v2(args):
#     pass
```

---

## Pattern Recognition Cheatsheet

| Problem says / asks... | Likely Pattern |
|------------------------|---------------|
| Sorted array, find a target | Binary Search |
| Answer is a value in range [lo, hi] | Binary Search on Answer |
| Find pair / triplet summing to X | Two Pointers (sorted) or HashMap |
| Max/min sum of contiguous subarray | Sliding Window or Kadane's |
| Subarray sum equals K | Prefix Sum + HashMap |
| Shortest path in unweighted graph/grid | BFS |
| All paths / exhaustive search | DFS / Backtracking |
| Prerequisites / build order | Topological Sort |
| Dynamic connectivity / grouping | Union-Find |
| Shortest path with positive weights | Dijkstra |
| How many ways / minimum cost | Dynamic Programming |
| Overlapping intervals | Sort by start + Greedy or Heap |
| Top K elements | Heap (heapq) |
| Next greater / smaller element | Monotonic Stack |
| Balanced parentheses / nested structure | Stack |
| Level-by-level in a tree | BFS with queue |
| Path in tree / subtree check | DFS (recursion) |
| Cycle detection | Fast & Slow Pointers or DFS + visited |
| Palindrome check or count | Two Pointers or Expand Around Centre |
| Anagram / character frequency | HashMap / Counter |
| Store words for prefix lookup | Trie |
| Find single/missing using XOR | Bit Manipulation |
| n ≤ 20, try all subsets | Bitmask DP or Backtracking |

---

## Complexity Targets

| Input Size (n) | Target Complexity | Typical Approach |
|----------------|-------------------|-----------------|
| n ≤ 20 | O(2^n) or O(n!) | Backtracking, Bitmask DP |
| n ≤ 100 | O(n^3) | Interval DP, Floyd-Warshall |
| n ≤ 1,000 | O(n^2) | 2D DP, O(n²) two-pointer |
| n ≤ 100,000 | O(n log n) | Merge Sort, Binary Search, Heap |
| n ≤ 1,000,000 | O(n) | Two Pointers, Sliding Window, BFS/DFS |
| n > 10,000,000 | O(log n) or O(1) | Binary Search, Math, Bit Tricks |

---

## Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode | neetcode.io | Best structured roadmap + video per pattern |
| LeetCode | leetcode.com | Primary practice platform |
| VisuAlgo | visualgo.net | Algorithm animations |
| CP-Algorithms | cp-algorithms.com | Deep theory and proofs |
| Striver A2Z DSA | takeuforward.org | Comprehensive notes + problems |