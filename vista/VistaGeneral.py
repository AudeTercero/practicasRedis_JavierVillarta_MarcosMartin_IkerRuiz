import math

from controlador.Colores import *
from controlador.VerificationExceptions import esRango, esNum
from colorama import Fore
from modelo.Personaje import getCabezas, getCuerpos, getPiernas


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
    bordePersonajesTop()
    bordeIzq()
    verde(str(getCabezas()[0][0] + "1 " + getCabezas()[1][0] + "2 " + getCabezas()[2][0]
              + "3 " + getCabezas()[3][0] + "4 " + getCabezas()[4][0] + "5 "))
    print("║")
    bordeIzq()
    verde(str(getCabezas()[0][1] + "  " + getCabezas()[1][1] + "  " + getCabezas()[2][1]
              + "  " + getCabezas()[3][1] + "  " + getCabezas()[4][1]))
    bordeDer()

    ########################### CUERPOS DE EJEMPLO #################################
    # Despues se muestra el cuerpo molde 5 veces, ya que hay 5 tipos de cabeza
    for i in range(5):
        bordeIzq()
        print(str(cuerpoMolde[i] + "  " + cuerpoMolde[i] + "  " + cuerpoMolde[i] + "  "
                  + cuerpoMolde[i] + "  " + cuerpoMolde[i]), end="")
        bordeDer()
    bordePersonajesBottom()


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
    bordePersonajesTop()
    bordeIzq()
    azul(str(getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " +
             getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0]))
    bordeDer()
    bordeIzq()
    azul(str(getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " +
             getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1]))
    bordeDer()

    ################################# CUERPOS ######################################
    bordeIzq()
    verde(str(getCuerpos()[0][0] + " 1" + getCuerpos()[1][0] + " 2" + getCuerpos()[2][0] + "3 " + getCuerpos()[3][0]
              + "4 " + getCuerpos()[4][0] + "5 "))
    print("║")
    bordeIzq()
    verde(str(getCuerpos()[0][1] + "  " + getCuerpos()[1][1] + "  " + getCuerpos()[2][1] + "  " + getCuerpos()[3][1]
              + "  " + getCuerpos()[4][1]))
    bordeDer()
    bordeIzq()
    verde(str(getCuerpos()[0][2] + "  " + getCuerpos()[1][2] + "  " + getCuerpos()[2][2] + "  "
              + getCuerpos()[3][2] + "  " + getCuerpos()[4][2]))
    bordeDer()

    ############################ PIERNAS DE EJEMPLO #################################
    bordeIzq()
    print(str(piernasMolde[0] + "  " + piernasMolde[0] + "  " + piernasMolde[0] + "  " + piernasMolde[0]
              + "  " + piernasMolde[0]), end="")
    bordeDer()
    bordeIzq()
    print(str(piernasMolde[1] + "  " + piernasMolde[1] + "  " + piernasMolde[1] + "  " + piernasMolde[1]
              + "  " + piernasMolde[1]), end="")
    bordeDer()
    bordePersonajesBottom()


def mostrarPiernas(cabeza, cuerpo):
    bordePersonajesTop()
    bordeIzq()
    azul(str(getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " +
             getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0]))
    bordeDer()
    bordeIzq()
    azul(str(getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " +
             getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1]))
    bordeDer()
    bordeIzq()
    azul(str(getCuerpos()[cuerpo][0] + "  " + getCuerpos()[cuerpo][0] + "  " + getCuerpos()[cuerpo][0] + "  " +
             getCuerpos()[cuerpo][0] + "  " + getCuerpos()[cuerpo][0]))
    bordeDer()
    bordeIzq()
    azul(str(getCuerpos()[cuerpo][1] + "  " + getCuerpos()[cuerpo][1] + "  " + getCuerpos()[cuerpo][1] + "  " +
             getCuerpos()[cuerpo][1] + "  " + getCuerpos()[cuerpo][1]))
    bordeDer()
    bordeIzq()
    azul(str(getCuerpos()[cuerpo][2] + "  " + getCuerpos()[cuerpo][2] + "  " + getCuerpos()[cuerpo][2] + "  " +
             getCuerpos()[cuerpo][2] + "  " + getCuerpos()[cuerpo][2]))
    bordeDer()

    bordeIzq()
    verde(str(getPiernas()[0][0] + "1 " + getPiernas()[1][0] + "2 " + getPiernas()[2][0] + "3 "
              + getPiernas()[3][0] + "4 " + getPiernas()[4][0] + "5 "))
    print("║")
    bordeIzq()
    verde(str(getPiernas()[0][1] + "  " + getPiernas()[1][1] + "  " + getPiernas()[2][1] + "  "
              + getPiernas()[3][1] + "  " + getPiernas()[4][1]))
    bordeDer()
    bordePersonajesBottom()


