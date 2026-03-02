# 49. Group Anagrams - Medium

# Link: https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagram_map[sorted_s].append(s)
        return list(anagram_map.values())

# Notes
# 1. We use a dictionary `anagram_map` to group the anagrams together. The key is the sorted version of the string, and the value is a list of strings that are anagrams of each other.
# 2. We iterate through each string in the input list `strs`, sort the characters of the string to get the key, and append the original string to the corresponding list in the dictionary.
# 3. Finally, we return the values of the dictionary as a list of lists, which contains the grouped anagrams.

# Time Complexity: O(n * k log k) - where n is the number of strings and k is the maximum length of a string. Sorting each string takes O(k log k).
# Space Complexity: O(n * k) - in the worst case, all strings are anagrams of each other, and we store all strings in the dictionary.
