import random
import numpy as np
import matplotlib.pyplot as plt

N = 100
MAX_ITERATION = 500
PRECISION = -10
# X_VEC = [0 for _ in range(N)]
X_VEC = random.sample(range(500), N)
B_VEC = list(range(1, N + 1))


def jacobin_alg(vectorX, copyOfVectorX):
    for index in range(N):
        if index == 0:
            vectorX[index] = (B_VEC[index] - vectorX[index + 1] - 0.2 * vectorX[index + 2]) / 3
        elif index == 1:
            vectorX[index] = (B_VEC[index] - copyOfVectorX[index - 1] - vectorX[index + 1] - 0.2 * vectorX[
                index + 2]) / 3
        elif index == N - 2:
            vectorX[index] = (B_VEC[index] - copyOfVectorX[index - 1] - 0.2 * copyOfVectorX[index - 2] -
                              vectorX[index + 1]) / 3
        elif index == N - 1:
            vectorX[index] = (B_VEC[index] - copyOfVectorX[index - 1] - 0.2 * copyOfVectorX[index - 2]) / 3
        else:
            vectorX[index] = (B_VEC[index] - copyOfVectorX[index - 1] - 0.2 * copyOfVectorX[index - 2] -
                              vectorX[index + 1] - 0.2 * vectorX[index + 2]) / 3
    return vectorX


def gauss_seidel_alg(vectorX):
    for index in range(N):
        if index == 0:
            vectorX[index] = (B_VEC[index] - vectorX[index + 1] - 0.2 * vectorX[index + 2]) / 3
        elif index == 1:
            vectorX[index] = (B_VEC[index] - vectorX[index - 1] - vectorX[index + 1] - 0.2 * vectorX[index + 2]) / 3
        elif index == N - 2:
            vectorX[index] = (B_VEC[index] - vectorX[index - 1] - 0.2 * vectorX[index - 2] - vectorX[index + 1]) / 3
        elif index == N - 1:
            vectorX[index] = (B_VEC[index] - vectorX[index - 1] - 0.2 * vectorX[index - 2]) / 3
        else:
            vectorX[index] = (B_VEC[index] - vectorX[index - 1] - 0.2 * vectorX[index - 2] -
                              vectorX[index + 1] - 0.2 * vectorX[index + 2]) / 3
    return vectorX


def get_list_of_approximations(vectorX, maxIteration, prec, methodToUse):
    prevNormVal = 0
    approximationsList = []
    while maxIteration:
        copyOfVectorX = vectorX.copy()
        vectorX = jacobin_alg(vectorX, copyOfVectorX) if methodToUse == 'jacobin' else gauss_seidel_alg(vectorX)

        actualNorm = np.linalg.norm(np.array(vectorX) - np.array(copyOfVectorX))
        approximationsList.append(vectorX.copy())

        if abs(prevNormVal - actualNorm) < 10 ** prec:
            break

        prevNormVal = actualNorm
        maxIteration -= 1

    return approximationsList


def generate_graph(approximationsJac, approximationsGauss):
    diffs1, diffs2 = [], []
    for i in range(len(approximationsJac) - 1):
        diffs1.append(np.sqrt(sum(map(lambda a, b: abs(a - b), approximationsJac[i], approximationsJac[-1]))))
    for i in range(len(approximationsGauss) - 1):
        diffs2.append(np.sqrt(sum(map(lambda a, b: abs(a - b), approximationsGauss[i], approximationsGauss[-1]))))

    plt.grid(True)
    plt.xlabel('n')
    plt.ylabel("$|x(n) - x.last|$")
    plt.yscale('log')
    plt.plot(list(range(len(diffs1))), diffs1, 'tab:blue')
    plt.plot(list(range(len(diffs2))), diffs2, 'tab:red')
    plt.legend(['Jacobin', 'Gauss-Seidel'])
    plt.title('Comparison of two iterative methods\nbetween their differences of Approximation')
    plt.show()


approximationsJacobin = get_list_of_approximations(X_VEC.copy(), MAX_ITERATION, PRECISION, methodToUse='jacobin')
approximationsGaussSeidel = get_list_of_approximations(X_VEC.copy(), MAX_ITERATION, PRECISION, methodToUse='gauss-seid')
print(f'Jacobin solution: \n{approximationsJacobin[-1]}')
print(f'Gauss-Seidel solution: \n{approximationsGaussSeidel[-1]}')
generate_graph(approximationsJacobin, approximationsGaussSeidel)
