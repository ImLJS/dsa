# 42. Trapping Rain Water - Hard

# Link: https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# Example:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water

# Notes:
# 1. We use two pointers, `left` and `right`, starting at the beginning and end of the array, respectively.
# 2. We keep track of the maximum height seen so far from the left and right sides.
# 3. We move the pointer that has the smaller maximum height inward, because the amount of water trapped at that pointer is limited by the smaller maximum height.
# 4. We calculate the water trapped at each step by subtracting the current height from the maximum height seen so far on that side.
# 5. We continue this process until the two pointers meet, at which point we have calculated the total amount of trapped water.

# Complexity:
# - Time: O(n) — single pass
# - Space: O(1) — constant extra space
