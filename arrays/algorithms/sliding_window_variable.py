# Sliding Window Variable Template

# Time Complexity: O(n)
# Space Complexity: O(1)

# The sliding window algorithm is used to find the maximum sum of a subarray of a variable size in an array.
# It is a dynamic programming algorithm that uses a sliding window approach to solve the problem in
# O(n) time complexity.

# Q. FInd the length of the longest subarray with the same value in an array


def slidingWindowVariable(nums):
    n = len(nums)
    maxL = 0
    L = 0

    for R in range(n):
        if nums[L] != nums[R]:  # If the elements are not equal
            L = R
        maxL = max(maxL, R - L + 1)  # Update the maximum length
    return maxL


# Q. Find the minimum length subarray where the sum is greater than or equal to a given target.
# All elements are positive


def slidingWindowVariableLength(nums, target):
    minL = float("inf")  # Initialize the minimum length to infinity
    n = len(nums)
    L, R = 0, 0  # Initialize the left and right pointers to 0
    curSum = 0

    for R in range(n):
        curSum += nums[R]  # Add the current element to the sum
        while curSum >= target:  # If the sum is greater than or equal to the target
            minL = min(minL, R - L + 1)  # Update the minimum length
            curSum -= nums[L]  # Subtract the left element from the sum
            L += 1  # Move the left pointer to the right
    return 0 if minL == float("inf") else minL


arr1 = [4, 2, 2, 3, 3, 3]
arr2 = [2, 3, 1, 2, 4, 3]

print(slidingWindowVariable(arr1))  # Output: 3 [3 consecutive 3's]
print(slidingWindowVariableLength(arr2, 6))  # Output: 2 [2, 4]