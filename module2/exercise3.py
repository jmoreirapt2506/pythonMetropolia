import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_weight_height():
    # 📌 Verificar si el archivo CSV existe antes de intentar leerlo
    csv_path = "weight-height.csv"
    if not os.path.exists(csv_path):
        print(f"❌ Error: El archivo {csv_path} no existe.")
        return "ERROR: CSV file not found"

    # 📌 Leer el archivo CSV
    df = pd.read_csv(csv_path)

    # 📌 Convertir unidades
    df["Height_cm"] = df["Height"] * 2.54
    df["Weight_kg"] = df["Weight"] * 0.453592

    # 📌 Calcular estadísticas
    stats = {
        "Mean": df[["Height_cm", "Weight_kg"]].mean().to_dict(),
        "Median": df[["Height_cm", "Weight_kg"]].median().to_dict(),
        "Std Dev": df[["Height_cm", "Weight_kg"]].std().to_dict(),
        "Variance": df[["Height_cm", "Weight_kg"]].var().to_dict()
    }

    print(stats)  # Flask mostrará estas estadísticas en la web

    # 📌 Crear el histograma
    plt.hist(df["Height_cm"], bins=20, color='blue', alpha=0.7)
    plt.xlabel("Height (cm)")
    plt.ylabel("Frequency")
    plt.title("Height Distribution")

    # 📌 Verificar si la carpeta static/ existe, si no, crearla
    img_dir = "static"
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    img_path = os.path.join(img_dir, "exercise3.png")
    plt.savefig(img_path)
    plt.close()

    return img_path  # Devolver la ruta de la imagen para Flask

if __name__ == "__main__":
    img_path = analyze_weight_height()
    print(img_path)  # Imprimir la ruta para que Flask pueda capturarla
