# Fonction principale pour démarrer l'applicaation
from Sortings import*
def main():
    root = tk.Tk()
    app = ColorWheelSorter(root)
    #app.update_interface_with_sorting_times()
    root.mainloop()
    

# Vérifier si le script est exécuté en tant que programme principal
if __name__ == "__main__":
    main()



