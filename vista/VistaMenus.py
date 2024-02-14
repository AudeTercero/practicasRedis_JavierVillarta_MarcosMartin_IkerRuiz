import math


def menuVisual(titulo, elementos):
    lenMayor = mayorElemento(elementos)
    print("\n╔",end="")
    rayasModulares(lenMayor,0)
    print("╗")
    print(f"║", end="")
    mostrarTituloMenu(titulo, lenMayor)
    print("║")
    print("╠╦",end="")
    rayasModulares(lenMayor, -1)
    print("╣")
    cont = 1
    for elemento in elementos:
        print(f"║╠ {cont}. ", end="")
        mostrarNombre(elemento, lenMayor)
        print("║")
        cont += 1
    print("║╠ 0. ",end="")
    mostrarNombre("Salir", lenMayor)
    print("║")
    print("╚╬",end="")
    rayasModulares(lenMayor, -1)
    print("╝")
    opc = input(" ╚═══╣Opcion: ")
    return opc


def rayasModulares(lenMayor,var):
    lenTotal = 17
    if lenMayor >= lenTotal:
        lenTotal = lenMayor + 8
    else:
        lenTotal += 5
    lenTotal += var
    for i in range(lenTotal):
        print("═", end="")


def mayorElemento(elementos):
    lenMayor = 0
    for elemento in elementos:
        if len(elemento) > lenMayor:
            lenMayor = len(elemento)
    return lenMayor


def mostrarNombre(elemento, lenMayor):
    lenTotal = 17
    if lenMayor >= lenTotal:
        lenTotal = lenMayor + 3
    disDer = math.ceil((lenTotal - len(elemento)))
    print(elemento.capitalize(), end="")
    while disDer > 0:
        print(" ", end="")
        disDer -= 1


def mostrarTituloMenu(nombre, lenMayor):
    lenTotal = 17
    if lenMayor >= lenTotal:
        lenTotal = lenMayor + 8
    else:
        lenTotal += 5
    disIzq = math.floor((lenTotal - len(nombre)) / 2)
    disDer = math.ceil((lenTotal - len(nombre)) / 2)
    while disIzq > 0:
        print(" ", end="")
        disIzq -= 1
    print(nombre.capitalize(), end="")
    while disDer > 0:
        print(" ", end="")
        disDer -= 1


def listadoLargo():
    listadoMenu = ("alta", "baja", "esternocleidomastoideo plus ultra")
    return listadoMenu


def listadoCorto():
    listadoMenu = ("alta", "baja", "modifica")
    return listadoMenu


menuVisual("Menu largo", listadoLargo())
menuVisual("Menu corto", listadoCorto())
