import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter_tabs import Tab, TabBar
from sys import exit
from variant import Variant
from plot import Plot
from pandastable import Table, TableModel


class ApplicationWindow(tk.Frame):

    def __init__(self, master):
        """
        Creates the main window with all widgets needed.
        :param master: the window where the content should be placed
        """
        tk.Frame.__init__(self, master)
        self.plot = Plot()
        self.bar = TabBar(self, "graph")
        fun_label = tk.Label(self, text="Differential Equation: y'=xy^2-3xy", font=("Times New Roman", 30))
        fun_label.pack()

        self.highlight_color = '#40A9CF'
        self.def_config = {
            'background': 'white',
        }

        self.btn_config = {
            'background': 'white',
            'highlightbackground': self.highlight_color,
            'foreground': 'black',
        }

        # Create the form
        self.create_form()

        # Create the graph tab
        graph_tab = Tab(self, 'graph')

        # Draw a graph and put its figure into a canvas
        df = self.plot.draw_functions(ax=plt.figure(1).gca())
        self.canvas1 = FigureCanvasTkAgg(plt.figure(1), master=graph_tab)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack(side=tk.TOP,
                                          fill=tk.BOTH,
                                          expand=tk.YES)

        # Create the errors tab
        errors_tab = Tab(self, 'errors')

        # Draw an errors graph and put its figure into a canvas
        self.plot.draw_errors(ax=plt.figure(2).gca())
        self.canvas2 = FigureCanvasTkAgg(plt.figure(2), master=errors_tab)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack(side=tk.TOP,
                                          fill=tk.BOTH,
                                          expand=tk.YES)

        # Create the table tab and put a table inside it
        table_tab = Tab(self, 'table')
        width, height = self.canvas1.get_width_height()
        self.table = Table(table_tab, dataframe=df, width=width-60, height=height-20, editable=False, cellwidth=188)
        self.table.colselectedcolor = self.table.rowselectedcolor = self.highlight_color
        self.table.show()

        self.set_config([self, self.bar, fun_label, graph_tab, errors_tab, table_tab], self.def_config)

        # Add tabs to the tab bar
        self.bar.add(graph_tab, self.btn_config)
        self.bar.add(errors_tab, self.btn_config)
        self.bar.add(table_tab, self.btn_config)
        self.bar.show()

    def update_window(self, x0, y0, x, h):
        """
        Updates the graphs and the table accroding to the given data
        :param x0: initial position on x-axis
        :param y0: f(x0)
        :param x: final position on x-axis
        :param h: a grid step
        :return: None
        """
        x0_new, y0_new, x_new, h_new = float(x0.get()), float(y0.get()), float(x.get()), float(h.get())
        if x0_new < x_new and h_new > 0 and (x_new - x0_new) / h_new <= 10000:
            plt.figure(1).gca().clear()
            plt.figure(2).gca().clear()
            df = self.plot.draw_functions(plt.figure(1).gca(), x0_new, y0_new, x_new, h_new)
            self.canvas1.draw()
            self.plot.draw_errors(plt.figure(2).gca(), x0_new, y0_new, x_new, h_new)
            self.canvas2.draw()
            self.table.updateModel(TableModel(df))
            self.table.show()

    def create_form(self):
        """
        Creates the form for changing the initial data
        :return: None
        """
        form = tk.Frame(self)

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

        btn_plot = tk.Button(master=form, text='Plot', command=lambda: self.update_window(x0, y0, x, h))
        btn_plot.pack()

        btn_quit = tk.Button(master=form, text='Quit', command=exit)
        btn_quit.pack()

        author = tk.Label(form, text="Author: Temur Kholmatov B17-5")
        author.pack(side=tk.RIGHT, fill=tk.X)

        self.set_config([form, x0_label, y0_label, x_label, h_label, author], self.def_config)
        self.set_config([x0, y0, x, h, btn_plot, btn_quit], self.btn_config)

        form.pack(side=tk.BOTTOM, fill=tk.X)

    @staticmethod
    def set_config(widgets, config):
        """
        Sets the config of widgets
        :param widgets: widgets for changing the bg color
        :param config: configs to be set for widgets
        :return: None
        """
        for widget in widgets:
            widget.configure(**config)
