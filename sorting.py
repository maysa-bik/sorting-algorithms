"""
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
    # Traverse through all array elements
    for i in range(len(arr)):
        # Last i elements are already sorted
        for j in range(0, len(arr) - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
"""

"""
tri par selection
"""
def tri_selection(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
"""
tri par bubble
"""
def tri_bulles(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Last i elements are already sorted
        for j in range(0, len(arr) - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

"""
# Tri par insertion
[5,3,8,6,9]

[5, 3,8,6,9]
[3,5, 8,6,9]
[3,5,8, 6,9]
[3,5,6,8, 9]
[",5,6,8,9]
"""
def tri_insertion(arr):
    for i in range (1, len(arr)):
        cle = arr[i]
        j = i - 1

        while j >= 0 and cle < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = cle

    return arr

"""
tri par fusion
"""


"""
tri par rapide
"""


"""
tri par tas
"""
# Tri par tas
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

"""
tri à peigne
"""

# Tri à peigne
def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

