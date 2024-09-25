#Un club tiene almacenada en 3 listas que se corresponden:
#Los números de sus socios en la primera lista, que no se repiten
#El estado de sus socios, que puede ser “vitalicio”, “federado” o “regular”. En la segunda lista.
#El año en que se asoció en la tercera
#La cuota del asociado se encuentra guardada en una variable llamada Cuota y es de 15000.
#● Desarrollar una función denominada Buscar que reciba una lista y un entero y retorne la
#posición de dicho entero en esa lista o -1 si no lo encuentra
#● Utilizar la función desarrollada en el punto anterior para:
#Desarrollar un programa principal donde se ingresa el número de un socio del club y muestre el
#estado del mismo y el año que se asoció.
#Si el año del socio es anterior a 1980 mostrar por pantalla el valor de la cuota con un 40 % de
#descuento de la misma
#Si el año del socio se encuentra entre 1981 y 1990 mostrar por pantalla el valor de la cuota con
#un 20 % de descuento de la cuota
#Si el socio ingresado no se encuentra en la lista informarlo con un cartel aclaratorio que diga
#“Bienvenido al club ¿Desea asociarse?”

def Buscar (lista, entero):
    for i in range (len(lista)):
        if lista[i]==entero:
            return i
    return -1

socio=int(input("ingrese el número de socio: "))
LisSocio= [9845, 1165, 987, 5267]
LisEstados = [ "vitalicio" , "federado" , "regular", "regular" ]
LisAños= [1975, 1983 , 2010, 1970 ]
busco=Buscar(LisSocio, socio)
if busco>-1:
    cuota=15000
    if LisAños[busco]<=1980:
        descuento=cuota*(40/100)
        cuota=cuota-descuento
    if LisAños[busco]>=1981 and LisAños[busco]<=1990:
        descuento=cuota*(20/100)
        cuota=cuota-descuento
    print("el Estado del socio ",LisSocio[busco], "es", LisEstados[busco], "el año de ingreso es ",LisAños[busco], ". Su cuota es ", cuota)

else:
    print("bienvenido al club, ¿desea asociarse?")