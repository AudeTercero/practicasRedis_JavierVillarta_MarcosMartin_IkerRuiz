from controlador.Colores import *


def getCabezas():
    """
    En esta funcion se guardan todas las cabezas disponibles para los personajes.
    Se trata de una lista para cada tipo de cabeza, que a su vez contiene una lista
    para cada linea de dibujado. De esta forma se pueden mostrar varios personajes
    a la vez.
    :return: Lista con el contenido
    """
    return [["     [#]    ", "    _|||_   "], ["            ", "     (-)    "]
        , ["      _     ", "    _/v\\_   "],
            ["     ___    ", "    /0-0\\   "], ["     ___    ", "   _/<_>\\_  "]]


def getCuerpos():
    """
    En esta funcion se guardan todas los cuerpos disponibles para los personajes.
    :return:
    """
    return [["  <[     ]> ", "  <[=====]> ", "  <[_____]> "], [" \\=\\  Y  /=/", "    \\ | /   ", "    |___|   "],
            ["    \\   /   ", " d==|   |==b", "    |___|   "], ["     ) (    ", "   /(   )\\  ", "   \\ )_( /  "],
            ["   _/   \\_  ", "  /=======\\ ", " /_________\\"]]


def getPiernas():
    """
    En esta funcion se guardan todas las piernas disponibles para los personajes.
    :return:
    """
    return [["    |   |   ", "    l   l   "], ["   //   \\\  ", " _//     \\\_"], ["    // \\\   ", "  _//   \\\_ "],
            ["    || ||   ", "    WW WW   "], ["    (_0_)   ", "            "]]


def mostrarCabezas():
    """
    Esta funcion muestra todas las cabezas disponibles para que el usuario pueda
    seleccionar la que quiera. Ademas de mostrar un cuerpo basico junto a las cabezas
    :return:
    """

    # Lista que contiene las lineas de caracteres necesarias para mostrar el cuerpo de ejemplo
    cuerpoMolde = [
        "   /[   ]\\  ",
        "  / [   ] \\ ",
        "    [___]   ",
        "    /   \\   ",
        "   /     \\  "]

    ################################# CABEZAS ######################################

    # Primero, se muestra la primera linea de cada tipo de cabeza y despues la segunda linea de cada cabeza
    # Se llama a la funcion verde, la cual muestra el contenido recibido en color verde
    verde(str(getCabezas()[0][0] + "1 " + getCabezas()[1][0] + "2 " + getCabezas()[2][0]
              + "3 " + getCabezas()[3][0] + "4 " + getCabezas()[4][0] + "5 "))
    verde(str(getCabezas()[0][1] + "  " + getCabezas()[1][1] + "  " + getCabezas()[2][1]
              + "  " + getCabezas()[3][1] + "  " + getCabezas()[4][1]))

    ########################### CUERPOS DE EJEMPLO #################################
    # Despues se muestra el cuerpo molde 5 veces, ya que hay 5 tipos de cabeza
    for i in range(5):
        print(str(cuerpoMolde[i] + "  " + cuerpoMolde[i] + "  " + cuerpoMolde[i] + "  "
                  + cuerpoMolde[i] + "  " + cuerpoMolde[i]))


def mostrarCuerpos(cabeza):
    """
    Esta funcion muestra todos los cuerpos disponibles junto con la cabeza
    :param cabeza:
    :return:
    """
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
#INICIO PRINTS/INPUTS MODIFICAR
def nombreModificar():
    opc = input('Introduce el nombre del personaje que quiera modificar o pulse 0 para salir.')
    return opc
def menuModificar():
    opc = input("\n\t[====== MODIFICACION PERSONAJE ======\n"
                    "\t[1.Nombre\n"
                    "\t[2.Cabeza\n"
                    "\t[3.Cuerpo\n"
                    "\t[4.Piernas\n"
                    "\t[5.Color\n"
                    "\t[6.Fuerza\n"
                    "\t[7.Inteligencia\n"
                    "\t[8.Vida\n"
                    "\t[9.Destreza\n"
                    "\t[0.Salir\n"
                    "\t[Opcion: ")
    return opc

# MENSAJES Y AVISOS
def saliendo():
    print("Saliendo...")


def errorEntrada():
    rojo("Entrada no valida")
def campoCorrecto():
    verde("Campo introducido correctamente")