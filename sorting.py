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
def tri_fusion(arr):
    if len(arr) <= 1:
        return arr
    else:
        milieu = len(arr) // 2
        gauche = tri_fusion(arr[:milieu])
        droite = tri_fusion(arr[milieu:])
        return fusionner(gauche, droite)

def fusionner(gauche, droite):
    resultat = []
    i = j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat

"""
tri par rapide
"""
def tri_rapide(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        moins = [x for x in arr[1:] if x <= pivot]
        plus = [x for x in arr[1:] if x > pivot]
        return tri_rapide(moins) + [pivot] + tri_rapide(plus)

"""
tri par tas
"""
# Tri par tas
def entasser_tas(arr, n, i):
    plus_grand = i
    gauche = 2 * i + 1
    droite = 2 * i + 2

    if gauche < n and arr[gauche] > arr[plus_grand]:
        plus_grand = gauche

    if droite < n and arr[droite] > arr[plus_grand]:
        plus_grand = droite

    if plus_grand != i:
        arr[i], arr[plus_grand] = arr[plus_grand], arr[i]
        entasser_tas(arr, n, plus_grand)

def tri_par_tas(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        entasser_tas(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        entasser_tas(arr, i, 0)


"""
tri à peigne
"""

# Tri à peigne
def tri_a_peigne(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    trie = False

    while not trie:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            trie = True
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                trie = False
            i += 1


