#implementar el código de arboles.py en un ejercicio
#enunciado:
#El objetivo del ejercicio es implementar un árbol de búsqueda binaria en Python y utilizarlo para buscar elementos en una lista de números. Primero, deberás implementar la estructura de datos del árbol de búsqueda binaria. Luego, se te proporcionará una lista de números y deberás insertar cada número en el árbol. Una vez que se hayan insertado todos los números, deberás buscar un número dado en el árbol y devolver su posición en la lista original.
#Por ejemplo, si la lista original es [5, 2, 7, 1, 8, 3, 6, 4] y se te pide buscar el número 6, tu programa deberá construir un árbol de búsqueda binaria con los números de la lista y luego buscar el número 6 en el árbol. Si el número 6 se encuentra en la lista original, deberás devolver su posición en la lista, en este caso la posición 6.
#Si el número 6 no se encuentra en la lista original, deberás devolver -1.



class NodoArbol:
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar_nodo(self, nodo):
        if self.raiz is None:
            self.raiz = None
        else:
            if nodo.info < self.raiz.info:
                if self.raiz.izq is None:
                    self.raiz.izq = nodo
                else:
                    self.insertar_nodo(self.raiz.izq, nodo)
            else:
                if self.raiz.der is None:
                    self.raiz.der = nodo
                else:
                    ArbolBinario.insertar_nodo(self.raiz.der, nodo)

    def buscar_nodo(self, clave):
        if self.raiz is None:
            return None
        else:
            if clave < self.raiz.info:
                return ArbolBinario.buscar_nodo(self.raiz.izq, clave)
            elif clave > self.raiz.info:
                return ArbolBinario.buscar_nodo(self.raiz.der, clave)
            else:
                return self.raiz

    def buscar_posicion(self, clave, lista):
        if self.raiz is None:
            return -1
        else:
            if clave < self.raiz.info:
                return ArbolBinario.buscar_posicion(self.raiz.izq, clave, lista)
            elif clave > self.raiz.info:
                return ArbolBinario.buscar_posicion(self.raiz.der, clave, lista)
            else:
                return lista.index(clave) 

    def eliminar_nodo(self, clave):
        x = None
        if self.raiz is not None:
            if clave < self.raiz.info:
                self.raiz.izq, x = ArbolBinario.eliminar_nodo(self.raiz.izq, clave)
            elif clave > self.raiz.info:
                self.raiz.der, x = ArbolBinario.eliminar_nodo(self.raiz.der, clave)
            else:
                x = self.raiz.info
                if self.raiz.izq is None:
                    self.raiz = self.raiz.der
                elif self.raiz.der is None:
                    self.raiz = self.raiz.izq
                else:
                    self.raiz.izq, aux = ArbolBinario.remplazar(self.raiz.izq)
                    self.raiz.info = aux.info
        return self.raiz, x
    
    def remplazar(self, nodo):
        if nodo.der is not None:
            nodo.der, aux = ArbolBinario.remplazar(nodo.der)
        else:
            aux = nodo
            nodo = nodo.izq
        return nodo, aux
    
    def inorden(self):
        if self.raiz is not None:
            ArbolBinario.inorden(self.raiz.izq)
            print(self.raiz.info)
            ArbolBinario.inorden(self.raiz.der)

    def preorden(self):
        if self.raiz is not None:
            print(self.raiz.info)
            ArbolBinario.preorden(self.raiz.izq)
            ArbolBinario.preorden(self.raiz.der)

    def postorden(self):
        if self.raiz is not None:
            ArbolBinario.postorden(self.raiz.izq)
            ArbolBinario.postorden(self.raiz.der)
            print(self.raiz.info)

    def recorrido_por_niveles(self):
        if self.raiz is not None:
            cola = [self.raiz]
            while cola:
                nodo = cola.pop(0)
                print(nodo.info)
                if nodo.izq is not None:
                    cola.append(nodo.izq)
                if nodo.der is not None:
                    cola.append(nodo.der)

    def altura(self):
        if self.raiz is None:
            return 0
        else:
            return ArbolBinario.altura(self.raiz)
        



def main():
    lista = [5, 2, 7, 1, 8, 3, 6, 4]
    arbol = ArbolBinario()
    for i in lista:
        nodo = NodoArbol(i)
        arbol.insertar_nodo(nodo)
    print(arbol.buscar_posicion(6, lista))
    print(arbol.buscar_posicion(9, lista))

if __name__ == '__main__':
    main()
