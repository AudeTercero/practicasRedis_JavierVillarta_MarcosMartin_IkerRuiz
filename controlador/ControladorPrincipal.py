from vista import VistaGeneral
from vista.VistaGeneral import *
def menu():
   finMenuAlumnos = False
   while not finMenuAlumnos:
      opc = VistaGeneral.menu()
      if opc == "1":
         alta()
      elif opc == "2":
         baja()
      elif opc == "3":
         modificar()
      elif opc == "4":
         consultar()
      elif opc == "5":
         mostrarTodos()
      elif opc == "0":
         saliendo()
         finMenuAlumnos = True
      else:
         errorEntrada()

def alta():
   print()

def baja():
   print()

def modificar():
   print()

def consultar():
   print()

def mostrarTodos():
   print()

