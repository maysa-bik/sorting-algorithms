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

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black')
        self.canvas.pack()

        self.colors = self.generate_random_colors()
        self.draw_circle()

        self.algorithms = [("Selection Sort", tri_selection), ("Bubble Sort", tri_bulles), ("Insertion Sort", tri_insertion)]
        self.results = {}

        self.start_button = tk.Button(self.root, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack()

        # Ajouter un nouveau bouton pour mélanger les couleurs
        self.shuffle_button = tk.Button(self.root, text="Shuffle Colors", command=self.shuffle_colors)
        self.shuffle_button.pack()

        self.labels = []
        for i, (name, _) in enumerate(self.algorithms):
            label = tk.Label(self.root, text=f"{name}: ")
            label.pack()
            self.labels.append(label)


    def shuffle_colors(self):
        # Générer de nouvelles couleurs aléatoires
        self.colors = self.generate_random_colors()
        # Redessiner le cercle avec les nouvelles couleurs
        self.draw_circle()
        # Mettre à jour l'affichage
        self.root.update()

    def generate_random_colors(self):
        return [(random.uniform(0, 1), 1, 1) for _ in range(200)]

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
        self.start_button.config(state="disabled")
        threads = []
        for name, algorithm in self.algorithms:
            thread = threading.Thread(target=self.run_algorithm, args=(name, algorithm))
            threads.append(thread)
            thread.start()

        self.root.after(100, self.update_interface)

    def run_algorithm(self, name, algorithm):
        start_time = time.time()
        sorted_colors = algorithm(self.colors[:])
        end_time = time.time()
        self.results[name] = end_time - start_time

        self.update_circle(sorted_colors, name)

    def update_circle(self, sorted_colors, algorithm_name):
        self.canvas.delete("color_arcs")

        angle_increment = 360 / len(sorted_colors)

        for i, hsv_color in enumerate(sorted_colors):
            rgb_color = mcolors.hsv_to_rgb(hsv_color)
            start_angle = i * angle_increment
            end_angle = (i + 1) * angle_increment
            fill_color = "#{:02x}{:02x}{:02x}".format(int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255))
            self.canvas.create_arc(400 - 250, 300 - 250, 400 + 250, 300 + 250,
                                    start=start_angle, extent=angle_increment, style=tk.PIESLICE, fill=fill_color, outline='')

        self.root.update()

    def update_interface(self):
        self.start_button.config(state="normal")
        for i, (name, _) in enumerate(self.algorithms):
            self.labels[i].config(text=f"{name}: {self.results.get(name, 'N/A'):.2f} sec")

def main():
    root = tk.Tk()
    app = ColorWheelSorter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
