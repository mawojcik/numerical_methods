import matplotlib.pyplot as plt
import numpy as np
import time

n = 100
how_many_points = 1000  # do wykresu uzylem 10000



def solve_numpy(size):
    a = np.diag([0.2] * (size - 1), -1)
    a += np.diag([1.2] * size)
    a += np.diag([0.1 / i for i in range(1, size)], 1)
    a += np.diag([0.4 / i ** 2 for i in range(1, size - 1)], 2)
    xVector = np.array([_ for _ in range(1, size + 1)])
    startTime = time.time()
    solution = np.linalg.solve(a, xVector)

    return solution, time.time() - startTime


def solve_numerically(size):
    a = [[0] + [0.2] * (size - 1), [1.2] * size]
    a.append([0.1 / i for i in range(1, size)] + [0])
    a.append([0.4 / i ** 2 for i in range(1, size - 1)] + [0] + [0])

    xVector = []
    for i in range(1, size + 1):
        xVector.append(i)
    startTime = time.time()
    for i in range(1, size - 2):
        a[0][i] = a[0][i] / a[1][i - 1]
        a[1][i] = a[1][i] - a[0][i] * a[2][i - 1]
        a[2][i] = a[2][i] - a[0][i] * a[3][i - 1]

    a[0][size - 2] = a[0][size - 2] / a[1][size - 3]
    a[1][size - 2] = a[1][size - 2] - a[0][size - 2] * a[2][size - 3]
    a[2][size - 2] = a[2][size - 2] - a[0][size - 2] * a[3][size - 3]

    a[0][size - 1] = a[0][size - 1] / a[1][size - 2]
    a[1][size - 1] = a[1][size - 1] - a[0][size - 1] * a[2][size - 2]

    for i in range(1, size):
        xVector[i] = xVector[i] - a[0][i] * xVector[i - 1]

    xVector[size - 1] = xVector[size - 1] / a[1][size - 1]
    xVector[size - 2] = (xVector[size - 2] - a[2][size - 2] * xVector[size - 1]) / a[1][size - 2]
    for i in range(size - 3, -1, -1):
        xVector[i] = (xVector[i] - a[3][i] * xVector[i + 2] - a[2][i] * xVector[i + 1]) / a[1][i]

    detA = 1
    for val in a[1]:
        detA *= val

    return xVector, detA, time.time() - startTime


def make_plot():
    numpyResults = {}
    numericalResults = {}

    for size in range(100, how_many_points, 200):
        numpyResults[size] = solve_numpy(size)[1] * 1000000
        numericalResults[size] = solve_numerically(size)[2] * 1000000

    plt.grid(True)
    plt.title('Computing time')
    plt.loglog(numpyResults.keys(), numpyResults.values(), 'tab:blue', label='Czas rozwiązania biblioteką numPy ')
    plt.loglog(numericalResults.keys(), numericalResults.values(), 'tab:green',
               label='Czas rozwiązywania zaimplementowanego algorytmu')
    plt.legend(loc=0, fontsize=13)
    plt.savefig('computing_time.pdf')


print(f'Rozwiązanie dla N = {n}:\n{solve_numerically(n)[0]}\n'
      f'Wyznacznik: det(A) = {solve_numerically(n)[1]}')
make_plot()
