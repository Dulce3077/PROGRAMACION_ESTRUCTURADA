'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control
  2.- Sin funciones

'''

print("\033c")
num_tabla=int(input("Ingrese el numero: "))


for num in range (1,11):
  multi=num_tabla*num
  print(f"{num_tabla} x {num} = {multi}")
  num+=1