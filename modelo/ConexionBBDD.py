import redis


def connect():
    return redis.Redis(host='localhost', port=6379, db=0)


def alta(nombre, cabeza, cuerpo, piernas, color, fuerza, inteligencia, vida, destreza, cp):
    con = connect()
    con.set(nombre, f'{nombre},{cabeza},{cuerpo},{piernas},{color},{fuerza},{inteligencia},{vida},{destreza},{cp}')


def baja(nombre):
    con = connect()
    con.delete(nombre)


def buscar(nombre):
    con = connect()
    return con.get(nombre)


def mostrar():
    con = connect()
    keys = con.keys('*')
    return con.mget(keys)


def existeNombre(nombre):
    con = connect()
    if con.exists(nombre) == 0:
        return False
    else:
        return True
