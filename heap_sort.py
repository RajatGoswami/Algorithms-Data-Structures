import sys

# Heap Sort

# Time complexity: O(n * log(n))
# Space complexity: O(1) (implemented in-place)

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


def heapify(array, size, index):
    while index < size:
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2

        if left_child >= size:
            break
        
        # Determine which child node is larger
        max_child_index = left_child
        if right_child < size and array[right_child] > array[left_child]:
            max_child_index = right_child

        # If the parent node is smaller than its children, swap
        if array[index] < array[max_child_index]:
            swap(array, index, max_child_index)

            # Bubble the node down the tree until it
            # matches the criteria of a max heap
            index = max_child_index
        else:
            break


def heap_sort(array):
    size = len(array)

    # Heapify the input array (bottom-up)
    for i in range(size - 1, -1, -1):
        heapify(array, size,  i)

    # Replace the root node with the lowest, right-most child
    # Decrease the size of the unsorted array
    while size > 0:
        swap(array, 0, size - 1)
        size = size - 1

        heapify(array, size, 0)


def main():
    # Array to be sorted
    array = sys.argv[1].split(',')
    array = [int(elem) for elem in array]

    # Ensure that the input array is not empty
    if len(array) < 0:
        print("Please provide a non-empty input array")
        return
    
    # Sort the input array from smallest to largest
    heap_sort(array)
    print(array)


if __name__ == "__main__":
    main()