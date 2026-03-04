# 242. Valid Anagram - Easy

# Link: https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
# Notes

# 1. We use the `Counter` class from the `collections` module to count the frequency of each character in both strings `s` and `t`.
# 2. We compare the two `Counter` objects. If they are equal, it means that both strings have the same characters with the same frequencies, and thus `t` is an anagram of `s`.
# 3. If the `Counter` objects are not equal, it means that the strings do not have the same characters with the same frequencies, and thus `t` is not an anagram of `s`.

# Time Complexity: O(n) - We iterate through both strings once to count the characters.
# Space Complexity: O(1) - The `Counter` will at most store 26 characters (since the problem states that the strings consist of lowercase English letters), which is a constant amount of space.