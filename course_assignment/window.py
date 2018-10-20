from methods import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter_tabs import Tab, TabBar
from sys import exit
e = 2.71828182846


class Variant:
    # initial conditions of variant #25
    x0 = 0.
    y0 = 2.
    x = 6.4
    h = 0.1

    @staticmethod
    def func(x, y):
        """
        Function of the o.d.e. of variant #25
        :param x: x-value
        :param y: y-value
        :return: result of function
        """
        try:
            return x * (y ** 2) - 3 * x * y
        except OverflowError:
            return float('inf')

    @staticmethod
    def solution(x_list):
        """
        Get the list of x-values and output y-values using analytical solution
        :param x_list: x-values
        :return: y-values
        """
        def solve(x_i):
            """
            Analytical solution to the o.d.e.
            :param x_i: x-value
            :return: y-value
            """
            try:
                return 6.0 / (2 + e ** (3 * (x_i ** 2) / 2.0))
            except OverflowError:
                return 0.0

        y_list = []
        for x in x_list:
            y_list.append(solve(x))
        return y_list


class Plot:
    @staticmethod
    def draw(x0=Variant.x0, y0=Variant.y0, x=Variant.x, h=Variant.h, ax=None):
        """
        Draw the graph of function using given parameters.
        :param x0: initial position on x-axis
        :param y0: f(x0)
        :param x: final position on x-axis
        :param h: a grid step
        :param ax: object of class matplotlib.axes.Axes
        :return: None
        """
        print("Differential Eq: y'=xy^2-3xy")
        print('Initial condition: y({})={}'.format(x0, y0))
        print('Range: [{},{}]'.format(x0, x))
        print('Grid step: {}'.format(h))
        print()

        dic = dict()
        x_list, y_list = euler_method(Variant.func, x0, y0, h, x)
        dic['x'] = x_list

        dic['Analytical Solution'] = Variant.solution(x_list)
        dic['Euler Method'] = y_list

        _, y_list = improved_euler_method(Variant.func, x0, y0, h, x)
        dic['Improved Euler Method'] = y_list

        _, y_list = runge_kuffa_method(Variant.func, x0, y0, h, x)
        dic['Runge-Kuffa Method'] = y_list

        df = pd.DataFrame(dic)
        df.fillna(0, inplace=True)

        if ax is None:
            ax = df.plot(x='x', y='Analytical Solution', color='Yellow', figsize=(10, 5))
        else:
            df.plot(x='x', y='Analytical Solution', color='Yellow', figsize=(10, 5), ax=ax)
        df.plot(x='x', y='Euler Method', color='Blue', ax=ax)
        df.plot(x='x', y='Improved Euler Method', color='Red', ax=ax)
        df.plot(x='x', y='Runge-Kuffa Method', color='LightGreen', ax=ax)
        return df

    def redraw(self, x0, y0, x, h, canvas):
        x0_new, y0_new, x_new, h_new = float(x0.get()), float(y0.get()), float(
            x.get()), float(h.get())
        if x0_new < x_new and (x_new - x0_new) / h_new <= 10000:
            plt.gca().clear()
            df = self.draw(x0_new, y0_new, x_new, h_new, plt.gca())
            canvas.draw()
            return df


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
