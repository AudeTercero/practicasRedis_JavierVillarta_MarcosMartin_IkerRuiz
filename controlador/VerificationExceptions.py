from vista.VistaErrores import *
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
    if type(num) != int:
        raise MisExceptions(msgErrNum())
def nombreExiste():
    raise MisExceptions(msgErrNombre())

