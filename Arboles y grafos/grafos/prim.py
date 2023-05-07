"""
El código implementa el algoritmo de Prim para 
encontrar el árbol de expansión mínimo de un grafo.

Primero, se inicializa el bosque con un solo vértice,
y se crea una lista de aristas que conectan ese vértice 
con sus adyacentes. Luego, se itera mientras el tamaño 
del bosque dividido entre dos sea menor que la cantidad 
total de vértices menos uno, que es la cantidad de aristas 
que debe tener el árbol de expansión mínimo.

Dentro del ciclo se busca la arista de menor peso que 
conecta un vértice del bosque con otro que no está en 
él. Si se encuentra dicha arista, se la agrega al bosque 
y se actualiza la lista de aristas.

Finalmente, se retorna el bosque, que debería contener todos 
los vértices del grafo y ser un árbol de expansión mínimo.
"""

import grafos
import monticulos as mont

def prim(grafo):
    """Algoritmo de Prime para hallar el árbol de expansión mínimo de un grafo"""
    bosque=[[grafo.inicio.info]]
    aristas=[]
    adyacentes=grafo.inicio.ady.inicio
    while adyacentes is not None:
        aristas.append([grafo.inicio.info, adyacentes.destino.info, adyacentes.info])
        adyacentes=adyacentes.sig
    while len(bosque[0])//2 < grafos.tamanio(grafo)-1:
        menor=aristas[0]
        menor_arista=None
        tipo=None
        for arista in aristas:
            origen = arista[0]
            destino = arista[1]
            if origen not in bosque[0] and destino in bosque[0]:
                if arista[2]<menor:
                    menor, menor_arista=arista[2], arista
                    tipo=True
            if origen in bosque[0] and destino not in bosque[0]:
                if arista[2]<menor:
                    menor, menor_arista=arista[2], arista
                    tipo=False
        arista= aristas.pop(aristas.index(menor_arista))
    if len(bosque[0])!=1:
        bosque[0]+=[arista[0], arista[1]]
    else:
        bosque.pop()
        bosque.append([arista[0], arista[1]])
    aux=None
    if tipo:
        aux=grafos.buscar_vertice(grafo, arista[0])
    else:
        aux=grafos.buscar_vertice(grafo, arista[1])
    adyacentes=aux.ady.inicio
    while adyacentes is not None:
        aristas.append([aux.info, adyacentes.destino.info, adyacentes.info])
        adyacentes=adyacentes.sig
    return bosque
