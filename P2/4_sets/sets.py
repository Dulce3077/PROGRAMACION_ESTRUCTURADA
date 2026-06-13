"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.

  El profe le llama conjunto
"""

print("\033c")

set1={"Hola","123","123","Mexico","Holanda",123,3.1416}

print(set1)

set1.add("Ganador")
print(set1)

set1.pop()
#Va a borrar 1 al azar
print(set1)

#Imprime los valores dentro del conjunto en orden aleatorio



#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista 
# y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
print("\033c")
set1={'Hola', '123', '123', 'Mexico', 'Holanda', 123, 3.1416}
print(set1)

set1.add('Ganador')
print(set1)

set1.pop() 
print(set1)

#Solucion 2

lista_emails = []
control = "si"
while control == "si":
    email = input("Introduce email: ").strip().lower()
    lista_emails.append(email)
    control = input("¿Desea agregar otro email? (si/no): ").strip().lower()
    
print(f"\nLista original con duplicados: {lista_emails}")
emails_sin_duplicados = set(lista_emails)
print(f"Emails únicos (sin duplicados): {emails_sin_duplicados}")



