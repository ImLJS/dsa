# 567. Permutation in String - Medium

# Link: https://leetcode.com/problems/permutation-in-string/

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Constraints:
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        for i in range(len(s2)):
            s2_count[ord(s2[i]) - ord('a')] += 1

            if i >= len(s1):
                s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if s1_count == s2_count:
                return True

        return False

# Notes:
# - We use a sliding window approach to compare the frequency of characters in s1 and the current window of s2.
# - The window size is fixed to the length of s1.
# - We update the frequency array for s2 as we slide the window, adding the new character and removing the old one.
# - If the frequency arrays match at any point, it means s2 contains a permutation of s1.

# Time Complexity: O(n), where n is the length of s2. We iterate through s2 once.
# Space Complexity: O(1), since the frequency arrays have a fixed size of 26.