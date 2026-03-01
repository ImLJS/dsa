# 📚 Stacks & Queues

> Stack for LIFO/matching. Queue for BFS/ordering. Monotonic stack for next-greater/smaller problems.

---

## Patterns Overview

| Pattern | When to Use | Key Idea |
|---------|------------|---------|
| [Matching & Validity](#-matching--validity) | Open/close pairs, undo ops | Push on open, verify on close |
| [Monotonic Stack](#-monotonic-stack) | Next greater/smaller, spans | Pop elements that break order |
| [Queue & Deque](#-queue--deque-patterns) | BFS, sliding window max | O(1) access to both ends |

---

## 🔗 Matching & Validity

**When to use:** Matching open/close pairs, undo operations, nested validity checks.

**Trigger keywords:** "valid parentheses", "balanced brackets", "nested", "undo"

```python
# Valid Parentheses
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else '#'
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)

    return not stack

# Min Stack — track minimum alongside values
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []     # stores (value, current_min)

    def push(self, val):
        min_val = min(val, self.min_stack[-1][1] if self.min_stack else val)
        self.stack.append(val)
        self.min_stack.append((val, min_val))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def getMin(self):
        return self.min_stack[-1][1]
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Valid Parentheses | #20 | 🟢 Easy | Push open brackets, pop and match on close |
| Min Stack | #155 | 🟡 Medium | Auxiliary stack tracks the running minimum |
| Basic Calculator II | #227 | 🟡 Medium | Stack for numbers and pending sign |
| Evaluate Reverse Polish Notation | #150 | 🟡 Medium | Pop two operands, push computed result |
| Remove Invalid Parentheses | #301 | 🔴 Hard | BFS on all single-removal variants |

### Common Mistakes
- Not handling empty stack before pop — always check `if stack`
- Forgetting that `stack.pop()` on empty list raises IndexError

---

## 📉 Monotonic Stack

**When to use:** Next greater/smaller element, largest rectangle, stock span. Pop elements that violate the monotonic property.

**Trigger keywords:** "next greater element", "next warmer day", "largest rectangle", "span"

```python
# Next Greater Element — decreasing monotonic stack
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []   # stores indices

    for i, val in enumerate(arr):
        # Pop all elements smaller than current — current is their "next greater"
        while stack and arr[stack[-1]] < val:
            idx = stack.pop()
            result[idx] = val
        stack.append(i)

    return result

# Daily Temperatures variant
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []   # stores indices

    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            idx = stack.pop()
            result[idx] = i - idx    # days waited
        stack.append(i)

    return result

# Largest Rectangle in Histogram
def largest_rectangle(heights):
    stack = []   # stores indices, increasing heights
    max_area = 0
    heights.append(0)   # sentinel to flush remaining elements

    for i, h in enumerate(heights):
        start = i
        while stack and heights[stack[-1]] > h:
            idx = stack.pop()
            width = i - (stack[-1] if stack else -1) - 1
            max_area = max(max_area, heights[idx] * width)
            start = idx
        stack.append(start)

    return max_area
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Daily Temperatures | #739 | 🟡 Medium | Decreasing stack — pop when a warmer day found |
| Next Greater Element I | #496 | 🟢 Easy | Mono stack + hashmap for query lookup |
| Largest Rectangle in Histogram | #84 | 🔴 Hard | Increasing stack — pop on each shorter bar |
| Trapping Rain Water | #42 | 🔴 Hard | Mono stack or two-pointer approach |
| Sum of Subarray Minimums | #907 | 🟡 Medium | Contribution of each element as the minimum |
| Online Stock Span | #901 | 🟡 Medium | Stack stores `(price, span)` pairs |

### Common Mistakes
- Confusing increasing vs decreasing stack direction
- Not handling remaining elements in stack after loop ends
- Forgetting to store indices instead of values (needed for width/distance calc)

---

## 🚶 Queue & Deque Patterns

**When to use:** BFS traversal, sliding window maximum, or O(1) access to both ends of a sequence.

**Trigger keywords:** "BFS", "level order", "sliding window maximum", "design queue"

```python
from collections import deque

# Always use deque, never list for queue operations
# list.pop(0) is O(n) — deque.popleft() is O(1)

dq = deque()
dq.append(x)        # add to right  O(1)
dq.appendleft(x)    # add to left   O(1)
dq.pop()            # remove right  O(1)
dq.popleft()        # remove left   O(1)

# Sliding Window Maximum — monotonic deque
def max_sliding_window(nums, k):
    dq = deque()    # stores indices, decreasing values
    result = []

    for i, num in enumerate(nums):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Maintain decreasing order — pop smaller from right
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])   # front = max

    return result
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Implement Queue Using Stacks | #232 | 🟢 Easy | Two stacks — lazy reversal on dequeue |
| Design Circular Queue | #622 | 🟡 Medium | Array with front/rear modular pointers |
| Sliding Window Maximum | #239 | 🔴 Hard | Monotonic deque: largest element at front |
| LRU Cache | #146 | 🟡 Medium | `OrderedDict` or doubly linked list + HashMap |
| Task Scheduler | #621 | 🟡 Medium | Greedy + max-heap + idle time calculation |

---

## 🔀 Combined Practice

> These problems require mixing 2+ patterns. Spend 15+ minutes before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| Largest Rectangle in Binary Matrix | #85 | 🔴 Hard | Monotonic Stack on each row as histogram |
| Decode String | #394 | 🟡 Medium | Stack for nested `[ ]` bracket structures |
| Asteroid Collision | #735 | 🟡 Medium | Stack — simulate directional collisions |
| Remove K Digits | #402 | 🟡 Medium | Monotonic increasing stack, pop k times |
| 132 Pattern | #456 | 🟡 Medium | Mono stack + track minimum prefix from left |

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

# Stack → use a plain list
stack = []
stack.append(x)     # push
stack.pop()         # pop — O(1)
stack[-1]           # peek

# Queue → always use deque
q = deque()
q.append(x)         # enqueue
q.popleft()         # dequeue — O(1)

# Never do this — O(n)
q = []
q.pop(0)            # ❌ O(n) — use deque instead
```