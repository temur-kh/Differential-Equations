import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter_tabs import Tab, TabBar
from sys import exit
from variant import Variant
from plot import draw_graph
from pandastable import Table, TableModel


class ApplicationWindow:
    def __init__(self, master):
        """
        Creates the main window with all widgets needed.
        :param master: the window where the content should be placed
        """
        self.root = master
        bar = TabBar(self.root, "graph")
        fun_label = tk.Label(self.root, text="Differential Equation: y'=xy^2-3xy", font=("Courier", 30))
        fun_label.pack()

        # Create the form
        self.create_form()

        # Create the graph tab
        graph_tab = Tab(self.root, 'graph')

        # Draw a graph and put its figure into a canvas
        df = draw_graph()
        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=graph_tab)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP,
                                         fill=tk.BOTH,
                                         expand=tk.YES)

        # Create the table tab and put a table inside it
        table_tab = Tab(self.root, 'table')
        self.table = Table(table_tab, dataframe=df, showtoolbar=True)
        self.table.show()

        bar.add(graph_tab)
        bar.add(table_tab)
        bar.show()

    def update(self, x0, y0, x, h):
        x0_new, y0_new, x_new, h_new = float(x0.get()), float(y0.get()), float(
            x.get()), float(h.get())
        if x0_new < x_new and (x_new - x0_new) / h_new <= 10000:
            plt.gca().clear()
            df = draw_graph(x0_new, y0_new, x_new, h_new, plt.gca())
            self.canvas.draw()
            self.table.updateModel(TableModel(df))
            self.table.show()

    def create_form(self):
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
                           command=lambda: self.update(x0, y0, x, h),
                           bg="white")
        button.pack()

        button = tk.Button(master=form,
                           text='Quit',
                           command=exit,
                           bg="white")
        button.pack()

        author = tk.Label(form, text="Author: Temur Kholmatov B17-5")
        author.pack(side=tk.RIGHT, fill=tk.X)

        form.pack(side=tk.BOTTOM, fill=tk.X)
