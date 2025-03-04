import json

ARCHIVO_NOTAS = "notas.json"

def guardar_notas(notas):
    """Guarda las notas en el archivo JSON."""
    with open(ARCHIVO_NOTAS, "w", encoding="utf-8") as file:
        json.dump(notas, file, indent=4, ensure_ascii=False)
