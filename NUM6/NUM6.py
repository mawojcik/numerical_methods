import numpy as np

matrix_M = np.array([[3, 6, 6, 9],
                     [1, 4, 0, 9],
                     [0, 0.2, 6, 12],
                     [0, 0, 0.1, 6]])

matrix_B = np.array([[3, 4, 2, 4],
                     [4, 7, 1, -3],
                     [2, 1, 3, 2],
                     [4, -3, 2, 2]])
precision = 10 ** -10


def qr_approximation(matrix):
    value = []
    for i in range(0, len(matrix) - 1):
        value.append(abs(matrix[i + 1][i]))
    for i in value:
        if i > precision:
            return True
    return False


def qr_iteration(matrix):
    Q, R = np.linalg.qr(matrix)
    return np.matmul(R, Q)


def qr_eigenvalues(matrix):
    eigenvalues = []
    for i in range(len(matrix)):
        eigenvalues.append(matrix[i][i])
    return eigenvalues


# QR
matrix_M_as_QR = qr_iteration(matrix_M)
while qr_approximation(matrix_M_as_QR):
    matrix_M_as_QR = qr_iteration(matrix_M_as_QR)

print("Iteration eigenvalues: " + str(qr_eigenvalues(matrix_M_as_QR)))  # podpunkt a
print("NumPy eigenvalues: " + str(np.linalg.eig(matrix_M)[0]))  # test a


def power_approximation(a_vec, b_vec):
    return np.linalg.norm(a_vec - b_vec) > precision


def power_iteration(matrix, vector):
    z = np.matmul(matrix, vector)
    return z / np.linalg.norm(z)


def power_eigenvalue(matrix, vector):
    return np.matmul(matrix, vector)[0] / vector[0]


# potegowa
corresponding_vector = []
for i in range(len(matrix_B)):
    corresponding_vector.append(1)

z = power_iteration(matrix_B, corresponding_vector)
while power_approximation(z, corresponding_vector):
    corresponding_vector = z
    z = power_iteration(matrix_B, corresponding_vector)

print("Max eigenvalue: " + str(power_eigenvalue(matrix_B, corresponding_vector)))  # podpunkt b
print("Corresponding vector: " + str(corresponding_vector))  # podpunkt b
