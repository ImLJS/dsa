# 🔀 Sorting

> Understand the algorithms cold. In interviews you rarely implement them — but you need to know when each one applies, what its complexity is, and how the partition/merge logic gets reused in problems.

---

## Algorithms Overview

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable | Key Idea |
|-----------|------------|-----------|-------------|-------|--------|---------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | Swap adjacent, largest bubbles to end |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ | Find min, place at front each pass |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | Insert each element into sorted left part |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | Divide + merge sorted halves |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | Partition around pivot |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | Build max-heap, extract max repeatedly |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) | ✅ | Count frequencies, works on integers only |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n + k) | ✅ | Sort digit by digit from least significant |

> **k** = range of input values (Counting Sort), number of digits (Radix Sort)

---

## When to Use Which

| Situation | Best Choice | Why |
|-----------|------------|-----|
| General purpose, unknown input | Merge Sort | Guaranteed O(n log n), stable |
| Memory is tight | Heap Sort | O(1) space, O(n log n) guaranteed |
| Nearly sorted input | Insertion Sort | O(n) on nearly sorted data |
| Small array (< 20 elements) | Insertion Sort | Low constant factor beats merge/quick |
| Integers in small range | Counting Sort | O(n + k), beats comparison sorts |
| Need stable sort in Python | `arr.sort()` / `sorted()` | Timsort — stable, O(n log n) |
| Kth largest / partition problems | Quick Select | O(n) average — based on quick sort partition |

---

## algorithm/

### bubble_sort.py

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break    # already sorted — O(n) best case
    return arr
```

**Complexity:** O(n²) average/worst, O(n) best (already sorted)
**Space:** O(1)
**Remember:** Never used in practice. Good for understanding stability and early termination.

---

### selection_sort.py

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Complexity:** O(n²) always
**Space:** O(1)
**Remember:** Makes exactly n−1 swaps. Useful when write operations are expensive.

---

### insertion_sort.py

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Complexity:** O(n²) average/worst, O(n) best
**Space:** O(1)
**Remember:** Best for small or nearly-sorted arrays. Used internally by Timsort for small subarrays.

---

### merge_sort.py

```python
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


# Count inversions variant — count how many swaps needed
def merge_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left,  lc = merge_count(arr[:mid])
    right, rc = merge_count(arr[mid:])
    merged, mc = merge_and_count(left, right)
    return merged, lc + rc + mc


def merge_and_count(left, right):
    result, count = [], 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
            count += len(left) - i    # all remaining left elements are inversions
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count
```

**Complexity:** O(n log n) always
**Space:** O(n)
**Remember:** Only sorting algorithm that works on linked lists efficiently. Stable. Used for count inversions.

---

### quick_sort.py

```python
def quick_sort(arr, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo < hi:
        pivot_idx = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, hi)
    return arr


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


# Quick Select — find Kth smallest in O(n) average
def quick_select(arr, lo, hi, k):
    if lo == hi:
        return arr[lo]
    pivot_idx = partition(arr, lo, hi)
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return quick_select(arr, lo, pivot_idx - 1, k)
    else:
        return quick_select(arr, pivot_idx + 1, hi, k)
```

**Complexity:** O(n log n) average, O(n²) worst (bad pivot choice)
**Space:** O(log n) stack
**Remember:** Partition logic is reused in Kth Largest/Smallest problems. Use random pivot to avoid worst case.

---

### heap_sort.py

```python
import heapq

# Simple version using Python's heapq
def heap_sort(arr):
    heapq.heapify(arr)          # O(n) build
    return [heapq.heappop(arr) for _ in range(len(arr))]   # O(n log n) extract


# Manual max-heap version (in-place)
def heap_sort_inplace(arr):
    n = len(arr)

    def heapify(arr, n, i):
        largest = i
        left, right = 2*i+1, 2*i+2
        if left  < n and arr[left]  > arr[largest]: largest = left
        if right < n and arr[right] > arr[largest]: largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    for i in range(n // 2 - 1, -1, -1):   # build max-heap
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):          # extract max one by one
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
```

**Complexity:** O(n log n) always
**Space:** O(1)
**Remember:** Not stable. Good when you need guaranteed O(n log n) with O(1) space.

---

### counting_sort.py

```python
def counting_sort(arr, max_val=None):
    if not arr: return arr
    if max_val is None: max_val = max(arr)

    count = [0] * (max_val + 1)
    for val in arr:
        count[val] += 1

    result = []
    for val, freq in enumerate(count):
        result.extend([val] * freq)
    return result


