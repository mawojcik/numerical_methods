import numpy as np

A1 = np.array([[2.34332898, -0.11253278,  -0.01485349, 0.33316649,  0.71319625],
               [-0.11253278, 1.67773628, -0.32678856, -0.31118836,  -0.43342631],
               [-0.01485349, -0.32678856,  2.66011353, 0.85462464, 0.16698798],
               [0.33316649, -0.31118836, 0.85462464, 1.54788582, 0.32269197],
               [0.71319625, -0.43342631, 0.16698798, 0.32269197, 3.27093538]])

A2 = np.array([[2.34065520, -0.05353743, 0.00237792, 0.32944082, 0.72776588],
               [-0.05353743, 0.37604149, -0.70698859, -0.22898376, -0.75489595],
               [0.00237792, -0.70698859, 2.54906441, 0.87863502, 0.07309288],
               [0.32944082, -0.22898376, 0.87863502, 1.54269444, 0.34299341],
               [0.72776588, -0.75489595, 0.07309288, 0.34299341, 3.19154447]])


b = np.array([3.55652063354463, -1.86337418741501, 5.84125684808554, -1.74587299057388, 0.84299677124244])

bp = np.add(b, (0.00001, 0, 0, 0, 0))


y1 = np.linalg.solve(A1, b)
y2 = np.linalg.solve(A2, b)
y1p = np.linalg.solve(A1, bp)
y2p = np.linalg.solve(A2, bp)

delta_1 = np.linalg.norm(y1 - y1p)      # liczenie normy euklidesowej
delta_2 = np.linalg.norm(y2 - y2p)

np.set_printoptions(formatter={'float': '{: 0.8f}'.format})     # Dla lepszego wyswietlania danych

print("y1: ", y1)
print("y1':", y1p)
print("y2: ", y2)
print("y2':", y2p, "\n")
print("Norma 1:", '{:.14f}'.format(delta_1))
print("Norma 2:", '{:.14f}'.format(delta_2), "\n")

print("Wspolczynnik uwarunkowania macierzy A1: ", np.linalg.cond(A1))
print("Wspolczynnik uwarunkowania macierzy A2: ", np.linalg.cond(A2))

# import numpy as np
# import copy
#
# A1 = np.array([[2.34332898, -0.11253278,  -0.01485349, 0.33316649,  0.71319625],
#                [-0.11253278, 1.67773628, -0.32678856, -0.31118836,  -0.43342631],
#                [-0.01485349, -0.32678856,  2.66011353, 0.85462464, 0.16698798],
#                [0.33316649, -0.31118836, 0.85462464, 1.54788582, 0.32269197],
#                [0.71319625, -0.43342631, 0.16698798, 0.32269197, 3.27093538]])
#
# A2 = np.array([[2.34065520, -0.05353743, 0.00237792, 0.32944082, 0.72776588],
#                [-0.05353743, 0.37604149, -0.70698859, -0.22898376, -0.75489595],
#                [0.00237792, -0.70698859, 2.54906441, 0.87863502, 0.07309288],
#                [0.32944082, -0.22898376, 0.87863502, 1.54269444, 0.34299341],
#                [0.72776588, -0.75489595, 0.07309288, 0.34299341, 3.19154447]])
#
#
# b = np.array([3.55652063354463, -1.86337418741501, 5.84125684808554, -1.74587299057388, 0.84299677124244])
#
# bp = np.add(b, (0.00001, 0, 0, 0, 0))
#
#
# def count_matrix_determinant(array):
#     return np.linalg.det(array)
#
#
# def count_y(array, result_of_equation):     # Twierdzenie Cramera
#     y = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
#     copied_array = copy.deepcopy(array)
#     main_det = count_matrix_determinant(array)
#
#     for i in range(len(array)):
#         copied_array[:, i] = result_of_equation
#         y[i] = count_matrix_determinant(copied_array) / main_det
#         copied_array = copy.deepcopy(array)
#     return y
#
#
# y1 = count_y(A1, b)
# y2 = count_y(A2, b)
# y1p = count_y(A1, bp)
# y2p = count_y(A2, bp)
#
#
# delta_1 = np.linalg.norm(y1 - y1p)      # liczenie normy euklidesowej
# delta_2 = np.linalg.norm(y2 - y2p)
#
# np.set_printoptions(formatter={'float': '{: 0.8f}'.format})     # Dla lepszego wyswietlania danych
#
# print("y1: ", y1)
# print("y1':", y1p)
# print("y2: ", y2)
# print("y2':", y2p, "\n")
# print("Norma 1:", '{:.14f}'.format(delta_1))
# print("Norma 2:", '{:.14f}'.format(delta_2), "\n")
#
# print("Wspolczynnik uwarunkowania macierzy A1: ", np.linalg.cond(A1))
# print("Wspolczynnik uwarunkowania macierzy A2: ", np.linalg.cond(A2))