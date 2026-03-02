# 🟢 Stacks & Queues — Basics

> Warm-up problems that don't require a named pattern. Just understand how the data structure works and simulate directly. Code goes in `problems/misc/`.

---

## What belongs here?

Problems solved by:
- Directly using a stack or queue as the problem describes
- Simple push/pop/peek operations
- No monotonic trick, no expression evaluation, no sliding window needed

---

## Problem List

| Problem | LC # | Difficulty | What It Practices | File |
|---------|------|-----------|------------------|------|
| Baseball Game | #682 | 🟢 Easy | Stack for running score with undo and special ops | `baseball_game.py` |
| Remove All Adjacent Duplicates In String | #1047 | 🟢 Easy | Stack — pop if top equals current char | `remove_adjacent_duplicates.py` |
| Make The String Great | #1544 | 🟢 Easy | Stack — pop if top and current are case opposites | `make_string_great.py` |
| Backspace String Compare | #844 | 🟢 Easy | Stack to simulate backspace `#` character | `backspace_string_compare.py` |
| Number of Students Unable to Eat Lunch | #1700 | 🟢 Easy | Queue simulation — students cycle, sandwiches don't | `students_lunch.py` |
| Time Needed to Buy Tickets | #2073 | 🟢 Easy | Queue simulation — count rounds until target done | `time_to_buy_tickets.py` |
| Implement Stack Using Queues | #225 | 🟢 Easy | Understand stack vs queue behaviour | `stack_using_queues.py` |
| Implement Queue Using Stacks | #232 | 🟢 Easy | Understand amortised cost with two stacks | `queue_using_stacks.py` |

---

## Solution Template

```python
"""
Problem: Baseball Game (#682)
Difficulty: Easy
Link: https://leetcode.com/problems/baseball-game/

Approach:
- Use a stack to track valid scores
- '+' sums top two, 'D' doubles top, 'C' removes top
- Otherwise push int(op) directly

Time:  O(n)
Space: O(n)
"""

def cal_points(operations):
    stack = []

    for op in operations:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(stack[-1] * 2)
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)
```

---

## Python Quick Reference

```python
from collections import deque

# Stack
stack = []
stack.append(x)         # push
stack.pop()             # pop  — O(1)
stack[-1]               # peek — O(1)
not stack               # check empty

# Queue
q = deque()
q.append(x)             # enqueue
q.popleft()             # dequeue — O(1)
q[0]                    # peek front
not q                   # check empty
```