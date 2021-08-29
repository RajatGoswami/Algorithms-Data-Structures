import sys

# Quicksort
# Divide-and-conquer, in-place algorithm

# Time complexity: O(n * log(n))
# Space complexity: O(1)

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def partition(array, l, h):
    # Using simplified approach to selecting a pivot:
    # Pick the last element of the array.
    pivot = array[h]

    i = l - 1
    j = l
    while j <= h - 1:
        # Compare each element with the pivot
        if array[j] < pivot:    
            i = i + 1

            # Swap
            swap(array, i, j)

        j = j + 1
    
    # Place the pivot in the correct location
    # i.e. all elements < pivot come before
    # and all elements > pivot appear after
    i = i + 1
    swap(array, i, h)

    return i


def quick_sort(array, l, h):
    if l < h:
        # Parition the array using a given pivot
        pivotIndex = partition(array, l, h)

        # Recursively sort partitioned sub-arrays
        quick_sort(array, l, pivotIndex - 1)
        quick_sort(array, pivotIndex + 1, h)


def main():
    # Array to be sorted
    array = sys.argv[1].split(',')
    array = [int(elem) for elem in array]

    # Ensure that the input array is not empty
    size = len(array)

    if size < 0:
        print("Please provide a non-empty input array")
        return
    
    # Sort the input array from smallest to largest
    quick_sort(array, 0, size - 1)
    print(array)

if __name__ == "__main__":
    main()