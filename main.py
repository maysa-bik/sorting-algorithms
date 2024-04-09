import tkinter as tk
import threading
import time
import random
import numpy as np
import matplotlib.colors as mcolors

from sorting import tri_bulles, tri_insertion, tri_selection

class ColorWheelSorter:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Wheel Sorter")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='white')  # Changer la couleur de fond à 'white'
        self.canvas.pack()

        self.colors = self.generate_random_colors()
        self.draw_circle()

        self.algorithms = [("Selection Sort", tri_selection), ("Bubble Sort", tri_bulles), ("Insertion Sort", tri_insertion)]
        self.results = {}

        self.start_button = tk.Button(self.root, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack()

    def generate_random_colors(self):
        return [(random.uniform(0, 1), 1, 1) for _ in range(50)]  # Générer des valeurs HSV aléatoires

    def draw_circle(self):
        center_x = 400
        center_y = 300
        radius = 250
        angle_increment = 360 / len(self.colors)

        for i, hsv_color in enumerate(self.colors):
            rgb_color = mcolors.hsv_to_rgb(hsv_color)
            start_angle = i * angle_increment
            end_angle = (i + 1) * angle_increment
            fill_color = "#{:02x}{:02x}{:02x}".format(int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255))
            self.canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                                    start=start_angle, extent=angle_increment, style=tk.PIESLICE, fill=fill_color, outline='')

    def start_sorting(self):
        self.start_button.config(state="disabled")  # Désactiver le bouton pendant le tri
        threads = []
        for name, algorithm in self.algorithms:
            thread = threading.Thread(target=self.run_algorithm, args=(name, algorithm))
            threads.append(thread)
            thread.start()

        # Planifier la mise à jour de l'interface utilisateur après l'exécution des algorithmes de tri
        self.root.after(100, self.update_interface)

    def run_algorithm(self, name, algorithm):
        start_time = time.time()
        sorted_colors = algorithm(self.colors[:])
        end_time = time.time()
        self.results[name] = end_time - start_time

        # Mettre à jour l'affichage du cercle
        self.update_circle(sorted_colors)

    def update_circle(self, sorted_colors):
        self.canvas.delete("color_arcs")  # Effacer les arcs de couleur actuels

        angle_increment = 360 / len(sorted_colors)

        for i, hsv_color in enumerate(sorted_colors):
            rgb_color = mcolors.hsv_to_rgb(hsv_color)
            start_angle = i * angle_increment
            end_angle = (i + 1) * angle_increment
            fill_color = "#{:02x}{:02x}{:02x}".format(int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255))
            self.canvas.create_arc(400 - 250, 300 - 250, 400 + 250, 300 + 250,
                                    start=start_angle, extent=angle_increment, style=tk.PIESLICE, fill=fill_color, outline='')

        self.root.update()  # Mettre à jour l'affichage

    def update_interface(self):
        self.start_button.config(state="normal")  # Activer à nouveau le bouton après le tri

def main():
    root = tk.Tk()
    app = ColorWheelSorter(root)
    root.mainloop()

if __name__ == "__main__":
    main()










