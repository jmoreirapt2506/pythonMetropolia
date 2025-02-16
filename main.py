import subprocess
import os


def ejecutar_ejercicio(ejercicio):
    if not os.path.exists(ejercicio):
        print(f"\n❌ Error: El archivo {ejercicio} no existe.\n")
        return

    print(f"\n🚀 Ejecutando: {ejercicio} ...\n")

    # Usa subprocess.run() sin capturar la salida para verla en tiempo real
    resultado = subprocess.run(["python", ejercicio])

    print(f"\n✅ Código de salida: {resultado.returncode}")


if __name__ == "__main__":
    while True:
        print("\n📌 Selecciona un ejercicio:")
        print("1 - Dibujar líneas")
        print("2 - Dibujar patrón de puntos")
        print("3 - Poblar tabla desde archivo CSV")
        print("4 - Determinante de matrices")
        print("5 - Matriz inversa")
        print("0 - Salir")

        opcion = input("🔹 Ingrese el número del ejercicio: ").strip()

        ejercicios = {
            "1": "module2/exercise1.py",
            "2": "module2/exercise2.py",
            "3": "module2/exercise3.py",
            "4": "module2/exercise4.py",
            "5": "module2/exercise5.py"
        }

        if opcion == "0":
            print("👋 Saliendo del programa...")
            break
        elif opcion in ejercicios:
            ejecutar_ejercicio(ejercicios[opcion])
        else:
            print("\n⚠️ Opción no válida. Intenta de nuevo.\n")
