# 🔍 Binary Search

> Halve the search space every step. O(log n). Works on sorted data AND on abstract answer ranges.

---

## Patterns Overview

| Pattern | When to Use | Key Idea |
|---------|------------|---------|
| [Classic Binary Search](#-classic-binary-search) | Sorted array, find target | lo/mid/hi loop |
| [Rotated Array](#-binary-search-on-rotated-array) | Sorted then rotated | One half is always sorted |
| [Search on Answer](#-binary-search-on-answer-search-space) | Answer is a value in a range | Write `check(X)`, binary search on X |
| [bisect Module](#-binary-search--bisect-module) | Insert/search in sorted list | Python built-in O(log n) |

---

## 📋 Classic Binary Search

**When to use:** Sorted array — find a target or the correct insertion position.

> ⚠️ Always use `lo + (hi - lo) // 2` instead of `(lo + hi) // 2` to avoid integer overflow.

```python
# Find exact target
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# Find leftmost occurrence
def first_occurrence(arr, target):
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            hi = mid - 1       # keep searching left
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result

# Find rightmost occurrence
def last_occurrence(arr, target):
    lo, hi = 0, len(arr) - 1
    result = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            result = mid
            lo = mid + 1       # keep searching right
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Binary Search | #704 | 🟢 Easy | Textbook — return mid or −1 |
| Search Insert Position | #35 | 🟢 Easy | Return `lo` after loop = correct insertion index |
| First Bad Version | #278 | 🟢 Easy | Minimise — find first True in boolean space |
| Find First and Last Position of Element | #34 | 🟡 Medium | Two passes: leftmost + rightmost |
| Search a 2D Matrix | #74 | 🟡 Medium | Treat 2D grid as flattened 1D index |

---

## 🔄 Binary Search on Rotated Array

**When to use:** Array was sorted then rotated at some pivot. Key insight: one half is always fully sorted — use that to decide which side the target is on.

```python
def search_rotated(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Find Minimum in Rotated Sorted Array | #153 | 🟡 Medium | Minimum is always in the unsorted half |
| Search in Rotated Sorted Array | #33 | 🟡 Medium | Identify sorted half, check target range |
| Search in Rotated Sorted Array II | #81 | 🟡 Medium | Duplicates — carefully shrink both ends |
| Find Minimum in Rotated Array II | #154 | 🔴 Hard | Same logic, skip duplicate boundaries |

---

## 🎯 Binary Search on Answer (Search Space)

**When to use:** The answer is a number in range `[lo, hi]`. Instead of searching an array, you're searching for the optimal value directly.

**How to identify:**
- "Find minimum X such that..."
- "Find maximum X such that..."
- You can write a `check(X)` function that returns True/False
- If `check(X)` is True, then `check(X+1)` is also True (or False) — monotonic

```python
# Template: find minimum X where check(X) is True
def solve():
    lo, hi = MIN_POSSIBLE, MAX_POSSIBLE

    def check(mid):
        # Return True if mid is a feasible answer
        pass

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if check(mid):
            hi = mid          # mid works, try smaller
        else:
            lo = mid + 1      # mid doesn't work, try larger

    return lo                 # lo == hi == answer


# Example: Koko Eating Bananas
def minEatingSpeed(piles, h):
    lo, hi = 1, max(piles)

    def can_finish(speed):
        return sum((p + speed - 1) // speed for p in piles) <= h

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if can_finish(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Koko Eating Bananas | #875 | 🟡 Medium | Min speed to finish all piles in h hours |
| Capacity to Ship Packages in D Days | #1011 | 🟡 Medium | Min capacity to ship within D days |
| Minimum Days to Make m Bouquets | #1482 | 🟡 Medium | Can we make m bouquets after d days? |
| Find Peak Element | #162 | 🟡 Medium | Climb toward the higher neighbour |
| Split Array Largest Sum | #410 | 🔴 Hard | Minimise the max subarray sum with m splits |
| Median of Two Sorted Arrays | #4 | 🔴 Hard | Binary search on the partition point |

---

## 📐 Binary Search + bisect Module

**When to use:** Need O(log n) insertion or search on a maintained sorted list.

```python
import bisect

arr = [1, 3, 5, 7, 9]

# Find insertion index (leftmost)
bisect.bisect_left(arr, 5)     # → 2 (index of 5)
bisect.bisect_left(arr, 4)     # → 2 (where 4 would go)

# Find insertion index (rightmost)
bisect.bisect_right(arr, 5)    # → 3 (after existing 5)

# Insert while keeping sorted
bisect.insort(arr, 6)          # arr becomes [1,3,5,6,7,9]

# LIS in O(n log n) using patience sort
def length_of_lis(nums):
    tails = []
    for n in nums:
        idx = bisect.bisect_left(tails, n)
        if idx == len(tails):
            tails.append(n)
        else:
            tails[idx] = n
    return len(tails)
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Time Based Key-Value Store | #981 | 🟡 Medium | `bisect_right` on list of timestamps |
| Find Right Interval | #436 | 🟡 Medium | Sort start points, `bisect_left` each endpoint |
| Longest Increasing Subsequence | #300 | 🟡 Medium | O(n log n) patience sort with `bisect_left` |
| Russian Doll Envelopes | #354 | 🔴 Hard | Sort + 2D patience sort with bisect |

---

## 🔀 Combined Practice

> These problems require mixing 2+ patterns. Spend 15+ minutes before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Maximum Profit in Job Scheduling | #1235 | 🔴 Hard | DP + Binary Search on start times |
| Median of Two Sorted Arrays | #4 | 🔴 Hard | Pure Binary Search on partition |
| Find K Closest Elements | #658 | 🟡 Medium | Binary Search + Two Pointer expansion |
| Max Side Length of Square ≤ Threshold | #1292 | 🟡 Medium | Prefix Sum + Binary Search on side length |
| Aggressive Cows | GFG | 🟡 Medium | Binary Search on Answer + Greedy check |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Binary Search Playlist | youtube.com/@NeetCode | Best search-space template coverage |
| LeetCode Explore — Binary Search | leetcode.com/explore/learn/card/binary-search | Official card with 3 templates |
| Python bisect docs | docs.python.org/3/library/bisect.html | `bisect_left`, `bisect_right`, `insort` |
| LC Discussion — 3 BS Templates | leetcode.com/discuss/general-discussion/786126 | Community guide covering all BS variants |

---

## 🐍 Python Tips

```python
import bisect

# bisect_left  → first index where arr[i] >= x
# bisect_right → first index where arr[i] >  x

# Check if x exists in sorted array
idx = bisect.bisect_left(arr, x)
exists = idx < len(arr) and arr[idx] == x

# Count elements < x
count_less = bisect.bisect_left(arr, x)

# Count elements <= x
count_leq = bisect.bisect_right(arr, x)
```