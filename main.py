import tkinter as tk
import threading
import time
import random
from sorting import tri_selection, tri_bulles, tri_insertion

class ColorCircleSorter:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Circle Sorter")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='white')
        self.canvas.pack()

        self.colors = self.generate_random_colors()
        self.draw_circle()

        self.algorithms = [("Selection Sort", tri_selection), ("Bubble Sort", tri_bulles), ("Insertion Sort", tri_insertion)]
        self.results = {}

        self.start_button = tk.Button(self.root, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack()

    def generate_random_colors(self):
        return ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(50)]

    def draw_circle(self):
        center_x = 400
        center_y = 300
        radius = 250
        angle_increment = 360 / len(self.colors)

        for i, color in enumerate(self.colors):
            start_angle = i * angle_increment
            end_angle = (i + 1) * angle_increment
            self.canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                                    start=start_angle, extent=angle_increment, style=tk.PIESLICE, fill=color)

    def start_sorting(self):
        threads = []
        for name, algorithm in self.algorithms:
            thread = threading.Thread(target=self.run_algorithm, args=(name, algorithm))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Afficher les résultats
        print("Résultats des tris:")
        for name, result in self.results.items():
            print(f"{name}: {result} secondes")

    def run_algorithm(self, name, algorithm):
        start_time = time.time()
        sorted_colors = algorithm(self.colors[:])
        end_time = time.time()
        self.results[name] = end_time - start_time

        # Mettre à jour l'affichage du cercle
        self.update_circle(sorted_colors)

    def update_circle(self, sorted_colors):
        self.canvas.delete("color_arcs")  # Effacez les arcs de couleur actuels

        delay = 100  # Délai entre chaque étape de l'animation en millisecondes

        for i, colors in enumerate(sorted_colors):
            for j, color in enumerate(colors):
                start_angle = j * 360 / len(self.colors)
                end_angle = (j + 1) * 360 / len(self.colors)
                self.canvas.create_arc(50, 50, 750, 550, start=start_angle, extent=360 / len(self.colors),
                                        style=tk.PIESLICE, fill=color, tags="color_arcs")

            self.root.update()  # Mettez à jour l'affichage
            time.sleep(delay / 1000)  # Attendez le délai avant la prochaine étape

def main():
    root = tk.Tk()
    app = ColorCircleSorter(root)
    root.mainloop()

if __name__ == "__main__":
    main()




