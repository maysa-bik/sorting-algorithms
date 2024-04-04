from sorting_algorithms import selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort, comb_sort


def main():
    arr = [5, 3, 8, 6, 7, 2]
    print("Array before sorting: ", arr)

    print("1. Tri par sélection")
    print("2. Tri à bulles")
    print("3. Tri par insertion")
    print("4. Tri fusion")
    print("5. Tri rapide")
    print("6. Tri par tas")
    print("7. Tri à peigne")

    sorting_algorithms = {
        '1': selection_sort,
        '2': bubble_sort,
        '3': insertion_sort,
        '4': merge_sort,
        '5': quick_sort,
        '6': heap_sort,
        '7': comb_sort,
    }

    choice = input("Choisissez un algorithme de tri: ")

    sorting_algorithm = sorting_algorithms.get(choice)

    if sorting_algorithm is not None:
        sorting_algorithm(arr)
        print("Array after sorting: ", arr)
    else:
        print("Choix non valide")
        main()


if __name__ == "__main__":
    print("Sorting algorithms")
    main()
