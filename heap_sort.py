import sys

# Heap Sort

# Time complexity: O(n * log(n))
# Space complexity: O(1) (in-place)

# A heap is a complete binary tree where the parent node is
# always greater-than its child nodes in the case of a max-heap
# and less-than in the case of a min-heap.

# We will be using an array to represent the heap data structure.
# Given a parent node at index i:
# - The left child node can be found at index (2 * i) + 1
# - The right child node can be found at index (2 * 1) + 2

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def heapify(array):
    pass

def heap_sort(array):
    return array

def main():
    # Array to be sorted
    array = sys.argv[1].split(',')
    array = [int(elem) for elem in array]

    # Ensure that the input array is not empty
    if len(array) < 0:
        print("Please provide a non-empty input array")
        return
    
    # Sort the input array from smallest to largest
    sorted_array = heap_sort(array)
    print(sorted_array)


if __name__ == "__main__":
    main()