from agregarNotas import agregar_nota
from listarNotas import listar_notas
from editarNotas import editar_nota
from eliminarNotas import eliminar_nota
from buscarNotas import buscar_nota

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
