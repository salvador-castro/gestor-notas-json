import json
import os
from datetime import datetime
from cargarNotas import cargar_notas
from guardarNotas import guardar_notas
from menu import menu
from agregarNotas import agregar_nota
from listarNotas import listar_notas
from editarNotas import editar_nota
from eliminarNotas import eliminar_nota
from buscarNotas import buscar_nota

if __name__ == "__main__":
    menu()
