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


def tri_insertion(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0.i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def tri_fusion(arr):
        # If the array has one or no elements, it is already sorted
        if len(arr) <= 1:
            return arr

        # Find the middle of the array
        mid = len(arr) // 2

        # Recursively sort the left and right halves
        left = tri_fusion(arr[:mid])
        right = tri_fusion(arr[mid:])

        # Initialize an empty list to hold the merged array
        merged = []

        # While there are elements in either left or right
        while left and right:
            # If the first element of left is smaller or equal, append it to the merged list
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            # Otherwise, append the first element of right
            else:
                merged.append(right.pop(0))

        # If there are remaining elements in either left or right, append them
        merged.extend(left if left else right)

        return merged


def tri_rapide(arr):
    # If the array has one or no elements, it is already sorted
    if len(arr) <= 1:
        return arr
    # Choose the middle element as the pivot
    pivot = arr[len(arr) // 2]
    # Partition the array into three parts: less than pivot, equal to pivot, greater than pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Recursively sort the left and right parts and concatenate the results
    return tri_rapide(left) + middle + tri_rapide(right)

def tri_par_tas(arr):
    # Import the heapq module
    import heapq
    # Transform the array into a heap
    heapq.heapify(arr)
    # Pop elements from the heap until it is empty
    return [heapq.heappop(arr) for _ in range(len(arr))]

def tri_a_peigne(arr):
    # Initialize the gap and the shrink factor
    gap = len(arr)
    shrink = 1.3
    # Initialize the is_sorted flag as False
    is_sorted = False
    # While the array is not sorted
    while not is_sorted:
        # Update the gap
        gap = int(gap / shrink)
        # If the gap is 1, the array is sorted
        if gap <= 1:
            gap = 1
            is_sorted = True
        # Initialize the index
        i = 0
        # While there are elements at index i and i + gap
        while i + gap < len(arr):
            # If the element at index i is greater than the one at i + gap, swap them
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                # The array is not sorted
                is_sorted = False
            # Increment the index
            i += 1
    # Return the sorted array
    return arr