import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter_tabs import Tab, TabBar
from sys import exit
from variant import Variant
from plot import Plot


class Window:
    def __init__(self, master):
        """
        Creates the main window with all widgets needed.
        :param master: the window where the content should be placed
        """
        self.root = master
        bar = TabBar(self.root, "graph")
        fun_label = tk.Label(self.root, text="Differential Equation: y'=xy^2-3xy", font=("Courier", 30))
        fun_label.pack()

        # Create form below
        form = tk.Frame(self.root)

        x0_label = tk.Label(form, text="x0")
        x0_label.pack()

        x0 = tk.Entry(form, width=30)
        x0.insert(tk.END, str(Variant.x0))
        x0.pack()

        y0_label = tk.Label(form, text="y0")
        y0_label.pack()

        y0 = tk.Entry(form, width=30)
        y0.insert(tk.END, str(Variant.y0))
        y0.pack()

        x_label = tk.Label(form, text="X")
        x_label.pack()

        x = tk.Entry(form, width=30)
        x.insert(tk.END, str(Variant.x))
        x.pack()

        h_label = tk.Label(form, text="Grid step")
        h_label.pack()

        h = tk.Entry(form, width=30)
        h.insert(tk.END, str(Variant.h))
        h.pack()

        button = tk.Button(master=form,
                           text='Plot',
                           command=lambda: self.plot.redraw(x0, y0, x, h, canvas),
                           bg="white")
        button.pack()

        button = tk.Button(master=form,
                           text='Quit',
                           command=exit,
                           bg="white")
        button.pack()
        # Print author's name
        author = tk.Label(form, text="Author: Temur Kholmatov B17-5")
        author.pack(side=tk.RIGHT, fill=tk.X)

        form.pack(side=tk.BOTTOM, fill=tk.X)

        # Create graph tab
        graph = Tab(self.root, 'graph')

        # Draw graph and put its figure into a canvas
        self.plot = Plot()
        self.plot.draw()
        canvas = FigureCanvasTkAgg(plt.gcf(), master=graph)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,
                                    fill=tk.BOTH,
                                    expand=tk.YES)

        # Create table tab
        table = Tab(self.root, 'table')

        bar.add(graph)
        bar.add(table)
        bar.show()
