"""
El algoritmo de la mochila, también conocido como 
"knapsack problem" en inglés, es un problema clásico 
de optimización combinatoria. Consiste en seleccionar
un conjunto de elementos, cada uno con un valor y un 
peso asociados, de tal manera que se maximice el valor 
total de los elementos seleccionados sin exceder la 
capacidad de una mochila o bolsa de capacidad limitada.

El algoritmo de la mochila es un algoritmo voraz que 
se basa en seleccionar los elementos de mayor valor 
por unidad de peso, es decir, se ordenan los elementos 
según su valor por unidad de peso de manera descendente 
y se van añadiendo a la mochila aquellos elementos que 
quepan y que tengan el mayor valor por unidad de peso. Este proceso se repite hasta que se llenen todos los espacios disponibles de la mochila o no queden más elementos por añadir.

Este algoritmo es eficiente para problemas pequeños o 
medianos, pero para problemas grandes es necesario 
utilizar técnicas más sofisticadas, como la programación 
dinámica.
"""

def mochila(pesos, valores, capacidad):
    n = len(valores)
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, capacidad+1):
            if pesos[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-pesos[i-1]] + valores[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    res = []
    i = n
    j = capacidad
    while i > 0 and j > 0:
        if dp[i][j] != dp[i-1][j]:
            res.append(i-1)
            j -= pesos[i-1]
        i -= 1

    return res[::-1], dp[n][capacidad]

if __name__=='__main__':
    pesos = [1, 2, 4, 2, 5]
    valores = [5, 3, 5, 3, 2]
    capacidad = 10   
    print ("disponemos de los siguientes valores que pesan lo siguiente: ")
    for i in range(len(valores)):
        print(valores[i], ":", pesos[i], "kg")
    print("y una mochila de capacidad", capacidad)
    print("Seleccionamos por tanto los siguientes valores:")
    print(mochila(pesos, valores, capacidad))
