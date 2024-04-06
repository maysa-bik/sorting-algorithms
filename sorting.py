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

def tri_bubble(arr):
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
def tri_insertion(liste):
    for i in range (1, len(liste)):
        cle = liste[i]
        j = i - 1

        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1

        liste[j + 1] = cle

    return liste


