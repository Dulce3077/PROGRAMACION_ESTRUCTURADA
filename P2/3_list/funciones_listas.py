"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, 
 para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""
#MEMORIZAR LAS CARACTERISTICAS DE LA TABLA DEL DOC PARA EL EXAMEN Y LA DE ¿CUAL DEBO USAR?

#Funciones más comunes en las listas
paises=["Mexico","Canada","EUA","Mexico","Brasil"]
numeros=[23,45,8,24]
varios=[33,3.1416,"hola",True]
vacio=[]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)

#Recorrer la lista
#1er forma 
#i guarda los paises
paises=["Mexico","Canada","EUA","Mexico","Brasil"]
for i in paises:
  print(i)

# #2do forma
paises=["Mexico","Canada","EUA","Mexico","Brasil"]

tamanio=len(paises)

for i in range(0,tamanio): #se puede poner tambien for i in range(0,len(paises)):
   print(paises[i])


#ordenar elementos de una lista
print(paises)
paises.sort()
print(paises)


#dar la vuelta a una lista
paises.reverse()
print(paises)



#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises=["Mexico","Canada","EUA","Mexico","Brasil"]
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Colombia")
print(paises)
paises.insert(8,"Polonia")
print(paises)



#Eliminar, borrar, suprimir, un elemento de una lista
paises=["Mexico","Canada","EUA","Mexica","Brasil"]
print(paises)

#1er forma
paises.pop(3)
#Marca error si no hay un elemento en la posición 3
print(paises)

#2da forma 
paises.remove("EUA")
print(paises)
#Busca todas las coincidencias y las elimina
#Marca error si no encuentra coincidencias

#Buscar un elemento dentro de la lista
encontro="EUA" in paises
#Si lo encuentra arroja un TRUE y si no un FALSE
print(encontro)
#Podria poner un if con encontro y ahora si remove

#Contar el numeros de veces que aparece un elemento dentro de una lista
paises=["Mexico","Canada","EUA","Mexico","Brasil"]
numeros=[23,45,8,24,100,23,23]

num_veces=numeros.count(23)
print(f"El valor 23 aparece: {num_veces} veces")

num_veces=paises.count("Mexico")
print(f"El valor 'Mexico' aparece: {num_veces} veces")
#Estas no generan error si no encuentran el valor

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
paises=["Mexico","Canada","EUA","Mexico","Brasil"]
posicion=paises.index("Mexico")
#Solo se ejecuta una vez, asi que solo nos da la posición del primer Mexico. Tendriamos que meterla en un ciclo que recorra toda la lista para poder saber todas las posiciones de "Mexico".
print(f"Encontre el valor en la posicion: {posicion}")

paises=["Mexico","Canada","EUA","Mexico","Brasil"]
for i in range (0,len(paises)):
    if paises[i]=="Mexico":
        posicion=i
        print(f"Encontre el valor en la posicion: {posicion}")



#Unir el contenido de una lista dentro de otra lista
numeros1=[23,45,8,24,23,100,23]
numeros2=[100,-100]
print(numeros1)
print(numeros2)
numeros1.extend(numeros2)
print(numeros1)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
numeros1=[23,45,8,24,23,100,23]
numeros2=[100,-100]

numeros1.sort()
numeros1.reverse()
print(numeros1)



