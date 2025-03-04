import json
import os

# Archivo donde se guardarán las notas
ARCHIVO_NOTAS = "notas.json"

def cargar_notas():
    """Carga las notas desde el archivo JSON."""
    if os.path.exists(ARCHIVO_NOTAS):
        with open(ARCHIVO_NOTAS, "r", encoding="utf-8") as file:
            return json.load(file)
    return []
