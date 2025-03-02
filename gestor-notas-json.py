import json
import os
from datetime import datetime

# Archivo donde se guardarán las notas
ARCHIVO_NOTAS = "notas.json"

def cargar_notas():
    """Carga las notas desde el archivo JSON."""
    if os.path.exists(ARCHIVO_NOTAS):
        with open(ARCHIVO_NOTAS, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def guardar_notas(notas):
    """Guarda las notas en el archivo JSON."""
    with open(ARCHIVO_NOTAS, "w", encoding="utf-8") as file:
        json.dump(notas, file, indent=4, ensure_ascii=False)

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

def menu():
    """Muestra el menú de opciones."""
    while True:
        print("\n📒 GESTOR DE NOTAS")
        print("1. Agregar Nota")
        print("2. Listar Notas")
        print("3. Editar Nota")
        print("4. Eliminar Nota")
        print("5. Buscar Nota")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_nota()
        elif opcion == "2":
            listar_notas()
        elif opcion == "3":
            editar_nota()
        elif opcion == "4":
            eliminar_nota()
        elif opcion == "5":
            buscar_nota()
        elif opcion == "6":
            print("\n👋 Saliendo del programa. ¡Hasta luego!\n")
            break
        else:
            print("\n❌ Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu()
