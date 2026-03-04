# 978. Longest Turbulent Subarray - Medium

# Link: https://leetcode.com/problems/longest-turbulent-subarray/

# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# Example 1:
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5

# Example 2:
# Input: arr = [4,8,12,16]
# Output: 2

# Constraints:
# 1 <= arr.length <= 4 * 10^4
# 0 <= arr[i] <= 10^9

from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R, res, prev = 0, 1, 1, ""

        while R < len(arr):
            if arr[R-1] > arr[R] and prev !='>':
                res = max(res, R-L+1)
                R+=1
                prev = '>'
            elif arr[R-1] < arr[R] and prev !='<':
                res = max(res, R-L+1)
                R+=1
                prev='<'
            else:
                R = R+1 if arr[R] == arr[R-1] else R
                L = R-1
                prev = ""
        return res
    
# Notes
# 1. We use two pointers `L` and `R` to represent the left and right boundaries of the current turbulent subarray.
# 2. We also maintain a variable `res` to keep track of the maximum length of a turbulent subarray found so far, and a variable `prev` to keep track of the previous comparison result (greater than or less than).
# 3. We iterate through the array using the right pointer `R` and compare the current element with the previous element.
# 4. If the current element is greater than the previous element and the previous comparison was not '>', we update the result and move the right pointer to the next element, and set `prev` to '>'.
# 5. If the current element is less than the previous element and the previous comparison was not '<', we update the result and move the right pointer to the next element, and set `prev` to '<'.
# 6. If the current element is equal to the previous element, we reset the left pointer to the current position and clear the `prev` variable.
# 7. Finally, we return the maximum length of a turbulent subarray found.

# Time Complexity: O(n) - We iterate through the array once.
# Space Complexity: O(1) - We use only a constant amount of extra space.
