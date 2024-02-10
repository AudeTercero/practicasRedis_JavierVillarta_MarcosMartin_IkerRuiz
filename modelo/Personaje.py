class Personaje:
    def __init__(self, nombre, cabeza, cuerpo, piernas, color, fuerza, inteligencia, vida, destreza):
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

