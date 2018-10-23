from math import e


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
    def solution(x_list, new_x0=x0, new_y0=y0):
        """
        Get the list of x-values and output y-values using analytical solution
        :param x_list: x-values
        :param new_x0: an initial x value
        :param new_y0: an initial y value
        :return: y-values
        """
        def solve(x_i, c):
            """
            Analytical solution to the o.d.e.
            :param x_i: x-value
            :param c: a constant
            :return: y-value
            """
            try:
                return 3.0 / (1 + c * e ** (3 * (x_i ** 2) / 2.0))
            except OverflowError:
                return 0.0

        c = (3.0 / new_y0 - 1) / e ** (3 * (new_x0 ** 2) / 2.0)
        y_list = []
        for x in x_list:
            y_list.append(solve(x, c))
        return y_list
