"""
La función dijkstra(grafo, origen) implementa el algoritmo de Dijkstra para 
encontrar el camino más corto desde un vértice de origen a todos los demás 
vértices de un grafo.

La función recibe como parámetros el grafo y el vértice de origen. Se crea un 
montículo de mínimo no_visitados y una pila camino para guardar los 
vértices visitados.

Se inicializa un ciclo mientras el grafo tenga nodos, y se agrega al montículo 
no_visitados cada nodo con un valor de distancia inicial de 9999, excepto el 
nodo de origen que tiene una distancia inicial de 0.

Luego se comienza otro ciclo mientras el montículo no_visitados no esté vacío. 
En cada iteración se extrae del montículo el nodo con la menor distancia, se apila 
en la pila camino, y se actualizan las distancias de los nodos adyacentes si es 
que se encuentra un camino más corto a través del nodo actual.

Finalmente, se devuelve la pila camino con los nodos visitados y sus distancias 
más cortas.
"""
import grafos
from arboles import monticulos as mont
from TDA.pilas import Pila
def dijkstra(grafo, origen):
    """Algoritmo de Dijkstra para hallar el camino más corto entre un vértice y los demás"""
    no_visitados=mont.Heap(grafos.tamanio(grafo))
    camino=Pila()
    aux=grafo.inicio
    while aux is not None:
        if aux.info==origen:
            mont.Arbol.agregar(no_visitados, [aux, None], 0)
        else:
            mont.Arbol.agregar(no_visitados, [aux, None], 9999)
        aux=aux.sig
    while not mont.Arbol.vacio(no_visitados):
        dato=mont.Arbol.atencion(no_visitados)
        mont.Arbol.apilar(camino, dato)
        aux=dato[1][0].ady.inicio
        while aux is not None:
            pos=mont.Arbol.busqueda(no_visitados, aux.destino)
            if no_visitados.vector[pos][0]>dato[0]+aux.info:
                no_visitados.vector[pos][1][1]=dato[1][0].info
                mont.Arbol.modificar(no_visitados, pos, no_visitados.vector[pos][0], no_visitados.vector[pos][1])
            aux=aux.sig
    return camino
