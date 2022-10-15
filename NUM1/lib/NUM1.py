import numpy as np
import matplotlib.pyplot as plt
import sys

# variables
accuracy = np.float64
f = np.sin      # funkcja
df = np.cos     # pochodna funkcji
point = 0.2     # punkt x


def derivative_a(x):
    return accuracy((accuracy(f(x + h)) - accuracy(f(x))) / h)
    # return accuracy((f(x+h) - f(x))/h)


def derivative_b(x):
    return accuracy((accuracy(f(x + h)) - accuracy(f(x - h))) / (2 * h))
    # return accuracy(f(x + h) - f(x - h)) / (2 * h)


def miscalculation(derivative, x):
    return accuracy(np.absolute(accuracy(derivative(x)) - accuracy(df(x))))
    # return accuracy(np.absolute(derivative(x) - df(x)))


def chart():
    plt.grid(True)
    plt.title('Miscalculation of function sin(x) in point: ' + str(point))
    plt.xlabel('h')
    plt.ylabel("|Dhf(x) - f'(x)|")
    plt.loglog(h, miscalculation(derivative_a, point))
    plt.loglog(h, miscalculation(derivative_b, point))
    plt.legend(['Derivative A', 'Derivative B'])
    plt.savefig('Miscalculation_chart.png')
    plt.show()


def print_miscalculation():
    print('miscalculation')


if len(sys.argv) != 3:
    print('Wrong number of arguments!')
    quit()
elif sys.argv[1] == 'float':
    accuracy = np.float32
    h = accuracy(np.logspace(-7, 0, 250))  # parametr # FLOAT
elif sys.argv[1] == 'double':
    accuracy = np.float64
    h = accuracy(np.logspace(-14, 0, 300))    # parametr # DOUBLE
else:
    print('Wrong argument!')

if sys.argv[2] == 'chart':
    chart()
elif sys.argv[2] == 'miscalculation':
    print_miscalculation()
else:
    print('Wrong argument!')
