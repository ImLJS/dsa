# ⛰️ Heaps (Priority Queues)

> A heap gives you the min (or max) element in O(1) and insert/remove in O(log n). Use it whenever you need repeated access to the smallest or largest element.

---

## Patterns Overview

| Pattern | When to Use |
|---------|------------|
| [Top K Elements](#-top-k-elements) | K largest, K most frequent, K closest |
| [K-way Merge](#-k-way-merge) | Merge K sorted lists/arrays |
| [Two Heaps](#-two-heaps) | Median of a stream, balanced partitioning |
| [Greedy + Heap](#-greedy--heap) | Scheduling, task assignment, minimum cost |

---

## Python Heap Basics

```python
import heapq

# Python only has min-heap
h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 2)
heapq.heappop(h)         # returns 1 (minimum)
h[0]                     # peek min — O(1)

# Max-heap trick — negate values
heapq.heappush(h, -val)
max_val = -heapq.heappop(h)

# Build heap from list — O(n)
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)

# Push tuples — heap compares first element
heapq.heappush(h, (priority, value))
heapq.heappush(h, (dist, node))

# Top K largest
heapq.nlargest(k, arr)       # O(n log k)
heapq.nsmallest(k, arr)      # O(n log k)
```

---

## 🏆 Top K Elements

**When to use:** Find the K largest, K most frequent, or K closest elements.

**Trigger keywords:** "top K", "K largest", "K most frequent", "K closest", "K strongest"

```python
# K largest elements — min-heap of size K
def k_largest(nums, k):
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)    # remove smallest — keeps K largest
    return list(heap)


# Top K frequent elements
from collections import Counter
def top_k_frequent(nums, k):
    freq = Counter(nums)
    # Min-heap of (frequency, value) — keep K most frequent
    return [val for val, _ in Counter(nums).most_common(k)]

# Alternative — bucket sort O(n)
def top_k_frequent_bucket(nums, k):
    freq = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for val, count in freq.items():
        buckets[count].append(val)
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]


# K closest points to origin
def k_closest(points, k):
    # Max-heap of size K — pop when we find a closer point
    heap = []
    for x, y in points:
        dist = -(x*x + y*y)      # negate for max-heap
        heapq.heappush(heap, (dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    return [[x, y] for _, x, y in heap]
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Kth Largest Element in an Array | #215 | 🟡 Medium | Min-heap size K — top = Kth largest |
| Top K Frequent Elements | #347 | 🟡 Medium | Counter + heap or bucket sort |
| K Closest Points to Origin | #973 | 🟡 Medium | Max-heap size K on distance |
| Kth Largest Element in a Stream | #703 | 🟢 Easy | Min-heap of size K, root = answer |
| Sort Characters by Frequency | #451 | 🟡 Medium | Counter + max-heap |
| Reorganize String | #767 | 🟡 Medium | Max-heap, always place most frequent first |

---

## 🔀 K-way Merge

**When to use:** Merging K sorted arrays or lists efficiently.

**Trigger keywords:** "merge K sorted", "smallest range covering K lists"

```python
# Merge K sorted arrays
def merge_k_sorted(arrays):
    heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))   # (val, array_idx, element_idx)

    result = []
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)
        if j + 1 < len(arrays[i]):
            heapq.heappush(heap, (arrays[i][j+1], i, j+1))
    return result


# Merge K sorted linked lists
def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = curr = ListNode(0)
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Merge K Sorted Lists | #23 | 🔴 Hard | Min-heap of (val, list_idx, node) |
| Kth Smallest Element in a Sorted Matrix | #378 | 🟡 Medium | K-way merge on rows |
| Find K Pairs with Smallest Sums | #373 | 🟡 Medium | Heap of (sum, i, j) — push next candidates |
| Smallest Range Covering K Lists | #632 | 🔴 Hard | Sliding window on merged stream |

---

## ⚖️ Two Heaps

**When to use:** Split a stream into two halves — max-heap for lower half, min-heap for upper half. Median is always accessible in O(1).

**Trigger keywords:** "median of stream", "median finder", "balance two groups"

```python
class MedianFinder:
    def __init__(self):
        self.lo = []    # max-heap (negate values) — lower half
        self.hi = []    # min-heap — upper half

    def add_num(self, num):
        # Always push to lo first
        heapq.heappush(self.lo, -num)

        # Balance: lo's max must be <= hi's min
        if self.hi and -self.lo[0] > self.hi[0]:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))

        # Keep sizes balanced — lo can be at most 1 larger
        if len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Find Median from Data Stream | #295 | 🔴 Hard | Max-heap lower half + min-heap upper half |
| Sliding Window Median | #480 | 🔴 Hard | Two heaps + lazy deletion |
| IPO (maximize capital) | #502 | 🔴 Hard | Min-heap on capital, max-heap on profit |

---

## 📅 Greedy + Heap

**When to use:** Scheduling tasks, assigning resources, or making locally optimal choices where the best available option changes dynamically.

**Trigger keywords:** "task scheduler", "meeting rooms", "minimum cost", "process in order"

```python
# Task Scheduler — minimum intervals with cooldown
from collections import Counter
def least_interval(tasks, n):
    freq = Counter(tasks)
    heap = [-f for f in freq.values()]
    heapq.heapify(heap)

    time = 0
    queue = []   # (available_time, freq)

    while heap or queue:
        time += 1
        if heap:
            freq = 1 + heapq.heappop(heap)    # -freq + 1 = one less task
            if freq:
                queue.append((time + n, freq))  # available after cooldown
        if queue and queue[0][0] == time:
            heapq.heappush(heap, queue.pop(0)[1])

    return time


# Meeting Rooms II — minimum rooms needed
def min_meeting_rooms(intervals):
    intervals.sort(key=lambda x: x[0])
    heap = []    # end times of ongoing meetings

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)    # reuse a room that's free
        heapq.heappush(heap, end)

    return len(heap)
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Task Scheduler | #621 | 🟡 Medium | Max-heap + cooldown queue |
| Meeting Rooms II | #253 | 🟡 Medium | Min-heap of end times — size = rooms needed |
| Last Stone Weight | #1046 | 🟢 Easy | Max-heap — smash two largest each round |
| Minimum Cost to Connect Sticks | #1167 | 🟡 Medium | Always merge two smallest first |
| K-th Largest in Stream | #703 | 🟢 Easy | Min-heap of size K |
| Ugly Number II | #264 | 🟡 Medium | Min-heap + multiply by 2, 3, 5 |

