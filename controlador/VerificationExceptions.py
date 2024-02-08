from vista.VistaErrores import *
from modelo.ConexionBBDD import existeNombre


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


def esRangoCinco(num):
    num = int(num.strip())
    if (num < 1 or num > 5):
        raise MisExceptions(msgErrNumCinco())


def esRangoDiez(num):
    num = int(num.strip())
    if (num < 1 or num > 10):
        raise MisExceptions(msgErrNumDiez())


def nombreExiste(nombre):
    if existeNombre(nombre):
        raise MisExceptions(msgErrNombre())
