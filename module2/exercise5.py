import numpy as np

def inverse_matrix():
    A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    A_inv = np.linalg.inv(A)

    result = "Matrix A:\n" + str(A) + "\n\n"
    result += "Inverse of A:\n" + str(A_inv) + "\n\n"

    identity_1 = np.round(A @ A_inv, decimals=5)
    identity_2 = np.round(A_inv @ A, decimals=5)

    result += "A * A_inv:\n" + str(identity_1) + "\n\n"
    result += "A_inv * A:\n" + str(identity_2)

    print(result)  # Flask leerá esta salida
    return result  # Devolver como string

if __name__ == "__main__":
    output = inverse_matrix()
    print(output)  # Asegurar que Flask pueda capturar el resultado