from colorama import Fore, Style


def rojo(msg):
    print(Fore.RED + msg + Fore.RESET)


def amarillo(msg):
    print(Fore.LIGHTYELLOW_EX + msg + Fore.RESET)


def azul(msg):
    print(Style.BRIGHT)
    print(Fore.CYAN + msg + Fore.RESET)
    print(Style.RESET_ALL)


def verde(msg):
    print(Fore.GREEN + msg + Fore.RESET)

def morado(msg):
    print(Fore.MAGENTA + msg + Fore.RESET)


