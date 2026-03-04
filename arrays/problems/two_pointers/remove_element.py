# 27. Remove Element - Easy

# Link - https://leetcode.com/problems/remove-element/

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_]

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,3,0,4,_,_,_]

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[L] = nums[i]
                L+=1
        
        return L
    
# Notes:
# 1. We can use two pointers to keep track of the current position in the array and the position of the last non-val element.
# 2. We iterate through the array and compare each element with val. If they are different, we update the position of the last non-val element and move the pointer forward.
# 3. Finally, we return the length of the non-val elements in the array.

# Time Complexity: O(n), where n is the length of the array.
# Space Complexity: O(1), since we are modifying the array in place and using only