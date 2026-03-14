# 🔙 Backtracking

> DFS with an undo step. Explore a path, and if it doesn't lead to a solution, undo the last choice and try the next option. The template is almost always the same — learn it once, apply everywhere.

---

## Patterns Overview

| Pattern | When to Use |
|---------|------------|
| [Subsets](#-subsets) | All possible subsets / power set |
| [Combinations](#-combinations) | Choose K items from N, with constraints |
| [Permutations](#-permutations) | All orderings of elements |
| [Decision / Constraint Problems](#-decision--constraint-problems) | Sudoku, N-Queens, valid placements |
| [Word / Path Search](#-word--path-search) | Paths in a grid or string construction |

---

## The Universal Backtracking Template

```python
def backtrack(state, choices):
    # 1. Base case — found a valid solution
    if is_solution(state):
        result.append(list(state))   # always copy!
        return

    for choice in choices:
        # 2. Check if this choice is valid
        if not is_valid(choice, state):
            continue

        # 3. Make the choice
        state.append(choice)
        mark_used(choice)

        # 4. Recurse
        backtrack(state, remaining_choices)

        # 5. Undo the choice (backtrack)
        state.pop()
        unmark_used(choice)
```

> **The golden rule:** Whatever you do before the recursive call, undo it after.

---

## 🧩 Subsets

**When to use:** Generate all possible subsets (power set) of a list.

**Trigger keywords:** "all subsets", "power set", "all combinations", "include or exclude"

```python
# Subsets — include or exclude each element
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(list(current))    # every state is a valid subset
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result


# Subsets II — with duplicates, no duplicate subsets
def subsets_with_dup(nums):
    result = []
    nums.sort()    # must sort first

    def backtrack(start, current):
        result.append(list(current))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue    # skip duplicate at same level
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Subsets | #78 | 🟡 Medium | Add current state at every node, not just leaves |
| Subsets II | #90 | 🟡 Medium | Sort + skip `nums[i] == nums[i-1]` at same level |

---

## 🔢 Combinations

**When to use:** Choose K elements from N. May allow reuse (unbounded) or not (0/1).

**Trigger keywords:** "combinations", "choose K", "sum equals target", "factor combinations"

```python
# Combinations — choose K from 1..n
def combine(n, k):
    result = []

    def backtrack(start, current):
        if len(current) == k:
            result.append(list(current))
            return
        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    backtrack(1, [])
    return result


# Combination Sum — reuse elements, sum to target
def combination_sum(candidates, target):
    result = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(list(current))
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])   # i not i+1 = reuse allowed
            current.pop()

    backtrack(0, [], target)
    return result


# Combination Sum II — no reuse, no duplicate combos
def combination_sum_2(candidates, target):
    result = []
    candidates.sort()

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(list(current))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break    # pruning — sorted so no point continuing
            if i > start and candidates[i] == candidates[i-1]:
                continue    # skip duplicates at same level
            current.append(candidates[i])
            backtrack(i + 1, current, remaining - candidates[i])
            current.pop()

    backtrack(0, [], target)
    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Combinations | #77 | 🟡 Medium | Choose K from 1..n, no reuse |
| Combination Sum | #39 | 🟡 Medium | Reuse allowed — pass `i` not `i+1` |
| Combination Sum II | #40 | 🟡 Medium | No reuse + skip duplicates at same level |
| Combination Sum III | #216 | 🟡 Medium | Choose K numbers 1–9 that sum to n |

---

## 🔄 Permutations

**When to use:** All orderings of a set of elements.

**Trigger keywords:** "all permutations", "all arrangements", "next permutation"

```python
# Permutations — distinct elements
def permute(nums):
    result = []

    def backtrack(current, remaining):
        if not remaining:
            result.append(list(current))
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()

    backtrack([], nums)
    return result


# Permutations — using visited array (more efficient)
def permute_visited(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == len(nums):
            result.append(list(current))
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False

    backtrack([])
    return result


# Permutations II — with duplicates
def permute_unique(nums):
    result = []
    nums.sort()
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == len(nums):
            result.append(list(current))
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue    # skip duplicate permutations
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False

    backtrack([])
    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Permutations | #46 | 🟡 Medium | Use visited array, try each unused element |
| Permutations II | #47 | 🟡 Medium | Sort + skip `nums[i]==nums[i-1] and not used[i-1]` |
| Letter Combinations of Phone Number | #17 | 🟡 Medium | Map digits to chars, backtrack each position |

---

## 👑 Decision / Constraint Problems

**When to use:** Place elements on a board or in slots subject to constraints. Prune early when a placement violates rules.

**Trigger keywords:** "N-queens", "sudoku", "place without conflict", "valid configuration"

```python
# N-Queens
def solve_n_queens(n):
    result = []
    cols    = set()
    pos_dia = set()   # r + c
    neg_dia = set()   # r - c

    board = [['.'] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row+col) in pos_dia or (row-col) in neg_dia:
                continue    # conflicts — prune
            cols.add(col); pos_dia.add(row+col); neg_dia.add(row-col)
            board[row][col] = 'Q'
            backtrack(row + 1)
            cols.remove(col); pos_dia.remove(row+col); neg_dia.remove(row-col)
            board[row][col] = '.'

    backtrack(0)
    return result


# Sudoku Solver
def solve_sudoku(board):
    def is_valid(row, col, num):
        box_row, box_col = 3*(row//3), 3*(col//3)
        for i in range(9):
            if board[row][i] == num: return False
            if board[i][col] == num: return False
            if board[box_row + i//3][box_col + i%3] == num: return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in '123456789':
                        if is_valid(r, c, num):
                            board[r][c] = num
                            if backtrack(): return True
                            board[r][c] = '.'
                    return False    # no valid number — backtrack
        return True    # all cells filled

    backtrack()
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| N-Queens | #51 | 🔴 Hard | Track cols + two diagonal sets for O(1) conflict check |
| N-Queens II — count solutions | #52 | 🔴 Hard | Same as above, count instead of store |
| Sudoku Solver | #37 | 🔴 Hard | Try 1-9 at each empty cell, validate 3 constraints |
| Palindrome Partitioning | #131 | 🟡 Medium | Backtrack + check if current slice is palindrome |

---

## 🔤 Word / Path Search

**When to use:** Construct words from characters, or find paths in a grid.

```python
# Word Break II — all sentences
def word_break(s, word_dict):
    word_set = set(word_dict)
    result   = []

    def backtrack(start, current):
        if start == len(s):
            result.append(' '.join(current))
            return
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                current.append(word)
                backtrack(end, current)
                current.pop()

    backtrack(0, [])
    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Word Search | #79 | 🟡 Medium | DFS on grid, mark visited, restore on backtrack |
| Generate Parentheses | #22 | 🟡 Medium | Track open/close counts — only add when valid |
| Word Break II | #140 | 🔴 Hard | Backtrack + memoisation |
| Restore IP Addresses | #93 | 🟡 Medium | 4 segments, each 0-255, no leading zeros |

---

## Combined Practice

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Word Search II | #212 | 🔴 Hard | Backtracking + Trie |
| Expression Add Operators | #282 | 🔴 Hard | Backtracking + Math |
| Remove Invalid Parentheses | #301 | 🔴 Hard | Backtracking + BFS |
| Partition to K Equal Sum Subsets | #698 | 🟡 Medium | Backtracking + pruning |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Backtracking Playlist | youtube.com/@NeetCode | Best visual of the decision tree |
| LeetCode Backtracking Pattern | leetcode.com/tag/backtracking | All tagged problems |

---

## 🐍 Pruning Tips

```python
# 1. Sort first — enables early termination
candidates.sort()
if candidates[i] > remaining: break   # no point continuing

# 2. Skip duplicates at the same tree level
if i > start and nums[i] == nums[i-1]: continue

# 3. Prune when current path can't possibly lead to a solution
if len(current) + len(remaining) < k: return   # can't fill K slots

# 4. Always copy when adding to result
result.append(list(current))       # not result.append(current)
result.append(current[:])          # same thing
```