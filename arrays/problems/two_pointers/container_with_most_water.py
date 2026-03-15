# 11. Container With Most Water - Medium

# Link: https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers height where each represents a vertical line at x = i,
# find two lines that together with the x-axis form a container that holds the most water.
# Return the maximum area.

# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Two-pointer approach: move the shorter side inward to try to find a taller line.

        Args:
            height: list of non-negative integers representing line heights.

        Returns:
            Maximum area that can be contained.
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, h * width)

            # Move the pointer at the shorter line inward — only that can increase min(height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Notes:
# - Initialize two pointers at both ends and compute area at each step.
# - Move the pointer at the smaller height inward because the area is limited by the shorter line.
# - If heights are equal, moving either pointer is fine.

# Time Complexity: O(n) — each pointer visits indices at most once.
# Space Complexity: O(1) — constant extra space.
