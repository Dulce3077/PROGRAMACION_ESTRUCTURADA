# 1er forma de utilizar los modulos 
#para usarlos los modulos deben estar en la misma carpeta o ubicación
#ejecuta todo el modulo "modulos.py"
import modulos

modulos.borrarPantalla()
modulos.funcion1()

#no es lo más recomendable hacer esto (acceder a las variables de otro modulo):
# print(modulos.hola)

nom="Daniel"
ape="Carreon"

name,lastname=modulos.funcion4(nom,ape)
print(f"Nombre: {name} \nApellidos: {lastname}")

#2da formar de utilizar modulos
from modulos import borrarPantalla,funcion1,funcion4
#from modulos import * (es para importar doas las funciones que tiene este modulo)

borrarPantalla()
funcion1()

nom="Daniel"
ape="Carreon"

name,lastname=funcion4(nom,ape)
print(f"Nombre: {name} \nApellidos: {lastname}")