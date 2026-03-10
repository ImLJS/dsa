# 229. Majority Element II - Medium

# Link: https://leetcode.com/problems/majority-element-ii/

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:
# Input: [3,2,3]
# Output: [3]

# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapping = Counter(nums)
        major = len(nums)//3

        res = [x for x in mapping if mapping[x]>major]

        return res

# Note:
# We use the Counter class from the collections module to count the frequency of each element in the array. Then, we iterate through the mapping and check which elements have a count greater than n/3, where n is the length of the input array. We return those elements as the result.

# Time Complexity: O(n) to count the frequencies and O(m) to iterate through the mapping, where m is the number of unique elements. Overall, it is O(n).
# Space Complexity: O(m) for the hash map storing the counts, where m is the number of unique elements in the input array. In the worst case, m can be O(n) if all elements are unique.