#ejemplo 1:
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