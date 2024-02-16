import json

import redis

from modelo.Personaje import Personaje


def connectBBDD():
    """
    Funcion que establece una conexion a la base de datos Redis y devuelve el objeto de conexion.
    Returns:
        Redis: Objeto de conexion a la base de datos Redis.
    """
    return redis.Redis(host='localhost', port=6379, db=0)


def altaBBDD(pj):
    """
        Funcion que agrega un personaje a la base de datos Redis mediante un json.
        """
    con = connectBBDD()
    pjToDic = {
        'nombre': pj.nombre,
        'cabeza': pj.cabeza,
        'cuerpo': pj.cuerpo,
        'piernas': pj.piernas,
        'fuerza': pj.fuerza,
        'inteligencia': pj.inteligencia,
        'vida': pj.vida,
        'destreza': pj.destreza
    }
    pjToJson = json.dumps(pjToDic)
    con.set(pj.nombre, pjToJson)

'''def altaBBDD(pj):
    """
    Funcion que agrega un personaje a la base de datos Redis mediante una cadena.
    """
    con = connectBBDD()
    con.set(pj.nombre,
            f'{pj.nombre},{pj.cabeza},{pj.cuerpo},{pj.piernas},{pj.color},{pj.fuerza},{pj.inteligencia},{pj.vida},{pj.destreza}')
'''


def bajaBBDD(nombre):
    """
    Funcion que agrega un personaje a la base de datos Redis.
    """
    con = connectBBDD()
    con.delete(nombre)

def buscarBBDD(nombre):
    """
        Funcion que busca por medio del nombre un personaje en json en la base de datos Redis y
        lo devuelve.
        :Params: nombre
        """
    con = connectBBDD()
    valores = con.get(nombre)
    pJson=json.loads(valores)
    return Personaje(
        pJson["nombre"],
        pJson["cabeza"],
        pJson["cuerpo"],
        pJson["piernas"],
        pJson["color"],
        pJson["fuerza"],
        pJson["inteligencia"],
        pJson["vida"],
        pJson["destreza"]
    )


'''def buscarBBDD(nombre):
    """
    Funcion que busca por medio del nombre un personaje en una cadena en la base de datos Redis y
    lo devuelve.
    :Params: nombre
    """
    con = connectBBDD()
    valores = con.get(nombre).decode('utf-8').split(',')
    return Personaje(nombre=valores[0], cabeza=valores[1], cuerpo=valores[2], piernas=valores[3], color=valores[4],
                     fuerza=valores[5], inteligencia=valores[6], vida=valores[7], destreza=valores[8])

'''

def mostrarBBDD():
    """
    Funcion que recoge los personajes en un json de la base de datos y los retorna en un listado de personajes
    :return:
    """
    con = connectBBDD()
    keys = con.keys('*')
    personajes = []
    for key in keys:
        valores = con.get(key)
        pJson = json.loads(valores)
        personajes.append(
            Personaje(
                pJson["nombre"],
                pJson["cabeza"],
                pJson["cuerpo"],
                pJson["piernas"],
                pJson["color"],
                pJson["fuerza"],
                pJson["inteligencia"],
                pJson["vida"],
                pJson["destreza"]
            )
        )
    return personajes

'''def mostrarBBDD():
    con = connectBBDD()
    keys = con.keys('*')
    personajes = []
    for key in keys:
        valores = con.get(key).decode('utf-8').split(',')
        personajes.append(
            Personaje(nombre=valores[0], cabeza=valores[1], cuerpo=valores[2], piernas=valores[3], color=valores[4],
                      fuerza=valores[5], inteligencia=valores[6], vida=valores[7], destreza=valores[8]))
    return personajes'''


def existeNombreBBDD(nombre):
    con = connectBBDD()
    if con.exists(nombre) == 0:
        return False
    else:
        return True


def hayPersonajes():
    con = connectBBDD()
    keys = con.keys('*')
    if len(keys) > 0:
        return True
    else:
        return False


def borrarTodaBD():
    con = connectBBDD()
    con.flushdb()


altaBBDD(Personaje("1111", 1, 1, 1, 1, 1, 1, 1, 1))
