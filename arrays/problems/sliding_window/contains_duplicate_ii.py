# 219. Contains Duplicate II - Easy

# Link: https://leetcode.com/problems/contains-duplicate-ii/

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k
# Output: false

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

            if len(seen) > k:
                seen.remove(nums[i - k])

        return False

# Notes:

# We can use a sliding window of size k to keep track of the last k elements we have seen. If we encounter a duplicate within this window, we return true. If the window exceeds size k, we remove the oldest element from the set.

# Time Complexity: O(n)
# Space Complexity: O(k)