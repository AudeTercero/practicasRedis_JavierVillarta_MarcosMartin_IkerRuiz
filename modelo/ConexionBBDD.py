import redis

from modelo.Personaje import Personaje


def connectBBDD():
    return redis.Redis(host='localhost', port=6379, db=0)


def altaBBDD(pj):
    con = connectBBDD()
    con.set(pj.nombre,
            f'{pj.nombre},{pj.cabeza},{pj.cuerpo},{pj.piernas},{pj.color},{pj.fuerza},{pj.inteligencia},{pj.vida},{pj.destreza}')


def bajaBBDD(nombre):
    con = connectBBDD()
    con.delete(nombre)


def buscarBBDD(nombre):
    con = connectBBDD()
    valores = con.get(nombre).decode('utf-8').split(',')
    return Personaje(nombre=valores[0], cabeza=valores[1], cuerpo=valores[2], piernas=valores[3], color=valores[4],
                     fuerza=valores[5], inteligencia=valores[6], vida=valores[7], destreza=valores[8])


def mostrarBBDD():
    con = connectBBDD()
    keys = con.keys('*')
    personajes = []
    for key in keys:
        valores = con.get(key).decode('utf-8').split(',')
        personajes.append(
            Personaje(nombre=valores[0], cabeza=valores[1], cuerpo=valores[2], piernas=valores[3], color=valores[4],
                      fuerza=valores[5], inteligencia=valores[6], vida=valores[7], destreza=valores[8]))
    return personajes


def existeNombreBBDD(nombre):
    con = connectBBDD()
    if con.exists(nombre) == 0:
        return False
    else:
        return True
