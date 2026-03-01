# DSA — Python

> Pattern-by-pattern preparation for coding interviews, with curated problems and solutions.
---

## Folder Structure

```
dsa/
│
├── README.md
│
├── arrays/
│   ├── README.md              ← patterns, notes, tips
│   ├── sorting/               ← algorithm implementations
│   ├── two_pointers/          ← pattern problems
│   ├── sliding_window/
│   ├── prefix_sum/
│   ├── kadanes/
│   └── hashmap/
│
├── strings/
│   ├── README.md
│   ├── sliding_window/
│   ├── two_pointers/
│   ├── hashmap/
│   └── parsing/
│
├── binary_search/
│   ├── README.md
│   ├── algorithm/             ← pure BS implementation
│   ├── classic/
│   ├── rotated_array/
│   ├── search_on_answer/
│   └── bisect_patterns/
│
├── stacks_queues/
│   ├── README.md
│   ├── matching_validity/
│   ├── monotonic_stack/
│   └── deque_patterns/
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
│   ├── algorithm/             ← traversal implementations
│   ├── dfs_recursive/
│   ├── bfs_level_order/
│   ├── bst/
│   └── construction/
│
├── graphs/
│   ├── README.md
│   ├── algorithm/             ← Dijkstra, BFS, DFS, Topo Sort
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
├── templates/                 ← copy-paste ready skeletons
│   ├── binary_search.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── union_find.py
│   ├── dijkstra.py
│   └── merge_sort.py
│
└── notes/
    └── DSA_Pattern_Bible.pdf
```

> **`topic/algorithm/`** — full implementation with explanation and complexity notes
> **`templates/`** — same algorithm, no comments, ready to copy into a solution
> **`topic/pattern/`** — actual LeetCode problems using that pattern

---

## Topics

| # | Topic | Patterns | README |
|---|-------|----------|--------|
| 1 | 📦 Arrays | Two Pointers · Sliding Window · Prefix Sum · Kadane's · HashMap | [arrays/README.md](./arrays/README.md) |
| 2 | 🔤 Strings | Sliding Window · Two Pointers · HashMap · Parsing | [strings/README.md](./strings/README.md) |
| 3 | 🔍 Binary Search | Classic · Rotated Array · Search on Answer · bisect | [binary_search/README.md](./binary_search/README.md) |
| 4 | 📚 Stacks & Queues | Matching · Monotonic Stack · Deque | [stacks_queues/README.md](./stacks_queues/README.md) |
| 5 | 🔗 Linked Lists | Fast & Slow · Reversal · Merge & Sort · HashMap | [linked_lists/README.md](./linked_lists/README.md) |
| 6 | 🌳 Trees | DFS · BFS · BST · Construction | [trees/README.md](./trees/README.md) |
| 7 | 🌐 Graphs | BFS · DFS · Topo Sort · Union-Find · Dijkstra | [graphs/README.md](./graphs/README.md) |
| 8 | 🧠 Dynamic Programming | 1D · 2D · Knapsack · Interval DP | [dynamic_programming/README.md](./dynamic_programming/README.md) |

---

## Progress Tracker

Mark `✅` when solved, `🔁` when needs review.

### 📦 Arrays
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Two Sum II | #167 | 🟢 | Two Pointers | ⬜ |
| Remove Duplicates from Sorted Array | #26 | 🟢 | Two Pointers | ⬜ |
| 3Sum | #15 | 🟡 | Two Pointers | ⬜ |
| Container With Most Water | #11 | 🟡 | Two Pointers | ⬜ |
| Trapping Rain Water | #42 | 🔴 | Two Pointers | ⬜ |
| Best Time to Buy and Sell Stock | #121 | 🟢 | Sliding Window | ⬜ |
| Minimum Size Subarray Sum | #209 | 🟡 | Sliding Window | ⬜ |
| Longest Repeating Char Replacement | #424 | 🟡 | Sliding Window | ⬜ |
| Sliding Window Maximum | #239 | 🔴 | Sliding Window | ⬜ |
| Subarray Sum Equals K | #560 | 🟡 | Prefix Sum | ⬜ |
| Product of Array Except Self | #238 | 🟡 | Prefix Sum | ⬜ |
| Maximum Subarray | #53 | 🟡 | Kadane's | ⬜ |
| Maximum Product Subarray | #152 | 🟡 | Kadane's | ⬜ |
| Two Sum | #1 | 🟢 | HashMap | ⬜ |
| Group Anagrams | #49 | 🟡 | HashMap | ⬜ |
| Longest Consecutive Sequence | #128 | 🟡 | HashMap | ⬜ |
| Merge Intervals | #56 | 🟡 | Sorting | ⬜ |
| Minimum Window Substring | #76 | 🔴 | Combined | ⬜ |

### 🔤 Strings
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Longest Substring Without Repeating | #3 | 🟡 | Sliding Window | ⬜ |
| Minimum Window Substring | #76 | 🔴 | Sliding Window | ⬜ |
| Find All Anagrams in a String | #438 | 🟡 | Sliding Window | ⬜ |
| Permutation in String | #567 | 🟡 | Sliding Window | ⬜ |
| Valid Palindrome | #125 | 🟢 | Two Pointers | ⬜ |
| Longest Palindromic Substring | #5 | 🟡 | Two Pointers | ⬜ |
| Valid Anagram | #242 | 🟢 | HashMap | ⬜ |
| Group Anagrams | #49 | 🟡 | HashMap | ⬜ |
| Decode String | #394 | 🟡 | Parsing | ⬜ |

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

