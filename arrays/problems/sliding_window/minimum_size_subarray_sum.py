# 209. Minimum Size Subarray Sum - Medium

# Link: https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_so_far = 0
        min_length = float('inf')

        for right in range(len(nums)):
            sum_so_far += nums[right]

            while sum_so_far >= target:
                min_length = min(min_length, right - left + 1)
                sum_so_far -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
    
# Notes:

# We use a sliding window approach to find the minimum length of a contiguous subarray that meets the target sum. We maintain two pointers, `left` and `right`, to represent the current window of elements we are considering. We expand the right pointer to include more elements until the sum of the current window is greater than or equal to the target. Once we have a valid window, we try to shrink it from the left to find the smallest valid window. We keep track of the minimum length found during this process.

# Time Complexity: O(n) - Each element is visited at most twice (once by the right pointer and once by the left pointer).
# Space Complexity: O(1) - We are using a constant amount of extra space.