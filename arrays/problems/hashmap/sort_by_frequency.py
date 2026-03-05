# 1636. Sort Array by Increasing Frequency - Easy

# Link: https://leetcode.com/problems/sort-array-by-increasing-frequency/

# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

# Example 1:
# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3. The sorted array is [3,1,1,2,2,2].

# Note:
# 1. 1 <= nums.length <= 100
# 2. -100 <= nums[i] <= 100

from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        return sorted(nums, key=lambda x: (frequency[x], -x))

# Notes:
# 1. We use the `Counter` class from the `collections` module to count the frequency of each integer in the input array `nums`.
# 2. We then sort the array using the `sorted` function with a custom sorting key. The key is a tuple where the first element is the frequency of the integer (which we want to sort in increasing order) and the second element is the negative of the integer itself (which we want to sort in decreasing order when frequencies are the same).

# Time Complexity: O(n log n), where n is the length of the input array, due to the sorting step.
# Space Complexity: O(n), as we are using a `Counter` to store the frequency of each integer, which can take up to O(n) space in the worst case.