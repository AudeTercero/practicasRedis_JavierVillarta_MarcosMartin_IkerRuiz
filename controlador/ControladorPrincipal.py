from controlador import VerificationExceptions
from modelo import ConexionBBDD
from modelo.Personaje import Personaje
from vista import VistaGeneral
from vista.VistaGeneral import *


def menu():
    finMenuAlumnos = False
    while not finMenuAlumnos:
        opc = VistaGeneral.menu()
        if opc == "1":
            alta()
        elif opc == "2":
            baja()
        elif opc == "3":
            modificar()
        elif opc == "4":
            consultar()
        elif opc == "5":
            mostrarTodos()
        elif opc == "0":
            saliendo()
            finMenuAlumnos = True
        else:
            errorEntrada()


def alta():
    nombre = None
    cabeza = None
    cuerpo = None
    piernas = None
    color = None
    fuerza = None
    inteligencia = None
    vida = None
    destreza = None
    intentos = 0
    opcSalir = None
    salir = False
    while (intentos < 5 and salir is False):

        try:
            if (nombre is None and opcSalir != '0'):
                aux = altaNombre()
                opcSalir = aux
                if (opcSalir != '0'):
                    VerificationExceptions.hayAlgo(aux)
                    verde("Nombre introducido correctamente")
                    nombre = aux
                    intentos = 0

            cabeza, intentos, opcSalir = pedirYComprobarValores(cabeza, intentos, opcSalir, 1, 5)
            cuerpo, intentos, opcSalir = pedirYComprobarValores(cuerpo, intentos, opcSalir, 2, 5)
            piernas, intentos, opcSalir = pedirYComprobarValores(piernas, intentos, opcSalir, 3, 5)
            color, intentos, opcSalir = pedirYComprobarValores(color, intentos, opcSalir, 4, 5)
            fuerza, intentos, opcSalir = pedirYComprobarValores(fuerza, intentos, opcSalir, 5, 10)
            inteligencia, intentos, opcSalir = pedirYComprobarValores(inteligencia, intentos, opcSalir, 6, 10)
            vida, intentos, opcSalir = pedirYComprobarValores(vida, intentos, opcSalir, 7, 10)
            destreza, intentos, opcSalir = pedirYComprobarValores(destreza, intentos, opcSalir, 8, 10)

            salir = True
            if (opcSalir == '0'):
                salir = True
        except VerificationExceptions.MisExceptions as err:
            intentos += 1
            rojo(str(err))

    if (intentos < 5 and opcSalir != '0'):
        pj = Personaje(nombre, cabeza, cuerpo, piernas, color, fuerza, inteligencia, vida, destreza)
        ConexionBBDD.alta(pj.nombre, pj.cabeza, pj.cuerpo, pj.piernas, pj.color, pj.fuerza, pj.inteligencia, pj.vida,
                          pj.destreza, pj.cp)
    elif (opcSalir == '0'):
        print("Saliendo")
    else:
        amarillo("Se han superado el maximo de errores.")


def pedirYComprobarValores(value, intentos, opcSalir, num, limite):
    if (value is None and opcSalir != '0'):
        aux = selectAlta(num)
        opcSalir = aux
        if (opcSalir != '0'):
            VerificationExceptions.esNum(aux)
            VerificationExceptions.esRango(aux, limite)
            verde("Direccion introducida correctamente")
            value = aux
            intentos = 0
    return value, intentos, opcSalir


def baja(nombre):
    ConexionBBDD.baja(nombre)


def modificar():
    print()


def consultar():  # -------------------------------- Lo he puesto aqui para poder hacer pruebas simplemente
    mostrarCabezas()
    cabeza = int(input("Escoge cabeza: ")) - 1
    mostrarCuerpos(cabeza)
    cuerpo = int(input("Escoge cuerpo: ")) - 1
    mostrarPiernas(cabeza, cuerpo)
    piernas = int(input("Escoge piernas: ")) - 1
    mostrarPersonaje(cabeza, cuerpo, piernas)


def mostrarTodos():
    resultado = ConexionBBDD.mostrar()
    for values in resultado:
        print(values)


def selectAlta(num):
    if num == 1:
        return altaCabeza()
    elif num == 2:
        return altaCuerpo()
    elif num == 3:
        return altaPiernas()
    elif num == 4:
        return altaColor()
    elif num == 5:
        return altaFuerza()
    elif num == 6:
        return altaInteligencia()
    elif num == 7:
        return altaVida()
    elif num == 8:
        return altaDestreza()
