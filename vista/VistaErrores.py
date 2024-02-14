from controlador.Colores import rojo
def msgErrLongitudCadena():
    """
    Funcion que devuelve un mensaje de error para cuando la longitud de una cadena
    no esta en el rango permitido.
    """
    return '\t║ ║ El nombre debe contener entre 3 y 20 caracteres.'


def msgErrNum():
    """
    Funcion que devuelve un mensaje de error para cuando se espera solo entrada
    numerica.
    """
    return '\t║ ║ Debe introducir solo numeros.'

def msgErrConexion():
    rojo("No hay contexion con la base de datos, comprueba que esta contectada")

def msgErrNombre():
    """
    Funcion que devuelve un mensaje de error para cuando un nombre ya existe.
    """
    return '\t║ ║ Ese nombre ya existe.'

def msgErrNombreNoEncontrado():
    """
    Funcion que devuelve un mensaje de error para cuando no se encuentra un
    nombre de personaje.
    """
    return '\t║ ║ Nombre de personaje no encontrado.'
def msgErrNumDiez():
    """
    Funcion que devuelve un mensaje de error para cuando se espera un numero
    en el rango del 1 al 10.
    """
    return '\t║ ║ Debe introducir un numero del 1 al 10.'


def msgErrNumCinco():
    """
    Funcion que devuelve un mensaje de error para cuando se espera un numero
    en el rango del 1 al 5.
    """
    return '\t║ ║ Debe introducir un numero del 1 al 5.'
