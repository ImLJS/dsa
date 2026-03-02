# 📚 Stacks & Queues

> Stack for LIFO and matching problems. Monotonic stack for next-greater/smaller in O(n). Queue and deque for BFS and sliding window maximum. These two data structures are kept together because they share patterns — the monotonic stack uses a deque, and sliding window maximum uses both ideas at once.

---

## Folder Structure

```
stacks_queues/
├── README.md              ← you are here
├── basics.md              ← warm-up problems, no named pattern needed
├── my_solutions.md        ← your personal progress log
└── problems/
    ├── misc/              ← problems that don't fit a named pattern
    ├── matching/          ← brackets, validity, expression evaluation
    ├── monotonic_stack/   ← next greater/smaller, histogram, span
    └── queue_deque/       ← BFS-adjacent, sliding window max, design
```

---

## Patterns Overview

| Pattern | When to Use | Trigger Keywords |
|---------|------------|-----------------|
| [Matching & Validity](#-matching--validity) | Open/close pairs, undo, nested structures | "valid parentheses", "balanced", "nested", "evaluate expression" |
| [Monotonic Stack](#-monotonic-stack) | Next greater/smaller, largest rectangle, span | "next greater", "next warmer", "largest rectangle", "stock span" |
| [Queue & Deque](#-queue--deque) | Sliding window max, design queue, BFS helpers | "sliding window maximum", "design queue", "first in first out" |

> **Note on BFS:** Full BFS problems (graphs, trees, grids) live in their own topic folders. The queue/deque pattern here covers problems where the deque itself is the trick — sliding window maximum, circular queue design, etc.

---

## 🔗 Matching & Validity

**When to use:** Any problem involving open/close pairs, nested brackets, or expression evaluation where you need to remember what came before. Push on open, pop and verify on close.

**Trigger keywords:** "valid parentheses", "balanced brackets", "nested structure", "evaluate expression", "undo"

**Time:** O(n) &nbsp;&nbsp; **Space:** O(n)

```python
# Template — valid brackets
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:                       # closing bracket
            top = stack.pop() if stack else '#'
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)                    # opening bracket

    return not stack                            # valid if nothing left unmatched
```

```python
# Min Stack — O(1) getMin at all times
class MinStack:
    def __init__(self):
        self.stack     = []
        self.min_stack = []     # tracks running minimum alongside each value

    def push(self, val):
        self.stack.append(val)
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

```python
# Evaluate Reverse Polish Notation
def eval_rpn(tokens):
    stack = []
    ops   = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),   # int() truncates toward zero
    }

    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()     # b is top, a is below
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))

    return stack[0]
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Valid Parentheses | #20 | 🟢 Easy | Push open brackets, pop and match on close |
| Min Stack | #155 | 🟡 Medium | Parallel min_stack tracks running minimum |
| Evaluate Reverse Polish Notation | #150 | 🟡 Medium | Pop two operands, push result |
| Basic Calculator II | #227 | 🟡 Medium | Stack holds numbers, apply sign on + and − |
| Basic Calculator | #224 | 🔴 Hard | Stack holds running sum and sign on `(` |
| Remove Invalid Parentheses | #301 | 🔴 Hard | BFS on all single-removal variants |

### Common Mistakes

- **Popping from an empty stack.** Always check `if stack` before `stack.pop()`, or use a sentinel like `'#'`.
- **Wrong operand order in RPN.** `b, a = stack.pop(), stack.pop()` — the second pop gives the left operand.
- **Not clearing the stack check at the end.** `return not stack` — a leftover open bracket means invalid.

---

## 📉 Monotonic Stack

**When to use:** Find the next greater or smaller element for every position in O(n). The stack maintains a monotonic order — elements that can never be an answer get popped as soon as a better candidate is found.

**Trigger keywords:** "next greater element", "next warmer day", "previous smaller", "largest rectangle", "stock span"

**Time:** O(n) — each element is pushed and popped at most once &nbsp;&nbsp; **Space:** O(n)

```python
# Next Greater Element — decreasing monotonic stack
def next_greater(arr):
    n      = len(arr)
    result = [-1] * n
    stack  = []             # stores indices

    for i in range(n):
        # Pop everything smaller than arr[i] — arr[i] is their next greater
        while stack and arr[stack[-1]] < arr[i]:
            idx         = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result           # remaining indices in stack have no next greater → -1
```

```python
# Previous Smaller Element — increasing monotonic stack
def prev_smaller(arr):
    result = [-1] * len(arr)
    stack  = []             # stores indices

    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        result[i] = arr[stack[-1]] if stack else -1
        stack.append(i)

    return result
```

```python
# Largest Rectangle in Histogram
def largest_rectangle(heights):
    stack    = []           # increasing stack of indices
    max_area = 0
    heights  = heights + [0]    # sentinel 0 flushes all remaining bars at the end

    for i, h in enumerate(heights):
        start = i
        while stack and heights[stack[-1]] > h:
            idx      = stack.pop()
            width    = i - (stack[-1] + 1 if stack else 0)
            max_area = max(max_area, heights[idx] * width)
            start    = idx          # extend start left to where we popped from
        stack.append(start)

    return max_area
```

### How to decide increasing vs decreasing

