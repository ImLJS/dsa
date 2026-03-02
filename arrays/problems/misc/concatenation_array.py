# 1929. Concatenation of Array - Easy

# Link: https://leetcode.com/problems/concatenation-of-array/

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]

# Example 2:
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]

# Constraints:
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (2 * n)
        for i in range(n):
            result[i] = nums[i]
            result[i + n] = nums[i]
        return result

# Notes

# 1. We create a new array `result` of size `2 * n` to hold the concatenated elements.
# 2. We iterate through the input array `nums` and fill the first half of `result` with the elements of `nums`.
# 3. We also fill the second half of `result` with the same elements from `nums` by accessing the index `i + n`.
# 4. Finally, we return the `result` array which contains the concatenated elements in the desired order.

# Time Complexity: O(n) - We iterate through the array once to fill the result.
# Space Complexity: O(n) - We use an additional array to store the result.
