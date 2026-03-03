# 3. Longest Substring Without Repeating Characters - Medium

# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters. 

# Example 1:
# Input: s = "abcabcbb"
# Output: 3

# Example 2:
# Input: s = "bbbbb"
# Output: 1

# Example 3:
# Input: s = "pwwkew"
# Output: 3

# Constraints:
# 0 <= s.length <= 5 * 10^4

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

# Notes:

# - We use a sliding window approach to keep track of the current substring without repeating characters.
# - We maintain a set to store the characters in the current window.
# - We expand the right pointer to include new characters and check for duplicates.
# - If a duplicate is found, we move the left pointer to the right until the duplicate
#   is removed from the set.
# - We update the maximum length of the substring whenever we expand the right pointer.

# Time Complexity: O(n), where n is the length of the string. Each character is visited at most twice (once by the right pointer and once by the left pointer).
# Space Complexity: O(min(m, n)), where m is the size of the character set and n is the length of the string. In the worst case, we may need to store all characters in the set.