# 217. Contains Duplicate - Easy

# Link: https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Notes

# 1. We use a set called `seen` to keep track of the numbers we have encountered as we iterate through the input array `nums`.
# 2. For each number in `nums`, we check if it is already in the `seen` set. If it is, we return `True` immediately, indicating that a duplicate has been found.
# 3. If the number is not in the `seen` set, we add it to the set and continue checking the next numbers.
# 4. If we finish iterating through the array without finding any duplicates, we return `False`.

# Time Complexity: O(n) - We iterate through the array once, and set operations (add and check) are O(1) on average.
# Space Complexity: O(n) - In the worst case, if all numbers are distinct, we will store all of them in the `seen` set.