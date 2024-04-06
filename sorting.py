# Tri par insertion
def tri_insertion(liste):
    for i in range (1, len(liste)):
        cle = liste[i]
        j = i - 1

        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1

        liste[j + 1] = cle

    return liste

