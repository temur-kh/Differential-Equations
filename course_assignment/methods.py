import numpy as np


def euler_method(func, x0, y0, h, X):
    x_list = [x0]
    y_list = [y0]
    for _ in np.arange(x0 + h, X + h, h):
        x = x_list[-1] + h
        y = y_list[-1] + h * func(x_list[-1], y_list[-1])
        x_list.append(round(x, 5))
        y_list.append(y)
    return x_list, [round(y, 8) for y in y_list]


def improved_euler_method(func, x0, y0, h, X):
    x_list = [x0]
    y_list = [y0]
    for _ in np.arange(x0 + h, X + h, h):
        x = x_list[-1] + h
        delta_y = h * func(x_list[-1] + h / 2, y_list[-1] + h / 2 * func(x_list[-1], y_list[-1]))
        y = y_list[-1] + delta_y
        x_list.append(round(x, 5))
        y_list.append(y)
    return x_list, [round(y, 8) for y in y_list]


def runge_kuffa_method(func, x0, y0, h, X):
    x_list = [x0]
    y_list = [y0]
    for _ in np.arange(x0 + h, X + h, h):
        x = x_list[-1] + h
        k1 = func(x_list[-1], y_list[-1])
        k2 = func(x_list[-1] + h / 2, y_list[-1] + h / 2 * k1)
        k3 = func(x_list[-1] + h / 2, y_list[-1] + h / 2 * k2)
        k4 = func(x_list[-1] + h, y_list[-1] + h * k3)
        delta_y = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y = y_list[-1] + delta_y
        x_list.append(round(x, 5))
        y_list.append(y)
    return x_list, [round(y, 8) for y in y_list]

