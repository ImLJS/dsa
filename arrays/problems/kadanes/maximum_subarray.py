# 53. Maximum Subarray - Medium

# Link: https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            current_sum = max(current_sum, 0)
        
        return max_sum

# Notes

# 1. We initialize `max_sum` to negative infinity to handle cases where all numbers are negative.
# 2. We iterate through each number in the input array `nums` and keep a running sum of the current subarray (`current_sum`).
# 3. After adding each number to `current_sum`, we update `max_sum` if `current_sum` is greater than `max_sum`.
# 4. If `current_sum` becomes negative, we reset it to 0, as a negative sum would not contribute to a maximum sum in future iterations.
# 5. Finally, we return `max_sum` which contains the largest sum of a contiguous subarray.

# Time Complexity: O(n) - We iterate through the array once.
# Space Complexity: O(1) - We use only a constant amount of extra space.