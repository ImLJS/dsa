# 977. Squares of a Sorted Array - Easy

# Link: https://leetcode.com/problems/squares-of-a-sorted-array/

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        L = 0
        R = len(nums)-1
        index = R

        while L<=R:
            if nums[L]**2 >= nums[R]**2:
                res[index] = nums[L]**2
                L+=1
            else:
                res[index] = nums[R]**2
                R-=1
            index-=1
        return res

    
# Notes:
# 1. We initialize a result array `res` of the same length as `nums` to store the squares.
# 2. We use two pointers, `L` starting at the beginning of the array and `R` starting at the end of the array.
# 3. We compare the squares of the elements at the `L` and `R` pointers. We place the larger square at the current `index` in the result array and move the corresponding pointer inward.
# 4. We continue this process until the `L` pointer exceeds the `R` pointer, ensuring that all squares are placed in the correct order in the result array.

# Time Complexity: O(n)
# Space Complexity: O(n)