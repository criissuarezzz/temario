#ejercicio2

#de manera iterativa:
def iterativaSarrus():
    print('\033[35m'+ "DE MANERA ITERATIVA " + '\033[0m')
    matriz = [] 
    for i in range(3): 
        matriz.append([])   
        for j in range(3): 
            matriz[i].append(int(input("ingrese el numero de la posicion ["+str(i)+"]["+str(j)+"]: "))) #creamos la matriz
    print("La matriz resultante es:")
    print(matriz[0][0], matriz[0][1], matriz[0][2])
    print(matriz[1][0], matriz[1][1], matriz[1][2])
    print(matriz[2][0], matriz[2][1], matriz[2][2])   
    print('\033[36m'+"¿desea cambiar algún numero de la matriz? (si/no)"+'\033[0m')
    respuesta = input("->")
    if respuesta == "si":   
        print("ingrese la posicion del numero que desea cambiar")
        print("fila: ") 
        fila = int(input("->")) 
        print("columna: ")
        columna = int(input("->")) 
        print("ingrese el nuevo numero: ")
        numero = int(input("->")) 
        matriz[fila][columna] = numero 
        print("la matriz es: ")
        print(matriz[0][0], matriz[0][1], matriz[0][2])
        print(matriz[1][0], matriz[1][1], matriz[1][2])
        print(matriz[2][0], matriz[2][1], matriz[2][2])
    else:  
        print("la matriz se queda igual")

    determinante = matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[0][2]*matriz[1][0]*matriz[2][1] - matriz[0][2]*matriz[1][1]*matriz[2][0] - matriz[0][1]*matriz[1][0]*matriz[2][2] - matriz[0][0]*matriz[1][2]*matriz[2][1] #utilizamos la fórmula del determinante de una matriz cuadrada de 3x3
    print("el determinante de la matriz es: ", determinante)   
    print('\033[35m'+ "===================" + '\033[0m')

iterativaSarrus()  

#de manera recursiva:
def recursivaSarrus():  
    print('\033[35m'+ "DE MANERA RECURSIVA " + '\033[0m')

    matriz = [] 
    for i in range(3):  
        matriz.append([])   
        for j in range(3):  
            matriz[i].append(int(input("ingrese el numero de la posicion ["+str(i)+"]["+str(j)+"]: "))) #agregamos los numeros ingresados por el usuario a la lista matriz
    print("la matriz es: ")
    print(matriz[0][0], matriz[0][1], matriz[0][2])
    print(matriz[1][0], matriz[1][1], matriz[1][2])
    print(matriz[2][0], matriz[2][1], matriz[2][2])
    print('\033[36m'+"¿desea cambiar algún numero de la matriz? (si/no)"+'\033[0m')
    respuesta = input()
    if respuesta == "si":   
        print("ingrese la posicion del numero que desea cambiar")
        print("fila: ") 
        fila = int(input("->")) 
        print("columna: ")
        columna = int(input("->")) 
        print("ingrese el nuevo numero: ")
        numero = int(input("->")) 
        matriz[fila][columna] = numero 
        print("la matriz es: ")
        print(matriz[0][0], matriz[0][1], matriz[0][2])
        print(matriz[1][0], matriz[1][1], matriz[1][2])
        print(matriz[2][0], matriz[2][1], matriz[2][2])
    else:  
        print("la matriz se queda igual")

    def determinante(matriz):   
        if len(matriz) == 1:   
            return matriz[0][0] 
        else:   
            det = 0 
            for i in range(len(matriz)):   
                det += (-1)**i*matriz[0][i]*determinante([fila[:i] + fila[i+1:] for fila in (matriz[1:])])   #lo calculamos por menores para que sea de manera recursiva
            return det  
        
    print("el determinante de la matriz es: ", determinante(matriz)) 
    print('\033[35m'+ "===================" + '\033[0m')  

recursivaSarrus()  


