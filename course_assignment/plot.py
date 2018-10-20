from methods import *
import pandas as pd
import matplotlib.pyplot as plt
from variant import Variant
from collections import OrderedDict

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

        dic = OrderedDict()
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
