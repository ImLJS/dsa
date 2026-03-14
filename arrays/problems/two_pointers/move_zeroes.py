# 283. Move Zeroes - Easy

# Link: https://leetcode.com/problems/move-zeroes/

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zeroes.
# Note that you must do this in-place without making a copy of the array. 

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

# Notes:
# 1. We initialize a pointer `left` to keep track of the position where the next non-zero element should be placed.
# 2. We iterate through the array with a pointer `right`. Whenever we encounter a non-zero element, we swap it with the element at the `left` pointer and then move the `left` pointer to the right.
# 3. This way, all non-zero elements are moved to the front of the array, and all zeroes are moved to the end of the array.

# Time Complexity: O(n), where n is the length of the input array `nums`.
# Space Complexity: O(1), as we are modifying the array in-place and using only a constant amount of extra space.