# 🐍 Python DSA Builtins

> Everything you need to know cold for an interview. No lookups, no imports you can't remember — just these.

---

## collections.Counter

```python
from collections import Counter

freq = Counter("aabbbc")        # Counter({'b': 3, 'a': 2, 'c': 1})
freq = Counter([1, 1, 2, 3])   # works on any iterable

freq['x']                       # 0 — never raises KeyError
freq.most_common(2)             # [('b', 3), ('a', 2)] — top-2
freq.most_common()[:-k-1:-1]    # bottom-k

Counter("abc") == Counter("bca")  # True — anagram check O(n)
Counter("abc") - Counter("ab")    # Counter({'c': 1}) — subtract

# Update
freq.update("bcd")              # add counts
freq.subtract("abc")            # subtract (can go negative)

# Convert to sorted list
sorted(freq.items(), key=lambda x: -x[1])
```

---

## collections.defaultdict

```python
from collections import defaultdict

graph  = defaultdict(list)      # adjacency list
count  = defaultdict(int)       # frequency map — default 0
nested = defaultdict(set)       # set per key

graph['a'].append('b')          # no KeyError on missing key
count['x'] += 1                 # start counting from 0

# Group anagrams
groups = defaultdict(list)
for word in words:
    groups[tuple(sorted(word))].append(word)
```

---

## collections.deque

```python
from collections import deque

dq = deque()
dq = deque([1, 2, 3])          # initialise from list
dq = deque(maxlen=k)            # auto-evicts oldest when full

dq.append(x)                    # add right   O(1)
dq.appendleft(x)                # add left    O(1)
dq.pop()                        # remove right O(1)
dq.popleft()                    # remove left  O(1) ← use instead of list.pop(0)
dq[0]                           # peek front  O(1)
dq[-1]                          # peek back   O(1)
dq.rotate(k)                    # rotate right k steps

# ❌ Never use list.pop(0) — it is O(n)
```

---

## heapq (min-heap)

```python
import heapq

h = []
heapq.heappush(h, val)          # O(log n)
heapq.heappop(h)                # O(log n) — returns smallest
h[0]                            # O(1) peek min — does NOT remove

heapq.heapify(arr)              # O(n) — convert list in-place
heapq.nlargest(k, arr)          # O(n log k) — top-k largest
heapq.nsmallest(k, arr)         # O(n log k) — top-k smallest

# Max-heap trick — negate values
heapq.heappush(h, -val)
max_val = -heapq.heappop(h)

# Heap of tuples — sorted by first element
heapq.heappush(h, (priority, item))

# K-way merge
import heapq
def merge_k_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    result = []
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j+1], i, j+1))
    return result
```

---

## bisect (binary search on sorted list)

```python
import bisect

# bisect_left  → first index where arr[i] >= x  (leftmost valid insertion)
# bisect_right → first index where arr[i] >  x  (rightmost valid insertion)

idx = bisect.bisect_left(arr, x)
idx = bisect.bisect_right(arr, x)

bisect.insort(arr, x)           # insert x maintaining sorted order O(n shift)

# Check if x exists in sorted array
idx = bisect.bisect_left(arr, x)
exists = idx < len(arr) and arr[idx] == x

# Count elements less than x
count_less = bisect.bisect_left(arr, x)

# Count elements in range [lo, hi]
count_range = bisect.bisect_right(arr, hi) - bisect.bisect_left(arr, lo)

# Longest Increasing Subsequence (patience sorting)
def lis_length(nums):
    tails = []
    for n in nums:
        idx = bisect.bisect_left(tails, n)
        if idx == len(tails):
            tails.append(n)
        else:
            tails[idx] = n
    return len(tails)
```

---

## functools.lru_cache (memoisation)

```python
import functools

@functools.lru_cache(maxsize=None)   # None = unlimited cache
def dp(i, j, state):
    if base_case(i, j): return ...
    return min(dp(i-1, j), dp(i, j-1))  # recurrence

dp.cache_clear()    # reset between test cases if reusing function
dp.cache_info()     # hits, misses, currsize

# Alternative: @cache (Python 3.9+)
from functools import cache

@cache
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)
```

---

## Sorting — Key Patterns

```python
# Sort ascending / descending
arr.sort()
arr.sort(reverse=True)

# Sort by custom key
arr.sort(key=lambda x: x[1])           # by second element
arr.sort(key=lambda x: (-x[0], x[1]))  # primary desc, secondary asc
arr.sort(key=lambda x: len(x))         # by length (strings)
arr.sort(key=lambda x: x.lower())      # case-insensitive

# Sort tuples — lexicographic by default
intervals.sort()                        # sort by start time
intervals.sort(key=lambda x: x[1])     # sort by end time

# Stable sort — equal elements keep original order
arr.sort(key=lambda x: x % 2)          # stable: evens before odds

# Sort and get sorted indices
order = sorted(range(len(arr)), key=lambda i: arr[i])
```

