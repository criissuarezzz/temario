#ejemplo 1:
#BURBUJA
# 11   3  81  7  45
# 3<=>11  81  7  45
# 3  11<=>81  7  45
# 3  11  81<=>7  45
# 3  11  7  81<=>45
# 3  11  7   45  81
# 3<=>11  7  45  81
# 3  11<=>7  45  81
# 3  7  11   45  81

#codigo de la burbuja:
def burbuja(lista):
    i=0
    for i in range(0, len(lista)-1):   #i es el numero de pasadas
        for j in range (0, len(lista)-i-1): #j es el numero de comparaciones
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
        i+=1
        print("Pasada",i,":",lista)
    return lista

#puesto a prueba:
print("Burbuja:")
print(burbuja([11,3,81,7,45]))

#BURBUJA MEJORADA
def burbuja_mejorada(lista):
    i=0   #i es el numero de pasadas
    control=True  #control, para determinar si se debemos seguir ordenando o la lista ya se encuentra ordenada
    while (i<=len(lista)-2) and control: #i<=len(lista)-2 es para que el numero de pasadas sea len(lista)-1 para que no se salga del rango
        control=False  #se pone a False para que si no se hace ningun cambio en la lista, se salga del bucle
        for j in range (0, len(lista)-i-1):  #j es el numero de comparaciones
            if lista[j] > lista[j+1]:  
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control=True
        i+=1  #se incrementa el numero de pasadas
    return lista

#puesto a prueba:
print("Burbuja mejorada:")
print(burbuja_mejorada([11,3,81,7,45]))


#BURBUJA BIDIRECCIONAL, "COCTAIL"
#11   3  81  7   45
#11<=>3  81  7<=>45
#3  11<=>81<=>7  45
#3<=>7  11  81<=>45
#3  7<=>11<=>45  81
#3  7   11   45  81


def coctel(lista):
    izquierda=0 #para empezar en la posicion 0
    derecha=len(lista)-1 #para empezar en la ultima posicion
    control=True #para determinar si se debemos seguir ordenando 
    while izquierda<=derecha and control: #mientras que la posicion izquierda sea menor o igual que la derecha y control sea True
        control=False #se pone a False para que si no se hace ningun cambio en la lista, se salga del bucle
        for i in range(izquierda, derecha): #para recorrer la lista de izquierda a derecha
            if lista[i]>lista[i+1]: #si el elemento de la posicion i es mayor que el de la posicion i+1
                lista[i], lista[i+1] = lista[i+1], lista[i] #se intercambian
                control=True #se pone a True para que no se salga del bucle
        derecha-=1 #se decrementa la posicion derecha
        for i in range(derecha, izquierda, -1): #para recorrer la lista de derecha a izquierda
            if lista[i]<lista[i-1]: #si el elemento de la posicion i es menor que el de la posicion i-1
                control=True #se pone a True para que no se salga del bucle
                lista[i], lista[i-1] = lista[i-1], lista[i] #se intercambian
    return lista

#puesto a prueba:
print("Coctel:")
print(coctel([11,3,81,7,45]))


#SELECCION
#11   3  81  7   45
#11<=>3  81  7   45    #comparamos el 11 con el numero de al lado y si es menor, el menor se compara con los demas numeros
#el 3 es menor que el 11 asi que se compara con el 81, 7 y 45, como es el meor de los 5 numeros se pone en primera posicion
#3  11<=>81  7   45
#3  11<=>7  81   45
#3  7   81<=>11  45
#3  7   11  81<=>45


def seleccion(lista):
    for i in range (0, len(lista)-1):
        minimo=i
        for j in range (i+1, len(lista)):   
            if lista[j]<lista[minimo]:
                minimo=j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

#puesto a prueba:
print("Seleccion:")
print(seleccion([11,3,81,7,45]))

