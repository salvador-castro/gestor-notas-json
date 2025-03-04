from datetime import datetime
from cargarNotas import cargar_notas
from guardarNotas import guardar_notas
from listarNotas import listar_notas

def editar_nota():
    """Edita una nota existente."""
    listar_notas()
    notas = cargar_notas()
    try:
        id_nota = int(input("Ingrese el ID de la nota a editar: "))
        for nota in notas:
            if nota["id"] == id_nota:
                nota["titulo"] = input("Nuevo título: ") or nota["titulo"]
                nota["contenido"] = input("Nuevo contenido: ") or nota["contenido"]
                nota["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                guardar_notas(notas)
                print("\n✅ Nota actualizada correctamente!\n")
                return
        print("\n❌ Nota no encontrada.\n")
    except ValueError:
        print("\n❌ ID inválido.\n")
