# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold - Medium

# Link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

# Example 1:
# Input: arr = [2,2,2,2,5,5,5], k = 3, threshold = 4
# Output: 3

# Example 2:
# Input: arr = [1,1,1,1,1], k = 1, threshold = 0
# Output: 5

# Example 3:
# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6

# Constraints:
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^4
# 1 <= k <= arr.length

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        window_sum = sum(arr[:k])
        target = threshold * k

        if window_sum >= target:
            count += 1

        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]

            if window_sum >= target:
                count += 1

        return count

# Notes:

# We can use a sliding window of size k to calculate the sum of each sub-array of size k. We compare the sum with the target (threshold * k) to determine if it meets the condition. We update the window sum by adding the new element and removing the old element as we slide the window. 

# Time Complexity: O(n)
# Space Complexity: O(1)