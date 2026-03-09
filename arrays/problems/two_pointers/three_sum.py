# 15. 3Sum - Medium

# Link: https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: The triplet [-1,0,1] sums to 0. The triplet [-1,-1,2] also sums to 0.
# The triplet [0,1,2] does not sum to 0.

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return triplets

# Notes:
# 1. We first sort the input array to facilitate the two-pointer approach and to easily skip duplicates.
# 2. We iterate through the sorted array, fixing one element and using two pointers to find pairs that sum to the negative of the fixed element.
# 3. If the sum of the three elements is zero, we add the triplet to the result list and move both pointers while skipping duplicates.
# 4. If the sum is less than zero, we move the left pointer to the right to increase the sum. If the sum is greater than zero, we move the right pointer to the left to decrease the sum.
# 5. We also skip duplicate elements for the fixed pointer to avoid duplicate triplets in the result.

# Time Complexity: O(n^2), where n is the length of the input array `nums`. Sorting takes O(n log n) and the two-pointer approach takes O(n^2) in the worst case.
# Space Complexity: O(1) for the in-place sorting, and O(k) for the output list of triplets, where k is the number of unique triplets found.