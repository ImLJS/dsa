# Remove Duplicates from Sorted Array - Easy - Leetcode 26

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1
        if len(nums)==1:
            return 1
        
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[L] = nums[i]
                L+=1
        
        return L

# Notes:

# 1. We can use two pointers to keep track of the current position in the array and the position of the last unique element.
# 2. We iterate through the array and compare each element with the previous one. If they are different, we update the position of the last unique element and move the pointer forward.
# 3. Finally, we return the length of the unique elements in the array.

# Time Complexity: O(n), where n is the length of the array.
# Space Complexity: O(1), since we are modifying the array in place and using only a constant amount of extra space.
