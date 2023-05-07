class nodoArista(object):
    """Clase nodo vértice"""
    def __init__(self, info, destino, sig=None):
        self.info = info
        self.destino = destino
        self.sig = sig

class nodoVertice(object):
    """Clase nodo vértice"""
    def __init__(self, info, sig=None, ady=None):
        self.info = info
        self.sig = sig
        self.ady = Arista()

class Grafo(object):
    """Clase grafo con implementación lista de listas de adyacencia"""
    def __init__(self, dirigido=True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0

class Arista(object):
    """Clase arista implementacion sobre lista"""
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato):
    """Inserta un vértice al grafo"""
    nodo = nodoVertice(dato, grafo.inicio)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig=grafo.inicio
        grafo.inicio = nodo
    else:
        ant=grafo.inicio
        act=grafo.inicio.sig
        while act is not None and act.info <= dato:
            ant=act
            act=act.sig
            nodo.sig=act
            ant.sig=nodo
    grafo.tamanio += 1

def insertar_arista(grafo, dato, origen, destino):
    """Inserta una arista al grafo"""
    nodo = nodoArista(dato, destino)
    aux = grafo.inicio
    while aux is not None and aux.info != origen:
        aux = aux.sig
    if aux is not None:
        aux.ady.insertar(nodo)
        if not grafo.dirigido:
            nodo = nodoArista(dato, origen)
            aux = grafo.inicio
            while aux is not None and aux.info != destino:
                aux = aux.sig
            if aux is not None:
                aux.ady.insertar(nodo)

def insertar_arista_noponderada(grafo, origen, destino):
    """Inserta una arista al grafo sin peso"""
    nodo = nodoArista(1, destino)
    aux = grafo.inicio
    while aux is not None and aux.info != origen:
        aux = aux.sig
    if aux is not None:
        aux.ady.insertar(nodo)
        if not grafo.dirigido:
            nodo = nodoArista(1, origen)
            aux = grafo.inicio
            while aux is not None and aux.info != destino:
                aux = aux.sig
            if aux is not None:
                aux.ady.insertar(nodo)

def eliminar_vertice(grafo, clave):
    """Elimina un vértice del grafo"""
    x = None
    ant = None
    aux = grafo.inicio
    while aux is not None and aux.info != clave:
        ant = aux
        aux = aux.sig
    if aux is not None:
        x = aux.info
        if ant is None:
            grafo.inicio = aux.sig
        else:
            ant.sig = aux.sig
        grafo.tamanio -= 1
        aux = grafo.inicio
        while aux is not None:
            aux.ady.eliminar(x)
            aux = aux.sig
    return x

def buscar_vertice(grafo, buscado):
    """Devuelve el vértice buscado"""
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux

def buscar_arista(grafo, origen, destino):
    """Devuelve la dirección del elemeto buscado, la arista buscada"""
    aux = grafo.inicio
    while aux is not None and aux.info != origen:
        aux = aux.sig
    if aux is not None:
        aux = aux.ady.inicio
        while aux is not None and aux.destino != destino:
            aux = aux.sig
    return aux

def eliminar_arista(grafo, origen, destino):
    """Elimina una arista del grafo"""
    x = None
    aux = grafo.inicio
    while aux is not None and aux.info != origen:
        aux = aux.sig
    if aux is not None:
        x = aux.ady.eliminar(destino)
    if not grafo.dirigido:
        aux = grafo.inicio
        while aux is not None and aux.info != destino:
            aux = aux.sig
        if aux is not None:
            aux.ady.eliminar(origen)
    return x

def tamanio(grafo):
    """Devuelve el número de vértices en el grafo"""
    return grafo.tamanio

def grafo_vacio(grafo):
    """Devuelve True si el grafo está vacio"""
    return grafo.inicio is None

def existe_paso(grafo, origen, destino):
    """Devuelve True si existe un paso entre los dos vértices"""
    resultado=False
    if not origen.visitado:
        origen.visitado=True
        ady=origen.ady.inicio
        while ady is not None and not resultado:
            ady=buscar_vertice(grafo, ady.destino)
            if ady.destino.info == destino.info:
                resultado=True
            else:
                resultado=existe_paso(grafo, ady.destino, destino)
            ady=ady.sig
    return resultado


def adyacentes(vertice):
    """Devuelve una lista con los vértices adyacentes al vértice pasado por parámetro"""
    lista = []
    aux = vertice.ady.inicio
    while aux is not None:
        lista.append(aux.destino)
        aux = aux.sig
    return lista

def es_adyacente(vertice, destino):
    """Devuelve True si el vértice destino es adyacente al vértice pasado por parámetro"""
    resultado=False
    aux = vertice.ady.inicio
    while aux is not None and not resultado:
        if aux.destino.info == destino.info:
            resultado=True
        aux = aux.sig
    return resultado

def marcar_no_visitado(grafo):
    """Marca todos los vértices del grafo como no visitados"""
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig

def barrido_vertices(grafo):
    """Barrido de todos los vértices del grafo"""
    aux = grafo.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig

def barrido_profundidad(grafo, vertice):
    """Barrido en profundidad del grafo"""
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.ady.inicio
            while adyacentes is not None:
                adyacentes = buscar_vertice(grafo, adyacentes.destino)
                barrido_profundidad(grafo, adyacentes)
                adyacentes = adyacentes.sig

from TDA.colas import Cola
def barrido_amplitud(grafo, vertice):
    """Barrido en amplitud del grafo"""
    cola = Cola()
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            Cola.arribo(cola, vertice)
        while not Cola.cola_vacia(cola):
            nodo = Cola.atencion(cola)
            print(nodo.info)
            adyacentes = nodo.ady.inicio
            while adyacentes is not None:
                adyacentes = buscar_vertice(grafo, adyacentes.destino)
                if not adyacentes.visitado:
                    adyacentes.visitado = True
                    Cola.arribo(cola, adyacentes)
                adyacentes = adyacentes.sig
        vertice = vertice.sig
