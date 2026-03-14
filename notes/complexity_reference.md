# ⚡ Complexity Reference

> Keep this open during practice. Before submitting any solution, verify your time and space complexity match the constraints.

---

## By Input Size — What Do You Need?

| Input Size (n) | Max Complexity | Common Patterns |
|----------------|---------------|----------------|
| n ≤ 15 | O(2ⁿ) or O(n!) | Backtracking, Bitmask DP, Brute Force |
| n ≤ 100 | O(n³) | Interval DP, Floyd-Warshall, 3-loop DP |
| n ≤ 1,000 | O(n²) | 2D DP, Naive Two Pointers, Bubble/Insert Sort |
| n ≤ 10,000 | O(n² log n) | Rare — some geometry / special DP |
| n ≤ 100,000 | O(n log n) | Merge Sort, Heap, Binary Search, Segment Tree |
| n ≤ 1,000,000 | O(n) | Two Pointers, Sliding Window, Prefix Sum, BFS/DFS |
| n > 10,000,000 | O(log n) or O(1) | Binary Search, Math, Bit Tricks |

> **Rule of thumb:** LeetCode problems generally allow ~10⁸ operations per second. So n=10⁵ with O(n²) = 10¹⁰ operations — will TLE.

---

## Data Structures

| Structure | Access | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Dynamic Array (list) | O(1) | O(n) | O(1) amort. | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) | O(n) |
| Stack (list) | O(1) top | — | O(1) | O(1) | O(n) |
| Queue (deque) | O(1) front | — | O(1) | O(1) | O(n) |
| HashMap (dict) | O(1) avg | O(1) avg | O(1) avg | O(1) avg | O(n) |
| HashSet (set) | — | O(1) avg | O(1) avg | O(1) avg | O(n) |
| Min/Max Heap | O(1) top | O(n) | O(log n) | O(log n) | O(n) |
| Binary Search Tree | O(log n) avg | O(log n) avg | O(log n) avg | O(log n) avg | O(n) |
| Trie | — | O(L) | O(L) | O(L) | O(n·L) |
| Segment Tree | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |

> L = length of the key/word. HashMap worst case is O(n) due to hash collisions (rare in practice).

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| Timsort (Python default) | O(n) | O(n log n) | O(n log n) | O(n) | ✅ Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ Yes |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n+k) | ✅ Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes |

> In Python, always use `arr.sort()` or `sorted(arr)` — both use Timsort.

---

## Algorithms by Pattern

### Arrays & Strings

| Algorithm / Pattern | Time | Space | Notes |
|--------------------|------|-------|-------|
| Two Pointers | O(n) | O(1) | Requires sorted or ordered structure |
| Sliding Window (fixed) | O(n) | O(1) | Window size k fixed |
| Sliding Window (variable) | O(n) | O(k) | k = distinct elements in window |
| Prefix Sum build | O(n) | O(n) | One-time cost |
| Prefix Sum query | O(1) | O(1) | After build |
| Kadane's (sum) | O(n) | O(1) | |
| Kadane's (product) | O(n) | O(1) | Track both max and min |
| HashMap lookup | O(1) avg | O(n) | |
| Sorting before Two Pointers | O(n log n) | O(1) | Dominates overall cost |

---

### Searching

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| Linear Search | O(n) | O(1) | |
| Binary Search | O(log n) | O(1) | Requires sorted input |
| Binary Search (recursive) | O(log n) | O(log n) | Call stack depth |
| Binary Search on Answer | O(log(hi-lo) · check) | O(1) | check = cost of feasibility function |

---

