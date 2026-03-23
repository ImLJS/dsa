# Title: Evaluate Reverse Polish Notation
# Difficulty: Medium
# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Examples:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

def evalRPN(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]

# Notes:
# - Use a stack to evaluate the expression.
# - Perform operations as tokens are encountered.

# Time Complexity: O(n)
# Space Complexity: O(n)