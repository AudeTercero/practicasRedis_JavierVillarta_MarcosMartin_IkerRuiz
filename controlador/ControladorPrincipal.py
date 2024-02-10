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
        ConexionBBDD.alta(pj)
    elif (opcSalir == '0'):
        print("Saliendo")
    else:
        amarillo("Se han superado el maximo de errores.")


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
                VerificationExceptions.hayAlgo(aux)
                VerificationExceptions.nombreNoExiste(aux)
                nombre = aux
                finBaja = True
        except VerificationExceptions.MisExceptions as err:
            fallos += 1
            rojo(str(err))

    if fallos < 5 and opcSalir != '0':
        salir = False
        while not salir:
            op = input("Seguro que quiere dar de baja al curso?[S/N]: ").lower()

            if op == "s":
                ConexionBBDD.baja(nombre)
                salir = True
            elif op == "n":
                salir = True
                print("Saliendo sin guardar...")
            else:
                VistaGeneral.errorEntrada()

    elif fallos == 5:
        amarillo("Has superado el maximos de fallos permitidos que son 5")
    else:
        print("Saliendo...")


def modificar():
    """
        Funcion que permite modificar los campos de un curso
        :return:
        """
    nombre = None
    cabeza = None
    cuerpo = None
    piernas = None
    color = None
    fuerza = None
    inteligencia = None
    vida = None
    destreza = None
    fallos = 0
    opcSalir = None
    salir = False
    while not salir and opcSalir != '0' and fallos < 5:
       try:
           aux = VistaGeneral.nombreModificar()
           opcSalir = aux
           if opcSalir != '0':
               VerificationExceptions.hayAlgo(aux)
               VerificationExceptions.nombreNoExiste(aux)
               nombre = aux
               salir = True
       except VerificationExceptions.MisExceptions as err:
           fallos += 1
           rojo(str(err))
    salir = False
    while fallos < 5 and not salir and opcSalir != '0':
       opc = VistaGeneral.menuModificar()
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
                       VerificationExceptions.hayAlgo(aux)
                       VerificationExceptions.nombreExiste(aux)
                       nuevoNombre = aux
                       salirNombre = True
                       verde("Nombre correcto")
               except VerificationExceptions.MisExceptions as err:
                   rojo(str(err))
                   fallos += 1
           if fallos < 5 and opcSalir != '0':
               op = None
               while not salir and op is None:
                   op = input("Seguro que quiere modificar el nombre del curso?[S/N]: ").lower()
                   if op == "s":
                       ConsultasCurso.consModificar(nombre, 'nombre', nuevoNombre)
                       verde("Modificacion realizada correctamente")
                       nombre = nuevoNombre
                   elif op == "n":
                       salir = True
                       print("Saliendo sin guardar...")
                   else:
                       rojo("Entrada no valida.")
           elif fallos == 5:
               amarillo("No puedes fallar mas de 5 veces")
           else:
               print("Saliendo...")
       elif opc == '2':
           nuevaDescripcion = None
           fallos = 0
           opcSalir = None
           while fallos < 5 and nuevaDescripcion is None and opcSalir != '0':
               try:
                   aux = input('Escriba la nueva descripcion o pulse 0 para salir:')
                   opcSalir = aux
                   if opcSalir != '0':
                       VerificationExceptions.hayAlgo(aux)
                       nuevaDescripcion = aux
                       verde("Descripcion Correcta")
               except VerificationExceptions.MisExceptions as err:
                   rojo(str(err))
                   fallos += 1
           if fallos < 5 and opcSalir != '0':
               op = None
               while not salir and op is None:
                   op = input("Seguro que quiere modificar la descripcion del curso?[S/N]: ").lower()
                   if op == "s":
                       ConsultasCurso.consModificar(nombre, 'descripcion', nuevaDescripcion)
                       print("Modificacion realizada correctamente")
                   elif op == "n":
                       salir = True
                       print("Saliendo sin guardar...")
                   else:
                       rojo("Entrada no valida.")
           elif fallos == 5:
               amarillo("No puedes fallar mas de 5 veces")
           else:
               print("Saliendo...")
       elif opc == '0':
           print("Saliendo...")
           salir = True
       else:
           rojo("No hay esa opcion")


def consultar():
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
            pj = ConexionBBDD.buscar(nombre)
            VistaGeneral.mostrarPj(pj)


        elif (fallos == 5):
            amarillo("Has superado el maximos de fallos permitidos que son 5")
        elif (opcSalir == '0'):
            print("Saliendo...")


def mostrarTodos():
    personajes = ConexionBBDD.mostrar()
    VistaGeneral.mostrarTodos(personajes)


def selectAlta(num):
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
