import matplotlib.pyplot as plt
import numpy as np


def line_graph():
    fig = plt.figure()
    plt.grid()
    x = np.array(range(-5, 5, 1))
    y = -1 / 2 - 4 * x
    plt.axhline(y=-8.5, color='k')
    plt.axhline(y=7.5, color='r')

    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')

    plt.plot(x, y, "-")
    plt.savefig('./line_graph.png')


def number_line():
    fig = plt.figure()
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.axes.get_yaxis().set_visible(False)
    x = np.array(range(-2, 2, 1))
    y = x * 0
    plt.plot(x, y, "o")
    plt.xticks(range(-5, 6, 1))
    plt.savefig('./numer_line.png')


line_graph()
number_line()
plt.show()