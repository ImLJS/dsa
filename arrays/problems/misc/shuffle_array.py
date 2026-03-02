# 1470. Shuffle the Array - Easy

# Link: https://leetcode.com/problems/shuffle-the-array/

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]

# Example 2:
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]

# Constraints:
# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10^3

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * (2 * n)
        for i in range(n):
            result[2 * i] = nums[i]
            result[2 * i + 1] = nums[i + n]
        return result

# Notes

# 1. We create a new array `result` of size `2 * n` to hold the shuffled elements.
# 2. We iterate through the first `n` elements of the input array `nums` and place them in the even indices of `result`.
# 3. We also place the corresponding elements from the second half of `nums` in the odd indices of `result`.
# 4. Finally, we return the `result` array which contains the shuffled elements in the desired order.

# Time Complexity: O(n) - We iterate through the array once to fill the result.
# Space Complexity: O(n) - We use an additional array to store the result.