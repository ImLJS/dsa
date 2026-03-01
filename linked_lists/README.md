# 🔗 Linked Lists

> All about pointer manipulation. Most patterns use two pointers: fast/slow or prev/curr/next.

---

## Patterns Overview

| Pattern | When to Use | Key Idea |
|---------|------------|---------|
| [Fast & Slow Pointers](#-fast--slow-pointers-floyds) | Cycle, middle, Kth from end | Fast moves 2×, slow moves 1× |
| [Reversal](#-reversal-patterns) | Reverse list, sublist, k-groups | Track prev, curr, next_node |
| [Merge & Sort](#-merge--sort) | Combining/sorting lists | Compare heads, attach smaller |
| [HashMap on Linked Lists](#-hashmap-on-linked-lists) | Clone, intersection, visited | Old node → new node mapping |

---

## Node Definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## ⚡ Fast & Slow Pointers (Floyd's)

**When to use:** Cycle detection, finding the middle node, or Kth from end. Fast pointer moves at 2× speed.

**Trigger keywords:** "cycle", "middle of list", "nth from end", "detect loop"

```python
# Find middle of linked list
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow   # slow is at middle

# Detect cycle
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Find cycle start (Floyd's)
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Reset one pointer to head, advance both 1× to find start
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Linked List Cycle | #141 | 🟢 Easy | Fast and slow meet → cycle exists |
| Linked List Cycle II | #142 | 🟡 Medium | Reset one pointer to head, advance 1× to find start |
| Middle of the Linked List | #876 | 🟢 Easy | Slow is at mid when fast reaches end |
| Happy Number | #202 | 🟢 Easy | Same Floyd's pattern on digit sequences |
| Find the Duplicate Number | #287 | 🟡 Medium | Treat array values as implicit linked list |

---

## 🔄 Reversal Patterns

**When to use:** Reverse full list, a sublist, or k-groups. Always track three pointers: `prev`, `curr`, `next_node`.

**Trigger keywords:** "reverse linked list", "reverse k nodes", "palindrome linked list"

```python
# Reverse entire list — iterative
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next   # save next
        curr.next = prev        # reverse pointer
        prev = curr             # advance prev
        curr = next_node        # advance curr
    return prev

# Reverse sublist from position left to right
def reverse_between(head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to node just before position left
    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    for _ in range(right - left):
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Reverse Linked List | #206 | 🟢 Easy | Iterative: prev / curr / next pointer dance |
| Reverse Linked List II | #92 | 🟡 Medium | Reverse sublist from position m to n |
| Reverse Nodes in k-Group | #25 | 🔴 Hard | Recursion + reverse exactly k nodes at a time |
| Palindrome Linked List | #234 | 🟢 Easy | Find mid, reverse second half, compare |
| Reorder List | #143 | 🟡 Medium | Find mid + reverse second half + interleave |

### Common Mistakes
- Not saving `next_node` before overwriting `curr.next`
- Losing the head of the list — always use a dummy node for clarity
- Off-by-one errors when targeting a specific position

---

## 🧩 Merge & Sort

**When to use:** Merging sorted lists, sorting a linked list, or combining multiple lists.

**Trigger keywords:** "merge sorted lists", "sort list", "add two numbers"

```python
# Merge two sorted lists
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

# Merge K sorted lists — min heap
import heapq

def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    curr = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Merge Two Sorted Lists | #21 | 🟢 Easy | Compare heads, always attach the smaller one |
| Merge K Sorted Lists | #23 | 🔴 Hard | Min heap of `(val, i, node)` — O(n log k) |
| Sort List | #148 | 🟡 Medium | Merge sort — fast/slow pointer to find split |
| Add Two Numbers | #2 | 🟡 Medium | Simulate addition digit by digit with carry |

---

## 🔍 HashMap on Linked Lists

**When to use:** Clone with random pointers, detect intersections, or track visited nodes.

**Trigger keywords:** "random pointer", "intersection", "clone", "remove nth"

```python
# Copy list with random pointer
def copy_random_list(head):
    if not head:
        return None
    old_to_new = {}

    # First pass: create all new nodes
    curr = head
    while curr:
        old_to_new[curr] = ListNode(curr.val)
        curr = curr.next

    # Second pass: assign next and random
    curr = head
    while curr:
        if curr.next:
            old_to_new[curr].next = old_to_new[curr.next]
        if curr.random:
            old_to_new[curr].random = old_to_new[curr.random]
        curr = curr.next

    return old_to_new[head]

# Remove Nth node from end — two pointers n apart
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next
```

### Problems

| Problem | LC # | Difficulty | Key Insight |
|---------|------|-----------|------------|
| Copy List with Random Pointer | #138 | 🟡 Medium | HashMap: old node → new node |
| Intersection of Two Linked Lists | #160 | 🟢 Easy | Equal-length trick or visited set |
| Remove Nth Node from End | #19 | 🟡 Medium | Two pointers n apart — single pass |
| Delete Node in a Linked List | #237 | 🟢 Easy | Copy next value into current, skip next |

---

## 🔀 Combined Practice

> These problems require mixing 2+ patterns. Spend 15+ minutes before checking hints.

| Problem | LC # | Difficulty | Patterns Required |
|---------|------|-----------|------------------|
| LRU Cache | #146 | 🟡 Medium | Doubly Linked List + HashMap |
| Sort List | #148 | 🟡 Medium | Fast/Slow (find mid) + Merge Sort |
| Flatten a Multilevel Doubly LL | #430 | 🟡 Medium | DFS or stack traversal on list |
| Palindrome Linked List | #234 | 🟢 Easy | Fast/Slow + Reversal of second half |
| Rotate List | #61 | 🟡 Medium | Find tail + modular rotation math |

---

## 📚 Resources

| Resource | Link | Best For |
|----------|------|---------|
| NeetCode Linked List Playlist | youtube.com/@NeetCode | Clear pointer manipulation visuals |
| VisuAlgo Linked List | visualgo.net/en/list | Animate insert, delete, reverse |
| LeetCode Explore — Linked List | leetcode.com/explore/learn/card/linked-list | Official card with exercises |

---

## 🐍 Python Tips

```python
# Always use a dummy node for edge cases
dummy = ListNode(0)
dummy.next = head
# ... manipulate list ...
return dummy.next    # new head

# Dummy node handles:
# - Deleting the actual head
# - Inserting before the head
# - Returning new head safely

# Two pointer gap setup
fast = slow = dummy
for _ in range(n):
    fast = fast.next
# Now fast is n steps ahead of slow
```