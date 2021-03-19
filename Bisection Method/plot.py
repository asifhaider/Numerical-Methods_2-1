import numpy as np
from matplotlib import pyplot as plt


def mole_fraction_function(x, p=3, k=0.05):
    # default argument used as specified in problem statement
    return (x / (1 - x) * ((2 * p) / (2 + x)) ** 0.5) - k


def plot_function():
    x = np.linspace(-1.0, 0.99999, 200)
    y = mole_fraction_function(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'b')

    plt.ylim(-3.0, 25.0)  # -5,15

    ax.set_xlabel('Mole Fraction Value')
    ax.set_ylabel('Function Value')
    ax.set_title('Graph: Function Plot')
    ax.grid(color='c')
    plt.show()
