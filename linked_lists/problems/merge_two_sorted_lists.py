# 21. Merge Two Sorted Lists - Easy

# Link: https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a new sorted list. The list should be made
# by splicing together the nodes of the first two lists.

# Example:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Merge two lists using a dummy head.

        Time: O(n+m)
        Space: O(1)
        """
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return dummy.next


# Notes
# - Approach: Use a dummy head and a `tail` pointer to build the merged list by
#   splicing nodes from `l1` and `l2`. At each step, compare `l1.val` and `l2.val`,
#   attach the smaller node to `tail.next`, and advance the chosen list and `tail`.
#   After one list is exhausted, attach the remaining list directly.
#
# - In-place vs new nodes: This implementation reuses existing nodes (splices them
#   into the merged list) and does not allocate new list nodes. If you need a
#   fresh list with copied values, you'd allocate new `ListNode` objects.
#
# - Edge cases:
#   - Both lists empty -> return `None`.
#   - One list empty -> return the other list as-is.
#   - Lists with duplicate values -> stable ordering preserved from original lists.
#
# - Example:
#   l1: 1 -> 2 -> 4
#   l2: 1 -> 3 -> 4
#   Merged steps: 1(l1), 1(l2), 2(l1), 3(l2), 4(l1), 4(l2)
#
# - Complexity:
#   - Time: O(n + m) where `n` and `m` are the lengths of `l1` and `l2` — each
#     node is processed once.
#   - Space: O(1) additional space (we only use pointers); the merged list reuses
#     the original nodes.
