# Title: Implement Stack using Queues
# Difficulty: Easy
# Link: https://leetcode.com/problems/implement-stack-using-queues/

# Examples:
# Input:
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False

from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue

# Notes:
# - Use a single queue to simulate stack operations.
# - Rotate the queue to maintain stack order.

# Time Complexity:
# - Push: O(n)
# - Pop: O(1)
# - Top: O(1)

# Space Complexity: O(n)