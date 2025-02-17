import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def analyze_weight_height():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "weight-height.csv")

    if not os.path.exists(csv_path):
        return f"ERROR: CSV file not found ({csv_path})"

    df = pd.read_csv(csv_path)

    df["Height_cm"] = df["Height"] * 2.54
    df["Weight_kg"] = df["Weight"] * 0.453592

    # 📌 Convertir cada estadística manualmente en un diccionario
    stats = {
        "Mean": {
            col: df[col].mean()
            for col in ["Height_cm", "Weight_kg"]
        },
        "Median": {
            col: df[col].median()
            for col in ["Height_cm", "Weight_kg"]
        },
        "Std Dev": {
            col: df[col].std()
            for col in ["Height_cm", "Weight_kg"]
        },
        "Variance": {
            col: df[col].var()
            for col in ["Height_cm", "Weight_kg"]
        }
    }

    img_path = "static/exercise3.png"
    plt.hist(df["Height_cm"], bins=20, color='blue', alpha=0.7)
    plt.xlabel("Height (cm)")
    plt.ylabel("Frequency")
    plt.title("Height Distribution")
    plt.savefig(img_path)
    plt.close()

    return stats, img_path


if __name__ == "__main__":
    output, img_path = analyze_weight_height()
    print(output)  # 📌 Mostrar estadísticas en consola
    print(img_path)  # 📌 Mostrar la ruta de la imagen en consola
