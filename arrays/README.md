# 📦 Arrays & Strings

> Arrays and strings share the same five core patterns. Arrays work on indices and numbers; strings add character frequency and parsing. Master these patterns once and you handle both data types across easy, medium, and hard problems.

---

## Folder Structure

```
arrays_strings/
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
|---------|-------------|-----------------|
| [Two Pointers](#-two-pointers) | Sorted array/string, pairs, triplets, palindrome check | "sorted", "pair that sums to", "reverse in-place", "palindrome" |
| [Sliding Window](#-sliding-window) | Best/longest/shortest contiguous subarray or substring | "contiguous subarray", "substring", "at most k", "longest without" |
| [Prefix Sum](#-prefix-sum) | Range queries, subarray sum = k | "range sum", "subarray sum equals", "sum between indices" |
| [Kadane's Algorithm](#-kadanes-algorithm) | Max/min sum of contiguous subarray | "maximum subarray", "largest sum contiguous" |
| [HashMap / Frequency](#-hashmap--frequency-count) | Complements, duplicates, anagrams, character counts | "two sum", "frequency", "anagram", "duplicate", "most common" |

> **Arrays vs Strings:** The templates are identical. The only difference is what you're indexing — numbers for arrays, characters for strings. Problems labelled `[String]` in the tables below apply the same pattern to string input.

---

## 👉 Two Pointers

**When to use:** Array or string is sorted, OR you need pairs/triplets summing to a target, OR you need to check/build from both ends (palindromes, reversals). Avoids the O(n²) brute force.

**Trigger keywords:** "sorted array", "pair that sums to", "remove duplicates in-place", "reverse in-place", "palindrome", "two numbers"

**Time:** O(n) &nbsp;&nbsp; **Space:** O(1)

```python
# Template — find pair summing to target in sorted array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1       # need a bigger sum — move left forward
        else:
            right -= 1      # need a smaller sum — move right back

    return []
```

```python
# Write-head variant — remove duplicates / move zeroes in-place
def remove_duplicates(nums):
    write = 1                               # write_head starts at index 1

    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:   # new unique value found
            nums[write] = nums[read]
            write += 1

    return write                            # new length
```

```python
# [String] Palindrome check — same idea, inward from both ends
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():  left  += 1
        while left < right and not s[right].isalnum(): right -= 1
        if s[left].lower() != s[right].lower(): return False
        left += 1; right -= 1
    return True
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|-------------|
| Two Sum II — Input Array Is Sorted | #167 | 🟢 Easy | Classic inward pointer on sorted array |
| Remove Duplicates from Sorted Array | #26 | 🟢 Easy | Left pointer is the write-head |
| Move Zeroes | #283 | 🟢 Easy | Write-head skips over zeroes |
| Valid Palindrome | #125 | 🟢 Easy | `[String]` Skip non-alphanumeric, inward from both ends |
| Reverse String | #344 | 🟢 Easy | `[String]` Classic two-pointer swap in-place |
| 3Sum | #15 | 🟡 Medium | Sort first, fix one element, two-pointer for the rest |
| 3Sum Closest | #16 | 🟡 Medium | Track closest sum seen, minimise absolute difference |
| Container With Most Water | #11 | 🟡 Medium | Always move the shorter side inward |
| Two Sum Less Than K | #1099 | 🟡 Medium | Sort + inward pointers, track best valid sum |
| Trapping Rain Water | #42 | 🔴 Hard | `water = min(left_max, right_max) - height[i]` |

### Common Mistakes

- **Forgetting to sort first.** Two pointers only work on sorted data (except write-head and palindrome variants).
- **Not skipping duplicates in 3Sum.** After finding a valid triplet, advance both pointers and skip while `arr[left] == arr[left-1]`.
- **Moving the wrong pointer.** Always move the pointer on the side that cannot improve the current result.

---

## 🪟 Sliding Window

**When to use:** Find the best, longest, or shortest contiguous subarray or substring satisfying a constraint. Expand the right boundary freely; shrink the left boundary when the constraint breaks.

