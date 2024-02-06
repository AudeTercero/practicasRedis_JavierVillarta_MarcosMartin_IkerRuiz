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
        return (fuerza + inteligencia + vida + destreza) / 4
