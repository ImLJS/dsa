# 344. Reverse String - Easy

# Link: https://leetcode.com/problems/reverse-string/

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Notes:
# 1. We initialize two pointers, `left` at the start of the array and `right` at the end of the array.
# 2. We swap the characters at the `left` and `right` pointers.
# 3. After the swap, we move the `left` pointer to the right and the `right` pointer to the left.
# 4. The loop continues until the two pointers meet, ensuring that the entire string is reversed.

# Time Complexity: O(n), where n is the length of the input array `s`.
# Space Complexity: O(1), as we are modifying the array in-place and using only a constant amount of extra space.