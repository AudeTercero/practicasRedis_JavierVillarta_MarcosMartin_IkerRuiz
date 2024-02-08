from controlador.Colores import *


def getCabezas():
    return [["     [#]    ", "    _|||_   "], ["            ", "     (-)    "]
        , ["      _     ", "    _/v\\_   "],
            ["     ___    ", "    /0-0\\   "], ["     ___    ", "   _/<_>\\_  "]]


def getCuerpos():
    return [["  <[     ]> ", "  <[=====]> ", "  <[_____]> "], [" \\=\\  Y  /=/", "    \\ | /   ", "    |___|   "],
            ["    \\   /   ", " d==|   |==b", "    |___|   "], ["     ) (    ", "   /(   )\\  ", "   \\ )_( /  "],
            ["   _/   \\_  ", "  /=======\\ ", " /_________\\"]]


def getPiernas():
    return [["    |   |   ", "    l   l   "], ["   //   \\\  ", " _//     \\\_"], ["    // \\\   ", "  _//   \\\_ "],
            ["    || ||   ", "    WW WW   "], ["    (_0_)   ", "            "]]


def mostrarCabezas():
    cuerpoMolde = [
        "   /[   ]\\  ",
        "  / [   ] \\ ",
        "    [___]   ",
        "    /   \\   ",
        "   /     \\  "]

    ################################# CABEZAS ######################################
    verde(str(getCabezas()[0][0] + "1 " + getCabezas()[1][0] + "2 " + getCabezas()[2][0]
              + "3 " + getCabezas()[3][0] + "4 " + getCabezas()[4][0] + "5 "))
    verde(str(getCabezas()[0][1] + "  " + getCabezas()[1][1] + "  " + getCabezas()[2][1]
              + "  " + getCabezas()[3][1] + "  " + getCabezas()[4][1]))


    ########################### CUERPOS DE EJEMPLO #################################
    for i in range(5):
        print(str(cuerpoMolde[i] + "  " + cuerpoMolde[i] + "  " + cuerpoMolde[i] + "  "
                  + cuerpoMolde[i] + "  " + cuerpoMolde[i]))


def mostrarCuerpos(cabeza):
    piernasMolde = [
        "    /   \\   ",
        "   /     \\  "]
    ################################# CABEZAS ######################################
    azul(str(getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " +
             getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0]))
    azul(str(getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " +
             getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1]))

    ################################# CUERPOS ######################################
    verde(str(getCuerpos()[0][0] + " 1" + getCuerpos()[1][0] + " 2" + getCuerpos()[2][0] + " 3" + getCuerpos()[3][0]
              + " 4" + getCuerpos()[4][0] + " 5"))
    verde(str(getCuerpos()[0][1] + "  " + getCuerpos()[1][1] + "  " + getCuerpos()[2][1] + "  " + getCuerpos()[3][1]
              + "  " + getCuerpos()[4][1]))
    verde(str(getCuerpos()[0][2] + "  " + getCuerpos()[1][2] + "  " + getCuerpos()[2][2] + "  "
              + getCuerpos()[3][2] + "  " + getCuerpos()[4][2]))

    ############################ PIERNAS DE EJEMPLO #################################
    print(str(piernasMolde[0] + "  " + piernasMolde[0] + "  " + piernasMolde[0] + "  " + piernasMolde[0]
              + "  " + piernasMolde[0]))
    print(str(piernasMolde[1] + "  " + piernasMolde[1] + "  " + piernasMolde[1] + "  " + piernasMolde[1]
              + "  " + piernasMolde[1]))

def mostrarPiernas(cabeza, cuerpo):
    azul(str(getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " +
              getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  "))
    azul(str(getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " +
              getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  "))
    azul(str(getCuerpos()[cuerpo][0] + "  " + getCuerpos()[cuerpo][0] + "  " + getCuerpos()[cuerpo][0] + "  " +
              getCuerpos()[cuerpo][0] + "  " + getCuerpos()[cuerpo][0] + "  "))
    azul(str(getCuerpos()[cuerpo][1] + "  " + getCuerpos()[cuerpo][1] + "  " + getCuerpos()[cuerpo][1] + "  " +
              getCuerpos()[cuerpo][1] + "  " + getCuerpos()[cuerpo][1] + "  "))
    azul(str(getCuerpos()[cuerpo][2] + "  " + getCuerpos()[cuerpo][2] + "  " + getCuerpos()[cuerpo][2] + "  " +
              getCuerpos()[cuerpo][2] + "  " + getCuerpos()[cuerpo][2] + "  "))


    verde(str(getPiernas()[0][0] + "1 " + getPiernas()[1][0] + "2 " + getPiernas()[2][0] + "3 "
              + getPiernas()[3][0] + "4 " + getPiernas()[4][0] + "5 "))
    verde(str(getPiernas()[0][1] + "  " + getPiernas()[1][1] + "  " + getPiernas()[2][1] + "  "
              + getPiernas()[3][1] + "  " + getPiernas()[4][1] + "  "))

def mostrarPersonaje(cabeza, cuerpo, piernas):
    print(str(getCabezas()[cabeza][0]))
    print(str(getCabezas()[cabeza][1]))
    print(str(getCuerpos()[cuerpo][0]))
    print(str(getCuerpos()[cuerpo][1]))
    print(str(getCuerpos()[cuerpo][2]))
    print(str(getPiernas()[piernas][0]))
    print(str(getPiernas()[piernas][1]))


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
    opc = input('Escoge la cabeza: ')
    return opc


def altaCuerpo():
    opc = input('Escoge el cuerpo: ')
    return opc


def altaPiernas():
    opc = input('Escoge las piernas: ')
    return opc


def altaColor():
    opc = input("\n\n\t[==== Escoge un color ====>\n"
                "\t[1. Rojo\n"
                "\t[2. Amarillo\n"
                "\t[3. Verde\n"
                "\t[4. Azul\n"
                "\t[5. Morado\n"
                "\t[0. Salir\n"
                "\t[===== Opcion: ")
    return opc


def altaFuerza():
    opc = input('Indica la fuerza del personaje del 1 al 10')
    return opc


def altaInteligencia():
    opc = input('Indica la inteligencia del personaje del 1 al 10')
    return opc


def altaVida():
    opc = input('Indica la vida del personaje del 1 al 10')
    return opc


def altaDestreza():
    opc = input('Indica la destreza del personaje del 1 al 10')
    return opc


# INICIO PRINTS/INPUTS BAJA

def baja():
    opc = input('Introduce el nombre del personaje que quieras borrar: ')
    return opc


def saliendo():
    print("Saliendo...")


def errorEntrada():
    rojo("Entrada no valida")
