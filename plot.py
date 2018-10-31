from methods import Methods
import pandas as pd
from variant import Variant
from collections import OrderedDict


class Plot:
    def __init__(self):
        self.methods = Methods()
        self.x_column = ['x']
        self.columns = [
            'Analytical Solution', 'Euler Method', 'Improved Euler Method', 'Runge-Kuffa Method'
        ]
        self.column_colors = {
            'Analytical Solution': 'Yellow',
            'Euler Method': 'Blue',
            'Improved Euler Method': 'Red',
            'Runge-Kuffa Method': 'LightGreen'
        }

    def draw_functions(self, ax, x0=Variant.x0, y0=Variant.y0, x=Variant.x, h=Variant.h):
        """
        Draw the graph of functions using given parameters.
        :param x0: initial position on x-axis
        :param y0: f(x0)
        :param x: final position on x-axis
        :param h: a grid step
        :param ax: object of class matplotlib.axes.Axes
        :return: pd.DataFrame object
        """
        # Plot the graph according to the data table
        df = self.__get_results_table(x0, y0, x, h)
        self.__plot_analytical_solution(df, ax)
        self.__plot_numerical_solutions(df, ax)
        return df[self.x_column + self.columns]

    def draw_local_errors(self, ax, x0=Variant.x0, y0=Variant.y0, x=Variant.x, h=Variant.h):
        """
        Draw the graph of errors compared to the analytical solution using given parameters.
        :param x0: initial position on x-axis
        :param y0: f(x0)
        :param x: final position on x-axis
        :param h: a grid step
        :param ax: object of class matplotlib.axes.Axes
        :return: pd.DataFrame object
        """
        # Plot the graph according to the data table
        df = self.__get_errors_table(x0, y0, x, h)
        self.__plot_numerical_solutions(df, ax)
        return df[self.x_column + self.columns]

    def draw_approximation_errors(self, ax, x0=Variant.x0, y0=Variant.y0, x=Variant.x, h=Variant.h):
        pass  # TODO draw total approximation errors

    def __get_errors_table(self, x0, y0, x, h):
        df = self.__get_results_table(x0, y0, x, h)
        df.update(df[self.columns].rsub(df[self.columns[0]], 0).abs())
        return df

    def __get_results_table(self, x0, y0, x, h):
        dic = dict()
        x_list, y_list = self.methods.euler_method(Variant.func, x0, y0, h, x)
        dic[self.x_column[0]] = x_list
        dic[self.columns[0]] = Variant.solution(x_list, x0, y0)
        dic[self.columns[1]] = y_list
        _, y_list = self.methods.improved_euler_method(Variant.func, x0, y0, h, x)
        dic[self.columns[2]] = y_list
        _, y_list = self.methods.runge_kuffa_method(Variant.func, x0, y0, h, x)
        dic[self.columns[3]] = y_list
        df = pd.DataFrame(dic)
        df.fillna(0.0, inplace=True)
        return df

    def __plot_analytical_solution(self, df, ax):
        df.plot(x=self.x_column[0], y=self.columns[0], color=self.column_colors[self.columns[0]], ax=ax)

    def __plot_numerical_solutions(self, df, ax):
        df.plot(x=self.x_column[0], y=self.columns[1], color=self.column_colors[self.columns[1]],
                figsize=(10, 5), ax=ax)
        df.plot(x=self.x_column[0], y=self.columns[2], color=self.column_colors[self.columns[2]], ax=ax)
        df.plot(x=self.x_column[0], y=self.columns[3], color=self.column_colors[self.columns[3]], ax=ax)
