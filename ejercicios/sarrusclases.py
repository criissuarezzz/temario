class nodoLista(object):
    info, sig = None, None

class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

    def insertar(lista, dato):
        nodo=nodoLista()
        nodo.info=dato
        if (lista.inicio is None) or (lista.inicio.info > dato):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            ant=lista.inicio
            act=lista.inicio.sig
            while (act is not None) and (act.info <= dato):
                ant=act
                act=act.sig
            nodo.sig=act
            ant.sig=nodo
            lista.tamanio += 1

    def lista_vacia(lista):
        return lista.inicio is None
        
    def eliminar(lista, dato):
            