import numpy as np

array_size = 50;
b = [5] * array_size


# A = B + a*a^T
def solve_using_sherman():
    A = [[9] * array_size, [7] * (array_size - 1) + [0]]

    # Backward subtitution dla obu równań
    z = [0] * array_size
    x = [0] * array_size
    z[array_size - 1] = b[array_size - 1] / A[0][array_size - 1]
    x[array_size - 1] = 1 / A[0][array_size - 1]

    for i in range(array_size - 2, -1, -1):
        z[i] = (b[array_size - 2] - A[1][i] * z[i + 1]) / A[0][i]
        x[i] = (1 - A[1][i] * x[i + 1]) / A[0][i]

    delta = sum(z) / (1 + sum(x))

    # Wyliczenie wyniku
    y = []
    for i in range(len(z)):
        y.append(z[i] - x[i] * delta)

    print(y)


def solve_using_numpy():
    A = np.ones((array_size, array_size), int)
    for i in range(array_size):
        for j in range(array_size):
            if i == j:
                A[i][i] = 10
                if j > 0:
                    A[i - 1][j] = 8


solve_using_sherman();


