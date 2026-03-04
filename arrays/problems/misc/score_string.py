# 3110. Score of a String - Easy

# Link: https://leetcode.com/problems/score-of-a-string/

# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters. Return the score of s.

# Example 1:
# Input: s = "abc"
# Output: 2
# Explanation: The score of "abc" is |'a' - 'b'| + |'b' - 'c'| = 1 + 1 = 2.

# Example 2:
# Input: s = "aaa"
# Output: 0
# Explanation: The score of "aaa" is |'a' - 'a'| + |'a' - 'a'| = 0 + 0 = 0.

# Constraints:
# 1 <= s.length <= 100

class Solution:
    def asciiDifference(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score