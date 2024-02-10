from vista.VistaErrores import *
from modelo.ConexionBBDD import existeNombreBBDD


class MisExceptions(Exception):
    """
    Clase creada para generar nuestras propias excepciones
    """

    def __init__(self, message="Error"):
        self.message = message

        super().__init__(self.message)


def hayAlgo(cadena):
    """
    Verifica que la cadena no este vacia
    Si lo esta, lanza una excepcion
    :param cadena: La cadena a validar
    :return:
    """
    if len(cadena) < 3:
        raise MisExceptions(msgErrHayAlgo())


def esNum(num):
    """
    Verifica que el numero introducido sea un numero
    En caso contrario lanza una excepcion
    :param num: El numero a validar
    :return:
    """
    num = num.strip()
    if not num.isdigit():
        raise MisExceptions(msgErrNum())


def esRango(num, lim):
    num = int(num.strip())
    if (num < 1 or num > lim):
        raise MisExceptions(msgErrNumCinco())


def nombreExiste(nombre):
    if existeNombreBBDD(nombre):
        raise MisExceptions(msgErrNombre())


def nombreNoExiste(nombre):
    if not existeNombreBBDD(nombre):
        raise MisExceptions(msgErrNombreNoEncontrado())