### Graph & Tree

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| BFS | O(V + E) | O(V) | V = vertices, E = edges |
| DFS (iterative) | O(V + E) | O(V) | Stack space |
| DFS (recursive) | O(V + E) | O(V) | Call stack depth |
| Topological Sort (Kahn's) | O(V + E) | O(V) | |
| Topological Sort (DFS) | O(V + E) | O(V) | |
| Dijkstra (min-heap) | O((V+E) log V) | O(V) | Positive weights only |
| Bellman-Ford | O(V · E) | O(V) | Handles negative weights |
| Floyd-Warshall | O(V³) | O(V²) | All-pairs shortest path |
| Union-Find (with PC+RU) | O(α(n)) ≈ O(1) | O(n) | PC = path compression, RU = rank union |
| Kruskal's MST | O(E log E) | O(V) | Sort edges + Union-Find |
| Prim's MST | O((V+E) log V) | O(V) | Min-heap |

---

### Dynamic Programming

| Problem Type | Time | Space | Optimised Space |
|-------------|------|-------|----------------|
| 1D DP (Fibonacci-style) | O(n) | O(n) | O(1) with two variables |
| 2D DP (grid) | O(n·m) | O(n·m) | O(min(n,m)) rolling row |
| 0/1 Knapsack | O(n·W) | O(n·W) | O(W) single array |
| Unbounded Knapsack | O(n·W) | O(n·W) | O(W) single array |
| Longest Common Subsequence | O(n·m) | O(n·m) | O(min(n,m)) |
| Edit Distance | O(n·m) | O(n·m) | O(min(n,m)) |
| Interval DP | O(n³) | O(n²) | — |
| Bitmask DP | O(2ⁿ · n) | O(2ⁿ) | — |

---

### Heaps

| Operation | Time | Notes |
|-----------|------|-------|
| heapq.heappush | O(log n) | |
| heapq.heappop | O(log n) | |
| heapq.heapify | O(n) | Build from list in-place |
| heapq.nlargest(k, arr) | O(n log k) | |
| heapq.nsmallest(k, arr) | O(n log k) | |
| Peek min | O(1) | `heap[0]` |
| Max-heap push | O(log n) | Negate values: `-val` |

---

### String-Specific

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| String concatenation in loop | O(n²) | O(n) | Use `"".join(list)` instead |
| `"".join(list)` | O(n) | O(n) | Always prefer this |
| `s[::-1]` reverse | O(n) | O(n) | |
| `s.split()` | O(n) | O(n) | |
| `Counter(s)` | O(n) | O(k) | k = unique chars |
| Substring check `t in s` | O(n·m) | O(1) | Use KMP for O(n+m) |
| `s.startswith / endswith` | O(k) | O(1) | k = prefix/suffix length |

---

## Python-Specific Costs

| Operation | Time | Notes |
|-----------|------|-------|
| `list.append(x)` | O(1) amort. | |
| `list.pop()` | O(1) | Remove last |
| `list.pop(0)` | O(n) | ❌ Never use — shifts all elements |
| `list.insert(0, x)` | O(n) | ❌ Never use — use deque |
| `deque.appendleft(x)` | O(1) | ✅ Use this instead |
| `deque.popleft()` | O(1) | ✅ Use this instead |
| `x in list` | O(n) | Use set for O(1) |
| `x in set` | O(1) avg | |
| `x in dict` | O(1) avg | |
| `sorted(arr)` | O(n log n) | Returns new list |
| `arr.sort()` | O(n log n) | In-place |
| `dict[key]` (missing) | KeyError | Use `.get(key, default)` |
| `defaultdict(int)[key]` | O(1) | Returns 0 if missing |

---

## Big-O Simplification Rules

| Rule | Example |
|------|---------|
| Drop constants | O(3n) → O(n) |
| Drop lower-order terms | O(n² + n) → O(n²) |
| Sequential steps add | O(n) + O(m) = O(n + m) |
| Nested loops multiply | O(n) inside O(n) = O(n²) |
| Recursion time | O(branches^depth) |
| Recursion space | O(depth) for call stack |
| log base doesn't matter | O(log₂n) = O(log n) |

---

## Space Complexity Notes

| Pattern | Space Used | What It Holds |
|---------|-----------|--------------|
| Two Pointers | O(1) | Just two index variables |
| Sliding Window (variable) | O(k) | Frequency map of window |
| Prefix Sum | O(n) | Prefix array |
| Recursion / DFS | O(depth) | Call stack frames |
| BFS | O(width) | Queue — worst case O(V) |
| Memoisation | O(states) | dp cache |
| Union-Find | O(n) | Parent + rank arrays |
| Trie | O(n·L) | Each character stored |

> **Inplace vs extra space:** Many interviewers ask for O(1) extra space. Two Pointers and write-head patterns achieve this. Prefix Sum and HashMap trade O(n) space for O(1) query time.