import os
import subprocess  # 📌 Asegura que subprocess esté importado
import logging
from flask import Flask, render_template, request  # 📌 Importa render_template y request


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
            output = resultado.stdout.strip()

            if output.startswith("static/") and os.path.exists(output):
                return render_template("result.html",
                                       output=output,
                                       modulo=modulo,
                                       ejercicio=ejercicio,
                                       es_imagen=True)
            else:
                return render_template("result.html",
                                       output=output,
                                       modulo=modulo,
                                       ejercicio=ejercicio,
                                       es_imagen=False)
        except subprocess.CalledProcessError as e:
            logging.error(f"❌ Error ejecutando {script_path}: {e.stderr}")
            return f"<h3>❌ Error ejecutando el script: {e.stderr}</h3><a href='/'>Volver</a>"
    else:
        logging.error(f"❌ Archivo no encontrado: {script_path}")
        return f"<h3>❌ Error: El archivo {script_path} no existe.</h3><a href='/'>Volver</a>"
