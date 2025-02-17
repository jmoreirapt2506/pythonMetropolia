import os
import subprocess
import logging
from flask import Flask, render_template, request  # 📌 Asegura que Flask está importado

# 📌 Definir la app ANTES de usar @app.route()
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


def obtener_ejercicios():
    ejercicios = {}
    for folder in sorted(
            os.listdir()):  # 📌 Asegurar que los módulos están ordenados
        if os.path.isdir(folder) and folder.startswith("module"):
            archivos = sorted([
                f.replace(".py", "") for f in os.listdir(folder)
                if f.startswith("exercise") and f.endswith(".py")
            ])  # 📌 Ordenar ejercicios
            ejercicios[folder] = archivos
    return ejercicios


@app.route('/run', methods=['POST'])
def run():
    modulo = request.form.get("modulo")
    ejercicio = request.form.get("ejercicio")

    script_path = os.path.abspath(f"{modulo}/{ejercicio}.py")

    if os.path.exists(script_path):
        try:
            logging.info(f"Ejecutando script: {script_path}")
            resultado = subprocess.run(["python", script_path],
                                       capture_output=True,
                                       text=True,
                                       check=True)
            output_lines = resultado.stdout.strip().split(
                "\n")  # 📌 Dividir la salida en líneas

            if len(output_lines) == 2 and output_lines[1].startswith(
                    "static/"):
                # 📌 Si la salida tiene dos líneas y la segunda es una imagen, la mostramos
                stats, img_path = output_lines[0], output_lines[1]
                return render_template("result.html",
                                       output=stats,
                                       img_path=img_path,
                                       modulo=modulo,
                                       ejercicio=ejercicio)
            else:
                return render_template("result.html",
                                       output=resultado.stdout,
                                       img_path=None,
                                       modulo=modulo,
                                       ejercicio=ejercicio)

        except subprocess.CalledProcessError as e:
            logging.error(f"❌ Error ejecutando {script_path}: {e.stderr}")
            return f"<h3>❌ Error ejecutando el script: {e.stderr}</h3><a href='/'>Volver</a>"
    else:
        logging.error(f"❌ Archivo no encontrado: {script_path}")
        return f"<h3>❌ Error: El archivo {script_path} no existe.</h3><a href='/'>Volver</a>"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