def mostrarPersonaje(cabeza, cuerpo, piernas):
    print(str(getCabezas()[cabeza][0]))
    print(str(getCabezas()[cabeza][1]))
    print(str(getCuerpos()[cuerpo][0]))
    print(str(getCuerpos()[cuerpo][1]))
    print(str(getCuerpos()[cuerpo][2]))
    print(str(getPiernas()[piernas][0]))
    print(str(getPiernas()[piernas][1]))


def menuVisual(titulo, elementos):
    print("\n╔══════════════════════╗")
    print(f"║ {titulo} ║")
    print("╠╦═════════════════════╣")
    cont = 1
    for elemento in elementos:
        print(f"║╠ {cont}. {elemento}", end="")
        for _ in range(17 - len(elemento)):
            print(" ", end="")
        print("║")
        cont += 1
    print("║╠ 0. Salir            ║")
    print("╚╬═════════════════════╝")
    opc = input(" ╚═══╣Opcion: ")
    return opc


def header(titulo):
    print("\n\t╔═══════════════════╦══════════╗")
    print(f"\t║  {titulo}   ║ 0. Salir ║")
    print("\t╠═╦═════════════════╩══════════╝")


def bordeIzq():
    print("\t║ ", end="")


def bordeIzqDoble():
    print("\t║ ╠ ", end="")


def bordeDer():
    print("  ║")


def bordeFinalAlta():
    print("\t╚═╩══╣ ", end="")
    azul("Alta realizada con exito")
    print()


def bordeFinalBaja():
    print("\t╚═╩══╣ ", end="")
    azul("Baja realizada con exito")
    print()


def bordeFinalConsulta():
    print("\t╠═╬══╣ ", end="")
    azul("Personaje encontrado")
    print()


def bordePersonajesTop():
    print("\t║ ╚═════════════════════════════════════════════════════════════════════╗")


def bordePersonajesBottom():
    print("\t║ ╔═════════════════════════════════════════════════════════════════════╝")


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
    nombre = input("\t║ ╠ Nombre: ").lower()
    return nombre


def altaApariencia():
    mostrarCabezas()
    cabeza = input("\t║ ╠═══╣ Escoge cabeza: ")
    esNum(cabeza)
    esRango(cabeza, 5)
    mostrarCuerpos(int(cabeza) - 1)

    cuerpo = input("\t║ ╠═══╣ Escoge cuerpo: ")
    esNum(cuerpo)
    esRango(cuerpo, 5)
    mostrarPiernas(int(cabeza) - 1, int(cuerpo) - 1)

    piernas = input("\t║ ╠═══╣ Escoge piernas: ")
    esNum(piernas)
    esRango(piernas, 5)
    # mostrarPersonaje(int(cabeza) - 1, int(cuerpo) - 1, int(piernas) - 1)

    return cabeza, cuerpo, piernas


def altaColor():
    print("\t║ ╠════════════════════════════════╗")
    print("\t║ ║ 1. Rojo  2. Amarillo  3. Verde ║")
    print("\t║ ║ 4. Azul  5. Morado    6. Salir ║")
    print("\t║ ╠════════════════════════════════╝")
    opc = input("\t║ ╠ Color: ")
    '''opc = input("\n\n\t[==== Escoge un color ====>\n"
                "\t[1. Rojo\n"
                "\t[2. Amarillo\n"
                "\t[3. Verde\n"
                "\t[4. Azul\n"
                "\t[5. Morado\n"
                "\t[0. Salir\n"
                "\t[===== Opcion: ")'''
    return opc


