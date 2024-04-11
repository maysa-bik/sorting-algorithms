import tkinter as tk
import threading
import time
import random
import matplotlib.colors as mcolors
import colorsys
from sorting import tri_selection, tri_bulles, tri_insertion, tri_fusion, tri_rapide, tri_par_tas, tri_a_peigne

class ColorWheelSorter:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Wheel Sorter")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black')
        self.canvas.pack()

        self.colors = self.generate_random_colors()
        self.draw_circle()

        self.algorithms = [("Selection Sort", tri_selection), ("Bubble Sort", tri_bulles), ("Insertion Sort", tri_insertion),("Fusion Sort", tri_fusion), ("Rapide Sort", tri_rapide), ("Tas Sort", tri_par_tas), ("Peigne Sort", tri_a_peigne)]
        self.results = {}

        self.start_button = tk.Button(self.root, text="Start Sorting", command=self.start_sorting)
        self.start_button.pack()

        # Ajouter un nouveau bouton pour mélanger les couleurs
        self.shuffle_button = tk.Button(self.root, text="Shuffle Colors", command=self.shuffle_colors)
        self.shuffle_button.pack()

        # Boutons pour chaque algorithme
        for name, _ in self.algorithms:
            button = tk.Button(self.root, text=name, command=lambda name=name: self.start_sorting(name))
            button.pack(side=tk.LEFT, padx=5, pady=5)

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

    def execute_sort_algorithm(self, algorithm_name):
        # Récupérer la fonction de tri associée au nom de l'algorithme
        algorithm_func = dict(self.algorithms)[algorithm_name]
        # Copier les couleurs pour éviter de les modifier
        colors_copy = self.colors[:]
        # Mesurer le temps d'exécution
        start_time = time.time()
        # Exécuter l'algorithme de tri
        sorted_colors = algorithm_func(colors_copy)
        end_time = time.time()
        # Calculer le temps d'exécution en secondes
        execution_time = end_time - start_time
        # Afficher le temps d'exécution dans la console
        print(f"{algorithm_name}: {execution_time:.4f} seconds")
        # Mettre à jour le cercle avec les couleurs triées
        self.update_circle(sorted_colors, algorithm_name)    



    def generate_random_colors(self):
        return [(random.uniform(0, 1), 1, 1) for _ in range(100)]

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

    def start_sorting(self, algorithm_name=None):
        self.start_button.config(state="disabled")
        # Si aucun algorithme n'est spécifié, utilisez le tri de sélection par défaut
        if algorithm_name is None:
            algorithm_name = "Selection Sort"
        # Récupérer la fonction de tri associée au nom de l'algorithme
        #algorithm_func = dict(self.algorithms)[algorithm_name]
        threading.Thread(target=self.execute_sort_algorithm, args=(algorithm_name,)).start()
        #thread.start()

    def run_algorithm(self, name, algorithm):
        start_time = time.time()
        sorted_colors = algorithm(self.colors[:])
        end_time = time.time()
        self.results[name] = end_time - start_time
        self.update_circle(sorted_colors, name)

    def update_circle(self, sorted_colors, algorithm_name):
        angle_increment = 360 / len(sorted_colors)

        for i, hsv_color in enumerate(sorted_colors):
            rgb_color = mcolors.hsv_to_rgb(hsv_color)
            start_angle = i * angle_increment
            end_angle = (i + 1) * angle_increment
            fill_color = "#{:02x}{:02x}{:02x}".format(int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255))

            # Vérifier s'il y a déjà un arc de couleur à cet indice
            item_id = f"color_arc_{i}"
            if self.canvas.find_withtag(item_id):
                # Mettre à jour la couleur de l'arc existant
                self.canvas.itemconfig(item_id, fill=fill_color)
            else:
                # Créer un nouvel arc de couleur
                self.canvas.create_arc(400 - 250, 300 - 250, 400 + 250, 300 + 250,
                                    start=start_angle, extent=angle_increment, style=tk.PIESLICE, fill=fill_color, outline='', tag=item_id)

        self.root.update()

    def update_interface(self):
        self.start_button.config(state="normal")
        for i, (name, _) in enumerate(self.algorithms):
            self.labels[i].config(text=f"{name}: {self.results.get(name, 'N/A'):.2f} sec")    

    def generer_couleurs(self,liste):
        hsv = [(x/len(liste), 1, 1) for x in liste]
        rgb = [colorsys.hsv_to_rgb(*x) for x in hsv]
        return rgb

    def temps_execution(self, fonction, *args, **kwargs):
        debut = time.time()
        fonction(*args, **kwargs)
        fin = time.time()
        temps_execution = fin - debut
        return temps_execution

def main():
    root = tk.Tk()
    app = ColorWheelSorter(root)
    root.mainloop()

if __name__ == "__main__":
    main()

