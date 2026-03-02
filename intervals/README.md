# 📅 Intervals

> Most interval problems are solved by sorting by start time, then applying one of three strategies: merge, sweep line, or greedy scheduling.

---

## Patterns Overview

| Pattern | When to Use |
|---------|------------|
| [Merge Intervals](#-merge-intervals) | Combine all overlapping intervals |
| [Insert Interval](#-insert-interval) | Add one interval, re-merge |
| [Sweep Line / Event Points](#-sweep-line--event-points) | Count overlaps at any point, room scheduling |
| [Greedy Interval Scheduling](#-greedy-interval-scheduling) | Max non-overlapping intervals, meeting rooms |
| [Interval DP](#-interval-dp) | Optimal cost over a range [i..j] |

---

## Key Insight: When Do Two Intervals Overlap?

```python
# Intervals [a, b] and [c, d] OVERLAP if:
a <= d and c <= b

# Intervals DO NOT overlap if:
b < c or d < a   # one ends before the other starts

# Merged interval of overlapping [a,b] and [c,d]:
[min(a, c), max(b, d)]
```

---

## 🔀 Merge Intervals

**When to use:** Given a list of intervals, merge all overlapping ones into a single consolidated list.

**Trigger keywords:** "merge intervals", "combine overlapping", "consolidate ranges"

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])   # sort by start
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:             # overlaps with last
            merged[-1][1] = max(merged[-1][1], end)   # extend end
        else:
            merged.append([start, end])        # no overlap — new interval

    return merged
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Merge Intervals | #56 | 🟡 Medium | Sort by start, extend end on overlap |
| Summary Ranges | #228 | 🟢 Easy | Group consecutive integers into ranges |
| Interval List Intersections | #986 | 🟡 Medium | Two pointers on two sorted interval lists |
| Remove Covered Intervals | #1288 | 🟡 Medium | Sort by start; if end <= prev end, it's covered |

---

## ➕ Insert Interval

**When to use:** A sorted, non-overlapping list exists. Insert a new interval and re-merge.

**Trigger keywords:** "insert interval", "add to existing intervals"

```python
def insert(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)

    # 1. Add all intervals that end before new_interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # 2. Merge all overlapping intervals with new_interval
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)

    # 3. Add remaining intervals
    result.extend(intervals[i:])
    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Insert Interval | #57 | 🟡 Medium | Three phases: before, overlap, after |
| My Calendar I | #729 | 🟡 Medium | Check overlap with each existing booking |
| My Calendar II | #731 | 🟡 Medium | Track double-booked intervals |
| My Calendar III | #732 | 🔴 Hard | Sweep line to find max concurrent bookings |

---

## 🧹 Sweep Line / Event Points

**When to use:** Count the number of overlapping intervals at any point, find peak concurrency, or process events in time order.

**Trigger keywords:** "how many meetings overlap", "maximum overlap at any time", "minimum rooms needed", "number of cars in lot"

```python
# Meeting Rooms II — minimum rooms needed
def min_meeting_rooms(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))    # +1 room needed
        events.append((end,  -1))   # -1 room freed

    events.sort(key=lambda x: (x[0], x[1]))   # tie: end before start

    rooms = max_rooms = 0
    for _, change in events:
        rooms += change
        max_rooms = max(max_rooms, rooms)
    return max_rooms


# Alternative — sort start and end separately
def min_meeting_rooms_v2(intervals):
    starts = sorted(s for s, e in intervals)
    ends   = sorted(e for s, e in intervals)

    rooms = 0
    e_ptr = 0
    for start in starts:
        if start < ends[e_ptr]:
            rooms += 1          # need new room
        else:
            e_ptr += 1          # reuse freed room
    return rooms
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Meeting Rooms | #252 | 🟢 Easy | Sort by start, check if any overlap |
| Meeting Rooms II | #253 | 🟡 Medium | Sweep line or min-heap of end times |
| Employee Free Time | #759 | 🔴 Hard | Merge all schedules, find gaps |
| Car Pooling | #1094 | 🟡 Medium | Sweep line on pickup/dropoff events |
| Number of Flowers in Full Bloom | #2251 | 🔴 Hard | Binary search on sorted starts/ends |

---

## 🎯 Greedy Interval Scheduling

**When to use:** Select the maximum number of non-overlapping intervals, or determine how many intervals to remove to make them non-overlapping.

**Trigger keywords:** "maximum non-overlapping", "minimum removal", "non-conflicting activities"

```python
# Maximum non-overlapping intervals (Activity Selection)
# Greedy: always pick the interval that ends earliest
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])   # sort by END time

    count = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end   # take this interval
        else:
            count += 1       # remove this interval (it overlaps)

    return count


# Minimum number of arrows to burst balloons
def find_min_arrow_shots(points):
    points.sort(key=lambda x: x[1])   # sort by end

    arrows = 1
    arrow_pos = points[0][1]

    for start, end in points[1:]:
        if start > arrow_pos:
            arrows += 1
            arrow_pos = end    # new arrow at this end

    return arrows
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Non-overlapping Intervals | #435 | 🟡 Medium | Sort by end, greedily keep earliest-ending |
| Minimum Number of Arrows | #452 | 🟡 Medium | Sort by end, one arrow covers overlapping balloons |
| Partition Labels | #763 | 🟡 Medium | Track last occurrence of each char, extend window |
| Jump Game II | #45 | 🟡 Medium | Interval greedy — each jump extends reach |

---

## 📐 Interval DP

**When to use:** Find optimal cost over a contiguous subrange [i..j]. Typical in problems like "burst balloons", "minimum cost to merge", "stone game".

```python
# Template — compute dp[i][j] for all lengths
def interval_dp(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    # Fill by increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j],
                               dp[i][k] + dp[k+1][j] + cost(i, k, j))

    return dp[0][n-1]


# Burst Balloons — last balloon k in [left, right]
def max_coins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                )
    return dp[0][n-1]
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Burst Balloons | #312 | 🔴 Hard | k = last balloon burst in range |
| Minimum Cost to Merge Stones | #1000 | 🔴 Hard | Merge k piles at a time |
| Strange Printer | #664 | 🔴 Hard | `dp[i][j]` = min turns to print s[i..j] |
| Stone Game VII | #1690 | 🟡 Medium | Interval DP, alternating player choices |

---

## Combined Practice

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Meeting Rooms II | #253 | 🟡 Medium | Sweep Line + Heap |
| Maximum Profit in Job Scheduling | #1235 | 🔴 Hard | Intervals + DP + Binary Search |
| My Calendar III | #732 | 🔴 Hard | Sweep Line + Segment Tree |
| Data Stream as Disjoint Intervals | #352 | 🔴 Hard | Insert Interval + sorted structure |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Intervals Playlist | youtube.com/@NeetCode | Merge + sweep line walkthroughs |
| LeetCode Interval Problems | leetcode.com/tag/line-sweep | All sweep line tagged problems |

---

## 🐍 Python Tips

```python
# Sort intervals by start time
intervals.sort(key=lambda x: x[0])

# Sort by end time (for greedy scheduling)
intervals.sort(key=lambda x: x[1])

# Sort by start, break ties by end descending
intervals.sort(key=lambda x: (x[0], -x[1]))

# Sweep line — use a list of events
events = []
for s, e in intervals:
    events.append((s, 1))    # start event
    events.append((e, -1))   # end event
events.sort()

# Check overlap — [a,b] and [c,d]
overlap = a <= d and c <= b
```