def mensajePuntos():
    print("\t║ ║\n\t║ ║ A continuacion, introduce la puntuacion del 1 al 10")
    print("\t║ ║ de los siguientes atributos\n\t║ ║")


def altaFuerza():
    bordeIzqDoble()
    opc = input('Fuerza: ')
    return opc


def altaInteligencia():
    bordeIzqDoble()
    opc = input('Inteligencia: ')
    return opc


def altaVida():
    bordeIzqDoble()
    opc = input('Vida: ')
    return opc


def altaDestreza():
    bordeIzqDoble()
    opc = input('Destreza: ')
    return opc


# INICIO PRINTS/INPUTS BAJA

def baja():
    bordeIzqDoble()
    opc = input('Introduce el nombre del personaje que quieras borrar: ').lower()
    return opc


def confirBaja():
    bordeIzqDoble()
    opc = input("Seguro que quieres dar de baja al personaje?[S/N]: ").lower()
    return opc


# INICIO PRINTS/INPUTS MODIFICAR
def nombreModificar():
    opc = input('Introduce el nombre del personaje que quiera modificar o pulse 0 para salir.').lower()
    return opc


def menuModificar():
    opc = input("\n\t[====== MODIFICACION PERSONAJE ======\n"
                "\t[1.Apariencia\n"
                "\t[2.Piernas\n"
                "\t[3.Color\n"
                "\t[4.Fuerza\n"
                "\t[5.Inteligencia\n"
                "\t[6.Vida\n"
                "\t[7.Destreza\n"
                "\t[0.Salir\n"
                "\t[Opcion: ")
    return opc


def confirModificar(campo):
    opc = input(f"Seguro que quiere modificar {campo} del curso?[S/N]: ").lower()
    return opc


def modificacionCorrecta():
    verdeOK("\tEntrada Valida")


# INICIO PRINTS/INPUTS BUSCAR
def buscar():
    bordeIzqDoble()
    opc = input('Introduce el nombre del personaje que quieras buscar: ').lower()
    return opc


