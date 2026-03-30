# Title: Min Stack
# Difficulty: Medium
# Link: https://leetcode.com/problems/min-stack/

# Examples:
# Input:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Notes:
# - Use an auxiliary stack to keep track of the minimum values.
# - Ensure the auxiliary stack is updated during push and pop operations.

# Time Complexity:
# - Push: O(1)
# - Pop: O(1)
# - Top: O(1)
# - GetMin: O(1)

# Space Complexity: O(n)