**Trigger keywords:** "contiguous subarray", "substring", "at most k distinct", "longest without repeating", "minimum size", "permutation in string"

**Time:** O(n) &nbsp;&nbsp; **Space:** O(1) fixed, O(k) variable

```python
# Fixed window — best result over every window of size k
def fixed_window(arr, k):
    window = sum(arr[:k])
    best   = window

    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]      # slide: add new, drop oldest
        best = max(best, window)

    return best
```

```python
# Variable window — expand right, shrink left when constraint breaks
def variable_window(arr):
    left = result = 0
    freq = {}

    for right in range(len(arr)):
        # 1. Expand — add arr[right] to window state
        freq[arr[right]] = freq.get(arr[right], 0) + 1

        # 2. Shrink — while window violates constraint
        while not is_valid(freq):
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            left += 1

        # 3. Record — only after window is valid
        result = max(result, right - left + 1)

    return result
```

```python
# [String] Fixed window — check if s2 contains a permutation of s1
from collections import Counter

def check_inclusion(s1, s2):
    if len(s1) > len(s2): return False
    need   = Counter(s1)
    window = Counter(s2[:len(s1)])

    if window == need: return True
    for i in range(len(s1), len(s2)):
        window[s2[i]] += 1
        old = s2[i - len(s1)]
        window[old] -= 1
        if window[old] == 0: del window[old]
        if window == need: return True
    return False
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|-------------|
| Best Time to Buy and Sell Stock | #121 | 🟢 Easy | Track running min price, record max profit |
| Maximum Average Subarray I | #643 | 🟢 Easy | Fixed window of exactly size k |
| Longest Substring Without Repeating Characters | #3 | 🟡 Medium | `[String]` Shrink left when a duplicate enters the window |
| Minimum Size Subarray Sum | #209 | 🟡 Medium | Shrink when running sum >= target |
| Longest Repeating Character Replacement | #424 | 🟡 Medium | `[String]` Valid when `window_size - max_freq <= k` |
| Permutation in String | #567 | 🟡 Medium | `[String]` Fixed-size window, compare char frequency maps |
| Fruit Into Baskets | #904 | 🟡 Medium | At most 2 distinct values — variable window |
| Minimum Window Substring | #76 | 🔴 Hard | `[String]` Dual freq maps; shrink to find minimum valid window |
| Sliding Window Maximum | #239 | 🔴 Hard | Monotonic deque keeps the max at the front |

### Common Mistakes

- **Using `list.pop(0)` instead of `deque.popleft()`.** The first is O(n), the second is O(1). Always use `deque` for sliding window maximum.
- **Updating result before shrinking.** Always shrink first, then record. An invalid window inflates your answer.
- **Over-shrinking.** Only shrink until the window is valid again — not further.

---

## ➕ Prefix Sum

**When to use:** Answer range sum queries in O(1) after an O(n) build step. Find subarrays summing to a target k using a running sum + hashmap. Works on arrays of numbers — less common for raw strings but applies to character index arrays.

**Trigger keywords:** "range sum", "subarray sum equals k", "sum between indices i and j", "pivot index", "divisible subarray"

**Time:** O(n) build + O(1) query &nbsp;&nbsp; **Space:** O(n)

```python
# Build — prefix[i] = sum of arr[0..i-1], with prefix[0] = 0
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i, val in enumerate(arr):
        prefix[i + 1] = prefix[i] + val
    return prefix

# Range query — sum of arr[l..r] inclusive — O(1)
def range_sum(prefix, l, r):
    return prefix[r + 1] - prefix[l]
```

```python
# Subarray sum equals k — running prefix + hashmap
from collections import defaultdict

def subarray_sum(arr, k):
    count = defaultdict(int)
    count[0] = 1            # CRITICAL — base case: empty prefix has sum 0
    running = result = 0

    for val in arr:
        running += val
        result  += count[running - k]   # complement seen before = valid subarray
        count[running] += 1

    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|-------------|
