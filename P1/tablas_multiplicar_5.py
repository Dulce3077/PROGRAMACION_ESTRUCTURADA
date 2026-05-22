'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- sin estructuras de control while con decrementos de 10
  2.- con funciones

'''

print("\033c")

def tabla(num_tab,n):
  mul=num_tab*n
  print(f"{num_tab} x {n} = {mul}")
  n+=1
  return n

num_tabla=int(input("Ingrese el numero: "))

num=1

num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)
num=tabla(num_tabla,num)