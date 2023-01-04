import sys
import sympy
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = 'data.txt'
X = sympy.Symbol('x')
FUNCTION_A_COMPONENTS = [sympy.sin(2*X), sympy.sin(3*X), sympy.cos(5*X), sympy.exp(-X)]
FUNCTION_B_COMPONENTS = [sympy.sin(2*X), sympy.cos(3*X)]
FUNCTION_B_COEFFICIENTS = [2, 3]
FUNCTION_B_XPOINTS = np.linspace(0, 10, 100)


# noinspection DuplicatedCode
def _evaluate_function(function_components: np.ndarray, function_coefficients: np.ndarray, x_args: np.ndarray)\
        -> np.ndarray:
    """
    The function retrieves components and function coefficients,
    then combines them into a single entity and calculates results for the given set of arguments x.

    :param function_components: Components of our function
    :param function_coefficients: Coefficients of our function
    :param x_args: List of x arguments
    :return: List containing the results of function calls for each given argument
    """
    function = sum([coefficient * component for coefficient, component in
                    zip(function_coefficients, function_components)])
    return np.array([function.evalf(subs={X: arg}) for arg in x_args])


def get_coefficients_using_least_squares_method(given_points, function_components):
    y_values = [y for x, y in given_points]
    matrix_A = np.column_stack(list(map(lambda f: [f.evalf(subs={X: x_value}) for x_value in given_points[:, 0]], function_components))).astype(np.double)
    return np.linalg.inv(matrix_A.T @ matrix_A) @ matrix_A.T @ y_values


def a_function(points_to_approximate, function_components):
    coefficients = get_coefficients_using_least_squares_method(points_to_approximate, function_components)
    dense_x_range = np.arange(points_to_approximate[:, 0].min(), points_to_approximate[:, 0].max() + 0.01, 0.01)
    plt.figure(figsize=(13, 8))
    plt.grid(True)
    plt.title("Aproksymacja przy użyciu metody najmniejszych kwadratów funkcji:"
              "f(x) = a*sin(2x) + b*sin(3x) +c*cos(5x) + d*exp(-x)")
    print("f(x) = a*sin(2x) + b*sin(3x) +c*cos(5x) + d*exp(-x)")
    print("Found coefficients = ", coefficients)
    plt.plot(points_to_approximate[:, 0], points_to_approximate[:, 1], 'o', color='black', label='Given dots')
    plt.plot(dense_x_range, evaluate_function(function_components, coefficients, dense_x_range), color='red', label='Approximated function')
    plt.legend(loc=0)
    plt.show()
    # @TODO: save plot


def b_function(function_components, exact_coefficients):
    yValues = evaluate_function(np.array(list(map(sympy.sympify, FUNCTION_B_COMPONENTS))), FUNCTION_B_COEFFICIENTS,
                                FUNCTION_B_XPOINTS)
    for a in range(len(yValues)):
        yValues[a] = yValues[a] + np.random.random()
    points_to_approximate = np.array([[x, y] for x, y in zip(FUNCTION_B_XPOINTS, yValues)])
    coefficients = get_coefficients_using_least_squares_method(points_to_approximate, function_components)
    dense_x_range = np.arange(points_to_approximate[:, 0].min(), points_to_approximate[:, 0].max() + 0.01, 0.01)

    plt.figure(figsize=(13, 8))
    plt.grid(True)
    plt.title("Aproksymacja przy użyciu metody najmniejszych kwadratów funkcji:"
              "g(x) = ")
    print("g(x) = ")
    print("Exact coefficients = ", exact_coefficients)
    print("Found coefficients = ", coefficients)
    plt.plot(dense_x_range, evaluate_function(function_components, exact_coefficients, dense_x_range), color='black', lw=3)
    plt.plot(dense_x_range, evaluate_function(function_components, coefficients, dense_x_range), color='red')
    plt.show()
    # @TODO: save plot


if sys.argv[1] == 'exercise_a':
    a_function(np.loadtxt(FILE_NAME), FUNCTION_A_COMPONENTS)
elif sys.argv[1] == 'exercise_b':
    b_function(FUNCTION_B_COMPONENTS, FUNCTION_B_COEFFICIENTS)

