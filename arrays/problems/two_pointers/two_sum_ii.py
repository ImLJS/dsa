# 167. Two Sum II - Input Array Is Sorted - Medium

# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9 
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []

# Notes:

# 1. We initialize two pointers, `left` at the start of the array and `right` at the end of the array.
# 2. We calculate the sum of the numbers at the `left` and `right` pointers.
# 3. If the sum is equal to the target, we return the indices (adjusted for 1-indexing).
# 4. If the sum is less than the target, we move the `left` pointer to the right to increase the sum.
# 5. If the sum is greater than the target, we move the `right` pointer to the left to decrease the sum.
# 6. The loop continues until the two pointers meet, ensuring that we find the correct pair of numbers that add up to the target.

# Time Complexity: O(n), where n is the length of the input array `numbers`.
# Space Complexity: O(1), as we are using only a constant amount of extra space