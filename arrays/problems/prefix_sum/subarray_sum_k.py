# 560. Subarray Sum Equals K - Medium

# Link: https://leetcode.com/problems/subarray-sum-equals-k/

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k. 

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2

# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curSum = 0
        freq = {0: 1}
        
        for num in nums:
            curSum += num
            diff = curSum - k
            count += freq.get(diff, 0)
            freq[curSum] = freq.get(curSum, 0) + 1
        
        return count
    
# Note:

# We use a hash map (dictionary) to store the frequency of prefix sums. The key idea is that if the difference between the current prefix sum and k has been seen before, it means there is a subarray that sums to k. We update the count accordingly and also update the frequency of the current prefix sum in the hash map.

# Time Complexity: O(n)
# Space Complexity: O(n) in the worst case when all prefix sums are unique.