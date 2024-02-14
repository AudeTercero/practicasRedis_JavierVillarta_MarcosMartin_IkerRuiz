import redis
from vista.VistaErrores import msgErrConexion
from controlador.ControladorPrincipal import menu
from modelo.ConexionBBDD import connectBBDD
'''
Arrancamos la aplicacion llamando al menu del controlador principal
'''
try:
    con = connectBBDD()
    con.ping()
    menu()
    con.close()
except redis.ConnectionError as e:
    msgErrConexion()