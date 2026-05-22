"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

   #en python no existen procedimientos, solo funciones
   #TODAS LAS FUNCIONES DEBEN TENER UN RETURN
"""

 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
   return nom,ape

nom=input("Nombre: ").upper().strip()
ape=input("Apellidos: ").upper().strip()
nombre,apellidos=funcion4(nom,ape)
print(f"El nombre del alumno es: {nombre} {apellidos}")