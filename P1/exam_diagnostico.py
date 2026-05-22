def borrarPantalla():
    print("\033c")

def ventaAutos(opc,autos,acum_pv):
    borrarPantalla()

    while opc=="si":
        #Entrada
        marca=input("Marca: ").strip().upper()
        origen=input("Origen: ").strip().upper()
        costo=float(input("Costo: "))

        #todas las variables en las que su valor dependa de una condición o un proceso deben inicializarse.
        #Proceso
        impuesto=0
        if origen=="ALEMANIA":
            impuesto=0.20
        elif origen=="JAPON":
            impuesto=0.30
        elif origen=="ITALIA":
            impuesto=0.15
        elif origen=="USA":
            impuesto=0.08

        impuesto_pesos=costo*impuesto
        precio_venta=impuesto_pesos+costo

        #Salida
        print(f"El impuesto a pagar es: ${impuesto_pesos}")
        print(f"El precio es: ${precio_venta}")

        autos+=1
        acum_pv+=precio_venta

        opc=input("¿Deseas hacer otra captura (si/no)?").lower().strip()

    return autos,acum_pv
    #El return tiene mas jerarquía que un while (es como un break)

autos=0
acum_pv=0
opc="si"

autos,acum_pv=ventaAutos(opc,autos,acum_pv)

#ESTOS DE ACA ABAJO LOS SACAMOS DEL WHILE
print(f"El total de los vehiculos ingresados es: {autos}")   
print(f"Y el monto total de los precios de venta es: {acum_pv}")