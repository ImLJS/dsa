# 🧠 Dynamic Programming

> Overlapping subproblems + optimal substructure. Always draw the table before you write code.

---

## Patterns Overview

| Pattern | When to Use | Key Idea |
|---------|------------|---------|
| [1D DP](#1️⃣-1d-dp--linear-sequence) | dp[i] depends on prev 1-2 states | Fibonacci-style transitions |
| [2D DP](#-2d-dp--grids--string-pairs) | Two sequences or a grid | `dp[i][j]` from left, up, or diagonal |
| [Knapsack Variants](#-knapsack-variants) | Pick items with constraints | 0/1 = use once, Unbounded = reuse |
| [Interval DP & Subsequences](#-interval-dp--subsequences) | Optimal over subrange [i..j] | Split point k between i and j |

---

## How to Approach Any DP Problem

```
1. Define state   → what does dp[i] or dp[i][j] represent?
2. Base case      → smallest valid input
3. Transition     → how do we get dp[i] from previous states?
4. Answer         → where is the final answer in the table?
5. Optimise       → can we reduce space? (often 1D → rolling variable)
```

---

## 1️⃣ 1D DP — Linear Sequence

**When to use:** `dp[i]` depends on a fixed number of previous states. Classic examples: Fibonacci, House Robber, Coin Change.

**Trigger keywords:** "minimum steps/coins", "number of ways", "rob/skip elements", "decode"

```python
# House Robber
def rob(nums):
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]

# Space optimised to O(1)
def rob_optimised(nums):
    prev2, prev1 = 0, 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1

# Coin Change — minimum coins
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Coin Change II — count ways (unbounded knapsack)
def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:           # outer loop = items
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Climbing Stairs | #70 | 🟢 Easy | `dp[i] = dp[i−1] + dp[i−2]` |
| House Robber | #198 | 🟡 Medium | `dp[i] = max(dp[i−1], dp[i−2] + val)` |
| House Robber II — circular | #213 | 🟡 Medium | Run 1D DP twice: `[0..n−2]` and `[1..n−1]` |
| Decode Ways | #91 | 🟡 Medium | Transitions for 1-digit and 2-digit substrings |
| Coin Change | #322 | 🟡 Medium | `dp[amount] = min(dp[amount − coin] + 1)` |
| Coin Change II — count ways | #518 | 🟡 Medium | Unbounded knapsack — count combinations |
| Word Break | #139 | 🟡 Medium | `dp[i] = True` if any `dp[j]` and `word[j:i]` in set |

---

## 📐 2D DP — Grids & String Pairs

**When to use:** Two sequences or a grid. `dp[i][j]` typically comes from `dp[i-1][j]`, `dp[i][j-1]`, or `dp[i-1][j-1]`.

**Trigger keywords:** "longest common subsequence", "edit distance", "unique paths", "minimum path sum"

```python
# Longest Common Subsequence
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1    # characters match
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])   # skip one

    return dp[m][n]

# Edit Distance
def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1): dp[i][0] = i   # delete all of word1
    for j in range(n + 1): dp[0][j] = j   # insert all of word2

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]   # no operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],     # delete from word1
                    dp[i][j-1],     # insert into word1
                    dp[i-1][j-1]    # replace
                )
    return dp[m][n]

# Unique Paths
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Unique Paths | #62 | 🟡 Medium | `dp[i][j] = dp[i−1][j] + dp[i][j−1]` |
| Minimum Path Sum | #64 | 🟡 Medium | `dp[i][j] = min(up, left) + grid[i][j]` |
| Longest Common Subsequence | #1143 | 🟡 Medium | Match → +1, else `max(skip row, skip col)` |
| Edit Distance | #72 | 🔴 Hard | Insert / delete / replace cost transitions |
| Maximal Square | #221 | 🟡 Medium | `dp[i][j] = min(left, up, diagonal) + 1` if `'1'` |

---

## 🎒 Knapsack Variants

**When to use:** Choose items within constraints. 0/1 = use each item once. Unbounded = reuse items freely.

**Trigger keywords:** "partition", "target sum", "subset sum", "knapsack", "can we reach"

