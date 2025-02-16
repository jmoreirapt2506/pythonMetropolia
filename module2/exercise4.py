import numpy as np

def determinant_matrices():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[-1, 1], [5, 7]])

    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)
    det_AB = np.linalg.det(A @ B)

    result = (
        f"Det(A): {det_A:.2f}\n"
        f"Det(B): {det_B:.2f}\n"
        f"Det(AB): {det_AB:.2f}\n"
        f"Det(A) * Det(B): {det_A * det_B:.2f}"
    )

    print(result)  # Flask leerá esta salida
    return result  # Devolver como string

if __name__ == "__main__":
    output = determinant_matrices()
    print(output)  # Asegurar que Flask pueda capturar el resultado
