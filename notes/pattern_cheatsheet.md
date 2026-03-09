# 🗺️ Pattern Cheatsheet

> Scan the problem statement for these signals. Match the signal to the pattern. Start coding.
>
> **How to use:** Read the problem → highlight key phrases → find them below → go to that pattern's page in the PDF.

---

## 🔑 Keyword → Pattern Map

### Arrays & Strings

| If the problem says or asks... | Reach for... |
|-------------------------------|-------------|
| "sorted array", "find pair summing to X" | **Two Pointers** |
| "remove duplicates in-place", "move zeroes" | **Two Pointers** (write-head) |
| "reverse string/array in-place" | **Two Pointers** |
| "valid palindrome", "palindrome check" | **Two Pointers** (inward) |
| "longest substring without repeating" | **Sliding Window** (variable) |
| "maximum sum subarray of size k" | **Sliding Window** (fixed) |
| "at most k distinct", "fruit into baskets" | **Sliding Window** (variable) |
| "minimum window containing all chars" | **Sliding Window** + HashMap |
| "permutation of s1 in s2" | **Sliding Window** (fixed) |
| "subarray sum equals k" | **Prefix Sum** + HashMap |
| "range sum query", "sum between indices" | **Prefix Sum** |
| "pivot index", "equal left and right sum" | **Prefix Sum** |
| "maximum subarray sum" | **Kadane's** |
| "maximum product subarray" | **Kadane's** (track min too) |
| "two sum", "find complement" | **HashMap** |
| "contains duplicate", "any repeat?" | **HashMap** / Set |
| "group anagrams", "valid anagram" | **HashMap** (sorted key) |
| "top k frequent elements" | **HashMap** + Heap |
| "longest consecutive sequence" | **HashMap** / Set |

---

### Binary Search

| If the problem says or asks... | Reach for... |
|-------------------------------|-------------|
| "sorted array", "find target" | **Binary Search** (classic) |
| "find leftmost / rightmost occurrence" | **Binary Search** (bisect variant) |
| "rotated sorted array" | **Binary Search** (rotated) |
| "find minimum in rotated array" | **Binary Search** (rotated) |
| "minimum / maximum feasible value" | **Binary Search on Answer** |
| "can we do it in X days / speed / weight?" | **Binary Search on Answer** |
| "k-th smallest/largest in sorted structure" | **Binary Search** + bisect |

---

### Stacks & Queues

| If the problem says or asks... | Reach for... |
|-------------------------------|-------------|
| "valid parentheses", "balanced brackets" | **Stack** (matching) |
| "evaluate expression", "RPN" | **Stack** |
| "next greater element" | **Monotonic Stack** (decreasing) |
| "next smaller element", "previous smaller" | **Monotonic Stack** (increasing) |
| "daily temperatures", "stock span" | **Monotonic Stack** |
| "largest rectangle in histogram" | **Monotonic Stack** |
| "sliding window maximum" | **Monotonic Deque** |
| "design queue using stacks" | **Two-Stack Queue** |
| "LRU cache" | **Deque** + HashMap |

---

### Linked Lists

| If the problem says or asks... | Reach for... |
|-------------------------------|-------------|
| "detect cycle", "does loop exist?" | **Fast & Slow Pointers** |
| "find cycle entry point" | **Fast & Slow Pointers** |
| "middle of linked list" | **Fast & Slow Pointers** |
| "reverse linked list", "reverse sublist" | **Reversal** (iterative) |
| "palindrome linked list" | **Reversal** + Fast & Slow |
| "merge two sorted lists" | **Merge** |
| "merge k sorted lists" | **Merge** + Heap |
| "remove nth from end" | **Two Pointers** (gap of n) |

---

### Trees

| If the problem says or asks... | Reach for... |
|-------------------------------|-------------|
| "height / depth", "max path sum" | **DFS** (post-order) |
| "path from root to leaf" | **DFS** (pre-order) |
| "validate BST", "kth smallest in BST" | **DFS** (in-order) |
| "level order traversal", "right side view" | **BFS** |
| "width of binary tree" | **BFS** with index encoding |
| "LCA", "lowest common ancestor" | **DFS** (post-order return) |
| "serialize / deserialize tree" | **BFS** or **DFS** |
| "construct from preorder + inorder" | **DFS** + HashMap |

---

### Graphs