def mostrarPj(pj):
    print(Style.BRIGHT, end="")

    cabeza = int(pj.cabeza) - 1
    cuerpo = int(pj.cuerpo) - 1
    piernas = int(pj.piernas) - 1

    print("\t║ ╚═╗")
    print("\t║   ╠═════════════════╦══════════════════════╗")
    print("\t║   ║  ", end="")
    colorPj(pj.color)
    print(getCabezas()[cabeza][0], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    mostrarNombre(pj.nombre, pj.color)
    print("║")
    print("\t║   ║  ", end="")
    colorPj(pj.color)
    print(getCabezas()[cabeza][1], end="")
    print(Fore.RESET, end="")
    print("   ╠══════════════════════╣")
    print("\t║   ║  ", end="")
    colorPj(pj.color)
    print(getCuerpos()[cuerpo][0], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    barraProgreso(int(pj.fuerza), "FUERZA  ")
    print("\t║   ║  ", end="")
    colorPj(pj.color)
    print(getCuerpos()[cuerpo][1], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    barraProgreso(int(pj.inteligencia), "INTELEC.")
    print("\t║   ║  ", end="")
    colorPj(pj.color)
    print(getCuerpos()[cuerpo][2], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    barraProgreso(int(pj.vida), "VIDA    ")
    print("\t║   ║  ", end="")
    colorPj(pj.color)
    print(getPiernas()[piernas][0], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    barraProgreso(int(pj.destreza), "DESTR.  ")
    print("\t║   ║  ", end="")
    colorPj(pj.color)
    print(getPiernas()[piernas][1], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    barraProgreso(int(pj.cp), "CP      ")
    print("\t║   ╠═════════════════╩══════════════════════╝")
    print(Style.RESET_ALL, end="")
    print("\t║ ╔═╝")
    '''x = PrettyTable()
    x.field_names = ["Nombre", "Color", "Fuerza", "Inteligencia", "Vida", "Destreza", "Puntos de Combate"]
    x.add_row([pj.nombre, colorPj(int(pj.color)), pj.fuerza, pj.inteligencia, pj.vida, pj.destreza, pj.cp])
    gris(str(x))'''


def barraProgreso(puntos, nombre):
    print(" [", end="")
    for i in range(puntos):
        print("■", end="")
    for i in range(10 - puntos):
        print(" ", end="")
    print(f"] {nombre}║")


def mostrarNombre(nombre, color):
    colorPj(color)
    disIzq = math.floor((22 - len(nombre)) / 2)
    disDer = math.ceil((22 - len(nombre)) / 2)
    while disIzq > 0:
        print(" ", end="")
        disIzq -= 1
    print(nombre.capitalize(), end="")
    while disDer > 0:
        print(" ", end="")
        disDer -= 1
    print(Fore.RESET, end="")


def mostrarTodos(personajes):
    print("\n")
    print(Style.BRIGHT, end="")
    cont = 0
    for pj in personajes:
        cont += 1

        cabeza = int(pj.cabeza) - 1
        cuerpo = int(pj.cuerpo) - 1
        piernas = int(pj.piernas) - 1

        if cont == 1:
            print("╔═════════════════╦══════════════════════╗")
        else:
            print("╠═════════════════╬══════════════════════╣")
        print("║  ", end="")
        colorPj(pj.color)
        print(getCabezas()[cabeza][0], end="")
        print(Fore.RESET, end="")
        print("   ║", end="")
        mostrarNombre(pj.nombre, pj.color)
        print("║")
        print("║  ", end="")
        colorPj(pj.color)
        print(getCabezas()[cabeza][1], end="")
        print(Fore.RESET, end="")
        print("   ╠══════════════════════╣")
        print("║  ", end="")
        colorPj(pj.color)
        print(getCuerpos()[cuerpo][0], end="")
        print(Fore.RESET, end="")
        print("   ║", end="")
        barraProgreso(int(pj.fuerza), "FUERZA  ")
        print("║  ", end="")
        colorPj(pj.color)
        print(getCuerpos()[cuerpo][1], end="")
        print(Fore.RESET, end="")
        print("   ║", end="")
        barraProgreso(int(pj.inteligencia), "INTELEC.")
        print("║  ", end="")
        colorPj(pj.color)
        print(getCuerpos()[cuerpo][2], end="")
        print(Fore.RESET, end="")
        print("   ║", end="")
        barraProgreso(int(pj.vida), "VIDA    ")
        print("║  ", end="")
        colorPj(pj.color)
        print(getPiernas()[piernas][0], end="")
        print(Fore.RESET, end="")
        print("   ║", end="")
        barraProgreso(int(pj.destreza), "DESTR.  ")
        print("║  ", end="")
        colorPj(pj.color)
        print(getPiernas()[piernas][1], end="")
        print(Fore.RESET, end="")
        print("   ║", end="")
        barraProgreso(int(pj.cp), "CP      ")
        if cont == len(personajes):
            print("╚═════════════════╩══════════════════════╝")
    print(Style.RESET_ALL)


# MENSAJES Y AVISOS


def noHayPersonajes():
    amarillo("\n\t\t╔═════════════════════════════════╗")
    amarillo("\t\t║ No hay personajes guardados aun ║")
    amarillo("\t\t╚═════════════════════════════════╝")


def saliendo():
    print("\t╚═╣Saliendo...")


def salirSinGuardar():
    print("\t╚═╣Saliendo sin guardar...")


def errorEntrada():
    rojo("     ╚═╣ Entrada no valida")


def maxErrores():
    amarillo("\t║ ║ Se han superado el maximo de 5 errores.")
    saliendo()


def campoCorrecto():
    verdeOK("\tEntrada Valida")


def colorPj(numString):
    num = int(numString)
    if num == 1:
        print(Fore.RED, end="")
    elif num == 2:
        print(Fore.LIGHTYELLOW_EX, end="")
    elif num == 3:
        print(Fore.GREEN, end="")
    elif num == 4:
        print(Fore.CYAN, end="")
    elif num == 5:
        print(Fore.MAGENTA, end="")
