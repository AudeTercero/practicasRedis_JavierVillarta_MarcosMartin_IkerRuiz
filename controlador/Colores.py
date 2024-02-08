from colorama import Fore, Style


def rojo(msg):
    print(Fore.RED + msg + Fore.RESET)


def amarillo(msg):
    print(Fore.LIGHTYELLOW_EX + msg + Fore.RESET)


def azul(msg):
    print(Style.BRIGHT, end="")
    print(Fore.CYAN + msg + Fore.RESET, end="")
    print(Style.RESET_ALL)


def verde(msg):
    print(Style.BRIGHT, end="")
    print(Fore.GREEN + msg + Fore.RESET, end="")
    print(Style.RESET_ALL)

def morado(msg):
    print(Fore.MAGENTA + msg + Fore.RESET)


