# 📦 Arrays

> The backbone of DSA. Most problems ultimately reduce to array manipulation.

---

## Patterns Overview

| Pattern | When to Use | Key Idea |
|---------|------------|---------|
| [Two Pointers](#-two-pointers) | Sorted array, pairs/triplets | Left & right pointers move inward |
| [Sliding Window](#-sliding-window) | Contiguous subarray with constraint | Expand right, shrink left |
| [Prefix Sum](#-prefix-sum) | Range sum queries, subarray sum = k | Build once O(n), query O(1) |
| [Kadane's Algorithm](#-kadanes-algorithm) | Max/min contiguous subarray sum | Extend or restart running sum |
| [Sorting-based](#-sorting-based-patterns) | Intervals, duplicates, custom order | Sort unlocks greedy/two-pointer |
| [HashMap / Frequency](#-hashmap--frequency-count) | Complements, duplicates, counts | O(1) lookup per element |

---

## 👉 Two Pointers

**When to use:** Array is sorted OR you need pairs/triplets. Move left and right pointers toward each other until they meet.

**Trigger keywords:** "sorted array", "pair that sums to", "remove duplicates in-place", "reverse"

```python
left, right = 0, len(arr) - 1
while left < right:
    current = arr[left] + arr[right]
    if current == target:
        return [left, right]
    elif current < target:
        left += 1
    else:
        right -= 1
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Two Sum II — Input Array Is Sorted | #167 | 🟢 Easy | Classic two-pointer on sorted array |
| Remove Duplicates from Sorted Array | #26 | 🟢 Easy | Left pointer acts as write head |
| 3Sum | #15 | 🟡 Medium | Sort + fix one element, two-pointer for rest |
| Container With Most Water | #11 | 🟡 Medium | Shrink the shorter side each step |
| Trapping Rain Water | #42 | 🔴 Hard | Track max boundary from both directions |
| 3Sum Closest | #16 | 🟡 Medium | Track minimum absolute difference from target |

### Common Mistakes
- Forgetting to sort the array first
- Not handling duplicates (skip `while arr[left] == arr[left-1]`)
- Off-by-one on pointer movement

---

## 🪟 Sliding Window

**When to use:** Contiguous subarray/substring with a constraint. Fixed window = known size `k`. Variable window = expand right, shrink left when constraint breaks.

**Trigger keywords:** "contiguous subarray", "substring", "at most k distinct", "longest/shortest subarray with..."

```python
# Variable window template
left = 0
result = 0
window_state = {}  # or a counter

for right in range(len(arr)):
    # 1. Expand: add arr[right] to window
    window_state[arr[right]] = window_state.get(arr[right], 0) + 1

    # 2. Shrink: while window is invalid
    while not is_valid(window_state):
        window_state[arr[left]] -= 1
        if window_state[arr[left]] == 0:
            del window_state[arr[left]]
        left += 1

    # 3. Update result
    result = max(result, right - left + 1)

return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Best Time to Buy and Sell Stock | #121 | 🟢 Easy | Track min price so far, record max profit |
| Maximum Average Subarray I | #643 | 🟢 Easy | Fixed window of exactly size k |
| Minimum Size Subarray Sum | #209 | 🟡 Medium | Variable — shrink when running sum ≥ target |
| Longest Repeating Character Replacement | #424 | 🟡 Medium | `window_size − max_freq ≤ k` |
| Fruit Into Baskets | #904 | 🟡 Medium | At most 2 distinct values — variable window |
| Sliding Window Maximum | #239 | 🔴 Hard | Monotonic deque keeps max at front |

### Common Mistakes
- Using `list.pop(0)` instead of `deque.popleft()` — O(n) vs O(1)
- Forgetting to shrink the window before updating the result
- Shrinking too aggressively (shrink only until valid, not more)

---

## ➕ Prefix Sum

**When to use:** Range sum queries or finding subarrays that sum to a target. Build the prefix array once in O(n), answer each query in O(1).

**Trigger keywords:** "range sum", "subarray sum equals k", "sum between indices i and j"

```python
# Build
prefix = [0] * (len(arr) + 1)
for i, val in enumerate(arr):
    prefix[i + 1] = prefix[i] + val

# Query: sum of arr[l..r] inclusive
def range_sum(l, r):
    return prefix[r + 1] - prefix[l]

# Subarray sum == k  →  prefix + hashmap
from collections import defaultdict
count = defaultdict(int)
count[0] = 1
running = 0
result = 0
for val in arr:
    running += val
    result += count[running - k]
    count[running] += 1
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Running Sum of 1D Array | #1480 | 🟢 Easy | Textbook prefix sum |
| Range Sum Query (Immutable) | #303 | 🟢 Easy | `prefix[r] − prefix[l−1]` |
| Subarray Sum Equals K | #560 | 🟡 Medium | Prefix + hashmap, count complements |
| Product of Array Except Self | #238 | 🟡 Medium | Prefix product × suffix product |
| Find Pivot Index | #724 | 🟢 Easy | `left_sum == total − left − arr[i]` |
| Continuous Subarray Sum | #523 | 🟡 Medium | Prefix mod k + first-seen hashmap |

### Common Mistakes
- Off-by-one: `prefix[r+1] - prefix[l]` not `prefix[r] - prefix[l-1]`
- Forgetting to initialise `count[0] = 1` for the "empty prefix" case

---

## 📈 Kadane's Algorithm

**When to use:** Maximum or minimum sum of a contiguous subarray. Extend the current run or restart from the current element.

**Trigger keywords:** "maximum subarray", "contiguous subarray with largest sum"

```python
# Standard Kadane's
max_sum = arr[0]
current = arr[0]

for val in arr[1:]:
    current = max(val, current + val)   # extend or restart
    max_sum = max(max_sum, current)

return max_sum
```

```python
# Product variant — track both max and min (negatives flip sign)
max_prod = min_prod = result = arr[0]

for val in arr[1:]:
    candidates = (val, max_prod * val, min_prod * val)
    max_prod = max(candidates)
    min_prod = min(candidates)
    result = max(result, max_prod)

return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Maximum Subarray | #53 | 🟡 Medium | Core Kadane — reset when current sum < 0 |
| Maximum Product Subarray | #152 | 🟡 Medium | Track both max and min (negatives flip sign) |
| Maximum Sum Circular Subarray | #918 | 🟡 Medium | `total − min_subarray` OR normal Kadane |
| Longest Turbulent Subarray | #978 | 🟡 Medium | Extend on alternating signs, else reset |

---

## 🔀 Sorting-based Patterns

**When to use:** Sort to unlock two-pointer logic, greedy interval merging, or clean duplicate handling.

**Trigger keywords:** "merge intervals", "overlapping intervals", "sort and..."

```python
# Merge Intervals
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]

for start, end in intervals[1:]:
    if start <= merged[-1][1]:          # overlap
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Sort Colors (Dutch National Flag) | #75 | 🟡 Medium | 3-way partition in-place |
| Merge Intervals | #56 | 🟡 Medium | Sort by start, merge overlapping |
| Insert Interval | #57 | 🟡 Medium | Find insertion point + merge |
| Largest Number | #179 | 🟡 Medium | Custom comparator: `a+b` vs `b+a` |

---

## 🗺️ HashMap / Frequency Count

**When to use:** Count occurrences, detect duplicates, find complement pairs — all in O(1) per lookup.

**Trigger keywords:** "two sum", "frequency", "anagram", "duplicate", "complement"

```python
from collections import Counter, defaultdict

# Complement lookup
seen = {}
for i, val in enumerate(arr):
    if target - val in seen:
        return [seen[target - val], i]
    seen[val] = i

# Frequency count
freq = Counter(arr)
freq.most_common(k)      # top-k elements
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Two Sum | #1 | 🟢 Easy | Complement lookup in hashmap |
| Contains Duplicate | #217 | 🟢 Easy | Set membership check |
| Majority Element | #169 | 🟢 Easy | Counter or Boyer-Moore voting |
| Top K Frequent Elements | #347 | 🟡 Medium | Counter + heap or bucket sort |
| Group Anagrams | #49 | 🟡 Medium | `sorted(word)` as the hashmap key |
| Longest Consecutive Sequence | #128 | 🟡 Medium | Set — only start chains at sequence minimum |

---

## 🔀 Combined Practice

> These problems require mixing 2+ patterns. Spend 15+ minutes before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Maximum Points You Can Obtain from Cards | #1423 | 🟡 Medium | Sliding Window + Prefix Sum |
| Subarray Sums Divisible by K | #974 | 🟡 Medium | Prefix Sum + HashMap (mod) |
| 4Sum | #18 | 🟡 Medium | Sort + Two Pointer × 2 |
| Minimum Operations to Reduce X to Zero | #1658 | 🟡 Medium | Sliding Window + Prefix |
| Find All Anagrams in a String | #438 | 🟡 Medium | Sliding Window + Frequency Map |
| Minimum Window Substring | #76 | 🔴 Hard | Sliding Window + Dual HashMaps |
| Max Sum of 3 Non-Overlapping Subarrays | #689 | 🔴 Hard | Prefix Sum + Sliding Window + DP |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Arrays Playlist | youtube.com/@NeetCode | Best video per pattern with clean Python |
| LeetCode Explore — Arrays | leetcode.com/explore/learn/card/array-and-string | Official structured problem card |
| VisuAlgo Sorting | visualgo.net/en/sorting | Animated sorting algorithm walkthroughs |

---

## 🐍 Python Tips

```python
# Reverse
arr[::-1]

# Enumerate (index + value)
for i, val in enumerate(arr):

# Zip two arrays
for a, b in zip(arr1, arr2):

# Sort by custom key
arr.sort(key=lambda x: (x[1], -x[0]))

# List comprehension with filter
[x for x in arr if x > 0]

# Flatten 2D list
[x for row in matrix for x in row]

# Transpose matrix
list(zip(*matrix))
```