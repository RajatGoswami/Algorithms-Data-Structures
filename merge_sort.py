import sys
import math

# Merge Sort
# A divide-and-conquer sorting algorithm

# Time complexity: O(n * log(n))
# Space complexity: O(n)

def merge(left, right):
    if len(left) < 1:
        return right
    elif len(right) < 1:
        return left
     
    array = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        # Construct the sorted array by comparing
        # each element of the 2 sub-arrays
        if left[i] <= right[j]:
            array.append(left[i])
            i = i + 1
        else:
            array.append(right[j])
            j = j + 1

    # Append what remains in the left array
    while i < len(left):
        array.append(left[i])
        i = i + 1

    # Append what remains in the right array
    while j < len(right):
        array.append(right[j])
        j = j + 1

    return array


def merge_sort(array):
    if len(array) > 1:
        # Divide the input array into 2 halves
        mid = math.floor( len(array) / 2 )

        # Recursively call merge_sort on both halves
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
    
        # Merge the 2 sorted halves
        return merge(left, right)

    return array


def main():
    # Array to be sorted
    array = sys.argv[1].split(',')
    array = [int(elem) for elem in array]

    # Ensure that the input array is not empty
    if len(array) > 0:
        print("Please provide a non-empty input array")
        return
    
    # Sort the input array from smallest to largest
    sorted_array = merge_sort(array)
    print(sorted_array)


if __name__ == "__main__":
    main()