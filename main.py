"""
# main.py

from sorting import tri_insertion

# Liste non triée
list = [64, 25, 12, 22, 11]
print("liste avant le tri", list)

# Appel de la fonction de tri par sélection
tri_insertion(list)

# Affichage de la liste triée
print("Liste triée:")
print(list)
"""

import tkinter as tk

def draw_circle(canvas, x, y, radius, color, number):
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
    canvas.create_text(x, y, text=str(number), fill='white', font=('Arial', 12))

def main():
    root = tk.Tk()
    root.title("Grand Cercle Coloré avec Numéros")

    canvas = tk.Canvas(root, width=400, height=400, bg='white')
    canvas.pack()

    # Paramètres du cercle
    circle_radius = 150
    circle_x = 200
    circle_y = 200

    # Dessiner le cercle
    draw_circle(canvas, circle_x, circle_y, circle_radius, 'blue', 1)

    root.mainloop()

if __name__ == "__main__":
    main()




