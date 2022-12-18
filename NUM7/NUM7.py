import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms


def a_node(n):
    return [-1 + 2*i / n for i in range(n+1)]


def b_node(n):
    return np.cos([((2 * i+1) / (2 * (n+1))) * np.pi for i in range(n+1)])


def y_function(x):
    return 1 / (25 * (x**2) + 1)


def fun2(x):
    return 1 / (3 * x**4 + 3)


def fun3(x):
    return x**4 / (1 + 2 * x**6)


def interpolation(fun, x_range, n, node):
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


def plot():
    x_range = np.arange(-1.0, 1.01, 0.01)
    fig, axs = plt.subplots(3, 2)
    fig.set_figheight(10)
    fig.set_figwidth(10)

    axs[0, 0].grid()
    axs[0, 0].set_title(
        'Wielomiany interpolacyjne dla\n' r'$y(x)=\frac{1}{1+25x^2}$ i $x_i=-1+2\frac{i}{n}$')
    axs[0, 0].plot(x_range, y_function(x_range), 'c', label='y(x)')
    axs[0, 0].plot(x_range, interpolation(y_function, x_range, 2, a_node), 'b', label=r'$W_2(x)$')
    axs[0, 0].plot(x_range, interpolation(y_function, x_range, 9, a_node), 'g', label=r'$W_9(x)$')
    axs[0, 0].plot(x_range, interpolation(y_function, x_range, 15, a_node), 'm', label=r'$W_{15}(x)$')
    axs[0, 0].legend(loc=9, prop={'size': 8})

    axs[0, 1].grid()
    axs[0, 1].set_title(
        'Wielomiany interpolacyjne dla\n' r'$y(x)=\frac{1}{1+25x^2}$ i $x_i=\cos(\pi\frac{2i+1}{2(n+1)})$')
    axs[0, 1].plot(x_range, y_function(x_range), 'c', label='y(x)')
    axs[0, 1].plot(x_range, interpolation(y_function, x_range, 2, b_node), 'b', label=r'$W_2(x)$')
    axs[0, 1].plot(x_range, interpolation(y_function, x_range, 9, b_node), 'g', label=r'$W_9(x)$')
    axs[0, 1].plot(x_range, interpolation(y_function, x_range, 40, b_node), 'm', label=r'$W_{40}(x)$')
    axs[0, 1].legend(loc=8, prop={'size': 9})

    axs[1, 0].grid()
    axs[1, 0].set_title(
        'Wielomiany interpolacyjne dla\n' r'$y(x)=\frac{1}{3x^4+3}$ i $x_i=-1+2\frac{i}{n}$')
    axs[1, 0].plot(x_range, fun2(x_range), 'c', label='y(x)')
    axs[1, 0].plot(x_range, interpolation(fun2, x_range, 2, a_node), 'b', label=r'$W_2(x)$')
    axs[1, 0].plot(x_range, interpolation(fun2, x_range, 3, a_node), 'g', label=r'$W_3(x)$')
    axs[1, 0].plot(x_range, interpolation(fun2, x_range, 30, a_node), 'm', label=r'$W_{30}(x)$')
    axs[1, 0].legend(loc=8, prop={'size': 9})

    axs[1, 1].grid()
    axs[1, 1].set_title(
        'Wielomiany interpolacyjne dla\n' r'$y(x)=\frac{1}{3x^4+3}$ i $x_i=\cos(\pi\frac{2i+1}{2(n+1)})$')
    axs[1, 1].plot(x_range, fun2(x_range), 'c', label='y(x)')
    axs[1, 1].plot(x_range, interpolation(fun2, x_range, 2, b_node), 'b', label=r'$W_2(x)$')
    axs[1, 1].plot(x_range, interpolation(fun2, x_range, 30, b_node), 'g', label=r'$W_{30}(x)$')
    axs[1, 1].plot(x_range, interpolation(fun2, x_range, 50, b_node), 'm', label=r'$W_{50}(x)$')
    axs[1, 1].legend(loc=8, prop={'size': 10})

    axs[2, 0].grid()
    axs[2, 0].set_title(
        'Wielomiany interpolacyjne dla\n' r'$y(x)=\frac{x^4}{1+2x^6}$ i $x_i=-1+2\frac{i}{n}$')
    axs[2, 0].plot(x_range, fun3(x_range), 'c', label='y(x)')
    axs[2, 0].plot(x_range, interpolation(fun3, x_range, 2, a_node), 'b', label=r'$W_2(x)$')
    axs[2, 0].plot(x_range, interpolation(fun3, x_range, 5, a_node), 'g', label=r'$W_5(x)$')
    axs[2, 0].plot(x_range, interpolation(fun3, x_range, 60, a_node), 'm', label=r'$W_{60}(x)$')
    axs[2, 0].legend(loc=9, prop={'size': 9})

    axs[2, 1].grid()
    axs[2, 1].set_title(
        'Wielomiany interpolacyjne dla\n' r'$y(x)=\frac{x^4}{1+2x^6}$ i $x_i=\cos(\pi\frac{2i+1}{2(n+1)})$')
    axs[2, 1].plot(x_range, fun3(x_range), 'c', label='y(x)')
    axs[2, 1].plot(x_range, interpolation(fun3, x_range, 2, b_node), 'b', label=r'$W_2(x)$')
    axs[2, 1].plot(x_range, interpolation(fun3, x_range, 7, b_node), 'g', label=r'$W_{7}(x)$')
    axs[2, 1].plot(x_range, interpolation(fun3, x_range, 90, b_node), 'm', label=r'$W_{90}(x)$')
    axs[2, 1].legend(loc=9, prop={'size': 10})

    fig.tight_layout(pad=3.0)
    fig.savefig(
        "lewy_gorny.pdf",
        bbox_inches=mtransforms.Bbox([[0, 0.65], [0.5, 0.96]]).transformed(
            fig.transFigure - fig.dpi_scale_trans
        )
    )
    fig.savefig(
        "prawy_gorny.pdf",
        bbox_inches=mtransforms.Bbox([[0.5, 0.65], [1, 0.96]]).transformed(
            fig.transFigure - fig.dpi_scale_trans
        )
    )
    fig.savefig(
        "lewy_srodkowy.pdf",
        bbox_inches=mtransforms.Bbox([[0, 0.35], [0.5, 0.65]]).transformed(
            fig.transFigure - fig.dpi_scale_trans
        )
    )
    fig.savefig(
        "prawy_srodkowy.pdf",
        bbox_inches=mtransforms.Bbox([[0.5, 0.35], [1, 0.65]]).transformed(
            fig.transFigure - fig.dpi_scale_trans
        )
    )
    fig.savefig(
        "lewy_dolny.pdf",
        bbox_inches=mtransforms.Bbox([[0, 0], [0.5, 0.35]]).transformed(
            fig.transFigure - fig.dpi_scale_trans
        )
    )
    fig.savefig(
        "prawy_dolny.pdf",
        bbox_inches=mtransforms.Bbox([[0.5, 0], [1, 0.35]]).transformed(
            fig.transFigure - fig.dpi_scale_trans
        )
    )
    plt.show()


plot()
