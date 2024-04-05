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

liste_exemple = [22, 27, 16, 2, 18, 6]
print("liste avant le tri", liste_exemple)

liste_triee = tri_insertion(liste_exemple)
print("Liste après le tri:", liste_triee)