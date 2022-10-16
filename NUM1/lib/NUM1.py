import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd



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
    a = miscalculation(derivative_a, point)
    b = miscalculation(derivative_b, point)

    # for x in range(300):
        # print("{:.5f}".format(a))
        # print("{:.10f}".format(a[x]), "{:.10f}".format(b[x]))


def generate_table():
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.axis('tight')

    a = miscalculation(derivative_a, point)
    b = miscalculation(derivative_b, point)

    for x in range(300):
        h[x] = '%0.15f' % h[x]

    table = pd.DataFrame(data ={'H': h,
                                'Function a miscalculation': a,
                                'Function b miscalculation:': b
                                })
    ax.table(cellText=table.values[::int(20)], colLabels=table.columns, loc='center')
    fig.tight_layout()
    plt.savefig('table.pdf')


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
    # print(miscalculation(derivative_a, point))
    # print_miscalculation()
    generate_table()
else:
    print('Wrong argument!')
