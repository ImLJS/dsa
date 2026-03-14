# 485. Max Consecutive Ones - Easy

# Link: https://leetcode.com/problems/max-consecutive-ones/

# Given a binary array, find the maximum number of consecutive 1s in this array. 
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Note:
# The input array will only contain 0 and 1.

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        current_consecutive_ones = 0
        
        for num in nums:
            if num == 1:
                current_consecutive_ones += 1
            else:
                max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
                current_consecutive_ones = 0
        
        return max(max_consecutive_ones, current_consecutive_ones)

# Notes:

# 1. We initialize two variables, `max_consecutive_ones` and `current_consecutive_ones`, to keep track of the maximum number of consecutive 1s found so far and the current count of consecutive 1s, respectively.
# 2. We iterate through each number in the input array `nums`. If the number is 1, we increment the `current_consecutive_ones` counter. If the number is 0, we compare the `current_consecutive_ones` with `max_consecutive_ones` and update it if necessary, then reset `current_consecutive_ones` to 0.
# 3. After the loop, we return the maximum of `max_consecutive_ones` and `current_consecutive_ones` to account for the case where the array ends with 1s.

# Time Complexity: O(n), where n is the length of the input array.
# Space Complexity: O(1), as we are using only a constant amount of extra space