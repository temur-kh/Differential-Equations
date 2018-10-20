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
