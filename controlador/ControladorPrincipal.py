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
                    VerificationExceptions.longCadena(aux)
                    campoCorrecto()
                    nombre = aux
                    intentos = 0

            if cabeza is None or cuerpo is None or piernas is None:
                cabeza, cuerpo, piernas = altaApariencia()

            color, intentos, opcSalir = pedirYComprobarValores(color, intentos, opcSalir, 1, 5)
            fuerza, intentos, opcSalir = pedirYComprobarValores(fuerza, intentos, opcSalir, 2, 10)
            inteligencia, intentos, opcSalir = pedirYComprobarValores(inteligencia, intentos, opcSalir, 3, 10)
            vida, intentos, opcSalir = pedirYComprobarValores(vida, intentos, opcSalir, 4, 10)
            destreza, intentos, opcSalir = pedirYComprobarValores(destreza, intentos, opcSalir, 5, 10)

            salir = True
            if (opcSalir == '0'):
                salir = True
        except VerificationExceptions.MisExceptions as err:
            intentos += 1
            rojo(str(err))

    if (intentos < 5 and opcSalir != '0'):
        pj = Personaje(nombre, cabeza, cuerpo, piernas, color, fuerza, inteligencia, vida, destreza)
        ConexionBBDD.altaBBDD(pj)
    elif (opcSalir == '0'):
        saliendo()
    else:
        maxErrores()


def pedirYComprobarValores(value, intentos, opcSalir, num, limite):
    """
    Funcion que pide y comprueba los datos del personaje que estamos dando de alta si pasa
    las verificaciones devolvera el valor pedido los intentos y si a pulsado cero para salir.
    """
    if (value is None and opcSalir != '0'):
        aux = selectAlta(num)
        opcSalir = aux
        if (opcSalir != '0'):
            VerificationExceptions.esNum(aux)
            VerificationExceptions.esRango(aux, limite)
            campoCorrecto()
            value = aux
            intentos = 0
    return value, intentos, opcSalir


def baja():
    """
       Funcion que da de baja un personaje
       :return:
       """
    nombre = None
    opcSalir = None
    fallos = 0
    finBaja = False
    while not finBaja and opcSalir != '0' and fallos < 5:
        try:
            aux = VistaGeneral.baja()
            opcSalir = aux
            if opcSalir != '0':
                VerificationExceptions.longCadena(aux)
                VerificationExceptions.nombreNoExiste(aux)
                nombre = aux
                finBaja = True
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            rojo(str(err))

    if fallos < 5 and opcSalir != '0':
        salir = False
        while not salir:
            op = confirBaja()

            if op == "s":
                ConexionBBDD.bajaBBDD(nombre)
                salir = True
            elif op == "n":
                salir = True
                salirSinGuardar()
            else:
                VistaGeneral.errorEntrada()

    elif fallos == 5:
        maxErrores()
    else:
        saliendo()


