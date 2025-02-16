import numpy as np


def inverse_matrix():
    A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    A_inv = np.linalg.inv(A)

    print("Matrix A:")
    print(A)

    print("\nInverse of A:")
    print(A_inv)

    identity_1 = np.round(A @ A_inv, decimals=5)
    identity_2 = np.round(A_inv @ A, decimals=5)

    print("\nA * A_inv:")
    print(identity_1)

    print("\nA_inv * A:")
    print(identity_2)


if __name__ == "__main__":
    inverse_matrix()
