"""
el método de Kruskal es un algoritmo de la teoría de grafos utilizado para 
encontrar el árbol de expansión mínimo de un grafo conexo y no dirigido. Este 
algoritmo se basa en ir uniendo los árboles del bosque generador, que inicialmente 
son todos los vértices del grafo como árboles separados, mediante las aristas más 
cortas del grafo, siempre y cuando no se forme un ciclo.

El algoritmo comienza creando el bosque generador con todos los vértices del 
grafo como árboles separados. Luego, se agregan todas las aristas del grafo a una 
estructura de montículo (heap) para que puedan ser procesadas en orden de 
menor a mayor peso.

El proceso principal consiste en tomar la arista de menor peso del montículo, y 
verificar si su inclusión en el bosque generador forma un ciclo o no. Si no forma un 
ciclo, se agrega la arista al bosque y se unen los árboles correspondientes. Si 
forma un ciclo, la arista se descarta y se toma la siguiente arista de menor peso.

Este proceso se repite hasta que se hayan agregado suficientes aristas como para 
formar el árbol de expansión mínimo del grafo. Finalmente, se devuelve el bosque 
generador resultante, que es el árbol de expansión mínimo.
"""

import grafos
import monticulos as mont
def kruskal(grafo):
    """Algoritmo de Kruskal para hallar el árbol de expansión mínimo de un grafo"""
    bosque = []
    aristas = mont.Heap(grafos.tamanio(grafo)**2)
    aux = grafo.inicio
    while aux is not None:
        bosque.append([aux.info])
        adyacentes = aux.ady.inicio
        while adyacentes is not None:
            mont.Arbol.agregar(aristas, [aux.info, adyacentes.destino.info], adyacentes.info)
            adyacentes = adyacentes.sig
        aux = aux.sig
    while len(bosque[0]) < grafos.tamanio(grafo):
        dato = mont.Arbol.atencion(aristas)
        origen = None
        for elemento in bosque:
            if dato[1][0] in elemento:
                origen = elemento
        destino = None
        for elemento in bosque:
            if dato[1][1] in elemento:
                destino = elemento
        if origen is not destino:
            bosque.remove(origen)
            bosque.remove(destino)
            bosque.append(origen + destino)
    return bosque

