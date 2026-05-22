'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control for con decrementos de 10
  2.- Sin funciones

'''

print("\033c")
num_tabla=int(input("Ingrese el numero: "))

num=1
for i in range (100,0,-10):
  multi=num_tabla*num
  print(f"{num_tabla} x {num} = {multi}")
  num+=1