#sarrus 5x5:
def sarrus5x5iterativo():
    print('\033[35m'+ "DE MANERA ITERATIVA " + '\033[0m')
    matriz=[]
    for i in range(5):
        matriz.append([])
        for j in range(5):
            matriz[i].append(int(input("ingrese el numero de la posicion ["+str(i)+"]["+str(j)+"]: ")))
    print("la matriz es: ")
    print(matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], matriz[0][4])
    print(matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3], matriz[1][4])
    print(matriz[2][0], matriz[2][1], matriz[2][2], matriz[2][3], matriz[2][4])
    print(matriz[3][0], matriz[3][1], matriz[3][2], matriz[3][3], matriz[3][4])
    print(matriz[4][0], matriz[4][1], matriz[4][2], matriz[4][3], matriz[4][4])
    print('\033[36m'+"¿desea cambiar algún numero de la matriz? (si/no)"+'\033[0m')
    respuesta = input("->")
    if respuesta == "si":
        print("ingrese la posicion del numero que desea cambiar")
        print("fila: ")
        fila = int(input("->"))
        print("columna: ")
        columna = int(input("->"))
        print("ingrese el nuevo numero: ")
        numero = int(input("->"))
        matriz[fila][columna] = numero
        print("la matriz es: ")
        print(matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], matriz[0][4])
        print(matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3], matriz[1][4])
        print(matriz[2][0], matriz[2][1], matriz[2][2], matriz[2][3], matriz[2][4])
        print(matriz[3][0], matriz[3][1], matriz[3][2], matriz[3][3], matriz[3][4])
        print(matriz[4][0], matriz[4][1], matriz[4][2], matriz[4][3], matriz[4][4])
    else:
        print("la matriz se queda igual")
    determinante = matriz[0][0]*matriz[1][1]*matriz[2][2]*matriz[3][3]*matriz[4][4] + matriz[0][1]*matriz[1][2]*matriz[2][3]*matriz[3][4]*matriz[4][0] + matriz[0][2]*matriz[1][3]*matriz[2][4]*matriz[3][0]*matriz[4][1] + matriz[0][3]*matriz[1][4]*matriz[2][0]*matriz[3][1]*matriz[4][2] + matriz[0][4]*matriz[1][0]*matriz[2][1]*matriz[3][2]*matriz[4][3] - matriz[0][4]*matriz[1][3]*matriz[2][2]*matriz[3][1]*matriz[4][0] - matriz[0][3]*matriz[1][2]*matriz[2][1]*matriz[3][0]*matriz[4][4] - matriz[0][2]*matriz[1][1]*matriz[2][0]*matriz[3][4]*matriz[4][3] - matriz[0][1]*matriz[1][0]*matriz[2][4]*matriz[3][3]*matriz[4][2] - matriz[0][0]*matriz[1][4]*matriz[2][3]*matriz[3][2]*matriz[4][1] #utilizamos la fórmula del determinante de una matriz cuadrada de 5x5
    print("el determinante de la matriz es: ", determinante)
    print('\033[35m'+ "===================" + '\033[0m')

sarrus5x5iterativo()

def recursivaSarrus5x5():
    print('\033[35m'+ "DE MANERA RECURSIVA " + '\033[0m')
    matriz=[]
    for i in range(5):
        matriz.append([])
        for j in range(5):
            matriz[i].append(int(input("ingrese el numero de la posicion ["+str(i)+"]["+str(j)+"]: ")))
    print("la matriz es: ")
    print(matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], matriz[0][4])
    print(matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3], matriz[1][4])
    print(matriz[2][0], matriz[2][1], matriz[2][2], matriz[2][3], matriz[2][4])
    print(matriz[3][0], matriz[3][1], matriz[3][2], matriz[3][3], matriz[3][4])
    print(matriz[4][0], matriz[4][1], matriz[4][2], matriz[4][3], matriz[4][4])
    print('\033[36m'+"¿desea cambiar algún numero de la matriz? (si/no)"+'\033[0m')
    respuesta = input("->")
    if respuesta == "si":
        print("ingrese la posicion del numero que desea cambiar")
        print("fila: ")
        fila = int(input("->"))
        print("columna: ")
        columna = int(input("->"))
        print("ingrese el nuevo numero: ")
        numero = int(input("->"))
        matriz[fila][columna] = numero
        print("la matriz es: ")
        print(matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], matriz[0][4])
        print(matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3], matriz[1][4])
        print(matriz[2][0], matriz[2][1], matriz[2][2], matriz[2][3], matriz[2][4])
        print(matriz[3][0], matriz[3][1], matriz[3][2], matriz[3][3], matriz[3][4])
        print(matriz[4][0], matriz[4][1], matriz[4][2], matriz[4][3], matriz[4][4])
    else:
        print("la matriz se queda igual")
    def determinante(matriz):
        if len(matriz) == 1:
            return matriz[0][0]
        else:
            det = 0
            for i in range(len(matriz)):
                det += (-1)**i * matriz[0][i] * determinante([fila[:i] + fila[i+1:] for fila in (matriz[1:])])
            return det
    print("el determinante de la matriz es: ", determinante(matriz))
    print('\033[35m'+ "===================" + '\033[0m')

recursivaSarrus5x5()


n=int(input("ingrese el tamaño de la matriz: "))
def recursivaSarrusnxn():
    matriz = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            matriz[i][j]=int(input("ingrese el numero de la posicion ["+str(i)+"]["+str(j)+"]: "))
    print("la matriz es: ")
    for i in range(n):
        for j in range(n):
            print(matriz[i][j], end=" ")
        print()

    print('\033[36m'+"¿desea cambiar algún numero de la matriz? (si/no)"+'\033[0m')
    respuesta = input("->")
    if respuesta == "si":
        print("ingrese la posicion del numero que desea cambiar")
        print("fila: ")
        fila = int(input("->"))
        print("columna: ")
        columna = int(input("->"))
        print("ingrese el nuevo numero: ")
        numero = int(input("->"))
        matriz[fila][columna] = numero
        print("la matriz es: ")
        for i in range(n):
            for j in range(n):
                print(matriz[i][j], end=" ")
            print()
    else:
        print("la matriz se queda igual")
    def determinante(matriz):
        if len(matriz) == 1:
            return matriz[0][0]
        else:
            det = 0
            for i in range(len(matriz)):
                det += (-1)**i * matriz[0][i] * determinante([fila[:i] + fila[i+1:] for fila in (matriz[1:])])
            return det
    print("el determinante de la matriz es: ", determinante(matriz))
    print('\033[35m'+ "===================" + '\033[0m')

recursivaSarrusnxn()
