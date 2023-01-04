import sys
import sympy
import numpy as np
import matplotlib.pyplot as plt

DATA = 'data.txt'
FUNCTION_B_COEFFICIENTS = [2, 3, 1]


def a_function(points_to_approximate):
    x_points = points_to_approximate[:, 0]
    y_points = points_to_approximate[:, 1]
    matrix = np.column_stack([np.sin(2 * x_points), np.sin(3 * x_points), np.cos(5 * x_points), np.exp(-x_points)])
    coefficients = np.linalg.inv(matrix.T @ matrix) @ matrix.T @ y_points

    plt.figure(figsize=(13, 8))
    plt.grid(True)
    plt.title("Aproksymacja przy użyciu metody najmniejszych kwadratów funkcji:\n"
              "f(x) = a*sin(2x) + b*sin(3x) +c*cos(5x) + d*exp(-x)", fontsize=20)
    print("f(x) = a*sin(2x) + b*sin(3x) +c*cos(5x) + d*exp(-x)")
    print("Znalezione wspolczynniki = ", coefficients)

    denser_x_points = np.arange(x_points.min(), x_points.max() + 0.01, 0.01)
    y_values = coefficients[0] * np.sin(2 * denser_x_points) + coefficients[1] * np.sin(3 * denser_x_points) + coefficients[2] * np.cos(5 * denser_x_points) + coefficients[3] * np.exp(-denser_x_points)
    plt.plot(x_points, y_points, 'o', color='black', label='Dokładne punkty')
    plt.plot(denser_x_points, y_values, color='red', label='Aproksymowana funkcja')
    plt.legend(loc=0, fontsize = 15)
    plt.savefig("a.pdf")
    plt.show()


def b_function(exact_coefficients):
    x_points = np.linspace(0, 10, 100)
    y_points = exact_coefficients[0] * 2 * x_points + exact_coefficients[1] * np.cos(3 * x_points) + exact_coefficients[2] * np.cos(5 * x_points)

    y_disturbed = []
    for a in range(len(y_points)):
        y_disturbed.append(y_points[a] + random.randrange(-1000, 1000) / 1000)
        print(random.randrange(-1000, 1000) / 1000)
    matrix = np.column_stack([2 * x_points, np.cos(3 * x_points), np.cos(5 * x_points)])
    coefficients = np.linalg.inv(matrix.T @ matrix) @ matrix.T @ y_disturbed

    plt.figure(figsize=(13, 8))
    plt.grid(True)
    plt.title("Aproksymacja przy użyciu metody najmniejszych kwadratów funkcji:\n"
              "g(x) = a*2x + b*cos(3x) +c*cos(5x)", fontsize=20)
    print("g(x) = a*cos(2x) + b*cos(3x) +c*cos(5x)")
    print("Dokladne wspolczynniki = ", exact_coefficients)
    print("Znalezione wspolczynniki = ", coefficients)

    denser_x_points = np.arange(x_points.min(), x_points.max() + 0.01, 0.01)
    y_values = exact_coefficients[0] * 2 * denser_x_points + exact_coefficients[1] * np.cos(3 * denser_x_points) + exact_coefficients[2] * np.cos(5 * denser_x_points)
    plt.plot(x_points, y_disturbed, 'o', color='black', label='Zaburzone punkty')
    plt.plot(denser_x_points, y_values, color='red', label='Dokładna funkcja')
    plt.legend(loc=0, fontsize = 15)
    plt.savefig("b.pdf")
    plt.show()


if sys.argv[1] == 'exercise_a':
    a_function(np.loadtxt(DATA))
elif sys.argv[1] == 'exercise_b':
    b_function(FUNCTION_B_COEFFICIENTS)
