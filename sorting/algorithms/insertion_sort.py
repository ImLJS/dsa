# Insertion Sort Algorithm

# Best case    : 0(n)
# Average case : 0(n^2)
# Worst case   : 0(n^2)
# Space complexity : 0(1)

# Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
# It has a sublist of sorted elements and the other sublist of unsorted elements. Initially, the sorted sublist
# contains the first element of the array and the unsorted sublist contains the rest. At each iteration, insertion
# sort removes an element from the unsorted sublist, finds its correct position in the sorted sublist, and inserts
# it there. It repeats until no input elements remain. The choice of the element being removed from the unsorted
# sublist is random and this process is repeated until all the elements in the list are sorted.


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
# arr = [1, 2, 3, 4, 5]

print(insertion_sort(arr))