class Personaje:
    def __init__(self, nombre, origen, fuerza, velocidad, vigor, destreza, inteligencia, magia):
        self.nombre = nombre
        self.origen = origen
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.vigor = vigor
        self.destreza = destreza
        self.inteligencia = inteligencia
        self.magia = magia
        self.cp = self.cpCalculate(nombre, fuerza, velocidad, vigor, destreza, inteligencia, magia)

    def cpCalculate(self, nombre, fuerza, velocidad, vigor, destreza, inteligencia, magia):
        return (nombre + fuerza + velocidad + vigor + destreza + inteligencia + magia) / 7
