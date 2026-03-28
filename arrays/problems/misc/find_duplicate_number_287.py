# 287. Find the Duplicate Number - Medium

# Link: https://leetcode.com/problems/find-the-duplicate-number/

# Given an array of integers nums containing n + 1 integers where each integer is in
# the range [1, n], there is only one repeated number in nums, return this repeated number.

# Example:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Constraints:
# - 1 <= n <= 10^5
# - nums.length == n + 1
# - 1 <= nums[i] <= n
# - All the integers in nums appear only once except for precisely one integer which appears two or more times.

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Floyd's Tortoise and Hare (cycle detection) applied to the value->index mapping.

        Idea: Treat each array value as a pointer to the next index: i -> nums[i]. Because
        values are in [1, n] and there are n+1 elements, there must be a cycle created by
        the duplicate. The entry point of the cycle is the duplicate value.

        Time: O(n)
        Space: O(1)
        """
        # Phase 1: find intersection point inside the cycle
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: find entrance to the cycle
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1


# Notes
# - Correctness intuition: The mapping i -> nums[i] forms a linked structure with a
#   guaranteed cycle because there are more nodes (n+1 indices) than distinct targets
#   (n values). The duplicate value is the start of the cycle. Floyd's algorithm finds
#   an intersection inside the cycle; then resetting one pointer to the start and moving
#   both one step at a time finds the cycle entrance.
#
# - Example walk-through:
#   nums = [1,3,4,2,2]
#   indices: 0 1 2 3 4
#   mapping: 0->1, 1->3, 2->4, 3->2, 4->2
#   Cycle: 2 -> 4 -> 2 (duplicate value 2 is cycle entry)
#
# - Alternatives:
#   - Use a set to detect the first repeated value: O(n) time, O(n) extra space.
#   - Sort the array and find adjacent equal elements: O(n log n) time, O(1) or O(n)
#     extra space depending on sort.
#   - Binary search on value range [1..n] counting how many elements <= mid to locate
#     the duplicate in O(n log n) time and O(1) space.
#
# - Edge cases:
#   - Problem constraints ensure at least one duplicate and values in the specified range.
#   - Works when the duplicate appears more than twice.
