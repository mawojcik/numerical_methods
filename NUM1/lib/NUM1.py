import numpy as np
import matplotlib.pyplot as plt
import sys

# variables
f = np.sin      # funkcja
df = np.cos     # pochodna funkcji
point = 0.2     # punkt x


def derivative_a(x):
    return accuracy((accuracy(f(x + h)) - accuracy(f(x))) / h)


def derivative_b(x):
    return accuracy((accuracy(f(x + h)) - accuracy(f(x - h))) / (2 * h))


def miscalculation(derivative, x):
    return accuracy(np.absolute(accuracy(derivative(x)) - accuracy(df(x))))


def chart():
    plt.grid(True)
    plt.title('Miscalculation of function sin(x) in point: ' + str(point))
    plt.xlabel('h')
    plt.ylabel("|Dhf(x) - f'(x)|")
    plt.loglog(h, miscalculation(derivative_a, point))
    plt.loglog(h, miscalculation(derivative_b, point))
    plt.legend(['Derivative A', 'Derivative B'])
    plt.savefig(chart_name)
    plt.show()


def print_miscalculation():
    a = miscalculation(derivative_a, point)
    b = miscalculation(derivative_b, point)

    print('    h value:           Miscalc. of func. a:      Miscalc. of func. b:')
    for x in range(0, points_on_chart, 1):
        print('{:.14f}         {:.14f}          {:.14f}'.format(h[x], a[x], b[x]))


if len(sys.argv) != 3:
    print('Wrong number of arguments!')
    quit()
elif sys.argv[1] == 'float':
    accuracy = np.float32
    points_on_chart = 250
    h = accuracy(np.logspace(-7, 0, points_on_chart))
    chart_name = 'miscalculation_chart_float.png'
elif sys.argv[1] == 'double':
    accuracy = np.float64
    points_on_chart = 300
    h = accuracy(np.logspace(-14, 0, points_on_chart))
    chart_name = 'miscalculation_chart_double.png'
else:
    print('Wrong argument!')


if sys.argv[2] == 'chart':
    chart()
elif sys.argv[2] == 'miscalculation':
    print_miscalculation()
else:
    print('Wrong argument!')
