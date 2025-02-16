import numpy as np
import matplotlib.pyplot as plt


def draw_lines():
    x = np.linspace(-10, 10, 400)
    y1, y2, y3 = 2 * x + 1, 2 * x + 2, 2 * x + 3

    plt.plot(x, y1, 'r-', label="y = 2x + 1")
    plt.plot(x, y2, 'g--', label="y = 2x + 2")
    plt.plot(x, y3, 'b:', label="y = 2x + 3")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Graph of y = 2x + b")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    draw_lines()
