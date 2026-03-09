# 1480. Running Sum of 1D Array - Easy

# Link: https://leetcode.com/problems/running-sum-of-1d-array/

# Given an array nums, return the running sum of the array.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: 1, 1+2, 1+2+3, 1+2+3+4.

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: 1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1.

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Calculate the running sum of a 1D array.

        Args:
            nums (List[int]): List of integers.

        Returns:
            List[int]: Running sum of the array.
        """
        running_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
        return running_sum

# Notes:

# 1. Initialize an empty list `running_sum` to store the cumulative sums.
# 2. Use a variable `current_sum` to keep track of the cumulative sum as we iterate through the array.
# 3. For each number in the input array, add it to `current_sum` and append the result to `running_sum`.
# 4. Return the `running_sum` list after processing all elements.

# Time Complexity: O(n), where n is the length of the input array. We iterate through the array once.
# Space Complexity: O(n), as we use an additional list to store the running sums.