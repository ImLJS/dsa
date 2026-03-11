# Bubble Sort in python

# Best Case: O(n)
# Average Case: O(n^2)
# Worst Case: O(n^2)
# Space Complexity: O(1)

# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
# if they are in wrong order.


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            print(j)
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(arr))