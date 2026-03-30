# Title: Implement Queue using Stacks
# Difficulty: Easy
# Link: https://leetcode.com/problems/implement-queue-using-stacks/

# Examples:
# Input:
# MyQueue myQueue = new MyQueue();
# myQueue.push(1);
# myQueue.push(2);
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1
# myQueue.empty(); // return false

class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

# Notes:
# - Use two stacks to simulate queue operations.
# - stack_in is used for push operations, stack_out for pop/peek.

# Time Complexity:
# - Push: O(1)
# - Pop: Amortized O(1)
# - Peek: Amortized O(1)

# Space Complexity: O(n)