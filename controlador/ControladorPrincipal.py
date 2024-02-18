from controlador import VerificationExceptions
from modelo import ConexionBBDD
from modelo.Personaje import Personaje
from vista import VistaGeneral
from vista.VistaGeneral import *
from vista.VistaMenus import menuVisual


def menu():
    """
    Funcion controlador del menu principal.
    :return:
    """
    finMenuAlumnos = False
    while not finMenuAlumnos:
        opc = menuVisual("MENU PRINCIPAL", ["Alta", "Baja", "Modificar", "Colsultar", "Mostrar Todos", "Mostrar por CP",
                                            "Mostrar por color", "Borrar todos los personajes"])
        if opc == "1":
            alta()
        elif opc == "2":
            if not ConexionBBDD.hayPersonajes():
                VistaGeneral.noHayPersonajes()
            else:
                baja()
        elif opc == "3":
            if not ConexionBBDD.hayPersonajes():
                VistaGeneral.noHayPersonajes()
            else:
                modificar()
        elif opc == "4":
            if not ConexionBBDD.hayPersonajes():
                VistaGeneral.noHayPersonajes()
            else:
                consultar()
        elif opc == "5":
            if not ConexionBBDD.hayPersonajes():
                VistaGeneral.noHayPersonajes()
            else:
                mostrarTodos()
        elif opc == "6":
            if not ConexionBBDD.hayPersonajes():
                VistaGeneral.noHayPersonajes()
            else:
                mostrarMayorMenorPj()
        elif opc == "7":
            if not ConexionBBDD.hayPersonajes():
                VistaGeneral.noHayPersonajes()
            else:
                mostrarPorColor()
        elif opc == "8":
            if not ConexionBBDD.hayPersonajes():
                VistaGeneral.noHayPersonajes()
            else:
                borrarTodos()
        elif opc == "0":
            saliendo()
            finMenuAlumnos = True
        else:
            errorEntrada()


