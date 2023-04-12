class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.superior = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.superior is None

    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo
        self.tamanio += 1

    def desapilar(self):
        if self.esta_vacia():
            return None
        else:
            nodo_eliminado = self.superior
            self.superior = self.superior.siguiente
            nodo_eliminado.siguiente = None
            self.tamanio -= 1
            return nodo_eliminado.dato

    def cima(self):
        if self.esta_vacia():
            return None
        else:
            return self.superior.dato

    def tamanioPila(self):
        return self.tamanio

    def mostrarPila(self):
        # Comenzamos desde la cima de la Pila
        actual = self.superior
        # Iteramos a través de cada nodo y lo imprimimos
        while actual:
            print(actual.dato)
            actual = actual.siguiente
