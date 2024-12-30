import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import json

def load_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def plot_graphs(data):
    root = tk.Tk()
    root.title("Movement Analysis Report")

    tab_control = ttk.Notebook(root)

    # Create tabs for each metric
    tabs = {}
    for metric in data.keys():
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text=metric)
        tabs[metric] = tab

    tab_control.pack(expand=1, fill='both')

    for metric, values in data.items():
        fig, ax = plt.subplots()
        ax.plot(values, marker='o')
        ax.set_title(metric)
        ax.set_xlabel('Frame')
        ax.set_ylabel(metric)

        canvas = FigureCanvasTkAgg(fig, master=tabs[metric])
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    root.mainloop()

