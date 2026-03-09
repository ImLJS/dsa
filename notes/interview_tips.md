# 🎯 Interview Tips

> What to do when you're in the room (or on the call). The technical skills matter, but this is what separates candidates who pass from those who don't at equal skill levels.

---

## The 5-Minute Framework

Before writing a single line of code, do this every time:

```
1. RESTATE   (30s)  — repeat the problem back in your own words
2. CLARIFY   (1min) — ask the questions below
3. EXAMPLES  (1min) — walk through 1–2 examples by hand
4. APPROACH  (1min) — state pattern + complexity BEFORE coding
5. CODE      (rest) — implement with narration
```

---

## Clarifying Questions (ask these every time)

| Category | Questions to Ask |
|----------|-----------------|
| Input | What is the input type and size range? Can it be empty or null? |
| Values | Can values be negative? Are there duplicates? Are strings ASCII only? |
| Output | Return value, or modify in-place? If multiple valid answers, which to return? |
| Edge cases | What should I return for empty input? Is n=0 a valid input? |
| Constraints | Any memory or time constraints beyond the standard limits? |

> **Don't ask questions you can figure out from the problem.** Only ask when the answer genuinely changes your approach.

---

## Stating Your Approach

Do this before coding. It earns you points even if you don't finish:

```
"I'm going to use a sliding window here. I'll expand the right pointer
freely and shrink the left pointer whenever the constraint breaks.
This gives me O(n) time and O(k) space where k is the window size.

Is that approach okay before I start implementing?"
```

Key elements:
- Name the pattern
- Describe the high-level idea in 1–2 sentences
- State time and space complexity
- Ask if they want you to proceed

---

## While Coding

**Narrate, don't go silent.** Say what you're doing as you do it:
- "I'm initialising two pointers at the start and end..."
- "I'm using a hashmap here to get O(1) lookup..."
- "This while loop shrinks the window when the constraint breaks..."

**Think out loud when stuck:**
- "Let me trace through a small example to see what's happening..."
- "I think the issue is with the boundary condition here..."
- "One approach would be X but that's O(n²). Let me think if there's a better way..."

**Write clean code:**
- Meaningful variable names (`left/right`, not `i/j` for pointers)
- Short comments at non-obvious steps
- Consistent indentation

---

## Testing Your Solution

After coding, always test before declaring done:

1. **Happy path** — the example from the problem statement
2. **Edge cases:**
   - Empty input: `[]`, `""`, `0`
   - Single element: `[1]`, `"a"`
   - Two elements
   - All same values: `[1,1,1,1]`
   - Already sorted / reverse sorted
   - Negative numbers (if applicable)
   - Very large input (check for overflow if relevant)

Say: *"Let me trace through the edge case of an empty array..."*

---

## When You're Stuck

In order:

1. **Re-read the problem** — you may have missed a constraint
2. **Trace a small example by hand** — often reveals the pattern
3. **State what you know:** *"I know the brute force is O(n²). I'm trying to find how to get to O(n)..."*
4. **Ask for a hint:** *"I'm a bit stuck on the transition between states — could I get a nudge?"* This is better than silence
5. **Start with brute force** and optimise: *"Let me get a working solution first and then optimise"*

> Never go silent for more than 60 seconds. Narrating a wrong approach is better than silent paralysis.

---

## Complexity Analysis

Always give both time and space. Be precise:

| Instead of... | Say... |
|--------------|--------|
| "It's fast" | "O(n) time" |
| "It uses some space" | "O(n) extra space for the hashmap" |
| "It's O(n)" | "O(n) time, O(1) space — just two pointers" |
| "It's linear" | "O(n) where n is the length of the input array" |

For recursive solutions, always mention:
- Time complexity of the recurrence
- Space complexity **including the call stack**

---

## Common Mistakes to Avoid

| Mistake | What to do instead |
|---------|-------------------|
| Jumping to code immediately | Always spend 2–3 min clarifying and planning |
| Changing approach mid-code without saying why | Say "I realise this approach has an issue with X, let me pivot to Y" |
| Not testing | Always trace through at least one example after coding |
| Forgetting edge cases | Explicitly list and check them before finishing |
| Over-optimising prematurely | Get a working solution first, then improve |
| Using bad variable names | `left/right`, `fast/slow`, `freq`, `curr` — not `a, b, x, y` |
| `list.pop(0)` in a loop | Always use `deque.popleft()` |
| Off-by-one in binary search | Use `lo + (hi - lo) // 2`, test with 2-element array |

---

## Pattern Recognition in the Room

When you read a problem, look for these signals in order:

```
1. Is it a subarray / substring?
   → Sliding Window or Prefix Sum or Kadane's

2. Is the input sorted, or does sorting help?
   → Binary Search or Two Pointers

3. Does it involve trees or graphs?
   → BFS (shortest) or DFS (all paths / components)

4. Does it ask "how many ways" or "minimum cost"?
   → Dynamic Programming

5. Does it involve intervals, scheduling, or top-k?
   → Heap or Sort + Greedy

6. Does it involve nested structures or next-greater?
   → Stack (Matching or Monotonic)

7. Does it need exhaustive enumeration?
   → Backtracking
```

---

## Behavioural Questions (quick reference)

Keep answers to 2 minutes max using STAR format:
- **S**ituation — brief context
- **T**ask — what you were responsible for
- **A**ction — what you specifically did
- **R**esult — outcome (quantify if possible)

Common questions:
- Tell me about a time you handled a conflict with a teammate
- Tell me about a project you're proud of
- Tell me about a time you failed and what you learned
- Why do you want to work here?
- Tell me about a time you dealt with ambiguity

---

## Final Checklist Before Submitting

```
□ Does my solution handle empty input?
□ Does it handle single-element input?
□ Did I state time and space complexity?
□ Did I trace through the example from the problem?
□ Did I check for edge cases out loud?
□ Are my variable names readable?
□ Is there any obvious optimisation I missed?
```