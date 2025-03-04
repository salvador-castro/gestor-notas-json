from cargarNotas import cargar_notas

def listar_notas():
    """Lista todas las notas guardadas."""
    notas = cargar_notas()
    if not notas:
        print("\n❌ No hay notas guardadas.\n")
        return
    print("\n📜 Lista de Notas:")
    for nota in notas:
        print(f"[{nota['id']}] {nota['titulo']} - {nota['fecha']}")
    print()
