# 125. Valid Palindrome - Easy

# Link - https://leetcode.com/problems/valid-palindrome/

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for letter in s:
            if letter.isalnum():
                word+=letter.lower()
        
        return word==word[::-1]

# Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalnum():
                left+=1
            while left < right and not s[right].isalnum():
                right-=1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left+=1
            right-=1
        
        return True

# Notes:
# 1. We can use two pointers to compare characters from the start and end of the string, moving towards the center.
# 2. We skip non-alphanumeric characters and compare the remaining characters in a case-insensitive manner.
# 3. If any characters do not match, we can immediately return false. If we successfully compare all characters, we return true.

# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(1), since we are using only a constant amount of extra space