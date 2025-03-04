from cargarNotas import cargar_notas
from guardarNotas import guardar_notas
from listarNotas import listar_notas

def eliminar_nota():
    """Elimina una nota por su ID."""
    listar_notas()
    notas = cargar_notas()
    try:
        id_nota = int(input("Ingrese el ID de la nota a eliminar: "))
        notas = [nota for nota in notas if nota["id"] != id_nota]
        guardar_notas(notas)
        print("\n✅ Nota eliminada correctamente!\n")
    except ValueError:
        print("\n❌ ID inválido.\n")
