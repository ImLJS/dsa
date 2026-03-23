# Title: Next Greater Element I
# Difficulty: Easy
# Link: https://leetcode.com/problems/next-greater-element-i/

# Examples:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: For 4 there is no greater element, for 1 it is 3, for 2 there is no greater element.

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: For 2 it is 3, for 4 there is no greater element.

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    return [next_greater.get(num, -1) for num in nums1]

# Notes:
# - Use a monotonic stack to find the next greater element.
# - Store results in a dictionary for quick lookup.

# Time Complexity: O(n + m)
# Space Complexity: O(n)