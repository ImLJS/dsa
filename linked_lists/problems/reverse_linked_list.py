# 206. Reverse Linked List - Easy

# Link: https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Iterative in-place reversal.

        Time: O(n)
        Space: O(1)
        """
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# Notes
# - Approach (iterative): Walk the list once maintaining three references:
#   `prev` (reversed prefix), `curr` (current node being processed), and `nxt`
#   (temporary holder for `curr.next`). At each step, point `curr.next` to `prev`,
#   then advance `prev` and `curr`. After the loop, `prev` is the new head.
#
# - Alternative (recursive): Recursively reverse the tail and attach the current
#   node to the end of the reversed tail; requires O(n) recursion stack (stack space).
#
# - Invariants:
#   - Before processing a node `curr`, `prev` is the head of the reversed list for
#     all nodes processed so far; nodes after `curr` remain in their original order.
#
# - Edge cases:
#   - Empty list -> returns `None`.
#   - Single-node list -> returns the same node.
#
# - Example:
#   Input: 1 -> 2 -> 3 -> None
#   Steps:
#     prev=None, curr=1  => 1.next = None
#     prev=1, curr=2     => 2.next = 1
#     prev=2, curr=3     => 3.next = 2
#   Result: prev points to 3 -> 2 -> 1 -> None
#
# - Complexity:
#   - Time: O(n) where `n` is the number of nodes (single pass).
#   - Space: O(1) iterative; recursive variant uses O(n) call stack.
