import sys
import math

# Binary Search

# Time complexity: O(log(n))
# Space complexity: O(1)

# Precondition: Binary search requires the input array to be sorted.

def binary_search(array, l, r, x):
    # Recursive implementation of binary search that returns the
    # index of x in the array if it exists, returns -1 otherwise.
    if r >= l:
        mid = math.floor( (r + l) / 2)

        if array[mid] == x:
            return mid
        elif x > array[mid]:
            return binary_search(array, mid + 1, r, x)
        else:
            return binary_search(array, 0, mid - 1, x)

    return -1


def main():
    # Parse input array
    array = sys.argv[1].split(',')
    array = [int(elem) for elem in array]

    # Parse target element
    x = int(sys.argv[2])

    size = len(array)

    # Ensure that the input array is not empty
    if size < 0:
        print("Please provide a non-empty input array")
        return

    # Ensure that the input array is sorted (least to greatest)
    for i in range(size - 2):
        if array[i] > array[i + 1]:
            print("Input array is not sorted. Performing sort before search.")
            from quick_sort import quick_sort
            quick_sort(array, 0, size - 1)

            print("Sorted array to be searched: {}".format(array))

    index = binary_search(array, 0, size - 1, x)

    if index != -1:
        print("Target element {} was found at index: {}".format(x, index))
    else:
        print("The target element {} does not exist in input array {}".format(x, array))


if __name__ == "__main__":
    main()