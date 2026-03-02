# 📦 Arrays

> The backbone of DSA. Nearly every algorithm eventually manipulates an array. Master these five patterns and you have a toolkit that solves the majority of array problems at any difficulty level.

---

## Folder Structure

```
arrays/
├── README.md              ← you are here
├── basics.md              ← warm-up problems, no named pattern needed
├── my_solutions.md        ← your personal progress log
└── problems/
    ├── misc/              ← problems that don't fit a named pattern
    ├── two_pointers/
    ├── sliding_window/
    ├── prefix_sum/
    ├── kadanes/
    └── hashmap/
```

---

## Patterns Overview

| Pattern | When to Use | Trigger Keywords |
|---------|------------|-----------------|
| [Two Pointers](#-two-pointers) | Sorted array, pairs, triplets | "sorted", "pair that sums to", "remove duplicates in-place" |
| [Sliding Window](#-sliding-window) | Contiguous subarray with a constraint | "contiguous subarray", "substring", "at most k", "longest/shortest" |
| [Prefix Sum](#-prefix-sum) | Range queries, subarray sum = k | "range sum", "subarray sum equals", "sum between indices" |
| [Kadane's Algorithm](#-kadanes-algorithm) | Max/min contiguous subarray | "maximum subarray", "largest sum contiguous" |
| [HashMap / Frequency](#-hashmap--frequency-count) | Complements, duplicates, counts | "two sum", "frequency", "anagram", "duplicate" |

> **Note on sorting:** Problems where you sort as a first step (e.g. 3Sum sorts before two-pointers) stay in the relevant pattern folder. Problems where sorting *is* the core skill (Sort Colors, Largest Number, Kth Largest) live in `sorting/`.

---

## 👉 Two Pointers

**When to use:** Array is sorted OR you need to find pairs/triplets with a target sum. Place one pointer at each end and move them inward based on the current sum vs target.

**Trigger keywords:** "sorted array", "pair that sums to", "remove duplicates in-place", "reverse in-place"

**Time:** O(n) &nbsp;&nbsp; **Space:** O(1)

```python
# Template — find pair summing to target in sorted array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1       # need a bigger sum — move left forward
        else:
            right -= 1      # need a smaller sum — move right backward

    return []
```

```python
# Write-head variant — remove duplicates / move zeroes
def remove_duplicates(nums):
    write = 1                           # write_head starts at index 1

    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:   # new unique value found
            nums[write] = nums[read]
            write += 1

    return write                        # new length
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Two Sum II — Input Array Is Sorted | #167 | 🟢 Easy | Classic inward two-pointer on sorted array |
| Remove Duplicates from Sorted Array | #26 | 🟢 Easy | Left pointer is the write-head |
| Move Zeroes | #283 | 🟢 Easy | Write-head skips over zeroes |
| 3Sum | #15 | 🟡 Medium | Sort first, fix one element, two-pointer for the other two |
| 3Sum Closest | #16 | 🟡 Medium | Track closest sum seen, minimise absolute difference |
| Container With Most Water | #11 | 🟡 Medium | Always move the shorter side inward |
| Trapping Rain Water | #42 | 🔴 Hard | Track max from both ends — water = min(left_max, right_max) - height |

### Common Mistakes

- **Forgetting to sort first.** Two pointers only work on sorted data (or problems where order is irrelevant like write-head pattern).
- **Not skipping duplicates in 3Sum.** After finding a valid triplet, advance both pointers and skip `while arr[left] == arr[left-1]`.
- **Wrong pointer movement.** Move the pointer on the side that can't improve the current result.

---

## 🪟 Sliding Window

**When to use:** Find the longest/shortest/best contiguous subarray or substring satisfying a constraint. Fixed window = known size k. Variable window = expand right, shrink left when constraint breaks.

**Trigger keywords:** "contiguous subarray", "substring", "at most k distinct", "longest without repeating", "minimum size"

**Time:** O(n) &nbsp;&nbsp; **Space:** O(1) fixed, O(k) variable

```python
# Fixed window — size k
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    result = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]      # slide: add new, remove old
        result = max(result, window_sum)

    return result
```

```python
# Variable window — expand right, shrink left
def variable_window(arr):
    left = 0
    result = 0
    window_state = {}       # track whatever the constraint is

    for right in range(len(arr)):
        # 1. Expand: add arr[right] to window
        window_state[arr[right]] = window_state.get(arr[right], 0) + 1

        # 2. Shrink: while window violates constraint
        while not is_valid(window_state):
            window_state[arr[left]] -= 1
            if window_state[arr[left]] == 0:
                del window_state[arr[left]]
            left += 1

        # 3. Update result with current valid window
        result = max(result, right - left + 1)

    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Best Time to Buy and Sell Stock | #121 | 🟢 Easy | Track running min price, record max profit |
| Maximum Average Subarray I | #643 | 🟢 Easy | Fixed window of exactly size k |
| Minimum Size Subarray Sum | #209 | 🟡 Medium | Shrink when running sum >= target |
| Longest Repeating Character Replacement | #424 | 🟡 Medium | `window_size - max_freq <= k` is the invariant |
| Fruit Into Baskets | #904 | 🟡 Medium | At most 2 distinct values — variable window |
| Sliding Window Maximum | #239 | 🔴 Hard | Monotonic deque keeps the max at front |

### Common Mistakes

- **Using `list.pop(0)` instead of `deque.popleft()`.** The first is O(n), the second is O(1). Always use `deque` for sliding window maximum.
- **Updating result before shrinking.** Always shrink first, then update. Recording an invalid window inflates your result.
- **Over-shrinking.** Only shrink until the window is valid again — not further.

---

## ➕ Prefix Sum

**When to use:** Answer range sum queries in O(1) after an O(n) build step. Find subarrays summing to a target k using a running sum + hashmap.

**Trigger keywords:** "range sum", "subarray sum equals k", "sum between indices i and j", "pivot index"

**Time:** O(n) build + O(1) query &nbsp;&nbsp; **Space:** O(n)

```python
# Build prefix sum array
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)      # prefix[0] = 0 (empty prefix)
    for i, val in enumerate(arr):
        prefix[i + 1] = prefix[i] + val
    return prefix

# Range sum query — sum of arr[l..r] inclusive
def range_sum(prefix, l, r):
    return prefix[r + 1] - prefix[l]   # note: prefix[l] not prefix[l-1]
```

```python
# Subarray sum equals k — prefix sum + hashmap
from collections import defaultdict

def subarray_sum(arr, k):
    count = defaultdict(int)
    count[0] = 1            # empty prefix has sum 0 — CRITICAL initialisation
    running = 0
    result = 0

    for val in arr:
        running += val
        result += count[running - k]    # how many prefixes give us sum k
        count[running] += 1

    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Running Sum of 1D Array | #1480 | 🟢 Easy | Textbook prefix sum, built in-place |
| Range Sum Query (Immutable) | #303 | 🟢 Easy | `prefix[r+1] - prefix[l]` |
| Find Pivot Index | #724 | 🟢 Easy | `left_sum == total - left_sum - arr[i]` |
| Subarray Sum Equals K | #560 | 🟡 Medium | Running sum + hashmap, count complements |
| Product of Array Except Self | #238 | 🟡 Medium | Prefix product × suffix product, no division |
| Continuous Subarray Sum | #523 | 🟡 Medium | Prefix mod k + first-seen index hashmap |
| Subarray Sums Divisible by K | #974 | 🟡 Medium | Prefix mod k, count matching remainders |

### Common Mistakes

- **Off-by-one.** Use `prefix[r+1] - prefix[l]` not `prefix[r] - prefix[l-1]`. The `+1` offset in the prefix array is what makes this clean.
- **Forgetting `count[0] = 1`.** Without this initialisation, subarrays starting from index 0 are missed entirely.

---

## 📈 Kadane's Algorithm

**When to use:** Find the maximum (or minimum) sum of a contiguous subarray. At each element, decide whether to extend the current subarray or start fresh from this element.

**Trigger keywords:** "maximum subarray", "contiguous subarray with largest sum", "max/min product subarray"

**Time:** O(n) &nbsp;&nbsp; **Space:** O(1)

```python
# Standard Kadane's — maximum sum
def max_subarray(arr):
    current = max_sum = arr[0]

    for val in arr[1:]:
        current = max(val, current + val)   # extend or restart
        max_sum = max(max_sum, current)

    return max_sum
```

```python
# Product variant — track both max AND min (negatives flip sign)
def max_product(arr):
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
| Maximum Subarray | #53 | 🟡 Medium | Reset current when `current + val < val` |
| Maximum Product Subarray | #152 | 🟡 Medium | Track both max and min — negatives flip |
| Maximum Sum Circular Subarray | #918 | 🟡 Medium | `max(normal_kadane, total - min_subarray)` |
| Longest Turbulent Subarray | #978 | 🟡 Medium | Extend on alternating signs, else reset to 1 |

### Common Mistakes

- **Initialising with 0 instead of `arr[0]`.** If all elements are negative, the correct answer is the largest negative, not 0.
- **Forgetting the product variant needs both max and min.** A negative times a negative is positive — the min could become the max.

---

## 🗺️ HashMap / Frequency Count

**When to use:** Count element occurrences, detect duplicates, or find complement pairs — all in O(1) per lookup using a dictionary or set.

**Trigger keywords:** "two sum", "frequency", "anagram", "duplicate", "complement", "most common"

**Time:** O(n) &nbsp;&nbsp; **Space:** O(n)

```python
# Complement lookup — Two Sum
def two_sum(nums, target):
    seen = {}                           # value → index

    for i, val in enumerate(nums):
        complement = target - val
        if complement in seen:
            return [seen[complement], i]
        seen[val] = i

    return []
```

```python
from collections import Counter

# Frequency counting
freq = Counter(arr)
freq.most_common(k)             # top-k most frequent elements

# Group by transformed key
from collections import defaultdict
groups = defaultdict(list)
for word in words:
    groups[tuple(sorted(word))].append(word)   # group anagrams
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Two Sum | #1 | 🟢 Easy | Complement lookup — store value → index |
| Contains Duplicate | #217 | 🟢 Easy | Set membership check — O(n) time O(n) space |
| Majority Element | #169 | 🟢 Easy | Counter or Boyer-Moore voting algorithm |
| Top K Frequent Elements | #347 | 🟡 Medium | Counter + min-heap of size k |
| Group Anagrams | #49 | 🟡 Medium | `sorted(word)` as the hashmap key |
| Longest Consecutive Sequence | #128 | 🟡 Medium | Set — only start chains at sequence minimum |

### Common Mistakes

- **Using `dict` when `set` is enough.** If you only need existence checks (not values), use a set.
- **Not handling the case where complement == val.** In Two Sum, `seen[complement]` must exist AND be a different index.

---

## 🔀 Combined Practice

> These problems require mixing 2 or more patterns. Spend at least 15 minutes before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Minimum Window Substring | #76 | 🔴 Hard | Sliding Window + Dual HashMaps |
| Subarray Sums Divisible by K | #974 | 🟡 Medium | Prefix Sum + HashMap (mod arithmetic) |
| 4Sum | #18 | 🟡 Medium | Sort + Two Pointer × 2 |
| Minimum Operations to Reduce X to Zero | #1658 | 🟡 Medium | Sliding Window + Prefix Sum |
| Find All Anagrams in a String | #438 | 🟡 Medium | Sliding Window + Frequency Map |
| Max Sum of 3 Non-Overlapping Subarrays | #689 | 🔴 Hard | Prefix Sum + Sliding Window + DP |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Arrays Playlist | youtube.com/@NeetCode | Best video per pattern with clean Python |
| LeetCode Explore — Arrays | leetcode.com/explore/learn/card/array-and-string | Official structured problem card |

---

## 🐍 Python Tips

```python
# Reverse
arr[::-1]

# Enumerate — index + value together
for i, val in enumerate(arr):
    pass

# Zip two arrays in parallel
for a, b in zip(arr1, arr2):
    pass

# Sort by custom key
arr.sort(key=lambda x: (x[1], -x[0]))      # primary asc, secondary desc

# List comprehension with filter
evens = [x for x in arr if x % 2 == 0]

# Flatten 2D list
flat = [x for row in matrix for x in row]

# Transpose matrix
transposed = list(zip(*matrix))

# Prefix sum in-place
for i in range(1, len(arr)):
    arr[i] += arr[i - 1]

# Quick frequency count
from collections import Counter
freq = Counter(arr)
```