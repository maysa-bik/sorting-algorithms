import random
import time
import tkinter as tk
from tkinter import ttk

import mplcursors
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tktooltip import ToolTip

from sorting import selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort, comb_sort

# Constants
BG_COLOR = 'lavender'
BUTTON_COLOR = 'plum1'
BUTTON_ACTIVE_COLOR = 'plum2'
THEME = "scidpurple"


class SortingVisualizer:
    def __init__(self, root):
        self.completion_label = None
        self.sorting_in_progress = False
        self.sorting_generator = None
        self.connection_id = None
        self.cursor = None
        self.root = root
        self.sorting_algorithms = {
            'Selection Sort': selection_sort,
            'Bubble Sort': bubble_sort,
            'Insertion Sort': insertion_sort,
            'Merge Sort': merge_sort,
            'Quick Sort': quick_sort,
            'Heap Sort': heap_sort,
            'Comb Sort': comb_sort
        }
        self.data = [random.randint(1, 100) for _ in range(50)]
        self.fig = Figure(figsize=(5, 5))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()
        self.draw_data()
        self.setup_ui()

    def setup_ui(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X)

        self.num_var = tk.IntVar(value=50)
        num_label = tk.Label(control_frame, text="Number of elements")
        num_label.pack(side=tk.LEFT, expand=True, anchor='center')
        num_entry = tk.Entry(control_frame, textvariable=self.num_var)
        num_entry.pack(side=tk.LEFT, expand=True, anchor='center')

        buttons = {}

        button_commands = {
            "Generate": self.generate_data,
        }

        for button_text, command in button_commands.items():
            button = tk.Button(control_frame, text=button_text, command=command)
            button.pack(side=tk.LEFT, expand=True, anchor='center')
            button.configure(bg=BUTTON_COLOR, activebackground=BUTTON_ACTIVE_COLOR)
            buttons[button_text] = button

        self.algo_var = tk.StringVar(value='Bubble Sort')
        algo_dropdown = ttk.Combobox(control_frame, textvariable=self.algo_var,
                                     values=list(self.sorting_algorithms.keys()))
        algo_dropdown.pack(side=tk.LEFT, expand=True, anchor='center')

        button_commands = {
            "Sort": self.sort_data,
            "Visualize Sort": self.visualize_sort_data
        }

        for button_text, command in button_commands.items():
            button = tk.Button(control_frame, text=button_text, command=command)
            button.pack(side=tk.LEFT, expand=True, anchor='center')
            button.configure(bg=BUTTON_COLOR, activebackground=BUTTON_ACTIVE_COLOR)
            buttons[button_text] = button

        self.message_frame = tk.Frame(self.root)
        self.message_frame.pack(fill=tk.BOTH, expand=True)

        self.time_label = tk.Label(self.message_frame, text="Try sorting the data!")
        self.time_label.pack()

        control_frame.configure(bg=BG_COLOR)
        self.message_frame.configure(bg=BG_COLOR)
        num_label.configure(bg=BG_COLOR)
        num_entry.configure(bg='white')
        self.time_label.configure(bg=BG_COLOR)
        algo_dropdown.configure(style='TCombobox', background='white')

        ToolTip(num_entry, msg="Enter the number of elements to generate")
        ToolTip(buttons["Generate"], msg="Generate random data")
        ToolTip(algo_dropdown, msg="Select a sorting algorithm")
        ToolTip(buttons["Sort"], msg="Sort the data")
        ToolTip(buttons["Visualize Sort"], msg="Visualize the sorting process")

    def draw_data(self):
        self.ax.clear()
        colors = [(1, 0.75 - (i / max(self.data) * 0.75), 0.8 + (i / max(self.data) * 0.2)) for i in self.data]
        bars = self.ax.bar(range(1, len(self.data) + 1), self.data, color=colors)
        self.ax.set_xlim([0, len(self.data) + 1])
        self.canvas.draw()

        self.cursor = mplcursors.cursor(bars, hover=mplcursors.HoverMode.Transient)
        self.connection_id = self.cursor.connect(
            "add",
            lambda sel: (
                sel.annotation.set_bbox(dict(facecolor='#F9B4F6', edgecolor='purple', boxstyle='round,pad=0.5')),
                sel.annotation.set_color('#AE388B')
            )
        )

    def sort_data(self):
        self.sorting_in_progress = False
        selected_algo = self.algo_var.get()
        start_time = time.time()
        sorting_generator = self.sorting_algorithms[selected_algo](self.data.copy())
        self.data = list(sorting_generator)[-1]  # Consume the iterator and get the final sorted list
        end_time = time.time()
        execution_time = end_time - start_time
        if execution_time < 1:
            execution_time = round(execution_time * 1000, 2)
            time_unit = "milliseconds"
        else:
            execution_time = round(execution_time, 2)
            time_unit = "seconds"
        self.time_label.config(text=f"Execution time of {selected_algo}: {execution_time} {time_unit}")
        self.draw_data()

    def visualize_sort_data(self):
        self.sorting_in_progress = True
        selected_algo = self.algo_var.get()
        self.sorting_generator = self.sorting_algorithms[selected_algo](self.data.copy())
        self.root.after(100, self.update_sort_visualization)

    def update_sort_visualization(self):
        if not self.sorting_in_progress:
            return
        try:
            self.data = next(self.sorting_generator)
            self.draw_data()
            self.root.after(100, self.update_sort_visualization)
        except StopIteration:
            self.sorting_in_progress = False
            self.completion_label = tk.Label(self.message_frame, text="Sorting visualization is complete.")
            self.completion_label.pack()
            self.completion_label.configure(bg='lavender', fg='purple')

    def generate_data(self):
        self.sorting_in_progress = False
        self.data = [random.randint(1, 100) for _ in range(self.num_var.get())]
        self.draw_data()
