# 🌐 Graphs

> BFS for shortest path. DFS for components and cycles. Topo sort for dependencies. Dijkstra for weights.

---

## Patterns Overview

| Pattern | When to Use | Key Idea |
|---------|------------|---------|
| [BFS](#-bfs--shortest-path--multi-source) | Shortest path, unweighted | Queue + visited set |
| [DFS](#-dfs--components--flood-fill) | Components, cycles, flood fill | Recursion or stack + visited |
| [Topological Sort](#-topological-sort) | Dependencies, build order | Kahn's BFS or DFS with post-order |
| [Union-Find](#-union-find) | Dynamic connectivity, grouping | find() + union() with path compression |
| [Dijkstra's](#-dijkstras-algorithm) | Shortest path with weights | Min-heap + dist array |

---

## Graph Representation

```python
# Adjacency list — most common
from collections import defaultdict
graph = defaultdict(list)
graph[u].append(v)
graph[v].append(u)   # undirected

# Build from edge list
def build_graph(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

# Grid graph — 4-directional
DIRS = [(0,1),(0,-1),(1,0),(-1,0)]
def neighbors(r, c, rows, cols):
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc
```

---

## 🌊 BFS — Shortest Path & Multi-source

**When to use:** Shortest path in an unweighted graph. Multi-source BFS: enqueue ALL starting nodes at time 0 and expand simultaneously.

**Trigger keywords:** "shortest path", "minimum steps", "BFS grid", "multi-source", "rotting/spreading"

```python
from collections import deque

# Single-source BFS
def bfs(graph, start):
    dist = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist

# Multi-source BFS — e.g. Rotting Oranges
def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))   # (row, col, time)
            elif grid[r][c] == 1:
                fresh += 1

    max_time = 0
    while queue:
        r, c, t = queue.popleft()
        for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                max_time = max(max_time, t + 1)
                queue.append((nr, nc, t + 1))

    return max_time if fresh == 0 else -1
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Number of Islands | #200 | 🟡 Medium | BFS/DFS on grid — mark cells visited in-place |
| Rotting Oranges | #994 | 🟡 Medium | Multi-source BFS from every rotten cell at t=0 |
| Shortest Path in Binary Matrix | #1091 | 🟡 Medium | BFS with 8-directional movement |
| 01 Matrix — Distance to Nearest 0 | #542 | 🟡 Medium | Multi-source BFS from all 0s at once |
| Word Ladder | #127 | 🔴 Hard | BFS on implicit word graph via 1-char edits |

---

## 🔍 DFS — Components & Flood Fill

**When to use:** Connected components, cycle detection, exhaustive path search, marking regions.

**Trigger keywords:** "number of islands", "connected components", "flood fill", "provinces", "detect cycle"

```python
# DFS — iterative
def dfs(graph, start):
    visited = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

# DFS — recursive
def dfs_recursive(node, visited, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(neighbor, visited, graph)

# Cycle detection in directed graph
def has_cycle(graph, n):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:   # back edge = cycle
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    return any(dfs(i) for i in range(n) if color[i] == WHITE)
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Clone Graph | #133 | 🟡 Medium | DFS + HashMap: old node → cloned node |
| Pacific Atlantic Water Flow | #417 | 🟡 Medium | Reverse DFS outward from each ocean coast |
| Surrounded Regions | #130 | 🟡 Medium | DFS from border O's first — mark safe |
| Max Area of Island | #695 | 🟡 Medium | DFS — accumulate connected cell count |
| Number of Provinces | #547 | 🟡 Medium | DFS on adjacency matrix |

---

## 📋 Topological Sort

**When to use:** Dependency ordering, build order, prerequisites. **Only valid on DAGs** (directed acyclic graphs).

**Trigger keywords:** "course schedule", "build order", "prerequisites", "dependency", "finish all tasks"

```python
from collections import deque

# Kahn's Algorithm — BFS-based
def topo_sort_kahn(n, prerequisites):
    in_degree = [0] * n
    graph = defaultdict(list)

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    # Start with all nodes that have no dependencies
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else []   # empty = cycle

# DFS-based topo sort
def topo_sort_dfs(n, graph):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        order.append(node)   # add AFTER visiting all descendants

    for i in range(n):
        if i not in visited:
            dfs(i)

    return order[::-1]   # reverse post-order
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Course Schedule | #207 | 🟡 Medium | Cycle detection — can all courses be completed? |
| Course Schedule II | #210 | 🟡 Medium | Return the valid topological order |
| Alien Dictionary | #269 | 🔴 Hard | Build char graph from word order, topo sort |
| Minimum Height Trees | #310 | 🟡 Medium | Topological leaf pruning toward centre |

---

## 🤝 Union-Find

**When to use:** Dynamic connectivity — group nodes, detect cycles in undirected graphs, merge components on the fly.

**Trigger keywords:** "connected components", "redundant connection", "group accounts", "union", "disjoint sets"

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n   # number of components

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False   # already connected
        # Union by rank
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Number of Connected Components | #323 | 🟡 Medium | Union edges, count distinct root nodes |
| Redundant Connection | #684 | 🟡 Medium | Find the single edge creating a cycle |
| Graph Valid Tree | #261 | 🟡 Medium | n−1 edges + no cycle = valid tree |
| Accounts Merge | #721 | 🟡 Medium | Union emails sharing the same account |

---

## ⚖️ Dijkstra's Algorithm

**When to use:** Shortest path with **positive** edge weights. Never re-settle a node once popped from heap.

**Trigger keywords:** "network delay", "cheapest path", "minimum cost to reach", "weighted graph"

```python
import heapq
from collections import defaultdict

def dijkstra(n, edges, source):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))   # undirected

    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]   # (cost, node)

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue   # outdated entry — skip
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    return dist
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Network Delay Time | #743 | 🟡 Medium | Classic single-source shortest path |
| Cheapest Flights Within K Stops | #787 | 🟡 Medium | Dijkstra with hop count constraint |
| Path with Minimum Effort | #1631 | 🟡 Medium | Dijkstra on grid — minimise max edge weight |
| Min Cost to Connect All Points | #1584 | 🟡 Medium | Prim's MST on a coordinate graph |

---

## 🔀 Combined Practice

> These problems require mixing 2+ patterns. Spend 15+ minutes before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Word Ladder II — All Shortest Paths | #126 | 🔴 Hard | BFS level graph + DFS backtracking |
| Reconstruct Itinerary | #332 | 🔴 Hard | DFS + Hierholzer's algorithm (Euler path) |
| Shortest Bridge | #934 | 🟡 Medium | DFS flood fill island + BFS expand to second |
| Making a Large Island | #827 | 🔴 Hard | DFS component labeling + Union-Find merge |
| Number of Ways to Arrive at Destination | #1976 | 🟡 Medium | Dijkstra + path count DP |
| Course Schedule III | #630 | 🔴 Hard | Greedy scheduling + Max-Heap |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Graphs Playlist | youtube.com/@NeetCode | All graph patterns with code and visuals |
| VisuAlgo Graph Traversal | visualgo.net/en/dfsbfs | Animated BFS and DFS step-by-step |
| VisuAlgo Dijkstra / SSSP | visualgo.net/en/sssp | Shortest path animation |
| CP-Algorithms Graphs | cp-algorithms.com/graph | Deep theory: Dijkstra, Bellman-Ford, Floyd |

---

## 🐍 Python Tips

```python
from collections import defaultdict, deque
import heapq

# Build adjacency list
graph = defaultdict(list)

# BFS skeleton
q = deque([start])
visited = {start}
while q:
    node = q.popleft()
    for nb in graph[node]:
        if nb not in visited:
            visited.add(nb)
            q.append(nb)

# Dijkstra skeleton
heap = [(0, start)]
dist = {start: 0}
while heap:
    cost, node = heapq.heappop(heap)
    if cost > dist.get(node, float('inf')): continue
    for nb, w in graph[node]:
        nc = cost + w
        if nc < dist.get(nb, float('inf')):
            dist[nb] = nc
            heapq.heappush(heap, (nc, nb))
```