```python
# 0/1 Knapsack — Partition Equal Subset Sum
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2

    dp = {0}   # set of achievable sums
    for num in nums:
        dp = dp | {s + num for s in dp}  # add num to all existing sums
        if target in dp:
            return True
    return target in dp

# Alternative — 1D boolean array
def can_partition_arr(nums):
    target = sum(nums) // 2
    if sum(nums) % 2 != 0: return False

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):  # iterate backwards for 0/1
            dp[j] = dp[j] or dp[j - num]

    return dp[target]
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Partition Equal Subset Sum | #416 | 🟡 Medium | 0/1 Knapsack — can we reach `target = sum/2`? |
| Target Sum | #494 | 🟡 Medium | Assign + or − to each number, count ways |
| Last Stone Weight II | #1049 | 🟡 Medium | Partition into two groups, minimise difference |
| Ones and Zeroes | #474 | 🟡 Medium | 2D knapsack on (count of 0s, count of 1s) |

> **Key difference — iteration order:**
> - **0/1 Knapsack** (use each item once): iterate `j` **backwards** `range(target, num-1, -1)`
> - **Unbounded Knapsack** (reuse items): iterate `j` **forwards** `range(num, target+1)`

---

## 📏 Interval DP & Subsequences

**When to use:** Optimal value over a subrange `[i..j]`, or longest/counted subsequence problems.

**Trigger keywords:** "burst balloons", "minimum cost to split", "longest palindromic subsequence", "LIS"

```python
# Longest Increasing Subsequence — O(n²) DP
def length_of_lis(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# LIS — O(n log n) with bisect (patience sort)
import bisect
def length_of_lis_fast(nums):
    tails = []
    for n in nums:
        idx = bisect.bisect_left(tails, n)
        if idx == len(tails):
            tails.append(n)
        else:
            tails[idx] = n
    return len(tails)

# Burst Balloons — interval DP
def max_coins(nums):
    nums = [1] + nums + [1]   # padding
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for k in range(left + 1, right):  # k = last balloon to burst in [left, right]
                dp[left][right] = max(
                    dp[left][right],
                    nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right]
                )
    return dp[0][n-1]
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Longest Increasing Subsequence | #300 | 🟡 Medium | O(n log n) patience sort with `bisect_left` |
| Longest Palindromic Substring | #5 | 🟡 Medium | `dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]` |
| Palindromic Substrings — count | #647 | 🟡 Medium | Expand around centre, count all valid |
| Burst Balloons | #312 | 🔴 Hard | `dp[i][j]` = max coins, k = last balloon popped |

---

## 🔀 Combined Practice

> These problems require mixing 2+ patterns. Spend 15+ minutes before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Maximum Profit in Job Scheduling | #1235 | 🔴 Hard | DP + Binary Search on start times |
| Wildcard Matching | #44 | 🔴 Hard | 2D DP with `?` and `*` transitions |
| Paint House III | #1473 | 🔴 Hard | 3D DP: house × color × neighbourhood |
| Minimum Cost to Cut a Stick | #1547 | 🔴 Hard | Interval DP |
| Largest Divisible Subset | #368 | 🟡 Medium | LIS variant with divisibility constraint |
| Minimum Number of Refueling Stops | #871 | 🔴 Hard | DP or Greedy + Max-Heap |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode DP Playlist | youtube.com/@NeetCode | Best video series — intro to advanced DP |
| Striver DP Series (50 problems) | takeuforward.org | Most comprehensive DP problem coverage |
| LeetCode DP Study Plan | leetcode.com/study-plan/dynamic-programming | Curated Easy → Hard progression |
| MIT 6.006 Lectures 19–22 | ocw.mit.edu | Rigorous DP theory |

---

## 🐍 Python Tips

```python
import functools

# Top-down memoisation with lru_cache
@functools.lru_cache(None)
def dp(i, j):
    # base case
    if i > j: return 0
    # recursive case
    return min(dp(i, k) + dp(k+1, j) for k in range(i, j+1))

# Clear cache between test cases if needed
dp.cache_clear()

# 2D DP table initialisation
dp = [[0] * (n+1) for _ in range(m+1)]

# Space optimisation — rolling array
# If dp[i][j] only needs row i-1, use two 1D arrays
prev = [0] * (n + 1)
curr = [0] * (n + 1)
# After each row: prev = curr[:]
```