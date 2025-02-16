import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def analyze_weight_height():
    df = pd.read_csv("weight-height.csv")

    df["Height_cm"] = df["Height"] * 2.54
    df["Weight_kg"] = df["Weight"] * 0.453592

    print("Mean (Height, Weight):", df[["Height_cm", "Weight_kg"]].mean())
    print("Median (Height, Weight):", df[["Height_cm", "Weight_kg"]].median())
    print("Std Dev (Height, Weight):", df[["Height_cm", "Weight_kg"]].std())
    print("Variance (Height, Weight):", df[["Height_cm", "Weight_kg"]].var())

    plt.hist(df["Height_cm"], bins=20, color='blue', alpha=0.7)
    plt.xlabel("Height (cm)")
    plt.ylabel("Frequency")
    plt.title("Height Distribution")
    plt.show()


if __name__ == "__main__":
    analyze_weight_height()
