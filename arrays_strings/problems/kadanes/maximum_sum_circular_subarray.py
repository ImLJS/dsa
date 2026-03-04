# 918. Maximum Sum Circular Subarray - Medium

# Link: https://leetcode.com/problems/maximum-sum-circular-subarray/

# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

# Example 1:
# Input: nums = [1,-2,3,-2]
# Output: 3

# Example 2:
# Input: nums = [5,-3,5]
# Output: 10

# Constraints:
# n == nums.length
# 1 <= n <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        max_sum = float('-inf')
        min_sum = float('inf')
        current_max = 0
        current_min = 0
        
        for num in nums:
            current_max += num
            max_sum = max(max_sum, current_max)
            current_max = max(current_max, 0)
            
            current_min += num
            min_sum = min(min_sum, current_min)
            current_min = min(current_min, 0)
        
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)
    
# Notes

# 1. We calculate the total sum of the array to handle the case where the maximum subarray is a circular one.
# 2. We use two variables `max_sum` and `min_sum` to keep track of the maximum and minimum subarray sums found so far.
# 3. We iterate through the array and update `current_max` and `current_min` for each element. We also update `max_sum` and `min_sum` accordingly.
# 4. If `max_sum` is negative, it means all numbers are negative, and we return `max_sum` as the result.
# 5. Otherwise, we return the maximum of `max_sum` and `total_sum - min_sum`, which accounts for the case where the maximum subarray is circular.

# Time Complexity: O(n) - We iterate through the array once.
# Space Complexity: O(1) - We use only a constant amount of extra space.
