# Sliding Window Template

# Time Complexity: O(n)
# Space Complexity: O(1)

# The sliding window algorithm is used to find the maximum sum of a subarray of a fixed size k in an array.
# It is a dynamic programming algorithm that uses a sliding window approach to solve the problem in
# O(n) time complexity.

# Used to find the maximum sum of a subarray of a fixed size k in an array


def slidingWindow(arr, k):
    maxSum = 0  # Initialize the maximum sum to 0
    curSum = sum(
        arr[:k]
    )  # Initialize the current sum to the sum of the first k elements of the array
    n = len(arr)
    for i in range(k, n):
        curSum += (
            arr[i] - arr[i - k]
        )  # Add the current element and subtract the first element of the window
        maxSum = max(maxSum, curSum)  # Update the maximum sum
    return maxSum


# Q. Given an array return true if there are two elements within the window of size k that are equal

# Time Complexity: O(n)
# Space Complexity: O(n)


def slidingWindowOpt(arr, k):
    n = len(arr)
    window = set()
    L = 0

    for R in range(n):
        if R - L + 1 > k:
            window.remove(arr[L])
            L += 1

        if arr[R] in window:
            return True

        window.add(arr[R])

    return False


arr1 = [1, 2, -3, 4, -5, 6, -7, 8, -9]
arr2 = [1, 2, 3, 2, 4, 3, 3]

k1 = 3
k2 = 2

print(slidingWindow(arr1, k1))  # Output: 7
print(slidingWindowOpt(arr2, k2))  # Output: True