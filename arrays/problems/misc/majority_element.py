# 169. Majority Element - Easy

# Link: https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

# Notes

# 1. We sort the input array `nums`. After sorting, the majority element will be located at the middle index of the array, which is `len(nums) // 2`.
# 2. We return the element at the middle index, which is guaranteed to be the majority element as it appears more than n/2 times.

# Time Complexity: O(n log n) - due to the sorting step.
# Space Complexity: O(1) - we are sorting the array in place and using only