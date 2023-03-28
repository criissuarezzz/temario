#la estructura de una función recursiva es:
#def nombre_funcion(parametros):
#    if condicion:
#        return valor
#    else:
#        return nombre_funcion(parametros)
#siempre tiene que haber un if para que si no se cumple llame a la función de nuevo hasta que se cumpla



#ej 1
def triangular(n):
    if n == 1:
        return 1
    else:
        return n + triangular(n-1)
    
print(triangular(5))

print("\n")
#ej 2
def cant_digitos(n):
    if n<10:
        return 1
    else:
        return 1 + cant_digitos(n//10)

print(cant_digitos(123456789))

print("\n")
#ej 3
def es_potencia(a,b):
    if a == b:
        return True
    elif a<b:
        return False
    else:
        return es_potencia(a/b,b)
    
print(es_potencia(8,2))
print(es_potencia(9,2))
print(es_potencia(70,10))
print(es_potencia(100,10))

print("\n")
#ej 4
def par(n):
    if n == 0:
        return True
    else:
        return impar(n-1)

def impar(n):
    if n == 0:
        return False
    else:
        return par(n-1)

print("Es par 4?")
print(par(4))
print("Es par 5?")
print(par(5))
print("Es impar 4?")
print(impar(4))
print("Es impar 5?")
print(impar(5))

print("\n")
#ej 5
def maximo(lista):
    if len(lista)==0:
        return []
    elif len(lista)==1:
        return lista[0]
    else:
        return max(lista[0],maximo(lista[1:]))  
    
print("El maximo de [1,2,3,4,5] es:")
print(maximo([1,2,3,4,5]))

print("\n")
#ej 6
def replicar(lista, n):
    if len(lista)==0:
        return []
    else:
        return [lista[0]]*n + replicar(lista[1:],n)

print("Replicar [1,2,3,4,5] 3 veces:")
print(replicar([1,2,3,4,5],3))

print("\n")
#ej 7
def invertir(lista):
    if len(lista)==0:
        return []
    else:
        return invertir(lista[1:]) + [lista[0]]
    
print("Invertir [1,2,3,4,5]:")
print(invertir([1,2,3,4,5]))

print("\n")
#ej 8
def es_capicua(lista):
    if len(lista)==0:
        return True
    else:
        return lista[0]==lista[-1] and es_capicua(lista[1:-1])
    
print("Es capicua [1,2,3,2,1]:")
print(es_capicua([1,2,3,2,1]))

print("\n")
#ej 9
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)
    
print("Pascal (5,2):")
print(pascal(5,2))

print("\n")
#ej 10
def combinaciones(lista, k):
    if k == 0:
        return [[]]
    elif len(lista) == k:
        return [lista]
    else:
        return [[lista[0]] + x for x in combinaciones(lista[1:], k-1)] + combinaciones(lista[1:], k)

print("Combinaciones [1,2,3,4,5] 3:")
print(combinaciones([1,2,3,4,5],3))

print("\n")
#ej 11
def bbinaria_rec(lista, e):
    if len(lista)==0:
        return False
    elif len(lista)==1:
        return lista[0]==e
    else:
        medio = len(lista)//2
        if lista[medio]==e:
            return True
        elif lista[medio]>e:
            return bbinaria_rec(lista[:medio],e)
        else:
            return bbinaria_rec(lista[medio:],e)
        
print("Busqueda binaria recursiva [1,2,3,4,5] 3:")
print(bbinaria_rec([1,2,3,4,5],3))
print("Busqueda binaria recursiva [1,2,3,4,5] 2:")
print(bbinaria_rec([1,2,3,4,5],2))

print("\n")
#ej 12
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print("Fibonacci 5:")
print(fibonacci(5))

print("\n")
#ej 13
def medidas_hojas_A(n):
    if n==0:
        return 0
    else:
        return 2**n + medidas_hojas_A(n-1)
    
print("Medidas hojas A 5:")
print(medidas_hojas_A(5))

print("\n")
#ej 14
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print("Factorial 5:")
print(factorial(5))

print("\n")
#ej 15
def numeros_pares_impares(n):
    cont_imp=0
    for i in range (1,n+1):     #range (1,n+1) es para que el rango sea de 1 a n+1, es decir, de 1 a n
        if i%2==0:
            print(i,"es par")
        else:
            print(i,"es impar")
            cont_imp+=1
    print("Cantidad de impares:",cont_imp)

numeros_pares_impares(10)

