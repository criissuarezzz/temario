from colas import Cola

class nodoArbol(object):
    """Clase nodo árbol"""

    def _init_(self, info):
        """Crea un nodo con la información cargada"""
        self.izq = None
        self.der = None
        self.info = info
        self.altura = 0

    def eliminar_nodo(raiz, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra"""
        x = None
        if (raiz is not None):
            if(clave < raiz.info):
                raiz.izq, x = nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif(clave > raiz.info):
                raiz.der, x = nodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if(raiz.izq is None):
                    raiz = raiz.der
                elif(raiz.der is None):
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info = aux.info
        raiz = nodoArbol.balancear(raiz)
        nodoArbol.actualizaraltura(raiz)
        return raiz, x
    
    def insertar_nodo(raiz, dato):
        """Inserta un dato al árbol"""
        if(raiz is None):
            raiz = nodoArbol(dato)
        elif(dato < raiz.info):
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
        raiz = nodoArbol.balancear(raiz)
        nodoArbol.actualizaraltura(raiz)
        return raiz

    def arbolvacio(raiz):
        """Devuelve true si el árbol esta vacío"""
        return raiz is None

    def remplazar(raiz):
        """Determina el nodo que remplazará al que se elimina"""
        aux = None
        if (raiz.der is None):
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = nodoArbol.remplazar(raiz.der)
        return raiz, aux
    
    def por_nivel(raiz):
        """Realiaza el barrido postorden del árbol"""
        pendientes = Cola()
        Cola.arribo(pendientes, raiz)
        while(not Cola.cola_vacia(pendientes)):
            nodo = Cola.atencion(pendientes)
            print(nodo.info)
            if(nodo.izq is not None):
                Cola.arribo(pendientes, nodo.izq)
            if(nodo.der is not None):
                Cola.arribo(pendientes, nodo.der)

    def buscar(raiz, clave):
        """Devuelve la dirección del elemento buscado"""
        pos = None
        if(raiz is not None):
            if(raiz.info == clave):
                pos = raiz
            elif clave < raiz.info:
                pos = nodoArbol.buscar(raiz.izq, clave)
            else:
                pos = nodoArbol.buscar(raiz.der, clave)
        return pos
    
    def inorden(raiz):
        """Realiza el barrido inorden del árbol"""
        if(raiz is not None):
            nodoArbol.inorden(raiz.izq)
            print(raiz.info)
            nodoArbol.inorden(raiz.der)

    def preorden(raiz):
        """Realiza el barrido preorden del árbol"""
        if(raiz is not None):
            print(raiz.info)
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)

    def postorden(raiz):
        """Realiza el barrido postorden del árbol"""
        if(raiz is not None):
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)

    def altura(raiz):
        """Devuelve la altura de un nodo"""
        if(raiz is None):
            return -1
        else:
            return raiz.altura
        
    def actualizaraltura(raiz):
        """Actualiza la altura de un nodo"""
        if(raiz is not None):
            alt_izq = nodoArbol.altura(raiz.izq)
            alt_der = nodoArbol.altura(raiz.der)
            raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1

    def rotar_simple(raiz, control):
        """Realiza una rotación simple de nodos a la derecha o a la izquierda"""
        if control:
            aux = raiz.izq
            raiz.izq = aux.der
            aux.der = raiz
        else:
            aux = raiz.der
            raiz.der = aux.izq
            aux.izq = raiz
        nodoArbol.actualizaraltura(raiz)
        nodoArbol.actualizaraltura(aux)
        raiz = aux
        return raiz
    
    def rotar_doble(raiz, control):
        """Realiza una rotación doble de nodos a la derecha o la izquierda"""
        if control:
            raiz.izq = nodoArbol.rotar_simple(raiz.izq, False)
            raiz = nodoArbol.rotar_simple(raiz, True)
        else:
            raiz.der = nodoArbol.rotar_simple(raiz.der, True)
            raiz = nodoArbol.rotar_simple(raiz, False)
        return raiz
    
    def balancear(raiz):
        """Determina que rotación hay que hacer para balancear el arbol"""
        if(raiz is not None):
            if(nodoArbol.altura(raiz.izq)-nodoArbol.altura(raiz.der) == 2):
                if(nodoArbol.altura(raiz.izq.izq) >= nodoArbol.altura(raiz.izq.der)):
                    raiz = nodoArbol.rotar_simple(raiz, True)
                else:
                    raiz = nodoArbol.rotar_doble(raiz, True)
            elif(nodoArbol.altura(raiz.der)-nodoArbol.altura(raiz.izq) == 2):
                if(nodoArbol.altura(raiz.der.der) >= nodoArbol.altura(raiz.der.izq)):
                    raiz = nodoArbol.rotar_simple(raiz, False)
                else:
                    raiz = nodoArbol.rotar_doble(raiz, False)
        return raiz

    def imprimir_arbol(raiz, nivel=0):
        """Imprime por pantalla el arbol"""
        if raiz is not None:
            nodoArbol.imprimir_arbol(raiz.der, nivel + 1)
            print('    ' * nivel + str(raiz.info))
            nodoArbol.imprimir_arbol(raiz.izq, nivel + 1)

            


if __name__=='__main__':
    arbol = nodoArbol(10)
    arbol = nodoArbol.insertar_nodo(arbol, 5)
    arbol = nodoArbol.insertar_nodo(arbol, 15)
    arbol = nodoArbol.insertar_nodo(arbol, 3)
    arbol = nodoArbol.insertar_nodo(arbol, 7)
    arbol = nodoArbol.insertar_nodo(arbol, 13)
    arbol = nodoArbol.insertar_nodo(arbol, 17)
    arbol = nodoArbol.insertar_nodo(arbol, 1)
    arbol = nodoArbol.insertar_nodo(arbol, 4)
    arbol = nodoArbol.insertar_nodo(arbol, 6)
    arbol = nodoArbol.insertar_nodo(arbol, 8)
    arbol = nodoArbol.insertar_nodo(arbol, 11)
    arbol = nodoArbol.insertar_nodo(arbol, 14)
    arbol = nodoArbol.insertar_nodo(arbol, 16)
    arbol = nodoArbol.insertar_nodo(arbol, 18)
    arbol = nodoArbol.insertar_nodo(arbol, 9)
    arbol = nodoArbol.insertar_nodo(arbol, 12)
    arbol = nodoArbol.insertar_nodo(arbol, 19)
    arbol = nodoArbol.insertar_nodo(arbol, 20)
    nodoArbol.imprimir_arbol(arbol)
    print('Barrido por nivel')
    nodoArbol.por_nivel(arbol)
    print('Barrido inorden')
    nodoArbol.inorden(arbol)
    print('Barrido preorden')
    nodoArbol.preorden(arbol)
    print('Barrido postorden')
    nodoArbol.postorden(arbol)
    print('Altura del arbol')
    print(nodoArbol.altura(arbol))
    print('Buscar un elemento')
    print(nodoArbol.buscar(arbol, 5))
    print('Eliminar un elemento')
    arbol = nodoArbol.eliminar(arbol, 5)
    nodoArbol.imprimir_arbol(arbol)
    print('Altura del arbol')
    print(nodoArbol.altura(arbol))
    