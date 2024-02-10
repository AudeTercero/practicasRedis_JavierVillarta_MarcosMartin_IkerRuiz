class Personaje:
    """
    Clase que representa a un personaje dentro de la aplicacion
    """
    def __init__(self, nombre, cabeza, cuerpo, piernas, color, fuerza, inteligencia, vida, destreza):
        """
        Constructor de la clase Personaje.

        Args:
            nombre (str): Nombre del personaje.
            cabeza (str): Descripcion de la cabeza del personaje.
            cuerpo (str): Descripcion del cuerpo del personaje.
            piernas (str): Descripcion de las piernas del personaje.
            color (str): Color del personaje.
            fuerza (int): Valor de la fuerza del personaje.
            inteligencia (int): Valor de la inteligencia del personaje.
            vida (int): Valor de la vida del personaje.
            destreza (int): Valor de la destreza del personaje.
        """
        self.nombre = nombre
        self.cabeza = cabeza
        self.cuerpo = cuerpo
        self.piernas = piernas
        self.color = color
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida
        self.destreza = destreza
        self.cp = self.cpCalculate(fuerza, inteligencia, vida, destreza)

    def cpCalculate(self, fuerza, inteligencia, vida, destreza):
        """
        Funcion que calcula el puntaje del personaje (cp) basado en sus atributos de habilidades
        Returns:
            float: Puntaje del personaje.
        """
        return (int(fuerza) + int(inteligencia) + int(vida) + int(destreza)) / 4


def getCabezas():
    """
    En esta funcion se guardan todas las cabezas disponibles para los personajes.
    Se trata de una lista para cada tipo de cabeza, que a su vez contiene una lista
    para cada linea de dibujado. De esta forma se pueden mostrar varios personajes
    a la vez.
    :return: Lista con el contenido
    """
    return [["     [#]    ", "    _|||_   "], ["            ", "     (-)    "]
        , ["      _     ", "    _/v\\_   "],
            ["     ___    ", "    /0-0\\   "], ["     ___    ", "   _/<_>\\_  "]]


def getCuerpos():
    """
    En esta funcion se guardan todas los cuerpos disponibles para los personajes.
    :return:
    """
    return [["  <[     ]> ", "  <[=====]> ", "  <[_____]> "], [" \\=\\  Y  /=/", "    \\ | /   ", "    |___|   "],
            ["    \\   /   ", " d==|   |==b", "    |___|   "], ["     ) (    ", "   /(   )\\  ", "   \\ )_( /  "],
            ["   _/   \\_  ", "  /=======\\ ", " /_________\\"]]


def getPiernas():
    """
    En esta funcion se guardan todas las piernas disponibles para los personajes.
    :return:
    """
    return [["    |   |   ", "    l   l   "], ["   //   \\\  ", " _//     \\\_"], ["    // \\\   ", "  _//   \\\_ "],
            ["    || ||   ", "    WW WW   "], ["    (_0_)   ", "            "]]

