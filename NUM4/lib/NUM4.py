import numpy as np
import time
import matplotlib.pyplot as plt  # Biblioteka do tworzenia wykresow

array_size = 50
b = [5] * array_size


def solve_using_sherman():
    A = [[9] * array_size, [7] * (array_size - 1) + [0]]
    start = time.time()

    # backward substitution
    z = [0] * array_size
    x = [0] * array_size
    z[array_size - 1] = b[array_size - 1] / A[0][array_size - 1]
    x[array_size - 1] = 1 / A[0][array_size - 1]

    for i in range(array_size - 2, -1, -1):
        z[i] = (b[array_size - 2] - z[i + 1] * A[1][i]) / A[0][i]
        x[i] = (1 - x[i + 1] * A[1][i]) / A[0][i]

    delta = sum(z) / (sum(x) + 1)

    y = []
    for i in range(len(z)):
        y.append(z[i] - x[i] * delta)

    print(y)

    return time.time()-start



def solve_using_numpy():
    A = np.ones((array_size, array_size), int)
    for i in range(array_size):
        for j in range(array_size):
            if i == j:
                A[i][i] = 10
                if j > 0:
                    A[i - 1][j] = 8
    start = time.time()
    print(np.linalg.solve(A, b))
    return time.time()-start



solve_using_sherman();