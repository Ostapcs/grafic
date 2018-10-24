import sys
from numpy import *
import matplotlib.pyplot as plt
from sympy import *

x = symbols("x")
init_printing(use_unicode=True)

print("Input your function ")
expr = input()
expr = sympify(expr)
arritems = input("Input beginnig, end & sampling via space")
arritems = arritems.split(" ")
try:
    arr = arange(float(arritems[0]), float(arritems[1]), float(arritems[2]))
    print(arr)
except:
    print("ERROR -- ", sys.exc_info()[0])
    exit()

plt.title(simplify(expr))
plt.xlabel('x label')
plt.ylabel('y label')

f = lambdify(x, expr, "numpy")
try:
    plt.plot(arr,f(arr))
    print(f(arr))
except SyntaxError:
    print("ERROR -- ", sys.exc_info()[0])
except TypeError:
    print("Invalid input")
except:
    print("Unexpected Error", sys.exc_info()[0])

plt.grid(True)
y0 = expr.evalf(subs={x: float(arritems[0])})
y1 = expr.evalf(subs={x: float(arritems[1])})

# plt.axis([int(arritems[0]), int(arritems[1]), int(y0), int(y1)])

plt.autoscale(True)
plt.show()
