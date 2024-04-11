import tkinter as tk
import colorsys
from math import cos, sin, pi, radians
import random
import time

class TriGraphique:
    def __init__(self):
        self.fenetre = tk.Tk()
        self.canvas = tk.Canvas(self.fenetre, width=800, height=700)
        self.canvas.pack()

        self.liste = self.generer_liste(100)
        self.couleurs = self.generer_couleurs(self.liste)
        self.roue = self.creer_roue(self.couleurs)

        self.create_buttons()

    def generer_liste(self, n):
        return list(range(1, n+1))

    def generer_couleurs(self, liste):
        hsv = [(x/len(liste), 1, 1) for x in liste]
        rgb = [colorsys.hsv_to_rgb(*x) for x in hsv]
        return rgb

    def creer_roue(self, couleurs):
        x = 400
        y = 400
        r = 200
        for i in range(len(couleurs)):
            angle = radians(i/len(couleurs) * 360)
            x1 = x + r * cos(angle)
            y1 = y + r * sin(angle)
            x2 = x + r * cos(angle + 2 * pi / len(couleurs))
            y2 = y + r * sin(angle + 2 * pi / len(couleurs))
            self.canvas.create_polygon(x, y, x1, y1, x2, y2, fill=f"#{int(couleurs[i][0]*255):02x}{int(couleurs[i][1]*255):02x}{int(couleurs[i][2]*255):02x}")

    def create_buttons(self):
        self.selection_button = tk.Button(self.fenetre, text="Tri par sélection", command=self.tri_par_selection)
        self.selection_button.pack()

        self.bubble_button = tk.Button(self.fenetre, text="Tri à bulles", command=self.tri_a_bulles)
        self.bubble_button.pack()

    def tri_par_selection(self):
        temps_execution = self.calculer_temps_execution(self.tri_selection, self.liste)
        print(f"Temps d'exécution pour Tri par sélection: {temps_execution} secondes")

    def tri_a_bulles(self):
        temps_execution = self.calculer_temps_execution(self.tri_bulles, self.liste)
        print(f"Temps d'exécution pour Tri à bulles: {temps_execution} secondes")

    def tri_selection(self, liste):
        n = len(liste)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if liste[j] < liste[min_idx]:
                    min_idx = j
            liste[i], liste[min_idx] = liste[min_idx], liste[i]
        return liste

    def tri_bulles(self, liste):
        n = len(liste)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if liste[j] > liste[j+1]:
                    liste[j], liste[j+1] = liste[j+1], liste[j]
        return liste

    def calculer_temps_execution(self, tri, liste):
        debut = time.time()
        tri(liste)
        fin = time.time()
        return fin - debut

    def run(self):
        self.fenetre.mainloop()

# Utilisation de la classe
tri_graphique = TriGraphique()
tri_graphique.run()