def alta():
    """
    Funcion para realizar las altas
    :return:
    """
    VistaGeneral.header("     ALTA     ")
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
                    VerificationExceptions.nombreExiste(aux)
                    campoCorrecto()
                    nombre = aux
                    intentos = 0

            if (cabeza is None or cuerpo is None or piernas is None) and opcSalir != '0':
                cabeza, cuerpo, piernas = altaApariencia()

            color, intentos, opcSalir = pedirYComprobarValores(color, intentos, opcSalir, 1, 5)
            if opcSalir != '0':
                VistaGeneral.mensajePuntos()
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
        VistaGeneral.bordeFinalAlta()
        VistaGeneral.mostrarPj2(pj)
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
    VistaGeneral.header("     BAJA     ")
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
                VistaGeneral.bordeFinalBaja()
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
        Funcion permite modificar los campos de un personaje
        :return:
        """
    VistaGeneral.header("   MODIFICAR  ")
    nombre = None
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
        bordeFinSimple()

        # opc = VistaGeneral.menuModificar()
        opc = menuVisual("MENU MODIFICAR", ["Nombre", "Apariencia", "Color", "Fuerza", "Inteligencia"
            , "Vida", "Destreza"])

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
                    op = confirModificar("el nombre")
                    if op == "s":
                        pj.nombre = nuevoNombre
                        modificacionSi()
                    elif op == "n":
                        salir = True
                        modificacionNo()
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
                    op = confirModificar("la apariencia")
                    if op == "s":
                        pj.cabeza = nCabeza
                        pj.cuerpo = nCuerpo
                        pj.piernas = nPiernas
                        modificacionSi()
                    elif op == "n":
                        salir = True
                        modificacionNo()
                    else:
                        errorEntrada()
            elif fallos == 5:
                maxErrores()
            else:
                saliendo()

        # Modificacion del color
        elif opc == '3':
            color, salir = modificarCampo(salir, 1, 5, "el color")
            if color is not None:
                pj.color = color
        # Modificacion de la fuerza
        elif opc == '4':
            fuerza, salir = modificarCampo(salir, 2, 10, "la fuerza")
            if fuerza is not None:
                pj.fuerza = fuerza
        # Modificacion de la inteligencia
        elif opc == '5':
            intel, salir = modificarCampo(salir, 3, 10, "la inteligencia")
            if intel is not None:
                pj.inteligencia = intel
        # Modificacion de la vida
        elif opc == '6':
            vida, salir = modificarCampo(salir, 4, 10, "la vida")
            if vida is not None:
                pj.vida = vida
        # Modificacion de la destreza
        elif opc == '7':
            destreza, salir = modificarCampo(salir, 5, 10, "la destreza")
            if destreza is not None:
                pj.destreza = destreza
        # Salir
        elif opc == '0':
            salir = True
        else:
            errorEntrada()

    if pj is not None:
        ConexionBBDD.bajaBBDD(nombre)
        ConexionBBDD.altaBBDD(pj)
    saliendo()


def modificarCampo(salir, campo, lim, nombreCampo):
    """
    Funcion que pide y devuelve un campo por medio de las vistas y la conexion de la base de datos para ser modificado
    :param salir: recibe el booleano para controlar salida
    :param campo: el numero del campo para modificar
    :param lim: el limite del rango que puede ser o 5 para colores o 10 para las estadisticas
    :param nombreCampo:
    :return:devuelve el nuevo valor del campo a modificar
    """
    nValor = None
    fallos = 0
    opcSalir = None
    aux = None
    while fallos < 5 and nValor is None and opcSalir != '0':
        try:
            aux = selectAlta(campo)
            if aux == '0':
                opcSalir = '0'
            else:
                VerificationExceptions.esNum(aux)
                VerificationExceptions.esRango(aux, lim)
                nValor = aux
                campoCorrecto()
        except VerificationExceptions.MisExceptions as err:
            rojo(str(err))
            fallos += 1
    if fallos < 5 and opcSalir != '0':
        op = None
        while not salir and op is None:
            op = confirModificar(nombreCampo)
            if op == "s":
                modificacionSi()
            elif op == "n":
                nValor = None
                modificacionNo()
            else:
                errorEntrada()
    elif fallos == 5:
        maxErrores()
    else:
        saliendo()
    return nValor, salir


def consultar():
    """
    Funcion que actua de intermediario entre la vista y la conexion a la base de datos
    para buscar un personaje por nombre.
    :return:
    """
    VistaGeneral.header("  CONSULTAR   ")
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
            fallos = 0
            pj = ConexionBBDD.buscarBBDD(nombre)
            VistaGeneral.bordeFinalConsulta()
            VistaGeneral.mostrarPj(pj)

        elif (fallos == 5):
            maxErrores()
        elif (opcSalir == '0'):
            saliendo()


def mostrarPorColor():
    """
    Funcion que recoge de la conexion de la base de datos los personajes guardados, guarda en una lista auxiliar los del color elegido
     y se los manda a la vista para mostrarlos
    :return:
    """
    opc = None
    aux = []
    salir = False
    while opc != '0' and salir == False:
        try:
            opc = VistaGeneral.altaColor()
            VerificationExceptions.esRango(opc, 5)
            personajes = ConexionBBDD.mostrarBBDD()
            for personaje in personajes:
                if personaje.color == opc:
                    aux.append(personaje)
            if len(aux) > 0:
                VistaGeneral.mostrarTodos(aux)
            else:
                VistaGeneral.noHayColor()
            salir = True
        except VerificationExceptions.MisExceptions as err:
            rojo(str(err))


def mostrarMayorMenorPj():
    """
        Funcion que recoge de la conexion de la base de datos los personajes guardados, los ordena por los
         puntos de combate (cp) y se los manda a la vista para mostrarlos
        :return:
        """
    personajes = ConexionBBDD.mostrarBBDD()
    for i in range(len(personajes)):
        for j in range(len(personajes) - 1):
            if personajes[j].cp < personajes[j + 1].cp:
                personajes[j], personajes[j + 1] = personajes[j + 1], personajes[j]
    VistaGeneral.mostrarTodos(personajes)


def mostrarTodos():
    """
    Funcion que recoge de la conexion de la base de datos los personajes guardados y que
    y se los manda a la vista para mostrarlos
    :return:
    """
    personajes = ConexionBBDD.mostrarBBDD()
    VistaGeneral.mostrarTodos(personajes)

def borrarTodos():
    """
    Funcion que para borrar los datos de la base de datos
    :return:
    """
    op = confirBajaRojo()
    if op == "s":
        ConexionBBDD.borrarTodaBD()
        VistaGeneral.bordeFinalBaja()
        salir = True
    elif op == "n":
        salir = True
        salirSinGuardar()
    else:
        VistaGeneral.errorEntrada()



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
