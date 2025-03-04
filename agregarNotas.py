from datetime import datetime
from cargarNotas import cargar_notas
from guardarNotas import guardar_notas

def agregar_nota():
    """Agrega una nueva nota."""
    titulo = input("Título de la nota: ")
    contenido = input("Contenido de la nota: ")
    notas = cargar_notas()
    nueva_nota = {
        "id": len(notas) + 1,
        "titulo": titulo,
        "contenido": contenido,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notas.append(nueva_nota)
    guardar_notas(notas)
    print("\n✅ Nota agregada correctamente!\n")
