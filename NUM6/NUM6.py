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


def qr_iteration(matrix):
    Q, R = np.linalg.qr(matrix)
    return np.matmul(R, Q)


def qr_approximation(matrix):
    value = []
    for i in range(1, len(matrix)):
        value.append(abs(matrix[i][i - 1]))
    for i in value:
        if i > precision:
            return True
    return False


def qr_eigenvalues(matrix):
    eigenvalues = []
    for i in range(len(matrix)):
        eigenvalues.append(matrix[i][i])
    return eigenvalues


matrix_M_as_QR = qr_iteration(matrix_M)
while qr_approximation(matrix_M_as_QR):
    matrix_M_as_QR = qr_iteration(matrix_M_as_QR)

print(qr_eigenvalues(matrix_M_as_QR))  # podpunkt a
print(np.linalg.eig(matrix_M)[0])  # test a


def power_iteration(matrix, vector):
    x = np.matmul(matrix, vector)
    return x / np.linalg.norm(x)


def power_approximation(a_vec, b_vec):
    return np.linalg.norm(a_vec - b_vec) > precision


def power_eigenvalue(matrix, vector):
    return np.matmul(matrix, vector)[0] / vector[0]


corresponding_vector = []
for i in range(len(matrix_B)):
    corresponding_vector.append(1)

temporary_vector = power_iteration(matrix_B, corresponding_vector)
while power_approximation(temporary_vector, corresponding_vector):
    corresponding_vector = temporary_vector
    temporary_vector = power_iteration(matrix_B, corresponding_vector)

print(power_eigenvalue(matrix_B, corresponding_vector)) # podpunkt b
print(corresponding_vector) # podpunkt b

# Do zrobienia: znalezc wektory wlasne
