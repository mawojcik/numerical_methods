import numpy as np
import copy

A1 = np.array([[2.34332898, -0.11253278, -0.01485349, 0.33316649, 0.71319625],
               [-0.11253278, 1.67773628, -0.32678856, -0.31118836, -0.43342631],
               [-0.01485349, -0.32678856, 2.66011353, 0.85462464, 0.16698798],
               [0.33316649, -0.31118836, 0.85462464, 1.54788582, 0.32269197],
               [0.71319625, -0.43342631, 0.16698798, 0.32269197, 3.27093538]])

A2 = np.array([[2.34065520, -0.05353743, 0.00237792, 0.32944082, 0.72776588],
               [-0.05353743, 0.37604149, -0.70698859, -0.22898376, -0.75489595],
               [-0.01485349, -0.32678856, 2.66011353, 0.85462464, 0.16698798],
               [0.32944082, -0.22898376, 0.87863502, 1.54269444, 0.34299341],
               [0.72776588, -0.75489595, 0.07309288, 0.34299341, 3.19154447]])


b = np.array([3.55652063354463, -1.86337418741501, 5.84125684808554, -1.74587299057388, 0.84299677124244])
# b = np.array([0, 0, 0, 0, 0])
bp = np.add(b, (0.00001, 0, 0, 0, 0))
# y = np.array([0, 0, 0, 0, 0])


def count_matrix_determinant(array):
    return np.linalg.det(array)


def count_y(array):
    y = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    main_det = count_matrix_determinant(array)
    original_array = copy.deepcopy(array)
    for i in range(5):
        array[:, i] = b
        y[i] = count_matrix_determinant(array) / main_det
        # print(array)
        # print("--------------------------------------------")
        array = copy.deepcopy(original_array)
    # array[:, 4] = b
    # print(array)
    return y

# print(count_matrix_determinant(A1))

# count_y(A1)
# count_y(A2)
# print(y)

print(count_y(A1))
print(count_y(A2))