---

## Combined Practice

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Find Median from Data Stream | #295 | 🔴 Hard | Two Heaps |
| Sliding Window Median | #480 | 🔴 Hard | Two Heaps + Sliding Window |
| Maximum Profit in Job Scheduling | #1235 | 🔴 Hard | Heap + DP + Binary Search |
| Minimum Number of Refueling Stops | #871 | 🔴 Hard | Greedy + Max-Heap |
| Trapping Rain Water II | #407 | 🔴 Hard | Min-Heap on grid boundaries |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Heap Playlist | youtube.com/@NeetCode | Top K + Two Heaps walkthroughs |
| Python heapq docs | docs.python.org/3/library/heapq.html | All heapq functions |

---

## 🐍 Python Tips

```python
import heapq

# Max-heap — negate all values
max_heap = []
heapq.heappush(max_heap, -val)
max_val = -heapq.heappop(max_heap)

# Heap of tuples — sorted by first element
heapq.heappush(h, (dist, node_id))   # tie-break on node_id

# Lazy deletion — mark stale entries instead of removing
valid = set()
while heap:
    val, key = heapq.heappop(heap)
    if key in valid:
        process(val, key)

# Fixed-size K heap — O(n log k) for top K
for val in stream:
    heapq.heappush(h, val)
    if len(h) > k:
        heapq.heappop(h)    # removes minimum, keeps K largest
```