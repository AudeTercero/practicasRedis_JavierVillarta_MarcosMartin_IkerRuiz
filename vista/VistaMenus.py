import math


def menuVisual(titulo, elementos):
    """
    Funcion que pinta un menu con un titulo y elementos especificos
    :param titulo: titulo que encabeza el menu
    :param elementos: elementos contenidos en el menu
    :return: opcion elegida
    """
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
    opc = input(" ╚══╣Opcion: ")
    return opc


def rayasModulares(lenMayor,var):
    '''
    Funcion que pinta las rayas de un menu a partir de una longitud espefica
    y le puede da mayor longitud al menu cuando se necesita.
    :param lenMayor: longitud del elemento mas largo que estara en el menu
    :param var: 0 si se trata de un titulo o -1 para el resto de elementos
    '''
    lenTotal = 17
    if lenMayor >= lenTotal:
        lenTotal = lenMayor + 8
    else:
        lenTotal += 5
    lenTotal += var
    for i in range(lenTotal):
        print("═", end="")


def mayorElemento(elementos):
    '''
    Funcion que devuelve la longitud del elemento mas largo de una lista
    :param elementos: lista de elementos que iran dentro de un menu
    :return lenMayor: longitud del elemento mas largo del listado
    '''
    lenMayor = 0
    for elemento in elementos:
        if len(elemento) > lenMayor:
            lenMayor = len(elemento)
    return lenMayor


def mostrarNombre(elemento, lenMayor):
    '''
    Funcion que muestra  colocado, el nombre de un personaje dentro de un menu
    :param elemento: nombre a pintar en el menu
    :param lenMayor:longitud del elemento mas grande del menu
    '''
    lenTotal = 17
    if lenMayor >= lenTotal:
        lenTotal = lenMayor + 3
    disDer = math.ceil((lenTotal - len(elemento)))
    print(elemento.capitalize(), end="")
    while disDer > 0:
        print(" ", end="")
        disDer -= 1


def mostrarTituloMenu(nombre, lenMayor):
    '''
    Funcion que muestra el tiulo colocado, dentro de un menu.
    :param nombre: titulo del menu
    :param lenMayor: longitud del elemento mas grande del menu
    '''
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



