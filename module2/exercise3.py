import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def analyze_weight_height():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "weight-height.csv")

    if not os.path.exists(csv_path):
        print(f"❌ Error: El archivo {csv_path} no existe en {os.getcwd()}")
        return f"ERROR: CSV file not found ({csv_path})"

    df = pd.read_csv(csv_path)

    df["Height_cm"] = df["Height"] * 2.54
    df["Weight_kg"] = df["Weight"] * 0.453592

    stats = {
        "Mean":
        df[["Height_cm",
            "Weight_kg"]].mean().to_frame().T.to_dict(orient="records")[0],
        "Median":
        df[["Height_cm",
            "Weight_kg"]].median().to_frame().T.to_dict(orient="records")[0],
        "Std Dev":
        df[["Height_cm",
            "Weight_kg"]].std().to_frame().T.to_dict(orient="records")[0],
        "Variance":
        df[["Height_cm",
            "Weight_kg"]].var().to_frame().T.to_dict(orient="records")[0]
    }

    print(stats)

    # 📌 Guardar la imagen en "static/" con una ruta accesible para Flask
    img_dir = os.path.join(os.path.dirname(script_dir), "static")
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    img_path = os.path.join(img_dir, "exercise3.png")
    plt.hist(df["Height_cm"], bins=20, color='blue', alpha=0.7)
    plt.xlabel("Height (cm)")
    plt.ylabel("Frequency")
    plt.title("Height Distribution")
    plt.savefig(img_path)
    plt.close()

    # 📌 Devolver solo la parte accesible de la imagen (ruta relativa)
    return "static/exercise3.png"


if __name__ == "__main__":
    output = analyze_weight_height()
    print(output)
