# 347. Top K Frequent Elements - Medium

# Link: https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. 

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        return [item[0] for item in frequency.most_common(k)]

# Notes
# 1. We use the `Counter` class from the `collections` module to count the frequency of each element in the input array `nums`.
# 2. The `most_common(k)` method of the `Counter` object returns a list of the k most common elements and their counts as tuples. We extract just the elements (the first item of each tuple) to return the result.

# Time Complexity: O(n log k) - where n is the number of elements in the input array. The `most_common` method has a time complexity of O(n log k) when k is small compared to n.
# Space Complexity: O(n) - in the worst case, all elements are unique and we store their counts in the `Counter` object.