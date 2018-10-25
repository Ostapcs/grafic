import sys
from numpy import *
import matplotlib.pyplot as plt
from sympy import *

x = symbols("x")
plt.style.use('seaborn-darkgrid')
n = 100000


def buildingGraf(expr, expr2):
    f = lambdify(x, expr, "numpy")
    g = lambdify(x, expr2, "numpy")
    f_y = f(arr)
    g_y = g(arr)

    plt.plot(arr, f_y, arr, g_y)

    return min(min(f_y), min(g_y)), max(max(f_y), max(g_y)), f, g


def fillGrafWithPoints(expr, expr2):
    expr = sympify(expr)
    expr2 = sympify(expr2)
    items = buildingGraf(expr, expr2)

    insideGraf = []
    outsideGraf = []
    for i in range(n):

        xCord = (maxArrX - minArrX) * random.random_sample() + minArrX  # виправити
        yCord = (items[1] - items[0]) * random.random_sample() + items[0]

        func1 = items[-2](xCord)
        func2 = items[-1](xCord)
        if min(func1, func2) <= yCord <= max(func1, func2):
            insideGraf.append((xCord, yCord))

        else:
            outsideGraf.append((xCord, yCord))

    list1, list2 = zip(*insideGraf)
    plt.scatter(list1, list2, s=.7, c='y')
    list3, list4 = zip(*outsideGraf)
    plt.scatter(list3, list4, s=.7)

    return monteKarlo(len(insideGraf), items[1], items[0])


def monteKarlo(LeninsideGraf, max_y, min_y):
    return (LeninsideGraf / n) * (maxArrX - minArrX) * (max_y - min_y)


# print("Input your function ")
# expr = input()
# expr = "-(x**2) + 15"
expr = "(cos(x)**2) * 4"
expr2 = "0.5*x"
# expr = sympify(expr)
# arritems = input("Input beginnig, end & sampling via space")
# arritems = arritems.split(" ")
try:
    # arr = arange(float(arritems[0]), float(arritems[1]), float(arritems[2]))
    arr = arange(-10, 10, 0.01)
    maxArrX = max(arr)
    minArrX = min(arr)
except:
    print("ERROR -- ", sys.exc_info()[0])
    exit()


plt.title("ITS MA GRAPh " f'Square is {fillGrafWithPoints(expr, expr2)}')
plt.xlabel("Here is x")
plt.ylabel("Here is y")
plt.legend()
plt.grid(True)
plt.autoscale(False)
plt.show()
