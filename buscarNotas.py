from cargarNotas import cargar_notas

def buscar_nota():
    """Busca notas por palabra clave en el título o contenido."""
    clave = input("Ingrese palabra clave para buscar: ").lower()
    notas = cargar_notas()
    resultados = [nota for nota in notas if clave in nota["titulo"].lower() or clave in nota["contenido"].lower()]
    if resultados:
        print("\n🔍 Resultados de la búsqueda:")
        for nota in resultados:
            print(f"[{nota['id']}] {nota['titulo']} - {nota['fecha']}")
    else:
        print("\n❌ No se encontraron notas con esa palabra clave.\n")
