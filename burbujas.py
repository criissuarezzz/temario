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


#Insertar
#11   3  81  7   45   comparamos la primera posicion con si misma y al ser el menor se queda ahi
#11<=>3<=>81  7   45   comparamos el 11 con el 3 y como es mayor que 3, comprobamos si los dos de al lado del 3 son menores que 3, como esta entre 11 y 81, el 3 va primero
#3   11<=>81<=>7   45      comparamos la tercera posición, es el 81 y tiene el 11 y el 7 a cada lado, los dos son menores, el 11 ya lo hemos comprobado antes, asi que toca comprobar que es el 7 el que hay que mover
#3  11  81<=>7<=>45      comparamos el 7 con el 45 y como es menor, se intercambian
#3  11  7  81  45      volvemos a empezar y comparamos la segunda posición como el paso 2
#3  7  11 81  45      comparamos la cuarta posición como el paso 3
#3  7  11  45  81      comparamos la quinta posición como el paso 4

def insercion(lista):
    for i in range (1, len(lista)+1):   #i es el numero de pasadas, empezamos en 1 porque la primera posicion ya esta ordenada
        k=i-1   #k es el numero de comparaciones
        while k>0 and lista[k]<lista[k-1]:   #mientras que k sea mayor que 0 y el numero de la posicion k sea menor que el de la posicion k-1
            lista[k], lista[k-1] = lista[k-1], lista[k]   #se intercambian
            k-=1   #se decrementa k
    return lista

#puesto a prueba:
print("Insercion:")
print(insercion([11,3,81,7,45]))


#quick sort
#11  3  81  7   45  #81=pivote
#(11 3) (81  7 45) #se divide la lista en dos partes
#(11 3) 81<=>7  45
#(11 3) 7  81  45
#(11 3) 7 81<=>45
#(11 3) 7 45  81
#(11 3) 7<=>45<=>81  #se compara el 45 con respecto a los de su alrededor y no solo respecto al pivote, como su valor está entre los dos de su lado se deja asi
#(11 3  7) 45  81  #el otro lado de la lista
#(11<=>3<=>7) 45  81  
#3  7  11  45  81  #se compara el 11 con respecto a los de su alrededor y no solo respecto al pivote, como su valor está entre los dos de su lado se deja asi

def quicksort(lista, primero, ultimo):
    izquierda=primero
    derecha=ultimo-1
    pivote=ultimo
    while(izquierda<derecha):
        while(lista[izquierda]<=lista[pivote] and izquierda<derecha):
            izquierda+=1
        while(lista[derecha]>lista[pivote] and derecha>izquierda):
            derecha-=1
        if(izquierda<derecha):
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
    if(lista[izquierda]>lista[pivote]):
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]
    if(primero<izquierda-1):
        quicksort(lista, primero, izquierda-1)
    if(ultimo>izquierda+1):
        quicksort(lista, izquierda+1, ultimo)
    return lista

#puesto a prueba:
print("Quick sort:")
print(quicksort([11,3,81,7,45], 0, 4))


#ordenamiento por mezcla     (merge sort)
#11  3  81  7   45  #se divide la lista en dos partes
#(11 3 81) (7 45)  #se divide cada una de las dos partes en dos partes
#(11 3) (81) (7 45)  #se divide cada una de las cuatro partes en dos partes
#(11) (3) (81) (7) (45)  #se divide cada una de las ocho partes en dos partes
#(3 11) (81) (7 45)  #se comparan los numeros de cada parte y se ordenan
#(11) (3) (81) (7) (45)  #se comparan los numeros de cada parte y se ordenan
#(3 11) (7 45) (81)  #se comparan los numeros de cada parte y se ordenan
#(3 7 11 45) (81)  #se comparan los numeros de cada parte y se ordenan
#(3 7 11 45 81)  #se comparan los numeros de cada parte y se ordenan

def mezcla(lista):
    if len(lista)<=1:
        return lista
    else:
        medio=len(lista)//2
        izquierda=mezcla(lista[:medio])
        derecha=mezcla(lista[medio:])
        return mezclar(izquierda, derecha)
    
def mezclar(izquierda, derecha):
    resultado=[]
    i=0
    j=0
    while i<len(izquierda) and j<len(derecha):
        if izquierda[i]<derecha[j]:
            resultado.append(izquierda[i])
            i+=1
        else:
            resultado.append(derecha[j])
            j+=1
    resultado+=izquierda[i:]
    resultado+=derecha[j:]
    return resultado

#puesto a prueba:
print("Mezcla:")
print(mezcla([11,3,81,7,45]))


#ordenamiento por mezcla contar cuantos pasos
def mezcla_contar(lista):
    if len(lista)<=1:
        return lista
    else:
        medio=len(lista)//2
        izquierda=mezcla_contar(lista[:medio])
        derecha=mezcla_contar(lista[medio:])
        return mezclar_contar(izquierda, derecha)
    
def mezclar_contar(izquierda, derecha):
    resultado=[]
    i=0
    j=0
    while i<len(izquierda) and j<len(derecha):
        if izquierda[i]<derecha[j]:
            resultado.append(izquierda[i])
            i+=1
        else:
            resultado.append(derecha[j])
            j+=1
    resultado+=izquierda[i:]
    resultado+=derecha[j:]
    print(resultado)
    return resultado

#puesto a prueba:
print("Mezcla contar:")
print(mezcla_contar([11,3,81,7,45]))

#mezclar listas
def merge(izquierda, derecha):
    lista_mezclada = []
    while len(izquierda) > 0 and len(derecha) > 0:
        if izquierda[0] < derecha[0]:
            lista_mezclada.append(izquierda[0])
            izquierda.remove(izquierda[0])
        else:
            lista_mezclada.append(derecha[0])
            derecha.remove(derecha[0])
    if len(izquierda) > 0:
        lista_mezclada += izquierda
    if len(derecha) > 0:
        lista_mezclada += derecha
    return lista_mezclada

#puesto a prueba:
print("Mezclar listas:")
print(merge([11,3,81,7,45], [1,2,3,4,5]))

#ordenar ovejas
def count_sort(lista, maximo):
    conteo=[0]*(maximo+1)
    ordenada=[None]*len(lista)
    for i in range(len(lista)):
        conteo[lista[i]]+=1
    for i in range(1, maximo+1):
        conteo[i]+=conteo[i-1]
    for i in range(len(lista)):
        ordenada[conteo[lista[i]]-1]=lista[i]
        conteo[lista[i]]-=1
    return ordenada

#puesto a prueba:
print("Ordenar ovejas:")
print(count_sort([9, 3, 1, 5, 9, 2, 0, 1], 9))

#SECUENCIAL
def secuencial(lista, valor):
    posicion=-1
    for i in range (0, len(lista)):
        if lista[i]==valor:
            posicion=i
            break
    return posicion

#puesto a prueba:
print("Secuencial:")
print(secuencial([11,3,81,7,45], 81))

#BINARIO
def binario(lista, buscado):
    posicion=-1
    primero=0
    ultimo=len(lista)-1
    while primero<=ultimo and posicion==-1:
        medio=(primero+ultimo)//2
        if lista[medio]==buscado:
            posicion=medio
        elif lista[medio]>buscado:
            ultimo=medio-1
        else:
            primero=medio+1
    return posicion

