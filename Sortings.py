import tkinter as tk
import threading
import time
import random
import matplotlib.colors as mcolors

class ColorWheelSorter:
    # Initialisation de l'interface utilisateur avec le canevas, les boutons et les algorithmes de tri
    # ainsi que la création des variables et des widgets nécessaires
    def __init__(self, root):
        self.root = root
        self.root.title("Color Wheel Sorter")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black')
        self.canvas.pack()

        self.colors = self.generate_random_colors()
        self.draw_circle()

        # Créer une étiquette pour afficher le temps d'exécution
        self.execution_time_label = tk.Label(self.root, text="")
        self.execution_time_label.pack()

        self.algorithms = [("Selection Sort", self.tri_selection), 
                           ("Bubble Sort", self.tri_bulles), 
                           ("Insertion Sort", self.tri_insertion),
                           ("Fusion Sort", self.tri_fusion), 
                           ("Rapide Sort", self.tri_rapide), 
                           ("Tas Sort", self.tri_par_tas), 
                           ("Peigne Sort", self.tri_a_peigne)]
        self.results = {}

        self.start_button = tk.Button(self.root, text="Commencer", command=self.start_sorting)
        self.start_button.pack()

        # Ajouter un nouveau bouton pour mélanger les couleurs
        self.shuffle_button = tk.Button(self.root, text="Remélanger Colors", command=self.shuffle_colors)
        self.shuffle_button.pack()

        # Créer une liste déroulante pour choisir l'algorithme de tri
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("Selection Sort")  # Algorithme par défaut
        self.algorithm_dropdown = tk.OptionMenu(self.root, self.algorithm_var, * [name for name, _ in self.algorithms])
        self.algorithm_dropdown.pack()

        # Ajouter un événement de souris pour le déplacement
        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag)

        # Initialiser les variables pour le déplacement
        self.drag_data = {"x": 0, "y": 0, "item": None}  
        
        self.sort_thread = None  # Variable pour stocker le thread de tri en cours
  
    # Méthode pour mélanger aléatoirement les couleurs sur le cercle
    def shuffle_colors(self):
        # Générer de nouvelles couleurs aléatoires
        self.colors = self.generate_random_colors()
        # Redessiner le cercle avec les nouvelles couleurs
        self.draw_circle()
        # Mettre à jour l'affichage
        self.root.update()


    # Méthode appelée lorsqu'un clic de souris est effectué pour démarrer le déplacement d'un élément sur le canevas
    def start_drag(self, event):
        # Trouver l'élément graphique cliqué
        item = self.canvas.find_closest(event.x, event.y)
        if item:
            self.drag_data["item"] = item[0]
            # Récupérer les coordonnées du clic de souris
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y
    
    # Méthode appelée lors du déplacement de la souris pour mettre à jour la position de l'élément déplacé
    def drag(self, event):
        if self.drag_data["item"]:
            # Calculer le déplacement
            delta_x = event.x - self.drag_data["x"]
            delta_y = event.y - self.drag_data["y"]
            # Déplacer l'élément graphique
            self.canvas.move(self.drag_data["item"], delta_x, delta_y)
            # Mettre à jour les coordonnées de référence pour le prochain déplacement
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y    

    
    # Méthode pour exécuter un algorithme de tri sélectionné et mettre à jour l'interface avec les résultats
    def execute_sort_algorithm(self, algorithm_name):
        # Récupérer la fonction de tri associée au nom de l'algorithme
        algorithm_func = dict(self.algorithms)[algorithm_name]
        # Copier les couleurs pour éviter de les modifier
        colors_copy = self.colors[:]
        # Initialiser le compteur de comparaisons
        comparisons = 0
        # Mesurer le temps d'exécution
        start_time = time.time()
        # Exécuter l'algorithme de tri
        sorted_colors = algorithm_func(colors_copy)
        end_time = time.time()
        # Calculer le temps d'exécution en secondes
        execution_time = end_time - start_time
        # Afficher le temps d'exécution dans la fenêtre Tkinter
        self.execution_time_label.config(text=f"{algorithm_name}: {execution_time:.4f} seconds")
        # Afficher le temps d'exécution dans la console
        print(f"{algorithm_name}: {execution_time:.4f} seconds")
        # Mettre à jour le cercle avec les couleurs triées
        self.update_circle(sorted_colors, algorithm_name)
        # Réactiver le bouton de démarrage une fois le tri terminé
        self.start_button.config(state="normal")

    # Méthode pour générer une liste de couleurs aléatoires au format HSV
    def generate_random_colors(self):
        return [(random.uniform(0, 1), 1, 1) for _ in range(100)]
    
    # Méthode pour dessiner le cercle avec les couleurs sur le canevas
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
    
    # Méthode pour démarrer le tri en fonction de l'algorithme sélectionné
    def start_sorting(self, algorithm_name=None):
        # Arrêter le tri en cours s'il y en a un
        self.stop_sorting()

        # Récupérer l'algorithme sélectionné à partir de la liste déroulante
        selected_algorithm = self.algorithm_var.get()
        # Lancer l'algorithme de tri sélectionné
        self.sort_thread = threading.Thread(target=self.execute_sort_algorithm, args=(selected_algorithm,))
        self.sort_thread.start()
        self.start_button.config(state="disabled")
    
    # Méthode pour arrêter le tri en cours s'il y en a un
    def stop_sorting(self):
        # Si un thread de tri est en cours, attendez qu'il se termine
        if self.sort_thread and self.sort_thread.is_alive():
            self.sort_thread.join()    
    
    # Méthode pour mettre à jour le cercle avec les couleurs triées
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

        # Mettre à jour l'affichage
        self.root.after(10, self.root.update)
    
    # Méthode pour réactiver le bouton de démarrage une fois le tri terminé
    def enable_start_button(self):
        self.start_button.config(state="normal")
        self.update_circle(self.colors, "Original Colors")
    
    # Méthode pour mesurer le temps d'exécution d'un algorithme de tri sur un ensemble de données
    def measure_sorting_time(self, algorithm_func, data):
        start_time = time.time()
        algorithm_func(data)
        end_time = time.time()
        return end_time - start_time
    
    # Méthode pour mesurer le temps d'exécution de tous les algorithmes de tri sur un ensemble de données
    def measure_sorting_times(self, data):
        times = {}
        for name, func in self.algorithms:
            times[name] = self.measure_sorting_time(func, data.copy())
        return times
    
    # Méthode pour mettre à jour l'interface utilisateur avec les temps d'exécution des algorithmes de tri
    def update_interface_with_sorting_times(self):
        data = self.generate_random_colors()
        times = self.measure_sorting_times(data)
        self.print_sorting_times(times)
        self.readme_sorting_times(times)
    
    # Méthode pour afficher les temps d'exécution des algorithmes de tri dans la console
    def print_sorting_times(self, times):
        print("Sorting Times:")
        for name, time in times.items():
            print(f"{name}: {time:.6f} seconds")
    
    # Méthode pour enregistrer les temps d'exécution des algorithmes de tri dans un fichier README.md
    def readme_sorting_times(self, times):
        with open("README.md", "a") as file:
            file.write("## Sorting Times\n\n")
            file.write("| Algorithm | Time (seconds) |\n")
            file.write("|-----------|----------------|\n")
            for name, time in times.items():
                file.write(f"| {name} | {time:.6f} |\n")    
    

    def tri_selection(self, liste):
        for i in range(len(liste)):
            min_index = i
            for j in range(i+1, len(liste)):
                if liste[j] < liste[min_index]:
                    min_index = j
            liste[i], liste[min_index] = liste[min_index], liste[i]
            # Mettre à jour l'interface graphique après chaque étape du tri
            self.update_circle(liste, "Selection Sort")
            self.root.update()
        return liste

    def tri_bulles(self, liste):
        n = len(liste)
        for i in range(n):
            for j in range(0, n-i-1):
                if liste[j] > liste[j+1]:
                    liste[j], liste[j+1] = liste[j+1], liste[j]
                    # Mettre à jour l'interface graphique après chaque étape du tri
                    self.update_circle(liste, "Bubble Sort")
                    self.root.update()
        return liste

    def tri_insertion(self, liste):
        for i in range(1, len(liste)):
            key = liste[i]
            j = i-1
            while j >=0 and key < liste[j] :
                    liste[j+1] = liste[j]
                    j -= 1
            liste[j+1] = key
            # Mettre à jour l'interface graphique après chaque étape du tri
            self.update_circle(liste, "Insertion Sort")
            self.root.update()
        return liste

    def tri_fusion(self, liste):
        if len(liste) > 1:
            mid = len(liste)//2
            L = liste[:mid]
            R = liste[mid:]
            self.tri_fusion(L)
            self.tri_fusion(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    liste[k] = L[i]
                    i += 1
                else:
                    liste[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                liste[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                liste[k] = R[j]
                j += 1
                k += 1
            # Mettre à jour l'interface graphique après chaque étape du tri
            self.update_circle(liste, "Fusion Sort")
            self.root.update()
        return liste

    def tri_rapide(self, liste):
        if len(liste) <= 1:
            return liste
        pivot = liste[len(liste) // 2]
        left = [x for x in liste if x < pivot]
        middle = [x for x in liste if x == pivot]
        right = [x for x in liste if x > pivot]
        # Mettre à jour l'interface graphique après chaque étape du tri
        self.update_circle(left + middle + right, "Rapide Sort")
        self.root.update()
        return self.tri_rapide(left) + middle + self.tri_rapide(right)

    def tri_par_tas(self, liste):
        def heapify(liste, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and liste[i] < liste[l]:
                largest = l
            if r < n and liste[largest] < liste[r]:
                largest = r
            if largest != i:
                liste[i], liste[largest] = liste[largest], liste[i]
                heapify(liste, n, largest)
        n = len(liste)
        for i in range(n, -1, -1):
            heapify(liste, n, i)
        for i in range(n-1, 0, -1):
            liste[i], liste[0] = liste[0], liste[i]
            heapify(liste, i, 0)
            # Mettre à jour l'interface graphique après chaque étape du tri
            self.update_circle(liste, "Tas Sort")
            self.root.update()
        return liste

    def tri_a_peigne(self, liste):
        n = len(liste)
        gap = n
        shrink = 1.3
        sorted = False
        while not sorted:
            gap = int(gap / shrink)
            if gap <= 1:
                gap = 1
                sorted = True
            i = 0
            while i + gap < n:
                if liste[i] > liste[i + gap]:
                    liste[i], liste[i + gap] = liste[i + gap], liste[i]
                    sorted = False
                i += 1
            # Mettre à jour l'interface graphique après chaque étape du tri
            self.update_circle(liste, "Peigne Sort")
            self.root.update()
        return liste


