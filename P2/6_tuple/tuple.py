"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.

   
inmutable= no crece
guarda valores constantes
si hay posiciones
usa tuplas para almacenar valores que no van a cambiar
set lo usaria para quitar valores duplicados
se quedan en el orden que las ingresamos


"""
print("\033c")

paises=("México","Canada","EUA")

varios=("Hola",True,33,3.1416)

print(paises)
print(varios)

for i in paises:
  print(i)

for i in range(0,len(paises)):
  print(paises[1])


i=0
while i<=2:
  print(paises[i])    
  i=i+1

print(f"El país que inagura la copa del mundo 2026 es: {paises[0]}")

edades=(23,24,18,20,20,23,24,19,24)

cuantos=edades.count(24)
print(cuantos)

#index busca la primera aparición

#crear un programa que lea un número y me diga en que posiciones se encuentra


#UTILIZANDO TUPLA
num=int(input("Ingresa en número: "))

posiciones=[]
for i in range (0,len(edades)):
  if edades[i]==num:
    posiciones.append(i) 

posiciones=tuple(posiciones)

for i in posiciones:
  print(f"El número {num} se encontro en la posicion: {i}")



#UTILIZANDO SET
num=int(input("Ingresa en número: "))
posiciones={""}
posiciones.clear()
posiciones=[]
for i in range (0,len(edades)):
  if edades[i]==num:
    posiciones.add(i) 

posiciones=tuple(posiciones)

for i in posiciones:
  print(f"El número {num} se encontro en la posicion: {i}")