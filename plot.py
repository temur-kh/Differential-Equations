from methods import Methods
import pandas as pd
from variant import Variant


class Plot:
    def __init__(self):
        self.methods = Methods()
        self.x_column = 'x'
        self.n_column = 'N'
        self.columns = ['Analytical Solution', 'Euler Method', 'Improved Euler Method', 'Runge-Kuffa Method']
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
        df = self.__get_results(x0, y0, x, h)
        self.__plot_analytical_solution(df, self.x_column, ax)
        self.__plot_numerical_solutions(df, self.x_column, ax)
        return df[[self.x_column] + self.columns]

    def draw_local_errors(self, ax, x0=Variant.x0, y0=Variant.y0, x=Variant.x, h=Variant.h):
        """
        Draw the graph of local errors compared to the analytical solution using given parameters.
        :param x0: initial position on x-axis
        :param y0: f(x0)
        :param x: final position on x-axis
        :param h: a grid step
        :param ax: object of class matplotlib.axes.Axes
        :return: pd.DataFrame object
        """
        # Plot the graph according to the data table
        df = self.__get_local_errors(x0, y0, x, h)
        self.__plot_numerical_solutions(df, self.x_column, ax)
        return df

    def draw_approximation_errors(self, ax, x0=Variant.x0, y0=Variant.y0, x=Variant.x):
        """
        Draw the graph of total approximation errors compared to the analytical solution using given parameters.
        :param x0: initial position on x-axis
        :param y0: f(x0)
        :param x: final position on x-axis
        :param ax: object of class matplotlib.axes.Axes
        :return: pd.DataFrame object
        """
        # Plot the graph according to the data table
        df = self.__get_approximation_errors(x0, y0, x)
        self.__plot_numerical_solutions(df, self.n_column, ax)
        return df

    def __get_approximation_errors(self, x0, y0, x):
        df = pd.DataFrame(columns=[self.n_column] + self.columns)
        for n in range(1, 1002, 50):
            h = (x - x0) / n
            n_df = pd.DataFrame([n], columns=[self.n_column])
            max_vals = self.__get_local_errors(x0, y0, x, h).max(axis=0)
            vals_df = pd.DataFrame([[max_vals[col] for col in self.columns]], columns=self.columns)
            row = pd.concat([n_df, vals_df], axis=1)
            df = df.append(row, sort=False)
        return df

    def __get_local_errors(self, x0, y0, x, h):
        df = self.__get_results(x0, y0, x, h)
        df.update(df[self.columns].rsub(df[self.columns[0]], 0).abs())
        return df

    def __get_results(self, x0, y0, x, h):
        dic = dict()
        x_list, y_list = self.methods.euler_method(Variant.func, x0, y0, h, x)
        dic[self.x_column] = x_list
        dic[self.columns[0]] = Variant.solution(x_list, x0, y0)
        dic[self.columns[1]] = y_list
        _, y_list = self.methods.improved_euler_method(Variant.func, x0, y0, h, x)
        dic[self.columns[2]] = y_list
        _, y_list = self.methods.runge_kuffa_method(Variant.func, x0, y0, h, x)
        dic[self.columns[3]] = y_list
        df = pd.DataFrame(dic)
        df.fillna(0.0, inplace=True)
        return df

    def __plot_analytical_solution(self, df, x_axis, ax):
        df.plot(x=x_axis, y=self.columns[0], color=self.column_colors[self.columns[0]], ax=ax)

    def __plot_numerical_solutions(self, df, x_axis, ax):
        df.plot(x=x_axis, y=self.columns[1], color=self.column_colors[self.columns[1]],
                figsize=(10, 5), ax=ax)
        df.plot(x=x_axis, y=self.columns[2], color=self.column_colors[self.columns[2]], ax=ax)
        df.plot(x=x_axis, y=self.columns[3], color=self.column_colors[self.columns[3]], ax=ax)
