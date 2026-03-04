# 424. Longest Repeating Character Replacement - Medium

# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

# Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
# In one operation, you can choose any character of the string and change it to any other uppercase English character.
# Find the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".

# Constraints:
# 1 <= s.length <= 10^5

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        largest, left, maxf = 0,0,0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            while (right-left+1)-maxf > k:
                count[s[left]]-=1
                left+=1
            largest = max(largest, right-left+1)
        return largest

# Notes:

# 1. We can use a sliding window approach to solve this problem efficiently.
# 2. We maintain a count of characters in the current window and keep track of the maximum frequency of any character in that window.
# 3. If the number of characters that need to be replaced (window size - max frequency) exceeds k, we shrink the window from the left until it is valid again.
# 4. We keep track of the largest valid window size throughout the process and return it at the end.

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1), since the count dictionary will at most have 26 entries for uppercase English letters.