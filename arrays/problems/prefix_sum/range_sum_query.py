# 303. Range Sum Query - Immutable - Easy

# Link: https://leetcode.com/problems/range-sum-query-immutable/

# Given an integer array nums, handle multiple queries of the following type:
# - Calculate the sum of the elements of nums between indices left and right
#   inclusive where left <= right.

# Implement the NumArray class:
# - NumArray(int[] nums)  initializes the object with the integer array nums.
# - int sumRange(int left, int right)  returns the sum of the elements of nums
#   between indices left and right inclusive.

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total+=n
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefix[right]
        preLeft = self.prefix[left-1] if left > 0 else 0
        return preRight-preLeft

# Notes:

# 1. We can use a prefix sum array to store the cumulative sums of the input array.
# 2. The prefix sum array allows us to calculate the sum of any range in O
#    time by subtracting the prefix sum at the left index from the prefix sum at the right index.
# 3. The space complexity of this solution is O(n) due to the prefix sum array, and the time complexity for each sumRange query is O(1).

# Pattern: Prefix Sum
# Time:  O(n) build, O(1) query
# Space: O(n)
