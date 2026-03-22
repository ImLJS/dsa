# 1. Two Sum - Easy

# Link: https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in mapping:
                return [mapping[diff], index]
            mapping[num] = index
        
        return []

# Note:

# 1. We can use a hash map to store the indices of the numbers we have seen so far.
# 2. For each number, we calculate the difference between the target and the current number.
# 3. If the difference is already in the hash map, we have found our solution and we return the indices.
# 4. If not, we add the current number and its index to the hash map and continue iterating through the array.
# 5. The time complexity of this solution is O(n) because we traverse the array once, and the space complexity is also O(n) in the worst case if all numbers are unique.

# Time Complexity: O(n)
# Space Complexity: O(n)