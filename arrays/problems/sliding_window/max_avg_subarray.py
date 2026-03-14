# 643. Maximum Average Subarray I - Easy

# Link: https://leetcode.com/problems/maximum-average-subarray-i/

# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value. 

# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

# Note:
# 1. 1 <= k <= n <= 30,000.

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sum(nums[:k])
        current_sum = max_sum
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k
    
# Time Complexity: O(n)
# Space Complexity: O(1)