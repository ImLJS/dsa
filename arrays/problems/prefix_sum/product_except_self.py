# 238. Product of Array Except Self - Medium

# Link: https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

# Notes:

# 1. We can solve this problem by calculating the prefix and postfix products for each element in the array. The prefix product is the product of all the elements to the left of the current element, and the postfix product is the product of all the elements to the right of the current element. We can then multiply these two products together to get the final result for each element.
# 2. We initialize the result array with 1s, and then we iterate through the input array twice: once from left to right to calculate the prefix products, and once from right to left to calculate the postfix products. This way, we can achieve the desired O(n) time complexity without using division.

# TIme Complexity: O(n)
# Space Complexity: O(1) (excluding the output array)