def modificar():
    """
        Funcion que permite modificar los campos de un curso
        :return:
        """
    nombre = None
    nCabeza = None
    nCuerpo = None
    nPiernas = None
    color = None
    fuerza = None
    inteligencia = None
    vida = None
    destreza = None
    pj = None
    fallos = 0
    opcSalir = None
    salir = False
    while not salir and opcSalir != '0' and fallos < 5:
        try:
            aux = VistaGeneral.nombreModificar()
            opcSalir = aux
            if opcSalir != '0':
                VerificationExceptions.longCadena(aux)
                VerificationExceptions.nombreNoExiste(aux)
                nombre = aux
                salir = True
                pj = ConexionBBDD.buscarBBDD(nombre)

        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            rojo(str(err))
    salir = False
    while fallos < 5 and not salir and opcSalir != '0':
        opc = VistaGeneral.menuModificar()

        # Modificacion del nombre
        if opc == '1':
            nuevoNombre = None
            fallos = 0
            opcSalir = None
            salirNombre = False
            while not salirNombre and fallos < 5 and opcSalir != '0':
                try:
                    aux = altaNombre()
                    opcSalir = aux
                    if opcSalir != '0':
                        VerificationExceptions.longCadena(aux)
                        VerificationExceptions.nombreExiste(aux)
                        nuevoNombre = aux
                        salirNombre = True
                        campoCorrecto()
                except VerificationExceptions.MisExceptions as err:
                    rojo(str(err))
                    fallos += 1
            if fallos < 5 and opcSalir != '0':
                op = None
                while not salir and op is None:
                    confirModificar("el nombre")
                    if op == "s":
                        pj.nombre = nuevoNombre
                        modificacionCorrecta()
                    elif op == "n":
                        salir = True
                        salirSinGuardar()
                    else:
                        errorEntrada()
            elif fallos == 5:
                maxErrores()
            else:
                saliendo()

        # Modificacion del cuerpo
        elif opc == '2':
            nCabeza = None
            nCuerpo = None
            nPiernas = None
            fallos = 0
            opcSalir = None
            while fallos < 5 and (nCabeza is None or nCuerpo is None or nPiernas is None) and opcSalir != '0':
                try:
                    nCabeza, nCuerpo, nPiernas = altaApariencia()
                    if nCabeza == '0' or nCuerpo == '0' or nPiernas == '0':
                        opcSalir = '0'
                    else:
                        campoCorrecto()
                except VerificationExceptions.MisExceptions as err:
                    rojo(str(err))
                    fallos += 1
            if fallos < 5 and opcSalir != '0':
                op = None
                while not salir and op is None:
                    confirModificar("la apariencia")
                    if op == "s":
                        pj.cabeza = nCabeza
                        pj.cuerpo = nCuerpo
                        pj.piernas = nPiernas
                        modificacionCorrecta()
                    elif op == "n":
                        salir = True
                        salirSinGuardar()
                    else:
                        errorEntrada()
            elif fallos == 5:
                maxErrores()
            else:
                saliendo()

        # Modificacion del color
        elif opc == '3':
            color, salir = modificarCampo(pj, salir, 1, 5, "el color")
            if color is not None:
                pj.color = color
        elif opc == '4':
            fuerza, salir = modificarCampo(pj, salir, 2, 10, "la fuerza")
            if fuerza is not None:
                pj.fuerza = fuerza
        elif opc == '5':
            intel, salir = modificarCampo(pj, salir, 3, 10, "la inteligencia")
            if intel is not None:
                pj.inteligencia = intel
        elif opc == '6':
            vida, salir = modificarCampo(pj, salir, 4, 10, "la vida")
            if vida is not None:
                pj.vida = vida
        elif opc == '7':
            destreza, salir = modificarCampo(pj, salir, 5, 10, "la destreza")
            if destreza is not None:
                pj.destreza = destreza
        elif opc == '0':
            saliendo()
            salir = True
        else:
            errorEntrada()

    if pj is not None:
        ConexionBBDD.bajaBBDD(nombre)
        ConexionBBDD.altaBBDD(pj)


def modificarCampo(pj, salir, campo, lim, nombreCampo):
    nValor = None
    fallos = 0
    opcSalir = None
    aux = None
    while fallos < 5 and nValor is None and opcSalir != '0':
        try:
            aux = selectAlta(campo)
            VerificationExceptions.esRango(aux, lim)
            if aux == '0':
                opcSalir = '0'
            else:
                campoCorrecto()
        except VerificationExceptions.MisExceptions as err:
            rojo(str(err))
            fallos += 1
    if fallos < 5 and opcSalir != '0':
        op = None
        while not salir and op is None:
            confirModificar(nombreCampo)
            if op == "s":
                nValor = aux
                modificacionCorrecta()
            elif op == "n":
                salir = True
                salirSinGuardar()
            else:
                errorEntrada()
    elif fallos == 5:
        maxErrores()
    else:
        saliendo()
    return nValor, salir


def consultar():
    """
    Funcion que
    :return:
    """
    nombre = None
    opcSalir = None
    fallos = 0
    while (opcSalir != '0' and fallos < 5):
        entrar = True
        try:
            nombre = VistaGeneral.buscar()
            opcSalir = nombre
            if (opcSalir != '0'):
                VerificationExceptions.nombreNoExiste(nombre)
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            entrar = False
            rojo(str(err))
        if (fallos < 5 and opcSalir != '0' and entrar):
            pj = ConexionBBDD.buscarBBDD(nombre)
            VistaGeneral.mostrarPj(pj)

        elif (fallos == 5):
            modificacionCorrecta()
        elif (opcSalir == '0'):
            saliendo()


def mostrarTodos():
    """
    Funcion que recoge de la conexion de la base de datos los personajes guardados y que
    y se los manda a la vista para mostrarlos
    :return:
    """
    personajes = ConexionBBDD.mostrarBBDD()
    VistaGeneral.mostrarTodos(personajes)


def selectAlta(num):
    """
    Funcion que selecciona el tipo de vista de altas
    :param num: recibe el numero para seleccionar el el tipo de vista de altas
    :return: devuelve la funcion de la vista del tipo de alta que le pasamos por parametro
    """
    if num == 1:
        return altaColor()
    elif num == 2:
        return altaFuerza()
    elif num == 3:
        return altaInteligencia()
    elif num == 4:
        return altaVida()
    elif num == 5:
        return altaDestreza()
