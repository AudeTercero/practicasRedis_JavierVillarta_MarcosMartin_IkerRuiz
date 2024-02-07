from controlador.Colores import *


def menu():
    opcion = input("\n\n\t[==== MENU PERSONAJES ====>\n"
                   "\t[1. Alta\n"
                   "\t[2. Baja\n"
                   "\t[3. Modificar\n"
                   "\t[4. Consultar\n"
                   "\t[5. Mostrar Todos\n"
                   "\t[0. Salir\n"
                   "\t[===== Opcion: ")
    return opcion

def altaNombre():
    nombre = input("Introduce el nombre: ")
    return nombre
def altaCabeza():
    opc = input('Escoja una de las 5 cabezas: ')
    return opc
def saliendo():
    print("Saliendo...")
def errorEntrada():
    rojo("Entrada no valida")