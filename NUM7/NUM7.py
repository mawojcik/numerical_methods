import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms



def y_function(x):
    return 1 / (25 * (x**2) + 1)


def fun2(x):
    return 1 / (x**2 + 1)


def a_node(n):
    return [-1 + 2*i / n for i in range(n+1)]


def b_node(n):
    return np.cos([((2 * i+1) / (2 * (n+1))) * np.pi for i in range(n+1)])


def interpolation(fun, node, x_range, n):
    fun_values = node(n)
    y = []
    for x in fun_values:
        y.append(fun(x))

    y_new = []
    for a in x_range:
        val = 0
        for i in range(n+1):
            tmp = 1
            for j in range(n+1):
                if i != j:
                    tmp = tmp * (a - fun_values[j])/(fun_values[i] - fun_values[j])
            val = val + y[i]*tmp
        y_new.append(val)
    return y_new


def plots():
    x_range = np.arange(-1.0, 1.01, 0.01)
    fig, axs = plt.subplots(2, 2)
    fig.set_figheight(6)
    fig.set_figwidth(12)
    axs[0, 0].set_title(
        'Wielomiany interpolacyjne dla funkcji\n' r'$f(x)=\frac{1}{1+25x^2}$ i siatki $x_i=-1+2\frac{i}{n}$')
    axs[0, 0].plot(x_range, y_function(x_range), 'r', label='f(x)', linewidth=2.5)
    axs[0, 0].plot(x_range, interpolation(y_function, a_node, x_range, 2), 'b', label=r'$W_2(x)$')
    axs[0, 0].plot(x_range, interpolation(y_function, a_node, x_range, 9), 'c', label=r'$W_9(x)$')
    axs[0, 0].plot(x_range, interpolation(y_function, a_node, x_range, 15), 'y', label=r'$W_{15}(x)$')
    axs[0, 0].legend(loc=8, prop={'size': 8})
    axs[0, 0].grid()

    axs[0, 1].set_title(
        'Wielomiany interpolacyjne dla funkcji\n' r'$f(x)=\frac{1}{1+25x^2}$ i siatki $x_i=\cos(\pi\frac{2i+1}{2(n+1)})$')
    axs[0, 1].plot(x_range, y_function(x_range), 'r', label='f(x)', linewidth=2.5)
    axs[0, 1].plot(x_range, interpolation(y_function, b_node, x_range, 2), 'b', label=r'$W_2(x)$')
    # axs[0, 1].plot(x_range, interpolation(y_function, b_node, x_range, 5), 'g', label=r'$W_5(x)$')
    axs[0, 1].plot(x_range, interpolation(y_function, b_node, x_range, 9), 'c', label=r'$W_8(x)$')
    # axs[0, 1].plot(x_range, interpolation(y_function, b_node, x_range, 20), 'm', label=r'$W_{20}(x)$')
    axs[0, 1].plot(x_range, interpolation(y_function, b_node, x_range, 40), 'y', label=r'$W_{40}(x)$')
    axs[0, 1].legend(loc=8, prop={'size': 8})
    axs[0, 1].grid()

    axs[1, 0].set_title(
        'Wielomiany interpolacyjne dla funkcji\n' r'$f(x)=\frac{1}{1+x^2}$ i siatki $x_i=-1+2\frac{i}{n}$')
    axs[1, 0].plot(x_range, fun2(x_range), 'r', label='f(x)', linewidth=2.5)
    axs[1, 0].plot(x_range, interpolation(fun2, a_node, x_range, 2), 'b', label=r'$W_2(x)$')
    axs[1, 0].plot(x_range, interpolation(fun2, a_node, x_range, 3), 'g', label=r'$W_3(x)$')
    # axs[1, 0].plot(x_range, interpolation(fun2, a_node, x_range, 9), 'c', label=r'$W_9(x)$')
    axs[1, 0].plot(x_range, interpolation(fun2, a_node, x_range, 30), 'm', label=r'$W_{30}(x)$')
    # axs[1, 0].plot(x_range, interpolation(fun2, a_node, x_range, 50), 'y', label=r'$W_{50}(x)$')
    axs[1, 0].legend(loc=8, prop={'size': 8})
    axs[1, 0].grid()

    axs[1, 1].set_title(
        'Wielomiany interpolacyjne dla funkcji\n' r'$f(x)=\frac{1}{1+x^2}$ i siatki $x_i=\cos(\pi\frac{2i+1}{2(n+1)})$')
    axs[1, 1].plot(x_range, fun2(x_range), 'r', label='f(x)', linewidth=2.5)
    axs[1, 1].plot(x_range, interpolation(fun2, b_node, x_range, 2), 'b', label=r'$W_2(x)$')
    axs[1, 1].plot(x_range, interpolation(fun2, b_node, x_range, 3), 'g', label=r'$W_3(x)$')
    axs[1, 1].plot(x_range, interpolation(fun2, b_node, x_range, 9), 'c', label=r'$W_9(x)$')
    axs[1, 1].plot(x_range, interpolation(fun2, b_node, x_range, 30), 'm', label=r'$W_{30}(x)$')
    axs[1, 1].plot(x_range, interpolation(fun2, b_node, x_range, 50), 'y', label=r'$W_{50}(x)$')
    axs[1, 1].legend(loc=8, prop={'size': 8})
    axs[1, 1].grid()

    # plt.setp(axs[:, :], xlabel='x')
    # plt.setp(axs[:, :], ylabel='y')
    fig.tight_layout(pad=1.0)
    # plt.savefig("test.pdf")

    # prawy dolny
    # fig.savefig(
    #     "test.pdf",
    #     bbox_inches=mtransforms.Bbox([[0.5, 0], [1, 0.5]]).transformed(
    #         fig.transFigure - fig.dpi_scale_trans
    #     )
    # )



    plt.show()


plots()