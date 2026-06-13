print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

numeros=[23,33,45,8,24,0,100]
print(numeros)

lista=""
for i in numeros:
    lista=lista+str(i)+"," #convierte i a un string
    lista+=f"{i}," #Es lo mismo que la linea 10
print(f"[{lista}]")

lista=""
for i in range(0,len(numeros)):
   lista=lista+str(numeros[i])+","
print(f"[{lista}]")

lista=""
i=0
while i<len(numeros):
   lista=lista+str(numeros[i])+","
   i=i+1
print(f"[{lista}]")
#VER PORQUE NO FUNCIONA


#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

palabras=["UTD","tercer","cuatrimestre","TI"]
palabra=input("Dame la palabra a buscar: ").strip()


#Tambien se puede cambiar la condición a if palabra in palabras: y quitamos el encontro=palabra in palabras


#1ERA FORMA
encontro=palabra in palabras
if encontro==True: #Se puede poner como if encontro:
   print(f"Encontre la palabra {palabra} en la lista")
else:
   print(f"No encontre la palabra {palabra} en la lista")


#2DA FORMA
palabras=["UTD","tercer","cuatrimestre","TI"]
palabra=input("Dame la palabra a buscar: ").strip()

for i in palabras:
   if i==palabra:
       print(f"Encontre la palabra {palabra} en la lista")
       break

    
encontro=False
for i in palabras:
   if i==palabra:
       encontro=True

if encontro:
   print(f"Encontre la palabra {palabra} en la lista")
else:
   print(f"No encontre la palabra {palabra} en la lista")


#3er FORMA
#AQUI SE USA LEN
encontro = False
for i in range(len(palabras)):
    if palabras[i] == palabra:
        encontro = True

if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")


#4TA FORMA
#AQUI SE USA while
encontro = False
i = 0

while i < len(palabras):
    if palabras[i] == palabra:
        encontro = True
        break
    i += 1

if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")


#Ejemplo 3 Añadir elementos a la lista

lista=[]

valor=input("Dame un valor: ").strip()
lista.append(valor)

#Opcion 1
true=True
while true:
   valor=input("Dame un valor: ").strip()
   lista.append(valor)
   true=input("Ingresa True/False para continuar: ").strip()
   if true=="False":
       true=False

#Opcion 2
true="si"
while true=="si":
   valor=input("Dame un valor: ").strip()
   lista.append(valor)
   true=input("Ingresa si/no para continuar: ").lower().strip()

print(lista)







#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

print("\033c")

agenda=[
    ["Carlos","6181234567"],
    ["Adrian","6182332456"],
    ["Luis","6182223444"]
]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])


lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]},"
    lista+="\n"
print(lista)

