# 41. First Missing Positive - Hard

# Link: https://leetcode.com/problems/first-missing-positive/

# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:
# Input: [1,2,0]
# Output: 3

# Example 2:
# Input: [3,4,-1,1]
# Output: 2

# Example 3:
# Input: [7,8,9,11,12]
# Output: 1

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        nums.sort()

        target = 1
        for n in nums:
            if n == target:
                target += 1
            elif n > target:
                return target
        
        return target

# Note:
# We first filter out non-positive integers and sort the remaining positive integers. We then iterate through the sorted list, looking for the smallest missing positive integer. If we find a number that matches our target, we increment the target. If we encounter a number greater than our target, we can return the target immediately since it means the target is missing.

# Time Complexity: O(n log n) due to sorting.
# Space Complexity: O(n) for the filtered list of positive integers.