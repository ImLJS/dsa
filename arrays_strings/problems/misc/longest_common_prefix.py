# 14. Longest Common Prefix - Easy

# Link: https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()

        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first))):
            if first[i] != last[i]:
                return first[:i]
        return first

# Notes

# 1. We first check if the input list `strs` is empty. If it is, we return an empty string.
# 2. We sort the list of strings. After sorting, the longest common prefix of all the strings will be a prefix of the first and last strings in the sorted list.
# 3. We compare the characters of the first and last strings until we find a mismatch. The index at which the mismatch occurs will give us the length of the longest common prefix.
# 4. We return the substring of the first string from the start to the index of the mismatch. If there is no mismatch, we return the entire first string as the longest common prefix.

# Time Complexity: O(n log n) - Sorting the list of strings takes O(n log n) time, where n is the number of strings. The comparison of the first and last strings takes O(m) time, where m is the length of the longest common prefix.
# Space Complexity: O(1) - We use only a constant amount of extra space for the variables. The sorting operation may take O(n) space depending on the sorting algorithm used, but it is generally considered O(1) for in-place sorting algorithms.