| Running Sum of 1D Array | #1480 | 🟢 Easy | Textbook prefix sum, built in-place |
| Range Sum Query (Immutable) | #303 | 🟢 Easy | `prefix[r+1] - prefix[l]` |
| Find Pivot Index | #724 | 🟢 Easy | `left_sum == total - left_sum - arr[i]` |
| Subarray Sum Equals K | #560 | 🟡 Medium | Running sum + hashmap, count complements |
| Product of Array Except Self | #238 | 🟡 Medium | Prefix product × suffix product, no division |
| Encode and Decode Strings | #271 | 🟡 Medium | `[String]` Length-prefix each word to encode safely |
| Continuous Subarray Sum | #523 | 🟡 Medium | Prefix mod k + first-seen index hashmap |
| Subarray Sums Divisible by K | #974 | 🟡 Medium | Count matching remainders — `prefix % k` |

### Common Mistakes

- **Off-by-one.** Use `prefix[r+1] - prefix[l]`, not `prefix[r] - prefix[l-1]`. The `+1` offset is what makes range queries clean.
- **Forgetting `count[0] = 1`.** Without this, subarrays starting from index 0 are missed entirely.

---

## 📈 Kadane's Algorithm

**When to use:** Find the maximum (or minimum) sum of a contiguous subarray. At each element, decide whether to extend the current subarray or restart fresh from this element.

**Trigger keywords:** "maximum subarray", "contiguous subarray with largest sum", "max/min product subarray", "turbulent subarray"

**Time:** O(n) &nbsp;&nbsp; **Space:** O(1)

```python
# Standard Kadane's — maximum subarray sum
def max_subarray(arr):
    current = best = arr[0]     # init with arr[0], NOT 0

    for val in arr[1:]:
        current = max(val, current + val)   # extend or restart
        best    = max(best, current)

    return best
```

```python
# Product variant — track both max AND min (negatives flip on multiply)
def max_product(arr):
    hi = lo = best = arr[0]

    for val in arr[1:]:
        hi, lo = max(val, hi*val, lo*val), min(val, hi*val, lo*val)
        best = max(best, hi)

    return best
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|-------------|
| Maximum Subarray | #53 | 🟡 Medium | Reset when `current + val < val` alone |
| Maximum Product Subarray | #152 | 🟡 Medium | Track both max and min — negatives flip |
| Maximum Sum Circular Subarray | #918 | 🟡 Medium | `max(normal_kadane, total - min_subarray)` |
| Longest Turbulent Subarray | #978 | 🟡 Medium | Extend on alternating signs, else reset to 1 |
| Maximum Score from Subarray | #2260 | 🟡 Medium | Kadane variant with an index constraint |

### Common Mistakes

- **Initialising `current = 0` instead of `arr[0]`.** If all elements are negative, the correct answer is the least-negative element — not zero.
- **Forgetting the product variant needs both max and min.** A negative times a negative is positive — the running minimum could flip to the best.

---

## 🗺️ HashMap / Frequency Count

**When to use:** Count element occurrences, detect duplicates, find complement pairs, or group items by a shared property — all in O(1) per lookup. Strings: character frequency is the core tool for anagrams, palindromes, and window matching.

**Trigger keywords:** "two sum", "frequency", "anagram", "duplicate", "complement", "most common", "group by", "first unique", "valid anagram"

**Time:** O(n) &nbsp;&nbsp; **Space:** O(n)

```python
# Complement lookup — Two Sum
def two_sum(nums, target):
    seen = {}                           # value → index

    for i, val in enumerate(nums):
        if target - val in seen:
            return [seen[target - val], i]
        seen[val] = i

    return []
```

```python
from collections import Counter, defaultdict

# Frequency map
freq = Counter(arr)
freq.most_common(k)                     # top-k most frequent elements

# [String] Anagram check
Counter(s1) == Counter(s2)

# Group by transformed key
groups = defaultdict(list)
for word in words:
    groups[tuple(sorted(word))].append(word)    # group anagrams by sorted key
