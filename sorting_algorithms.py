def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    # Implement bubble sort
    pass


def insertion_sort(arr):
    # Implement insertion sort
    pass


def merge_sort(arr):
    # Implement merge sort
    pass


def quick_sort(arr):
    # Implement quick sort
    pass


def heap_sort(arr):
    # Implement heap sort
    pass


def comb_sort(arr):
    # Implement comb sort
    pass
