from ttkthemes.themed_tk import ThemedTk

from app.sorting_visualizer import SortingVisualizer

if __name__ == "__main__":
    root = ThemedTk(theme="THEME")
    app = SortingVisualizer(root)
    root.configure(bg='white')
    root.mainloop()
