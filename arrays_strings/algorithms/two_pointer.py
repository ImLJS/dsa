# Two Pointers Algorithm

# Used to find the indices of the two numbers that add up to a target sum in a sorted array.

# Time Complexity: O(n)
# Space Complexity: O(1)

def twoPointers(arr, target):
    L, R = 0, len(arr) - 1  # Initialize the left and right pointers to the first and last index of the array
    while L < R:  # While the left pointer is less than the right pointer
        curSum = arr[L] + arr[R]  # Calculate the current sum of the two numbers at the left and right pointers
        if curSum == target:  # If the current sum is equal to the target, return the indices of the two numbers
            return [L, R]
        elif curSum < target:  # If the current sum is less than the target, move the left pointer to the right
            L += 1
        else:  # If the current sum is greater than the target, move the right pointer to the left
            R -= 1
    return [-1, -1]  # Return [-1, -1] if no such pair exists

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
print(twoPointers(arr, target))  # Output: [0, 8] (1 + 9 = 10)