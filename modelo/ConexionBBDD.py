import redis

from modelo.Personaje import Personaje


def connect():
    return redis.Redis(host='localhost', port=6379, db=0)


def alta(pj):
    con = connect()
    con.set(pj.nombre,
            f'{pj.nombre},{pj.cabeza},{pj.cuerpo},{pj.piernas},{pj.color},{pj.fuerza},{pj.inteligencia},{pj.vida},{pj.destreza}')


def baja(nombre):
    con = connect()
    con.delete(nombre)


def buscar(nombre):
    con = connect()
    valores = con.get(nombre).decode('utf-8').split(',')
    return Personaje(nombre=valores[0], cabeza=valores[1], cuerpo=valores[2], piernas=valores[3], color=valores[4],
                     fuerza=valores[5], inteligencia=valores[6], vida=valores[7], destreza=valores[8])


def mostrar():
    con = connect()
    keys = con.keys('*')
    personajes = []
    for key in keys:
        valores = con.get(key).decode('utf-8').split(',')
        personajes.append(
            Personaje(nombre=valores[0], cabeza=valores[1], cuerpo=valores[2], piernas=valores[3], color=valores[4],
                      fuerza=valores[5], inteligencia=valores[6], vida=valores[7], destreza=valores[8]))
    return personajes


def existeNombre(nombre):
    con = connect()
    if con.exists(nombre) == 0:
        return False
    else:
        return True
