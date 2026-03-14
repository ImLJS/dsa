# 📝 Notes

> Reference material, cheatsheets, and study documents. Nothing to run — everything to read.
>
> Keep this folder open alongside your coding environment during practice sessions.

---

## Files

| File | Description |
|------|-------------|
| [`DSA_Interview_Prep.pdf`](#dsa-interview-prep) | Main study guide — all topics, patterns, code templates, problems, appendices |
| [`pattern_cheatsheet.md`](#pattern_cheatsheetmd) | Keyword → pattern lookup + decision flowchart + tricky overlaps |
| [`complexity_reference.md`](#complexity_referencemd) | Time & space for every data structure and algorithm |
| [`python_builtins.md`](#python_builtinsmd) | Counter, deque, heapq, bisect, lru_cache + all algorithm templates |
| [`study_plan.md`](#study_planmd) | 8-week structured preparation schedule with daily problem lists |
| [`interview_tips.md`](#interview_tipsmd) | What to do in the room — framework, edge cases, when stuck |

---

## DSA_Interview_Prep.pdf

The main study PDF. Generated from `dsa_v4.py` using ReportLab raw canvas.

**Structure:**
- Cover page — all 14 topics at a glance
- Per topic: intro page (pattern overview, quick-pick guide, difficulty breakdown) → one page per pattern
- Per pattern: When to Use · How to Solve · Code Template · Practice Problems · Common Mistakes
- Per topic: Resources · Combined Practice problems

**Appendices:**
- Appendix A — Pattern Recognition Cheatsheet (keyword → pattern, complexity by input size)
- Appendix B — Python Built-ins & Templates (Counter, deque, heapq, bisect, BFS, DSU, Trie, Backtracking, Monotonic Stack, lru_cache)
- Appendix C — Time & Space Complexity Reference (19 algorithms + Big-O rules)

**Topics covered (14):**
Arrays & Strings · Binary Search · Sorting · Stacks & Queues · Linked Lists · Trees · Graphs · Dynamic Programming · Tries · Heaps · Backtracking · Bit Manipulation · Math & Number Theory · Intervals

---

## pattern_cheatsheet.md

One-page quick reference for pattern identification. Use this when you read a problem and aren't sure which pattern applies.

**Contains:**
- Keyword → Pattern table organised by topic (Arrays, Binary Search, Stacks, Linked Lists, Trees, Graphs, DP, and more)
- Complexity Signal Table — which complexity you need based on input size
- Decision Flowchart — step-by-step pattern selection
- Tricky Overlaps — Prefix Sum vs Sliding Window, BFS vs DFS, HashMap vs Two Pointers, etc.

**When to use:** Open this before starting a new problem. Scan for keywords from the problem statement.

---

## complexity_reference.md

Full complexity reference for every data structure, algorithm, and Python operation.

**Contains:**
- Input size → max complexity table (with rule of thumb for LeetCode TLE)
- Data structures — access, search, insert, delete, space
- Sorting algorithms — best, average, worst, space, stable?
- Algorithm complexity by pattern: Arrays, Searching, Graph & Tree, DP, Heaps, String
- Python-specific costs — the ones that surprise people (`list.pop(0)` is O(n), etc.)
- Big-O simplification rules
- Space complexity notes by pattern

**When to use:** After writing a solution, verify your stated complexity is accurate here.

---

## python_builtins.md

Everything Python-specific you need for DSA interviews — with code you can run.

**Contains:**
- `collections.Counter` — all methods, anagram check, most_common
- `collections.defaultdict` — adjacency list, frequency map, grouping
- `collections.deque` — all O(1) operations, maxlen, rotate
- `heapq` — push, pop, heapify, nlargest, max-heap trick, k-way merge
- `bisect` — bisect_left/right, insort, LIS with patience sort
- `functools.lru_cache` — memoisation, cache_clear, `@cache`
- Sorting — all key patterns, stable sort, sort by multiple keys
- `itertools` — combinations, permutations, product, accumulate
- String methods — every DSA-relevant method
- Full templates: Binary Search, BFS, Union-Find, Trie, Backtracking (subsets + permutations), Dijkstra, Monotonic Stack

**When to use:** When implementing a solution and you can't remember exact syntax.

---

## study_plan.md

8-week preparation schedule with specific problems assigned to each day.

**Structure:**
- Week 1: Arrays & Strings (foundation — most important week)
- Week 2: Binary Search & Sorting
- Week 3: Stacks, Queues & Linked Lists
- Week 4: Trees
- Week 5: Graphs
- Week 6: Dynamic Programming (hardest — allow extra time)
- Week 7: Heaps, Tries, Backtracking, Intervals, Bit Manipulation
- Week 8: Review & Mock Interviews

**Also includes:**
- Daily practice template (log problem, time taken, complexity, notes)
- Difficulty progression framework (Easy → Medium → Hard per pattern)
- Red flags to watch for during practice

**When to use:** At the start of each week to plan what to work on.

---

## interview_tips.md

Practical advice for performing well during the actual interview, not just during practice.

**Contains:**
- 5-minute framework: Restate → Clarify → Examples → Approach → Code
- Clarifying questions to ask (and which to skip)
- How to state your approach before coding
- What to narrate while coding
- Testing checklist — happy path + 6 categories of edge cases
- What to do when stuck (in order, including when to ask for a hint)
- How to state complexity precisely
- Common mistakes table (what to avoid + what to do instead)
- Pattern recognition quick guide for the room
- Behavioural questions STAR format
- Final submission checklist

**When to use:** Read this the night before an interview and once more the morning of.

---

## Quick Reference Card

> Print this or keep it on a second monitor during practice.

```
PATTERN SIGNALS
───────────────────────────────────────────────────
Sorted + find pair           → Two Pointers
Contiguous subarray          → Sliding Window / Kadane's
Subarray sum = k             → Prefix Sum + HashMap
Sorted + find value          → Binary Search
Min/max feasible value       → Binary Search on Answer
Shortest path (unweighted)   → BFS
All paths / components       → DFS
Dependencies / ordering      → Topological Sort
How many ways / min cost     → Dynamic Programming
Brackets / next-greater      → Stack
Top-k / streaming median     → Heap
Word prefix / autocomplete   → Trie
All subsets / permutations   → Backtracking
Overlapping intervals        → Sort + Greedy
XOR / missing number         → Bit Manipulation

COMPLEXITY TARGETS
───────────────────────────────────────────────────
n ≤ 20         →  O(2ⁿ) or O(n!)
n ≤ 100        →  O(n³)
n ≤ 1,000      →  O(n²)
n ≤ 100,000    →  O(n log n)
n ≤ 1,000,000  →  O(n)
n > 10,000,000 →  O(log n) or O(1)

PYTHON GOTCHAS
───────────────────────────────────────────────────
list.pop(0)     → O(n) ❌   use deque.popleft() O(1) ✅
list.insert(0)  → O(n) ❌   use deque.appendleft() O(1) ✅
x in list       → O(n) ❌   use set/dict for O(1) ✅
str concat loop → O(n²) ❌  use "".join(list) O(n) ✅
```