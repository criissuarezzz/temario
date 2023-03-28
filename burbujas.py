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
    for i in range(0, len(lista)-1):   #i es el numero de pasadas
        for j in range (0, len(lista)-i-1): #j es el numero de comparaciones
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

#puesto a prueba:
print("Burbuja:")
print(burbuja([11,3,81,7,45]))

#BURBUJA MEJORADA
def burbuja_mejorada(lista):
    i=0   #i es el numero de pasadas
    control=True  #control es una variable de control que se usa para saber si se ha hecho algun cambio en la lista
    while (i<=len(lista)-2) and control: #i<=len(lista)-2 es para que el numero de pasadas sea len(lista)-1 para que no se salga del rango
        control=False  #se pone a False para que si no se hace ningun cambio en la lista, se salga del bucle
        for j in range (0, len(lista)-i-1):  #j es el numero de comparaciones
            if lista[j] > lista[j+1]:  
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control=True
        i+=1  #se incrementa el numero de pasadas
        print("Pasada",i,":",lista)
    return lista

#puesto a prueba:
print("Burbuja mejorada:")
print(burbuja_mejorada([11,3,81,7,45]))