# For negative numbers / arbitrary range
def counting_sort_range(arr):
    min_val = min(arr)
    offset  = -min_val              # shift all values to be >= 0
    count   = [0] * (max(arr) - min_val + 1)
    for val in arr:
        count[val + offset] += 1
    result = []
    for i, freq in enumerate(count):
        result.extend([i - offset] * freq)
    return result
```

**Complexity:** O(n + k) where k = range of values
**Space:** O(k)
**Remember:** Only works on integers. Very fast when k is small (e.g. sort 0–9, sort by age 0–100).

---

### radix_sort.py

```python
def radix_sort(arr):
    if not arr: return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr


def counting_sort_by_digit(arr, exp):
    n      = len(arr)
    output = [0] * n
    count  = [0] * 10

    for val in arr:
        digit = (val // exp) % 10
        count[digit] += 1

    for i in range(1, 10):    # cumulative count
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):    # fill output right-to-left (stable)
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    return output
```

**Complexity:** O(nk) where k = number of digits
**Space:** O(n + k)
**Remember:** Stable. Faster than comparison sorts for integers with a fixed number of digits.

---

## problems/

### LeetCode Problems Where Sorting is the Key

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Sort Colors (Dutch National Flag) | #75 | 🟡 Medium | 3-way partition in-place — lo/mid/hi pointers |
| Kth Largest Element in an Array | #215 | 🟡 Medium | Quick Select O(n) avg, or min-heap O(n log k) |
| Largest Number | #179 | 🟡 Medium | Custom comparator: compare `a+b` vs `b+a` as strings |
| Merge Intervals | #56 | 🟡 Medium | Sort by start time, merge overlapping |
| Insert Interval | #57 | 🟡 Medium | Find insertion point, merge with neighbours |
| Meeting Rooms II | #253 | 🟡 Medium | Sort start/end separately, two pointers |
| H-Index | #274 | 🟡 Medium | Sort descending, find where i+1 > citations[i] |
| Find K Closest Elements | #658 | 🟡 Medium | Sort by distance then value, or binary search |
| Wiggle Sort II | #324 | 🟡 Medium | Sort + interleave medium and large elements |
| Count of Smaller Numbers After Self | #315 | 🔴 Hard | Merge sort + count inversions |

---

## Combined Practice

> These problems combine sorting with another pattern.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Kth Largest Element | #215 | 🟡 Medium | Quick Select or Heap |
| Count of Smaller Numbers After Self | #315 | 🔴 Hard | Merge Sort + count inversions |
| Merge Intervals | #56 | 🟡 Medium | Sort + Greedy merging |
| Meeting Rooms II | #253 | 🟡 Medium | Sort + Two Pointers / Heap |
| Maximum Gap | #164 | 🔴 Hard | Bucket Sort + Pigeonhole principle |
| Russian Doll Envelopes | #354 | 🔴 Hard | Sort + LIS (Binary Search) |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| VisuAlgo Sorting | visualgo.net/en/sorting | Animated comparisons of all algorithms |
| CS50 Sorting Lecture | cs50.harvard.edu | Best visual + intuition for beginners |
| NeetCode Kth Largest | youtube.com/@NeetCode | Quick Select walkthrough |

---

## 🐍 Python Tips

```python
# Python uses Timsort — stable, O(n log n)
arr.sort()                              # in-place
sorted(arr)                             # returns new list

# Custom key — sort by second element
arr.sort(key=lambda x: x[1])

# Sort descending
arr.sort(reverse=True)

# Multi-key sort — primary asc, secondary desc
arr.sort(key=lambda x: (x[0], -x[1]))

# Custom comparator (use functools.cmp_to_key)
import functools
def cmp(a, b):
    return -1 if a + b > b + a else 1   # for Largest Number problem
arr.sort(key=functools.cmp_to_key(cmp))

# Kth largest using heap — O(n log k)
import heapq
heapq.nlargest(k, arr)[-1]              # kth largest
heapq.nsmallest(k, arr)[-1]            # kth smallest
```