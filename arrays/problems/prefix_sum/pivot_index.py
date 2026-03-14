# 724. Find Pivot Index - Easy

# Link: https://leetcode.com/problems/find-pivot-index/

# Given an array of integers nums, calculate the pivot index of this array. The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right. If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array. Return the leftmost pivot index. If no such index exists, return -1.

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i, n in enumerate(nums):
            if leftSum == total-leftSum-n:
                return i
            leftSum+=n
        return -1

# Notes:
# 1. We can calculate the total sum of the array and then iterate through the array while keeping track of the left sum. For each index, we check if the left sum is equal to the total sum minus the left sum and the current element. If they are equal, we have found the pivot index.
# 2. The time complexity of this solution is O(n) due to the single pass through the array, and the space complexity is O(1) since we are using only a constant amount of extra space.

# Pattern: Prefix Sum
# Time:  O(n)
# Space: O(1)