---

## itertools (useful extras)

```python
from itertools import combinations, permutations, product, accumulate

# Combinations — choose k from n, order doesn't matter
list(combinations([1,2,3], 2))   # [(1,2),(1,3),(2,3)]

# Permutations — all orderings of length k
list(permutations([1,2,3], 2))   # [(1,2),(1,3),(2,1),...]

# Cartesian product
list(product([0,1], repeat=3))   # all 3-bit binary strings

# Prefix sum via accumulate
from itertools import accumulate
prefix = list(accumulate(arr))           # [a0, a0+a1, ...]
prefix = list(accumulate(arr, initial=0)) # [0, a0, a0+a1, ...]
```

---

## String Methods (DSA-relevant)

```python
s.lower() / s.upper()
s.strip() / s.lstrip() / s.rstrip()
s.split()                        # split on any whitespace
s.split(",")                     # split on delimiter
" ".join(words)                  # join list to string
s[::-1]                          # reverse

s.isalnum()                      # alphanumeric check
s.isdigit() / s.isalpha()
s.startswith("pre") / s.endswith("suf")
s.replace("a", "b")             # replace all occurrences
s.count("ab")                   # count non-overlapping occurrences
s.find("ab")                    # index of first occurrence, -1 if not found
s.index("ab")                   # same but raises ValueError if not found

# Build string from list (O(n) not O(n²))
"".join(char_list)

# Check palindrome
s == s[::-1]

# Iterate characters
for i, ch in enumerate(s): ...
```

---

## Templates

### Binary Search

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2      # avoids overflow
        if arr[mid] == target:   return mid
        elif arr[mid] < target:  lo = mid + 1
        else:                    hi = mid - 1
    return -1

def binary_search_on_answer(lo, hi, check):
    """Find minimum x in [lo, hi] where check(x) is True."""
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if check(mid): hi = mid
        else:          lo = mid + 1
    return lo
```

---

### BFS

```python
from collections import deque

def bfs(graph, start, target=None):
    visited = {start}
    queue   = deque([(start, 0)])   # (node, distance)
    while queue:
        node, dist = queue.popleft()
        if node == target: return dist
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                queue.append((nb, dist + 1))
    return -1

def bfs_grid(grid, sr, sc):
    rows, cols = len(grid), len(grid[0])
    visited = {(sr, sc)}
    queue   = deque([(sr, sc, 0)])
    DIRS    = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        r, c, d = queue.popleft()
        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited:
                if grid[nr][nc] != 0:           # replace with your wall check
                    visited.add((nr,nc))
                    queue.append((nr,nc,d+1))
```

---

### Union-Find (DSU)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank   = [0] * n
        self.count  = n             # number of components

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False   # already connected
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)
```

---

### Trie

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end   = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children: return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children: return False
            node = node.children[ch]
        return True
```

---

### Backtracking

```python
def backtrack(result, state, start, choices):
    if is_complete(state):
        result.append(list(state))  # snapshot — never append state directly
        return
    for i in range(start, len(choices)):
        if not is_valid(choices[i], state):
            continue
        state.append(choices[i])        # choose
        backtrack(result, state, i + 1, choices)  # explore (i+1 for combos, i for perms)
        state.pop()                     # undo

# Subsets
def subsets(nums):
    result = []
    def bt(start, curr):
        result.append(list(curr))
        for i in range(start, len(nums)):
            curr.append(nums[i]); bt(i+1, curr); curr.pop()
    bt(0, [])
    return result

# Permutations
def permutations(nums):
    result = []
    def bt(curr, used):
        if len(curr) == len(nums): result.append(list(curr)); return
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True; curr.append(nums[i])
            bt(curr, used)
            used[i] = False; curr.pop()
    bt([], [False]*len(nums))
    return result
```

---

### Dijkstra

```python
import heapq
from collections import defaultdict

def dijkstra(n, edges, source):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))     # remove for directed graph

    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]            # (cost, node)

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]: continue   # stale entry
        for nb, w in graph[node]:
            nc = cost + w
            if nc < dist[nb]:
                dist[nb] = nc
                heapq.heappush(heap, (nc, nb))

    return dist
```

---

### Monotonic Stack

```python
# Next Greater Element — O(n)
def next_greater(arr):
    result = [-1] * len(arr)
    stack  = []                     # stores indices
    for i, v in enumerate(arr):
        while stack and arr[stack[-1]] < v:
            result[stack.pop()] = v
        stack.append(i)
    return result                   # remaining indices have no next greater

# Next Smaller Element — increasing stack
def next_smaller(arr):
    result = [-1] * len(arr)
    stack  = []
    for i, v in enumerate(arr):
        while stack and arr[stack[-1]] > v:
            result[stack.pop()] = v
        stack.append(i)
    return result
```