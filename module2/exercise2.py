import numpy as np
import matplotlib.pyplot as plt


def draw_dot_pattern():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array(
        [-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78])

    plt.scatter(x, y, marker="+", color="black")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Dot Pattern")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    draw_dot_pattern()