| If the problem says or asks... | Reach for... |
|-------------------------------|-------------|
| "number of islands", "connected components" | **DFS** / **BFS** flood fill |
| "shortest path", "minimum steps" | **BFS** (unweighted) |
| "rotting oranges", "multi-source spread" | **Multi-source BFS** |
| "course schedule", "build order" | **Topological Sort** (Kahn's) |
| "detect cycle in directed graph" | **DFS** (3-colour) |
| "union find", "redundant edge" | **Union-Find** |
| "minimum spanning tree" | **Union-Find** / Kruskal's |
| "shortest path with weights" | **Dijkstra** |
| "cheapest path within k stops" | **Bellman-Ford** / modified Dijkstra |

---

### Dynamic Programming

| If the problem says or asks... | Reach for... |
|-------------------------------|-------------|
| "how many ways", "count paths" | **DP** (1D or 2D) |
| "minimum cost / steps / operations" | **DP** |
| "can we achieve X?" (boolean) | **DP** (knapsack style) |
| "longest common subsequence" | **2D DP** |
| "edit distance", "min insertions/deletions" | **2D DP** |
| "0/1 knapsack", "partition equal subset" | **DP** (knapsack) |
| "unbounded knapsack", "coin change" | **DP** (unbounded) |
| "interval DP", "burst balloons" | **DP** (range `[i,j]`) |
| "palindromic subsequence / substring" | **DP** or Expand Around Centre |

---

### Other Patterns

| If the problem says or asks... | Reach for... |
|-------------------------------|-------------|
| "top k", "k closest", "k largest" | **Heap** (heapq) |
| "k-way merge", "merge k sorted" | **Min-Heap** |
| "median of stream" | **Two Heaps** (max + min) |
| "word search", "prefix autocomplete" | **Trie** |
| "generate all subsets" | **Backtracking** |
| "all permutations", "all combinations" | **Backtracking** |
| "N-Queens", "Sudoku solver" | **Backtracking** + constraints |
| "merge intervals", "insert interval" | **Sort by start** + Greedy |
| "minimum meeting rooms" | **Sort** + Heap (min end time) |
| "XOR", "find the missing number" | **Bit Manipulation** |
| "single number", "power of 2" | **Bit Manipulation** |
| "bitmask DP", "n ≤ 20 subsets" | **Bitmask DP** |
| "GCD", "prime factorisation" | **Math** (Euclidean) |
| "modular exponentiation" | **Math** (fast power) |

---

## ⚡ Complexity Signal Table

> Use this to validate your approach before coding. If n doesn't fit the complexity, rethink.

| Input Size (n) | Max Complexity | Typical Patterns |
|----------------|---------------|-----------------|
| n ≤ 20 | O(2ⁿ) or O(n!) | Backtracking, Bitmask DP, Brute Force |
| n ≤ 100 | O(n³) | Interval DP, Floyd-Warshall |
| n ≤ 1,000 | O(n²) | 2D DP, O(n²) Two Pointers |
| n ≤ 100,000 | O(n log n) | Merge Sort, Binary Search, Heap |
| n ≤ 1,000,000 | O(n) | Two Pointers, Sliding Window, Prefix Sum, BFS/DFS |
| n > 10,000,000 | O(log n) or O(1) | Binary Search, Math, Bit Tricks |

---

## 🧭 Decision Flowchart

```
Read the problem
      │
      ├─ Is the input sorted (or can you sort)?
      │         ├─ Yes + find pair/target → Two Pointers
      │         └─ Yes + find value → Binary Search
      │
      ├─ Is it a subarray / substring problem?
      │         ├─ Max/min/best + contiguous → Sliding Window or Kadane's
      │         └─ Sum equals k → Prefix Sum + HashMap
      │
      ├─ Is it a graph / grid / tree?
      │         ├─ Shortest path, unweighted → BFS
      │         ├─ All paths / components / flood → DFS
      │         ├─ With edge weights → Dijkstra
      │         └─ Dependencies / ordering → Topo Sort
      │
      ├─ Does it ask "how many ways" or "minimum cost"?
      │         └─ Dynamic Programming
      │
      ├─ Does it involve brackets, next-greater, histograms?
      │         └─ Stack (Matching or Monotonic)
      │
      ├─ Does it need top-k or streaming median?
      │         └─ Heap
      │
      └─ Does it need exhaustive enumeration (subsets, perms)?
                └─ Backtracking
```

---

## 📌 Tricky Overlaps — Which One?

| Situation | Use This, Not That |
|-----------|-------------------|
| Subarray sum = k | Prefix Sum (not Sliding Window — values can be negative) |
| Max sum subarray | Kadane's (not Prefix Sum — Kadane's is O(1) space) |
| Longest substring without repeat | Sliding Window (not Two Pointers — unsorted) |
| Find pair summing to k, unsorted | HashMap (not Two Pointers — needs sort first) |
| Find pair summing to k, sorted | Two Pointers (not HashMap — O(1) space) |
| Shortest path in grid | BFS (not DFS — BFS guarantees shortest) |
| All paths in grid | DFS / Backtracking (not BFS) |
| Cycle in undirected graph | Union-Find (not DFS — simpler for this case) |
| Cycle in directed graph | DFS 3-colour (Union-Find doesn't work for directed) |