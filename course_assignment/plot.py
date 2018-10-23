from methods import *
import pandas as pd
from math import fabs
from variant import Variant
from collections import OrderedDict


def draw_graph(ax, x0=Variant.x0, y0=Variant.y0, x=Variant.x, h=Variant.h, graph_type=True):
    """
    Draw the graph of function using given parameters.
    :param x0: initial position on x-axis
    :param y0: f(x0)
    :param x: final position on x-axis
    :param h: a grid step
    :param graph_type: type of graph
    :param ax: object of class matplotlib.axes.Axes
    :return: None
    """
    dic = OrderedDict()
    x_list, y_list = euler_method(Variant.func, x0, y0, h, x)
    dic['x'] = x_list

    if graph_type:
        dic['Analytical Solution'] = Variant.solution(x_list, x0, y0)
        dic['Euler Method'] = y_list
        _, y_list = improved_euler_method(Variant.func, x0, y0, h, x)
        dic['Improved Euler Method'] = y_list
        _, y_list = runge_kuffa_method(Variant.func, x0, y0, h, x)
        dic['Runge-Kuffa Method'] = y_list
    else:
        analytical_solution = Variant.solution(x_list, x0, y0)
        dic['Euler Method'] = [fabs(y1 - y2) for y1, y2 in zip(y_list, analytical_solution)]
        _, y_list = improved_euler_method(Variant.func, x0, y0, h, x)
        dic['Improved Euler Method'] = [fabs(y1 - y2) for y1, y2 in zip(y_list, analytical_solution)]
        _, y_list = runge_kuffa_method(Variant.func, x0, y0, h, x)
        dic['Runge-Kuffa Method'] = [fabs(y1 - y2) for y1, y2 in zip(y_list, analytical_solution)]

    df = pd.DataFrame(dic)
    df.fillna(0, inplace=True)

    if graph_type:
        df.plot(x='x', y='Analytical Solution', color='Yellow', figsize=(10, 5), ax=ax)
    df.plot(x='x', y='Euler Method', color='Blue', figsize=(10, 5), ax=ax)
    df.plot(x='x', y='Improved Euler Method', color='Red', ax=ax)
    df.plot(x='x', y='Runge-Kuffa Method', color='LightGreen', ax=ax)
    return df