### 📚 Stacks & Queues
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Valid Parentheses | #20 | 🟢 | Matching | ⬜ |
| Min Stack | #155 | 🟡 | Matching | ⬜ |
| Evaluate Reverse Polish Notation | #150 | 🟡 | Matching | ⬜ |
| Daily Temperatures | #739 | 🟡 | Monotonic Stack | ⬜ |
| Largest Rectangle in Histogram | #84 | 🔴 | Monotonic Stack | ⬜ |
| Sum of Subarray Minimums | #907 | 🟡 | Monotonic Stack | ⬜ |
| Sliding Window Maximum | #239 | 🔴 | Deque | ⬜ |
| LRU Cache | #146 | 🟡 | Deque | ⬜ |

### 🔗 Linked Lists
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Linked List Cycle | #141 | 🟢 | Fast & Slow | ⬜ |
| Linked List Cycle II | #142 | 🟡 | Fast & Slow | ⬜ |
| Middle of the Linked List | #876 | 🟢 | Fast & Slow | ⬜ |
| Reverse Linked List | #206 | 🟢 | Reversal | ⬜ |
| Reverse Linked List II | #92 | 🟡 | Reversal | ⬜ |
| Palindrome Linked List | #234 | 🟢 | Reversal | ⬜ |
| Reorder List | #143 | 🟡 | Reversal | ⬜ |
| Merge Two Sorted Lists | #21 | 🟢 | Merge | ⬜ |
| Merge K Sorted Lists | #23 | 🔴 | Merge | ⬜ |
| Sort List | #148 | 🟡 | Merge | ⬜ |
| Copy List with Random Pointer | #138 | 🟡 | HashMap | ⬜ |
| Remove Nth Node from End | #19 | 🟡 | HashMap | ⬜ |

### 🌳 Trees
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Maximum Depth of Binary Tree | #104 | 🟢 | DFS | ⬜ |
| Invert Binary Tree | #226 | 🟢 | DFS | ⬜ |
| Path Sum | #112 | 🟢 | DFS | ⬜ |
| Path Sum II | #113 | 🟡 | DFS | ⬜ |
| Diameter of Binary Tree | #543 | 🟢 | DFS | ⬜ |
| Binary Tree Max Path Sum | #124 | 🔴 | DFS | ⬜ |
| Binary Tree Level Order Traversal | #102 | 🟡 | BFS | ⬜ |
| Binary Tree Right Side View | #199 | 🟡 | BFS | ⬜ |
| Validate BST | #98 | 🟡 | BST | ⬜ |
| Kth Smallest in BST | #230 | 🟡 | BST | ⬜ |
| LCA of BST | #235 | 🟢 | BST | ⬜ |
| Build Tree from Preorder + Inorder | #105 | 🟡 | Construction | ⬜ |
| Serialize and Deserialize BT | #297 | 🔴 | Construction | ⬜ |

### 🌐 Graphs
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

### 🧠 Dynamic Programming
| Problem | LC # | Difficulty | Pattern | Status |
|---------|------|-----------|---------|--------|
| Climbing Stairs | #70 | 🟢 | 1D DP | ⬜ |
| House Robber | #198 | 🟡 | 1D DP | ⬜ |
| House Robber II | #213 | 🟡 | 1D DP | ⬜ |
| Coin Change | #322 | 🟡 | 1D DP | ⬜ |
| Coin Change II | #518 | 🟡 | 1D DP | ⬜ |
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
| Overlapping intervals | Sort by start + Greedy |
| Top K elements | Heap (heapq) |
| Next greater / smaller element | Monotonic Stack |
| Balanced parentheses / nested structure | Stack |
| Level-by-level in a tree | BFS with queue |
| Path in tree / subtree check | DFS (recursion) |
| Cycle detection | Fast & Slow Pointers or DFS + visited |
| Palindrome | Two Pointers or Expand Around Centre |
| Anagram / frequency match | HashMap / Counter |

---

## Complexity Targets

| Input Size (n) | Target Complexity | Typical Approach |
|----------------|-------------------|-----------------|
| n ≤ 20 | O(2^n) or O(n!) | Backtracking, Bitmask DP |
| n ≤ 100 | O(n^3) | Interval DP, Floyd-Warshall |
| n ≤ 1,000 | O(n^2) | 2D DP, O(n²) two-pointer |
| n ≤ 100,000 | O(n log n) | Merge Sort, Binary Search, Heap |
| n ≤ 1,000,000 | O(n) | Two Pointers, Sliding Window, BFS/DFS |
| n > 10,000,000 | O(log n) or O(1) | Binary Search, Math |

---

## Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode | neetcode.io | Best structured roadmap + video per pattern |
| LeetCode | leetcode.com | Primary practice platform |
| VisuAlgo | visualgo.net | Algorithm animations |
| CP-Algorithms | cp-algorithms.com | Deep theory and proofs |
| Striver A2Z DSA | takeuforward.org | Comprehensive notes + problems |