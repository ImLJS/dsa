# 141. Linked List Cycle - Easy

# Link: https://leetcode.com/problems/linked-list-cycle/

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example:
# Input: head = [3,2,0,-4], pos = 1
# Output: true

# Constraints:
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Detect cycle using Floyd's Tortoise and Hare algorithm.

        Time: O(n)
        Space: O(1)
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


# Notes
# - Approach: Use Floyd's Tortoise and Hare (two-pointer) algorithm. Maintain two pointers
#   `slow` (moves one step) and `fast` (moves two steps). If there is a cycle, `fast` will
#   eventually lap `slow` and they will reference the same node. If `fast` reaches the
#   end (`None`), the list has no cycle.
#
# - Why it works (intuition): On each step the distance between `fast` and `slow` in the
#   cycle decreases by 1 modulo the cycle length (since `fast` advances one extra step).
#   Thus within at most `k` steps (k = cycle length) they must meet.
#
# - Proof sketch: If the list has a cycle of length `k`, once both pointers are inside the
#   cycle their positions can be seen modulo `k`. Let their difference be `d` (0 < d < k).
#   On each iteration the difference becomes `(d+1) mod k`. Repeatedly adding 1 mod `k`
#   will hit 0 within at most `k` steps, so they collide.
#
# - Edge cases:
#   - Empty list (`head is None`) -> return `False`.
#   - Single node pointing to itself -> return `True`.
#   - Single node with `next is None` -> return `False`.
#
# - Example walk-through:
#   For list `A -> B -> C -> D -> B` (cycle starts at `B`) the pointers move:
#     slow: A, B, C, D, B, C, ...
#     fast: A, C, B, D, C, B, ...
#   They meet at node `C` after a few steps.
#
# - Complexity:
#   - Time: O(n) where `n` is the number of nodes — each pointer moves through nodes
#     at most a constant number of times before termination.
#   - Space: O(1) constant extra space for pointers.
