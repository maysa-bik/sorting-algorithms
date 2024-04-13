def selection_sort(arr: list):
    """Iteratively selects the smallest element from the unsorted segment and swaps it with the first unsorted item."""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr
    yield arr


def bubble_sort(arr: list):
    """Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            yield arr
        if not swapped:
            break
    yield arr


def insertion_sort(arr: list):
    """Builds the final sorted array one item at a time by inserting each element into its proper place."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr
        arr[j + 1] = key
    yield arr


def merge_sort(arr: list):
    """Divides the array into halves, sorts each half, and merges them back together."""
    if len(arr) <= 1:
        yield arr
        return
    mid = len(arr) // 2
    left_half, right_half = list(merge_sort(arr[:mid]))[-1], list(merge_sort(arr[mid:]))[-1]
    arr = []
    while left_half and right_half:
        if left_half[0] < right_half[0]:
            arr.append(left_half.pop(0))
        else:
            arr.append(right_half.pop(0))
        yield arr
    arr.extend(left_half or right_half)
    yield arr


def quick_sort(arr: list, low=0, high=None):
    """Picks a pivot, partitions the array into elements less than and greater than the pivot, and recursively sorts the sub-arrays."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = yield from partition(arr, low, high)
        yield from quick_sort(arr, low, pi - 1)
        yield from quick_sort(arr, pi + 1, high)
    yield arr


def partition(arr, low, high):
    """Helper function for quick_sort to perform the partitioning."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr
    return i + 1


def heap_sort(arr: list):
    """Converts the array into a heap and repeatedly extracts the maximum element to sort the array."""

    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
        yield arr
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
        yield arr


def comb_sort(arr: list):
    """Improves on bubble sort by using a larger gap between compared elements, which reduces to 1 in the end."""
    gap = len(arr)
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            yield arr
            i += 1


def get_sorting_algorithm(name: str):
    """Dictionary to fetch the sorting function based on the provided algorithm name."""
    algorithms = {
        'Selection Sort': selection_sort,
        'Bubble Sort': bubble_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort,
        'Heap Sort': heap_sort,
        'Comb Sort': comb_sort
    }
    return algorithms.get(name)