```

```python
# [String] Longest palindromic substring — expand around every centre
def longest_palindrome(s):
    res = ""

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

    for i in range(len(s)):
        res = max(expand(i, i),   res, key=len)   # odd  length
        res = max(expand(i, i+1), res, key=len)   # even length

    return res
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|-------------|
| Two Sum | #1 | 🟢 Easy | Complement lookup — store value → index |
| Contains Duplicate | #217 | 🟢 Easy | Set membership check — O(n) time O(n) space |
| Valid Anagram | #242 | 🟢 Easy | `[String]` `Counter(s) == Counter(t)` |
| Majority Element | #169 | 🟢 Easy | Counter or Boyer-Moore voting algorithm |
| First Unique Character in a String | #387 | 🟢 Easy | `[String]` Counter then scan for first with freq == 1 |
| Top K Frequent Elements | #347 | 🟡 Medium | Counter + min-heap of size k |
| Group Anagrams | #49 | 🟡 Medium | `[String]` `sorted(word)` as the hashmap key |
| Longest Consecutive Sequence | #128 | 🟡 Medium | Set — only start chains at sequence minimum |
| Longest Palindromic Substring | #5 | 🟡 Medium | `[String]` Expand around every centre — odd and even |

### Common Mistakes

- **Using `dict` when `set` is enough.** If you only need to check existence (not store a value), use a set.
- **Not handling the case where complement equals current value.** In Two Sum, the complement must exist at a **different** index.
- **Sorting to check anagrams.** `sorted(s1) == sorted(s2)` works but is O(n log n). `Counter(s1) == Counter(s2)` is O(n) — prefer it.

---

## 🔀 Combined Practice

> These problems require mixing 2 or more patterns. Spend at least 15 minutes on each before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Minimum Window Substring | #76 | 🔴 Hard | Sliding Window + Dual HashMaps `[String]` |
| Subarray Sums Divisible by K | #974 | 🟡 Medium | Prefix Sum + HashMap (mod arithmetic) |
| 4Sum | #18 | 🟡 Medium | Sort + Two Pointer × 2 |
| Minimum Operations to Reduce X to Zero | #1658 | 🟡 Medium | Sliding Window + Prefix Sum |
| Longest Substring with At Most K Distinct | #340 | 🟡 Medium | Sliding Window + HashMap `[String]` |
| Find All Anagrams in a String | #438 | 🟡 Medium | Sliding Window + Frequency Map `[String]` |
| Max Sum of 3 Non-Overlapping Subarrays | #689 | 🔴 Hard | Prefix Sum + Sliding Window + DP |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Arrays & Strings | youtube.com/@NeetCode | Best video per pattern with clean Python |
| LeetCode Explore — Arrays | leetcode.com/explore/learn/card/array-and-string | Official structured problem card |
| LeetCode Explore — Strings | leetcode.com/explore/learn/card/array-and-string | Same card covers both |

---

## 🐍 Python Tips

```python
# ── Array ──────────────────────────────────────────────────────────────
arr[::-1]                               # reverse (returns new list)
arr.sort(key=lambda x: (x[1], -x[0]))  # sort by primary asc, secondary desc
[x for x in arr if x % 2 == 0]         # filter with list comprehension
[x for row in matrix for x in row]     # flatten 2D list
list(zip(*matrix))                      # transpose matrix

# Prefix sum in-place
for i in range(1, len(arr)):
    arr[i] += arr[i - 1]

# ── String ─────────────────────────────────────────────────────────────
s.lower() / s.upper()                   # case conversion
s.isalnum() / s.isdigit() / s.isalpha()# character type checks
s.strip() / s.lstrip() / s.rstrip()    # remove whitespace
s.split() / s.split(",")               # split on whitespace or delimiter
" ".join(words)                         # join list back to string
s[::-1]                                 # reverse a string
s[i:j]                                  # substring / slice

# ── Frequency ──────────────────────────────────────────────────────────
from collections import Counter
freq = Counter(arr)                     # works on list or string
freq.most_common(k)                     # top-k elements
freq['missing'] == 0                    # no KeyError — defaults to 0
Counter(s1) == Counter(s2)              # anagram check in O(n)
```