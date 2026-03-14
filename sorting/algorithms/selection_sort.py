# Selection Sort Algorithm

# Best case    : 0(n^2)
# Average case : 0(n^2)
# Worst case   : 0(n^2)
# Space complexity : 0(1)
#
# Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each
# iteration and places that element at the beginning of the unsorted list. It repeats this process until
# all the elements are sorted.


def selection_sort(arr):
    for i in range(len(arr)):
        swapped = False
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                print("Hi")
                min = j
                swapped = True

        if not swapped:
            return arr
        arr[i], arr[min] = arr[min], arr[i]


# arr = [64, 34, 25, 12, 22, 11, 90]
arr = [1, 2, 3, 4, 5]

print(selection_sort(arr))