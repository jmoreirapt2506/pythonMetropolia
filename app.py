from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)


# 📌 Detectar módulos y ejercicios en la estructura correcta
def obtener_ejercicios():
    ejercicios = {}
    for folder in os.listdir():
        if os.path.isdir(folder) and folder.startswith(
                "module"):  # Solo módulos que empiezan con "module"
            archivos = [
                f.replace(".py", "") for f in os.listdir(folder)
                if f.startswith("exercise") and f.endswith(".py")
            ]
            ejercicios[folder] = archivos  # Agregar módulo y sus ejercicios
    return ejercicios


@app.route('/')
def home():
    ejercicios = obtener_ejercicios()
    return render_template("index.html", ejercicios=ejercicios)


@app.route('/run', methods=['POST'])
def run():
    modulo = request.form.get("modulo")
    ejercicio = request.form.get("ejercicio")

    script_path = f"{modulo}/{ejercicio}.py"

    if os.path.exists(script_path):
        # 📌 Ejecutar el script seleccionado y capturar la salida
        resultado = subprocess.run(["python", script_path],
                                   capture_output=True,
                                   text=True)
        return render_template("result.html",
                               output=resultado.stdout,
                               modulo=modulo,
                               ejercicio=ejercicio)
    else:
        return f"<h3>❌ Error: El archivo {script_path} no existe.</h3><a href='/'>Volver</a>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
