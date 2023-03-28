#un nodo es un objeto que tiene un valor y un puntero al siguiente nodo,
#sirve para apuntar a la siguiente posicion de la lista
class Nodo:
    def __init__(self, valor, siguiente=None):
        self.dato = valor
        self.siguiente = siguiente

