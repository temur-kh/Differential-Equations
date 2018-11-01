# Differential Equations Course Assignment
This is a GUI application created on Python with the use of [matplotlib][plt], [numpy][np], [pandas][pd], [tkinter][tk] and [pandastable][pdt] libraries. Using it you can check the graph of function for some specific differential equation. In this project the equation is y'=xy^2-3xy (variant #25).

Clone this repository to your machine using [Git][git]:
```sh
$ git clone https://github.com/temur-kh/Differential-Equations.git
```

In oder to run the application, you should install all required packages. You can do it (not necessary step) 
primarily creating and activating a virtual environment:
```sh
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

Install all requirements from requirements.txt file:
```sh
$ pip install -r requirements.txt
```

Now you can run the application:
```sh
$ python main.py
```

The values of initial conditions are changeable through the form in the window of the application. However, to change the differential equation and the function of the analytical solution, you need to change the code.

   [plt]: <https://matplotlib.org/>
   [np]: <http://www.numpy.org/>
   [pd]: <https://pandas.pydata.org/>
   [tk]: <https://en.wikipedia.org/wiki/Tkinter>
   [pdt]: <https://github.com/dmnfarrell/pandastable>
   [git]: <https://git-scm.com/>
