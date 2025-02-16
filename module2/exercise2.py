import numpy as np
import matplotlib.pyplot as plt
import os

def draw_dot_pattern():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78])

    plt.scatter(x, y, marker="+", color="black")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Dot Pattern")
    plt.grid(True)

    # 📌 Verificar si la carpeta static/ existe, si no, crearla
    img_dir = "static"
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    img_path = os.path.join(img_dir, "exercise2.png")
    plt.savefig(img_path)
    plt.close()

    return img_path  # Devolver la ruta para que Flask la pueda mostrar

if __name__ == "__main__":
    img_path = draw_dot_pattern()
    print(img_path)  # Imprimir la ruta para que Flask la capture
