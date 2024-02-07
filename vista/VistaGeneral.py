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


# INICIO PRINTS/INPUTS ALTAS
def altaNombre():
    nombre = input("Introduce el nombre: ")
    return nombre


def altaCabeza():
    opc = input('Escoja una de las 5 cabezas: ')
    return opc


def altaCuerpo():
    opc = input('Escoja un cuerpo: ')
    return opc


def altaPiernas():
    opc = input('Escoja las piernas: ')
    return opc


def altaColor():
    opc = input("\n\n\t[==== Escoja un color ====>\n"
                "\t[1. Rojo\n"
                "\t[2. Amarillo\n"
                "\t[3. Verde\n"
                "\t[4. Azul\n"
                "\t[5. Morado\n"
                "\t[0. Salir\n"
                "\t[===== Opcion: ")
    return opc


def altaFuerza():
    opc = input('Indique la fuerza del personaje del 1 al 10')
    return opc


def altaInteligencia():
    opc = input('Indique la inteligencia del personaje del 1 al 10')
    return opc


def altaVida():
    opc = input('Indique la vida del personaje del 1 al 10')
    return opc


def altaDestreza():
    opc = input('Indique la destreza del personaje del 1 al 10')
    return opc

# INICIO PRINTS/INPUTS BAJA

def baja():
    opc = input('Introduce el nombre del personaje que quieras borrar: ')
    return opc

def saliendo():
    print("Saliendo...")


def errorEntrada():
    rojo("Entrada no valida")
