from colorama import Fore, Style


def rojo(msg):
    """
    Funcion que colorea de rojo el mensaje que recibe y lo muestra
    :param msg: El mensaje a colorear
    """
    print(Style.BRIGHT, end="")
    print(Fore.LIGHTRED_EX + msg + Fore.RESET)
    print(Style.RESET_ALL, end="")



def amarillo(msg):
    """
    Funcion que colorea de amarillo el mensaje que recibe y lo muestra
    :param msg: El mensaje a colorear
    """
    print(Style.BRIGHT, end="")
    print(Fore.LIGHTYELLOW_EX + msg + Fore.RESET)
    print(Style.RESET_ALL)



def azul(msg):
    """
    Funcion que colorea de azul el mensaje que recibe y lo muestra
    :param msg: El mensaje a colorear
    """
    print(Style.BRIGHT, end="")
    print(Fore.CYAN + msg + Fore.RESET, end="")
    print(Style.RESET_ALL)


def verde(msg):
    """
    Funcion que colorea de verde el mensaje que recibe y lo muestra
    :param msg: El mensaje a colorear
    """
    print(Style.BRIGHT, end="")
    print(Fore.GREEN + msg + Fore.RESET, end="")
    print(Style.RESET_ALL)


def verdeOK(msg):
    """
    Funcion que colorea de verde el mensaje que recibe y lo muestra
    :param msg: El mensaje a colorear
    """
    print("\t║ ║ ", end="")
    print(Style.BRIGHT, end="")
    print(Fore.GREEN + msg + Fore.RESET, end="")
    print(Style.RESET_ALL)


def morado(msg):
    """
    Funcion que colorea de morado el mensaje que recibe y lo muestra
    :param msg: El mensaje a colorear
    """
    print(Style.BRIGHT, end="")
    print(Fore.MAGENTA + msg + Fore.RESET)
    print(Style.RESET_ALL)



def gris(msg):
    """
    Funcion que colorea de gris el mensaje que recibe y lo muestra
    :param msg: El mensaje a colorear
    """
    print(Style.BRIGHT, end="")
    print(Fore.LIGHTBLACK_EX + msg + Fore.RESET)
    print(Style.RESET_ALL)

