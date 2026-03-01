# 📋 Templates

> Copy-paste ready algorithm skeletons. No comments, no explanation — just the clean code to drop into a solution.
>
> For full explanations, complexity analysis, and walkthroughs, see the topic README (e.g. `graphs/README.md`).

---

## Files

| File | Algorithm | Time | Space | When to Copy |
|------|-----------|------|-------|-------------|
| [`binary_search.py`](#binary_searchpy) | Binary Search | O(log n) | O(1) | Any sorted array search or search-on-answer problem |
| [`bfs.py`](#bfspy) | Breadth-First Search | O(V + E) | O(V) | Shortest path unweighted, level order, multi-source spread |
| [`dfs.py`](#dfspy) | Depth-First Search | O(V + E) | O(V) | Components, cycle detection, exhaustive path search |
| [`union_find.py`](#union_findpy) | Union-Find (DSU) | O(α(n)) | O(n) | Dynamic connectivity, grouping, redundant edge detection |
| [`dijkstra.py`](#dijkstrapy) | Dijkstra's Algorithm | O((V+E) log V) | O(V) | Shortest path with positive edge weights |
| [`merge_sort.py`](#merge_sortpy) | Merge Sort | O(n log n) | O(n) | Sorting linked lists, count inversions |
| [`topo_sort.py`](#topo_sortpy) | Topological Sort | O(V + E) | O(V) | Dependencies, build order, course scheduling |

---

## binary_search.py

```python
# ── Find exact target ────────────────────────────────────────
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:   return mid
        elif arr[mid] < target:  lo = mid + 1
        else:                    hi = mid - 1
    return -1


# ── Leftmost occurrence ──────────────────────────────────────
def bisect_left(arr, target):
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            hi = mid - 1
        elif arr[mid] < target:  lo = mid + 1
        else:                    hi = mid - 1
    return result


# ── Rightmost occurrence ─────────────────────────────────────
def bisect_right(arr, target):
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            lo = mid + 1
        elif arr[mid] < target:  lo = mid + 1
        else:                    hi = mid - 1
    return result


# ── Search on answer (find minimum X where check(X) is True) ─
def binary_search_on_answer(lo, hi):
    def check(mid):
        pass  # return True if mid is feasible

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if check(mid):  hi = mid
        else:           lo = mid + 1
    return lo
```

---

## bfs.py

```python
from collections import deque


# ── Graph BFS ────────────────────────────────────────────────
def bfs(graph, start):
    visited = {start}
    queue   = deque([start])
    dist    = {start: 0}

    while queue:
        node = queue.popleft()
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                dist[nb] = dist[node] + 1
                queue.append(nb)

    return dist


# ── Grid BFS (4-directional) ─────────────────────────────────
def bfs_grid(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    visited = {(start_r, start_c)}
    queue   = deque([(start_r, start_c, 0)])  # (row, col, dist)
    DIRS    = [(0,1),(0,-1),(1,0),(-1,0)]

    while queue:
        r, c, d = queue.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                if grid[nr][nc] != BLOCKED:   # replace BLOCKED with your condition
                    visited.add((nr, nc))
                    queue.append((nr, nc, d + 1))


# ── Multi-source BFS ─────────────────────────────────────────
def bfs_multi_source(grid, sources):
    queue   = deque([(r, c, 0) for r, c in sources])
    visited = set(sources)
    DIRS    = [(0,1),(0,-1),(1,0),(-1,0)]

    while queue:
        r, c, d = queue.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if valid(nr, nc) and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, d + 1))
```

---

## dfs.py

```python
# ── Graph DFS — iterative ────────────────────────────────────
def dfs(graph, start):
    visited = {start}
    stack   = [start]

    while stack:
        node = stack.pop()
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                stack.append(nb)


# ── Graph DFS — recursive ────────────────────────────────────
def dfs_recursive(node, visited, graph):
    visited.add(node)
    for nb in graph[node]:
        if nb not in visited:
            dfs_recursive(nb, visited, graph)


# ── Grid DFS (flood fill) ────────────────────────────────────
def dfs_grid(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:  return
    if (r, c) in visited or grid[r][c] == 0:       return

    visited.add((r, c))
    dfs_grid(grid, r+1, c, visited)
    dfs_grid(grid, r-1, c, visited)
    dfs_grid(grid, r, c+1, visited)
    dfs_grid(grid, r, c-1, visited)


# ── Cycle detection — directed graph ─────────────────────────
def has_cycle(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY
        for nb in graph[node]:
            if color[nb] == GRAY:               return True
            if color[nb] == WHITE and dfs(nb):  return True
        color[node] = BLACK
        return False

    return any(dfs(i) for i in range(n) if color[i] == WHITE)
```

---

## union_find.py

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank   = [0] * n
        self.count  = n          # number of connected components

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False         # already connected — would form a cycle
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)


# ── Functional version (no class) ───────────────────────────
def make_uf(n):
    parent = list(range(n))
    rank   = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb: return False
        if rank[ra] < rank[rb]: ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]: rank[ra] += 1
        return True

    return find, union
```

---

## dijkstra.py

```python
import heapq
from collections import defaultdict


# ── Standard Dijkstra ────────────────────────────────────────
def dijkstra(n, edges, source):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))     # remove this line for directed graph

    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]            # (cost, node)

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue                # outdated entry — skip
        for nb, w in graph[node]:
            nc = cost + w
            if nc < dist[nb]:
                dist[nb] = nc
                heapq.heappush(heap, (nc, nb))

    return dist                     # dist[i] = shortest distance from source to i


# ── Grid Dijkstra (variable movement cost) ──────────────────
def dijkstra_grid(grid):
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]              # (cost, row, col)
    DIRS = [(0,1),(0,-1),(1,0),(-1,0)]

    while heap:
        cost, r, c = heapq.heappop(heap)
        if cost > dist[r][c]: continue
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                nc_cost = cost + grid[nr][nc]   # adjust cost function
                if nc_cost < dist[nr][nc]:
                    dist[nr][nc] = nc_cost
                    heapq.heappush(heap, (nc_cost, nr, nc))

    return dist[rows-1][cols-1]
```

---

## merge_sort.py

```python
# ── Array Merge Sort ─────────────────────────────────────────
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid   = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j  = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ── Linked List Merge Sort ───────────────────────────────────
def sort_list(head):
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid       = slow.next
    slow.next = None               # split
    left  = sort_list(head)
    right = sort_list(mid)
    return merge_lists(left, right)

def merge_lists(l1, l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val: curr.next = l1; l1 = l1.next
        else:                curr.next = l2; l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```

---

## topo_sort.py

```python
from collections import deque, defaultdict


# ── Kahn's Algorithm (BFS) ───────────────────────────────────
def topo_sort_kahn(n, prerequisites):
    graph     = defaultdict(list)
    in_degree = [0] * n

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    queue = deque(i for i in range(n) if in_degree[i] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nb in graph[node]:
            in_degree[nb] -= 1
            if in_degree[nb] == 0:
                queue.append(nb)

    return order if len(order) == n else []   # empty list = cycle detected


# ── DFS Post-order (recursive) ───────────────────────────────
def topo_sort_dfs(n, graph):
    visited = set()
    order   = []

    def dfs(node):
        visited.add(node)
        for nb in graph[node]:
            if nb not in visited:
                dfs(nb)
        order.append(node)         # add AFTER all descendants

    for i in range(n):
        if i not in visited:
            dfs(i)

    return order[::-1]             # reverse post-order = topological order
```