| Goal | Stack order | Pop when |
|------|-------------|---------|
| Next **greater** element | Decreasing | `arr[stack[-1]] < current` |
| Next **smaller** element | Increasing | `arr[stack[-1]] > current` |
| Previous **smaller** element | Increasing | pop until stack top < current |
| Largest rectangle | Increasing | `heights[stack[-1]] > current` |

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Next Greater Element I | #496 | 🟢 Easy | Mono stack + hashmap for query lookup |
| Daily Temperatures | #739 | 🟡 Medium | Decreasing stack — record `i - idx` when popping |
| Online Stock Span | #901 | 🟡 Medium | Stack stores `(price, span)` — accumulate span |
| Sum of Subarray Minimums | #907 | 🟡 Medium | Each element's contribution as subarray minimum |
| Next Greater Element II | #503 | 🟡 Medium | Circular array — iterate twice, use `i % n` |
| Remove K Digits | #402 | 🟡 Medium | Increasing stack — pop larger digits greedily |
| Largest Rectangle in Histogram | #84 | 🔴 Hard | Increasing stack — pop on each shorter bar |
| Trapping Rain Water | #42 | 🔴 Hard | Mono stack or two-pointer — water = min boundary - height |

### Common Mistakes

- **Storing values instead of indices.** Most problems need the index to compute width or distance — always push `i`, not `arr[i]`.
- **Forgetting remaining elements after the loop.** Elements still in the stack after iterating have no next greater/smaller. Handle them or use a sentinel.
- **Wrong stack direction.** Decreasing stack for next-greater, increasing for next-smaller — mixing these up gives wrong answers.

---

## 🚶 Queue & Deque

**When to use:** Sliding window maximum (monotonic deque), designing a queue from stacks, or any problem requiring O(1) access to both the front and back of a sequence.

**Trigger keywords:** "sliding window maximum", "design queue using stacks", "first in first out", "circular queue"

**Time:** O(n) &nbsp;&nbsp; **Space:** O(k) for window size k

```python
from collections import deque

# deque basics — O(1) at both ends
dq = deque()
dq.append(x)        # add to right
dq.appendleft(x)    # add to left
dq.pop()            # remove from right
dq.popleft()        # remove from left
dq[0]               # peek front
dq[-1]              # peek back
```

```python
# Sliding Window Maximum — monotonic decreasing deque of indices
def max_sliding_window(nums, k):
    dq     = deque()    # stores indices, values are decreasing
    result = []

    for i, num in enumerate(nums):
        # 1. Remove indices that have fallen outside the window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # 2. Remove indices whose values are smaller than current
        #    (they can never be the max while current is in the window)
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # 3. Window is full — record the max (front of deque)
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

```python
# Implement Queue Using Two Stacks
class MyQueue:
    def __init__(self):
        self.inbox  = []    # new items always go here
        self.outbox = []    # dequeue from here — refill lazily

    def push(self, x):
        self.inbox.append(x)

    def pop(self):
        self._refill()
        return self.outbox.pop()

    def peek(self):
        self._refill()
        return self.outbox[-1]

    def empty(self):
        return not self.inbox and not self.outbox

    def _refill(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Implement Queue Using Stacks | #232 | 🟢 Easy | Two stacks — lazy refill on dequeue |
| Implement Stack Using Queues | #225 | 🟢 Easy | Push to back, rotate so new element is at front |
| Design Circular Queue | #622 | 🟡 Medium | Array with front/rear modular pointers |
| Sliding Window Maximum | #239 | 🔴 Hard | Monotonic deque — largest index at front |
| LRU Cache | #146 | 🟡 Medium | OrderedDict or doubly linked list + HashMap |

### Common Mistakes

- **Using `list.pop(0)` instead of `deque.popleft()`.** `list.pop(0)` is O(n) — it shifts every element. `deque.popleft()` is O(1). Always use deque for queue operations.
- **Not checking `dq[0] < i - k + 1` before removing.** The window expiry check must come before the monotonic order check.

---

## 🔀 Combined Practice

> These problems require mixing 2 or more patterns. Spend at least 15 minutes before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Largest Rectangle in Binary Matrix | #85 | 🔴 Hard | Monotonic Stack on each row treated as histogram |
| Decode String | #394 | 🟡 Medium | Matching Stack — handle nested `[ ]` structures |
| Asteroid Collision | #735 | 🟡 Medium | Stack — simulate directional collision rules |
| 132 Pattern | #456 | 🟡 Medium | Monotonic Stack + track running minimum prefix |
| Maximum Frequency Stack | #895 | 🔴 Hard | Stack + HashMap frequency grouping |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Stack Playlist | youtube.com/@NeetCode | Monotonic stack patterns with clean code |
| LeetCode Explore — Queue & Stack | leetcode.com/explore/learn/card/queue-stack | Official structured card |
| VisuAlgo Stack / Queue | visualgo.net/en/list | Animated push/pop/enqueue operations |
| Python deque docs | docs.python.org/3/library/collections.html | All deque methods and time complexities |

---

## 🐍 Python Tips

```python
from collections import deque

# Stack — use a plain list
stack = []
stack.append(x)     # push   O(1)
stack.pop()         # pop    O(1)
stack[-1]           # peek   O(1)

# Queue — always use deque, never list
q = deque()
q.append(x)         # enqueue  O(1)
q.popleft()         # dequeue  O(1)
q[0]                # peek     O(1)

# ❌ Never do this — O(n) for every dequeue
bad_queue = []
bad_queue.pop(0)

# deque with max size — auto-evicts oldest item
dq = deque(maxlen=k)

# Initialise deque from a list
dq = deque([1, 2, 3])

# Rotate — move last element to front
dq.rotate(1)
```