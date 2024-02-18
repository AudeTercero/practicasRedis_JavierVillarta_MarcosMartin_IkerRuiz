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
    verdeSinSalto(str(getCabezas()[0][0] + "1 " + getCabezas()[1][0] + "2 " + getCabezas()[2][0]
                      + "3 " + getCabezas()[3][0] + "4 " + getCabezas()[4][0] + "5 "))
    print("║")
    bordeIzq()
    verdeSinSalto(str(getCabezas()[0][1] + "  " + getCabezas()[1][1] + "  " + getCabezas()[2][1]
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
    :param cabeza: Cabeza seleccionada previamente
    :return:
    """
    piernasMolde = [
        "    /   \\   ",
        "   /     \\  "]
    ################################# CABEZAS ######################################
    bordePersonajesTop()
    bordeIzq()
    azulSinSalto(str(getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " +
                     getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0]))
    bordeDer()
    bordeIzq()
    azulSinSalto(str(getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " +
                     getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1]))
    bordeDer()

    ################################# CUERPOS ######################################
    bordeIzq()
    verdeSinSalto(
        str(getCuerpos()[0][0] + " 1" + getCuerpos()[1][0] + " 2" + getCuerpos()[2][0] + "3 " + getCuerpos()[3][0]
            + "4 " + getCuerpos()[4][0] + "5 "))
    print("║")
    bordeIzq()
    verdeSinSalto(
        str(getCuerpos()[0][1] + "  " + getCuerpos()[1][1] + "  " + getCuerpos()[2][1] + "  " + getCuerpos()[3][1]
            + "  " + getCuerpos()[4][1]))
    bordeDer()
    bordeIzq()
    verdeSinSalto(str(getCuerpos()[0][2] + "  " + getCuerpos()[1][2] + "  " + getCuerpos()[2][2] + "  "
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
    """
    Esta funcion muestra todas las piernas disponibles junto con la cabeza y el cuerpo
    :param cabeza: Cabeza seleccionada previamente
    :param cuerpo: Cuerpo seleccionado previamente
    :return:
    """
    bordePersonajesTop()
    bordeIzq()
    azulSinSalto(str(getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0] + "  " +
                     getCabezas()[cabeza][0] + "  " + getCabezas()[cabeza][0]))
    bordeDer()
    bordeIzq()
    azulSinSalto(str(getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1] + "  " +
                     getCabezas()[cabeza][1] + "  " + getCabezas()[cabeza][1]))
    bordeDer()
    bordeIzq()
    azulSinSalto(str(getCuerpos()[cuerpo][0] + "  " + getCuerpos()[cuerpo][0] + "  " + getCuerpos()[cuerpo][0] + "  " +
                     getCuerpos()[cuerpo][0] + "  " + getCuerpos()[cuerpo][0]))
    bordeDer()
    bordeIzq()
    azulSinSalto(str(getCuerpos()[cuerpo][1] + "  " + getCuerpos()[cuerpo][1] + "  " + getCuerpos()[cuerpo][1] + "  " +
                     getCuerpos()[cuerpo][1] + "  " + getCuerpos()[cuerpo][1]))
    bordeDer()
    bordeIzq()
    azulSinSalto(str(getCuerpos()[cuerpo][2] + "  " + getCuerpos()[cuerpo][2] + "  " + getCuerpos()[cuerpo][2] + "  " +
                     getCuerpos()[cuerpo][2] + "  " + getCuerpos()[cuerpo][2]))
    bordeDer()

    bordeIzq()
    verdeSinSalto(str(getPiernas()[0][0] + "1 " + getPiernas()[1][0] + "2 " + getPiernas()[2][0] + "3 "
                      + getPiernas()[3][0] + "4 " + getPiernas()[4][0] + "5 "))
    print("║")
    bordeIzq()
    verdeSinSalto(str(getPiernas()[0][1] + "  " + getPiernas()[1][1] + "  " + getPiernas()[2][1] + "  "
                      + getPiernas()[3][1] + "  " + getPiernas()[4][1]))
    bordeDer()
    bordePersonajesBottom()


def header(titulo):
    """
    Muestra la cabecera de los apartados
    :param titulo: El titulo de la cabecera
    :return:
    """
    print("\n\t╔═══════════════════╦══════════╗")
    print(f"\t║  {titulo}   ║ 0. Salir ║")
    print("\t╠═╦═════════════════╩══════════╝")


def bordeIzq():
    """
    Funcion que facilita la impresion grafica de la aplicacion
    :return:
    """
    print("\t║ ", end="")


def bordeIzqDoble():
    """
    Funcion que facilita la impresion grafica de la aplicacion
    :return:
    """
    print("\t║ ╠ ", end="")


def bordeDer():
    """
    Funcion que facilita la impresion grafica de la aplicacion
    :return:
    """
    print("  ║")


def bordeFinalAlta():
    """
    Se muestra tras finalizar un alta
    :return:
    """
    print("\t╚═╩══╣ ", end="")
    azulSinSalto("Alta realizada con exito")
    print()


def bordeFinalBaja():
    """
    Se muestra tras finalizar una baja
    :return:
    """
    print("\t╚═╩══╣ ", end="")
    azulSinSalto("Baja realizada con exito")
    print()


def bordeFinalConsulta():
    """
    Se muestra tras finalizar una consulta
    :return:
    """
    print("\t╠═╬══╣ ", end="")
    azulSinSalto("Personaje encontrado")
    print()


def bordePersonajesTop():
    """
    Funcion que facilita la impresion grafica de la aplicacion
    :return:
    """
    print("\t║ ╚═════════════════════════════════════════════════════════════════════╗")


def bordePersonajesBottom():
    """
    Funcion que facilita la impresion grafica de la aplicacion
    :return:
    """
    print("\t║ ╔═════════════════════════════════════════════════════════════════════╝")


def bordeFinSimple():
    """
    Funcion que facilita la impresion grafica de la aplicacion
    :return:
    """
    print("\t╚═╝")


# INICIO PRINTS/INPUTS ALTAS
def altaNombre():
    """
    Recibe, muestra y devuelve el parametro nombre
    :return: nombre
    """
    nombre = input("\t║ ╠ Nombre: ").lower()
    return nombre


def altaApariencia():
    """
    Maneja el alta de los parametros para la creacion del personaje
    :return: parametros del personaje
    """
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
    """
    Maneja la eleccion del color
    :return: color seleccionado
    """
    print("\t║ ╠════════════════════════════════╗")
    print("\t║ ║ ", end="")
    rojoSinSalto("1. Rojo  ")
    amarilloSinSalto("2. Amarillo  ")
    verdeSinSalto("3. Verde ")
    print("║")
    print("\t║ ║ ", end="")
    azulSinSalto("4. Azul  ")
    morado("5. Morado    ")
    print("0. Salir ║")
    print("\t║ ╠════════════════════════════════╝")
    opc = input("\t║ ╠ Color: ")
    return opc


def mensajePuntos():
    """
    Mensaje que informa al usuario
    :return:
    """
    print("\t║ ║\n\t║ ║ A continuacion, introduce la puntuacion del 1 al 10")
    print("\t║ ║ de los siguientes atributos\n\t║ ║")


def altaFuerza():
    """
    Recibe, muestra y devuelve el parametro fuerza
    :return: fuerza
    """
    bordeIzqDoble()
    opc = input('Fuerza: ')
    return opc


def altaInteligencia():
    """
    Recibe, muestra y devuelve el parametro inteligencia
    :return: inteligencia
    """
    bordeIzqDoble()
    opc = input('Inteligencia: ')
    return opc


def altaVida():
    """
    Recibe, muestra y devuelve el parametro vida
    :return: vida
    """
    bordeIzqDoble()
    opc = input('Vida: ')
    return opc


def altaDestreza():
    """
    Recibe, muestra y devuelve el parametro destreza
    :return: destreza
    """
    bordeIzqDoble()
    opc = input('Destreza: ')
    return opc


# INICIO PRINTS/INPUTS BAJA

def baja():
    """
    Pide el personaje que se quiere dar de baja
    :return: personaje seleccionado
    """
    bordeIzqDoble()
    opc = input('Introduce el nombre del personaje que quieras borrar: ').lower()
    return opc


def confirBaja():
    """
    Pide confirmacion para la baja
    :return: resultado
    """
    bordeIzqDoble()
    opc = input("Seguro que quieres dar de baja al personaje?[S/N]: ").lower()
    return opc


def confirBajaRojo():
    """
    Pide confirmacion para borrar todos los personajes
    :return:
    """
    bordeIzqDoble()
    rojoSinSalto("Seguro que quieres dar de baja a todos los personajes [S/N]: ")
    opc = input().lower()
    return opc


# INICIO PRINTS/INPUTS MODIFICAR
def nombreModificar():
    """
    Permite la busqueda del personaje a modificar
    :return: resultado
    """
    bordeIzqDoble()
    opc = input('Introduce el nombre del personaje que quieras modificar: ').lower()
    return opc


def confirModificar(campo):
    """
    Pide la confirmacion para modificar
    :param campo: El campo que se modifica
    :return: resultado
    """
    bordeIzqDoble()
    opc = input(f"Seguro que quieres modificar {campo} del curso?[S/N]: ").lower()
    return opc


def modificacionSi():
    """
    Mensaje de campo modificado
    :return:
    """
    print("\t║ ║\t", end="")
    azulSinSalto("\tCampo Modificado")
    print()


def modificacionNo():
    """
    Mensaje de salir sin modificar
    :return:
    """
    print("\t║ ║\tVolviendo sin Modificar...")


# INICIO PRINTS/INPUTS BUSCAR
def buscar():
    """
    Pide el nombre del personaje a buscar
    :return:
    """
    bordeIzqDoble()
    opc = input('Introduce el nombre del personaje que quieras buscar: ').lower()
    return opc


def mostrarPj(pj):
    """
    Muestra el personaje de forma atractiva para el usuario para la consulta
    :param pj: El personaje a mostrar
    :return:
    """
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


def mostrarPj2(pj):
    """
    Muestra el personaje de forma atractiva para el usuario tras el alta
    :param pj: El personaje
    :return:
    """
    print(Style.BRIGHT, end="")

    cabeza = int(pj.cabeza) - 1
    cuerpo = int(pj.cuerpo) - 1
    piernas = int(pj.piernas) - 1

    print("\n\t╔═════════════════╦══════════════════════╗")
    print("\t║  ", end="")
    colorPj(pj.color)
    print(getCabezas()[cabeza][0], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    mostrarNombre(pj.nombre, pj.color)
    print("║")
    print("\t║  ", end="")
    colorPj(pj.color)
    print(getCabezas()[cabeza][1], end="")
    print(Fore.RESET, end="")
    print("   ╠══════════════════════╣")
    print("\t║  ", end="")
    colorPj(pj.color)
    print(getCuerpos()[cuerpo][0], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    barraProgreso(int(pj.fuerza), "FUERZA  ")
    print("\t║  ", end="")
    colorPj(pj.color)
    print(getCuerpos()[cuerpo][1], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    barraProgreso(int(pj.inteligencia), "INTELEC.")
    print("\t║  ", end="")
    colorPj(pj.color)
    print(getCuerpos()[cuerpo][2], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    barraProgreso(int(pj.vida), "VIDA    ")
    print("\t║  ", end="")
    colorPj(pj.color)
    print(getPiernas()[piernas][0], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    barraProgreso(int(pj.destreza), "DESTR.  ")
    print("\t║  ", end="")
    colorPj(pj.color)
    print(getPiernas()[piernas][1], end="")
    print(Fore.RESET, end="")
    print("   ║", end="")
    barraProgreso(int(pj.cp), "CP      ")
    print("\t╚═════════════════╩══════════════════════╝")
    print(Style.RESET_ALL, end="")


def barraProgreso(puntos, nombre):
    """
    Funcion usada al morstrar un personaje
    Muestra una barra de progreso de un valor recibido
    :param puntos: la cantidad de puntos
    :param nombre: el nombre del atributo
    :return:
    """
    print(" [", end="")
    for i in range(puntos):
        print("■", end="")
    for i in range(10 - puntos):
        print(" ", end="")
    print(f"] {nombre}║")


def mostrarNombre(nombre, color):
    """
    Muestra un nombre manejando los espacios a su alrededor
    en funciond de la longitud de caracteres
    Se usa en mostrarPj()
    :param nombre: nombre
    :param color: color del nombre
    :return:
    """
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
    """
    Muestra todos los personajes que la funcion de mostrarPj()
    :param personajes: lista con los personajes
    :return:
    """
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
    """
    Muestra un cartel informando de que no hay personajes registrados en la BD
    :return:
    """
    amarillo("\n\t\t╔═════════════════════════════════╗")
    amarillo("\t\t║ No hay personajes guardados aun ║")
    amarillo("\t\t╚═════════════════════════════════╝")


def noHayColor():
    """
    Muestra un aviso de que no hay ningun personaje con ese color
    :return:
    """
    amarillo("\t║ ║ No existe ningun personaje con ese color.")


def saliendo():
    """
    Muestra un mensaje de salir
    :return:
    """
    print("\t╚═╣Saliendo...")


def salirSinGuardar():
    """
    Muestra un mensaje de salir sin guardar
    :return:
    """
    print("\t╚═╣Saliendo sin guardar...")


def errorEntrada():
    """
    Muestra un mensaje de entrada no valida
    :return:
    """
    rojo("    ╚═╣ Entrada no valida")


def maxErrores():
    """
    Muestra un mensaje del maximo de errores
    :return:
    """
    amarillo("\t║ ║ Se han superado el maximo de 5 errores.")
    saliendo()


def campoCorrecto():
    """
    Muestra un mensaje de campo correcto
    :return:
    """
    verdeOK("\tEntrada Valida")


def colorPj(numString):
    """
    Maneja el control de los colores
    Usado en la funcion mostrarPj()
    :return:
    """
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
