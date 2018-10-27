from methods import Methods
import pandas as pd
from math import fabs
from variant import Variant
from collections import OrderedDict


class Plot:
    def __init__(self):
        self.methods = Methods()

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
        dic = OrderedDict()
        x_list, y_list = self.methods.euler_method(Variant.func, x0, y0, h, x)
        dic['x'] = x_list
        dic['Analytical Solution'] = Variant.solution(x_list, x0, y0)
        dic['Euler Method'] = y_list
        _, y_list = self.methods.improved_euler_method(Variant.func, x0, y0, h, x)
        dic['Improved Euler Method'] = y_list
        _, y_list = self.methods.runge_kuffa_method(Variant.func, x0, y0, h, x)
        dic['Runge-Kuffa Method'] = y_list

        df = pd.DataFrame(dic)
        df.fillna(0, inplace=True)

        df.plot(x='x', y='Analytical Solution', color='Yellow', figsize=(10, 5), ax=ax)
        df.plot(x='x', y='Euler Method', color='Blue', figsize=(10, 5), ax=ax)
        df.plot(x='x', y='Improved Euler Method', color='Red', ax=ax)
        df.plot(x='x', y='Runge-Kuffa Method', color='LightGreen', ax=ax)
        return df

    def draw_errors(self, ax, x0=Variant.x0, y0=Variant.y0, x=Variant.x, h=Variant.h):
        """
        Draw the graph of errors compared to the analytical solution using given parameters.
        :param x0: initial position on x-axis
        :param y0: f(x0)
        :param x: final position on x-axis
        :param h: a grid step
        :param ax: object of class matplotlib.axes.Axes
        :return: pd.DataFrame object
        """
        dic = OrderedDict()
        x_list, y_list = self.methods.euler_method(Variant.func, x0, y0, h, x)
        dic['x'] = x_list
        analytical_solution = Variant.solution(x_list, x0, y0)
        dic['Euler Method'] = [fabs(y1 - y2) for y1, y2 in zip(y_list, analytical_solution)]
        _, y_list = self.methods.improved_euler_method(Variant.func, x0, y0, h, x)
        dic['Improved Euler Method'] = [fabs(y1 - y2) for y1, y2 in zip(y_list, analytical_solution)]
        _, y_list = self.methods.runge_kuffa_method(Variant.func, x0, y0, h, x)
        dic['Runge-Kuffa Method'] = [fabs(y1 - y2) for y1, y2 in zip(y_list, analytical_solution)]

        df = pd.DataFrame(dic)
        df.fillna(0, inplace=True)

        df.plot(x='x', y='Euler Method', color='Blue', figsize=(10, 5), ax=ax)
        df.plot(x='x', y='Improved Euler Method', color='Red', ax=ax)
        df.plot(x='x', y='Runge-Kuffa Method', color='LightGreen', ax=ax)
        return df
