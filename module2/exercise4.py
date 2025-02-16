import numpy as np


def determinant_matrices():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[-1, 1], [5, 7]])

    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)
    det_AB = np.linalg.det(A @ B)

    print(f"Det(A): {det_A:.2f}")
    print(f"Det(B): {det_B:.2f}")
    print(f"Det(AB): {det_AB:.2f}")
    print(f"Det(A) * Det(B): {det_A * det_B:.2f}")


if __name__ == "__main__":
    determinant_matrices()
