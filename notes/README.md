# 📝 Notes

> Reference material, cheatsheets, and study documents. Nothing to run — everything to read.

---

## Files

| File | Description |
|------|-------------|
| [`DSA_Interview_Prep.pdf`](#dsa-interview-prep) | Full study guide — 14 topics, patterns, problems, resources, cheatsheets |
| [`pattern_cheatsheet.md`](#pattern-cheatsheet) | One-page keyword → pattern lookup |
| [`complexity_reference.md`](#complexity-reference) | Time & space for every major algorithm |
| [`python_builtins.md`](#python-builtins) | Counter, deque, heapq, bisect, lru_cache + templates |

---

## DSA Interview Prep

The main study PDF. Contains:
- 14 topics with patterns, focused problems, and combined practice
- Per-pattern: When to Use · How to Solve · Code Template · Practice Problems · Common Mistakes
- Per-topic learning resources (NeetCode, LeetCode Explore)
- Appendix A — Pattern Recognition Cheatsheet (keyword → pattern)
- Appendix B — Python Built-ins & Templates (Counter, deque, heapq, bisect, BFS, DSU, Trie, Backtracking)
- Appendix C — Time & Space Complexity Reference

Drop `DSA_Interview_Prep.pdf` here after downloading.

---

## Pattern Cheatsheet

> When you read a problem — scan for these signals and jump straight to the right pattern.

| Problem says / asks... | Likely Pattern |
|------------------------|---------------|
| Sorted array, find a target | Binary Search |
| Answer is a value in range [lo, hi] | Binary Search on Answer |
| Find pair / triplet summing to X | Two Pointers (sorted) or HashMap |
| Max/min sum of contiguous subarray | Sliding Window or Kadane's |
| Subarray sum equals K | Prefix Sum + HashMap |
| Count subarrays with a property | Prefix Sum or Sliding Window |
| Shortest path in unweighted graph/grid | BFS |
| All paths exist? / exhaustive search | DFS / Backtracking |
| Prerequisites / build order / dependencies | Topological Sort |
| Dynamic connectivity / grouping nodes | Union-Find |
| Shortest path with positive weights | Dijkstra's Algorithm |
| How many ways... / minimum cost... | Dynamic Programming |
| Overlapping intervals — merge or count | Sort by start + Greedy / Heap |
| Top K elements | Heap (heapq) |
| Next greater / smaller element | Monotonic Stack |
| Balanced parentheses / nested structure | Stack |
| Level-by-level in a tree | BFS with queue |
| Path in tree / subtree check / height | DFS (recursion) |
| Cycle detection in list or graph | Fast & Slow Pointers or DFS + visited set |
| Palindrome check or count | Two Pointers or Expand Around Centre |
| Anagram / character frequency match | HashMap / Counter |
| Store words for prefix lookup | Trie |
| Find single/missing element | XOR / Bit Manipulation |
| n ≤ 20, try all subsets | Bitmask DP or Backtracking |

---

## Complexity Reference

### By Input Size — What complexity do you need?

| Input Size (n) | Target Complexity | Typical Approach |
|----------------|-------------------|--------------------|
| n ≤ 20 | O(2^n) or O(n!) | Backtracking, Brute Force, Bitmask DP |
| n ≤ 100 | O(n^3) | Interval DP, Floyd-Warshall, 3-loop DP |
| n ≤ 1,000 | O(n^2) | 2D DP, O(n^2) two-pointer, naive sorting |
| n ≤ 100,000 | O(n log n) | Merge Sort, Binary Search, Heap, BST |
| n ≤ 1,000,000 | O(n) | Two Pointers, Sliding Window, Prefix Sum, BFS/DFS |
| n > 10,000,000 | O(log n) or O(1) | Binary Search, Math, Bit Manipulation |

### By Algorithm — What are the costs?

| Operation / Algorithm | Time Complexity | Space Complexity |
|-----------------------|-----------------|--------------------|
| Array access / assignment | O(1) | O(1) |
| Array linear search | O(n) | O(1) |
| Binary Search | O(log n) | O(1) |
| HashMap get / set | O(1) average | O(n) |
| Heap push / pop | O(log n) | O(n) |
| heapq.heapify (build heap) | O(n) | O(n) |
| BFS / DFS on graph | O(V + E) | O(V) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort (average) | O(n log n) | O(log n) stack |
| Two Pointer | O(n) | O(1) |
| Sliding Window | O(n) | O(k) window |
| Prefix Sum — build | O(n) | O(n) |
| Prefix Sum — query | O(1) | O(1) |
| Trie insert / search | O(L) | O(L) |
| Dijkstra (min-heap) | O((V+E) log V) | O(V) |
| Union-Find (amortized) | O(α(n)) ≈ O(1) | O(n) |
| 1D DP | O(n) | O(n) or O(1) |
| 2D DP | O(n × m) | O(n × m) |
| Backtracking | O(b^d) | O(d) call stack |

### Big-O Simplification Rules

| Rule | Example |
|------|---------|
| Drop constants | O(2n) → O(n) |
| Drop smaller terms | O(n² + n) → O(n²) |
| Sequential loops add | Two O(n) loops = O(n), not O(n²) |
| Nested loops multiply | O(n) inside O(n) = O(n²) |
| Recursion time | O(branches ^ depth) |
| Recursion space | O(depth) for call stack |

---

## Python Builtins

### collections.Counter
```python
from collections import Counter

freq = Counter(arr)          # {'a': 3, 'b': 1} — works on list or string
freq.most_common(k)          # top-k elements
freq['missing_key']          # returns 0, no KeyError
Counter(s1) == Counter(s2)   # anagram check in O(n)
```

### collections.defaultdict
```python
from collections import defaultdict

graph = defaultdict(list)    # adjacency list, no KeyError on missing key
count = defaultdict(int)     # frequency map, default 0
graph[node].append(neighbor)
```

### collections.deque
```python
from collections import deque

dq = deque()
dq.append(x)       # add right    O(1)
dq.appendleft(x)   # add left     O(1)
dq.pop()           # remove right O(1)
dq.popleft()       # remove left  O(1)

# Never use list.pop(0) — it is O(n)
```

### heapq (min-heap)
```python
import heapq

h = []
heapq.heappush(h, val)        # push         O(log n)
heapq.heappop(h)              # pop min      O(log n)
heapq.heappush(h, -val)       # max-heap trick — negate values
heapq.nlargest(k, arr)        # top-k largest
heapq.heapify(arr)            # build in-place O(n)
```

### bisect
```python
import bisect

bisect.bisect_left(arr, x)    # first index where arr[i] >= x
bisect.bisect_right(arr, x)   # first index where arr[i] >  x
bisect.insort(arr, x)         # insert maintaining sorted order O(n)
```

### functools.lru_cache
```python
import functools

@functools.lru_cache(None)    # memoises all recursive calls
def dp(i, j):
    if base_case: return ...
    return recurrence(dp(i-1, j), dp(i, j-1))

dp.cache_clear()              # reset between test cases if needed
```

### Key Templates

```python
# Binary Search
lo, hi = 0, len(arr) - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if arr[mid] == target:   return mid
    elif arr[mid] < target:  lo = mid + 1
    else:                    hi = mid - 1

# BFS
from collections import deque
q = deque([start]); visited = {start}
while q:
    node = q.popleft()
    for nb in graph[node]:
        if nb not in visited:
            visited.add(nb); q.append(nb)

# Union-Find
parent = list(range(n)); rank = [0] * n
def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: return False
    if rank[ra] < rank[rb]: ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]: rank[ra] += 1
    return True

# Backtracking
def backtrack(state, start):
    if is_complete(state):
        result.append(list(state)); return
    for i in range(start, len(choices)):
        if not is_valid(choices[i]): continue
        state.append(choices[i])    # choose
        backtrack(state, i + 1)     # explore
        state.pop()                 # undo
```