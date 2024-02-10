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
    """
       Verifica que el numero introducido este dentro
       de un rango especifico
       :param num: El numero a validar
       :param lim: El rango en el que debe encontrase el numero
       :return:
       """
    num = int(num.strip())
    if (num < 1 or num > lim):
        raise MisExceptions(msgErrNumCinco())


def nombreExiste(nombre):
    """
        Verifica que el nombre que recibe exista en la base de datos
        :param nombre: El nombre a comprobar
        :return:
        """
    if existeNombreBBDD(nombre):
        raise MisExceptions(msgErrNombre())


def nombreNoExiste(nombre):
    """
        Verifica que el nombre que recibe no exista en la base de datos
        :param nombre: El nombre a comprobar
        :return:
        """
    if not existeNombreBBDD(nombre):
        raise MisExceptions(msgErrNombreNoEncontrado())
