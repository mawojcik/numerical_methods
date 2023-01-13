import matplotlib.pyplot as plt
import numpy as np
import time


def get_solution_by_numpy_lib(size):
    a = np.diag([0.2] * (size - 1), -1)
    a += np.diag([1.2] * size)
    a += np.diag([0.1 / i for i in range(1, size)], 1)
    a += np.diag([0.4 / i ** 2 for i in range(1, size - 1)], 2)
    xVector = np.array([_ for _ in range(1, size + 1)])

    startTime = time.time()
    solution = np.linalg.solve(a, xVector)

    return solution, time.time() - startTime


def get_solution_numerically(size):
    a = [[0] + [0.2] * (size - 1), [1.2] * size]
    a.append([0.1 / i for i in range(1, size)] + [0])
    a.append([0.4 / i ** 2 for i in range(1, size - 1)] + [0] + [0])

    xVector = []
    for i in range(1, size+1):
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


def generate_graph():
    numpyResults = {}
    numericalResults = {}

    for size in range(100, 6000, 200):
        numpyResults[size] = get_solution_by_numpy_lib(size)[1] * 1000000
        numericalResults[size] = get_solution_numerically(size)[2] * 1000000

    plt.grid(True)
    plt.title('Computing time')
    plt.loglog(numpyResults.keys(), numpyResults.values(), 'tab:green')
    plt.loglog(numericalResults.keys(), numericalResults.values(), 'tab:red')
    # plt.loglog(numericalResults.keys(), np.array(list(numericalResults.keys())), 'tab:gray')
    # plt.loglog(numpyResults.keys(), np.array(list(numpyResults.keys())) ** 2, 'tab:gray')
    # @TODO: write in plt
    plt.legend(['Solving time by numPy library', 'Solving time numerically', 'f(x) = x', 'f(x) = x^2'])
    plt.savefig('computing_time.svg')


if __name__ == '__main__':
    n = 100
    print(f'The solution of the equation for N = {n}:\n{get_solution_numerically(n)[0]}\n'
          f'The determinant of A is equal: det(A) = {get_solution_numerically(n)[1]}')
    generate_graph()
