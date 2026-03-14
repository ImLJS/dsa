# 20. Valid Parentheses - Easy

# Link: https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Constraints:
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char not in mapping:
                stack.append(char)
            elif not stack or stack.pop() != mapping[char]:
                return False
        
        return not stack

# Notes
# 1. We use a stack to keep track of the opening brackets.
# 2. We define a mapping of closing brackets to their corresponding opening brackets.
# 3. We iterate through each character in the string `s`:
#    - If the character is an opening bracket, we push it onto the stack.
#    - If the character is a closing bracket, we check if the stack is empty or if the top of the stack does not match the corresponding opening bracket. If either condition is true, we return False.
# 4. After processing all characters, we check if the stack is empty. If it is empty, it means all brackets were matched correctly, and we return True. Otherwise, we return False.

# Time Complexity: O(n) - We iterate through the string once.
# Space Complexity: O(n) - In the worst case, we may have all opening brackets