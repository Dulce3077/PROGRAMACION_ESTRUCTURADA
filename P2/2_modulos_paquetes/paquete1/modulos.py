# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

def borrarPantalla():
   print("\033c")

def funcion1():
   nombre=input("Nombre: ").upper().strip()
   apellidos=input("Apellidos: ").upper().strip()
   print(f"El nombre del alumno es: {nombre} {apellidos}")
    
 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):
   print(f"El nombre del alumno es: {nom} {ape}")

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
   nombre=input("Nombre: ").upper().strip()
   apellidos=input("Apellidos: ").upper().strip()
   return nombre,apellidos

 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
   
   return nom,ape

hola=5