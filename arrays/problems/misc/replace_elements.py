# 1299. Replace Elements with Greatest Element on Right Side - Easy

# Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1. 

# After doing so, return the array.

# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]

# Example 2:
# Input: arr = [400]
# Output: [-1]

# Constraints:
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, temp)
        return arr

# Notes:

# 1. We can iterate through the array from the end to the beginning, keeping track of the maximum element seen so far.
# 2. For each element, we store the current maximum in the array and then update the maximum if the current element is greater.
# 3. This approach has a time complexity of O(n) and a space complexity of O(1) since we are modifying the array in place.

# Time Complexity: O(n)
# Space Complexity: O(1)