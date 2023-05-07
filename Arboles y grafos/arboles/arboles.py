#Hijo-> depende directamente de otro nodo
#Padre-> es aquel nodo que tiene al menos de un nodo hijo
#Hermano-> son nodos que tienen el mismo padre
#Descendiente -> aquellos nodos que pertenecen a los subárboles de los hijos de un nodo
#Ancestros -> los nodos en el camino desde la raíz hasta el nodo dado
#Hoja -> es aquel nodo que no tiene hijos
#Nodo  interno -> es aquel nodo que tiene al menos un hijo
#Grado de un nodo-> es el número de hijos que tiene un nodo
#Rama -> es la conexion entre dos nodos, también llamado enlace
#Grado de un árbol -> la máxima cantidad de hijos que tiene un nodo en el árbol
#Camino -> es la secuencia de nodos que se encuentran en el camino desde un nodo a otro
#Nivel -> es la distancia entre un nodo y la raíz mas uno
#Altura de un nodo-> es el número de ramas del camino más largo entre ese nodo y una hoja
#Altura de un árbol -> es la altura del nodo raíz
#Profundidad de un nodo -> es el número de ramas desde la raíz del árbol hasta dicho nodo
#Subárbol -> es un árbol que tiene como raíz a un nodo del árbol original
#Bosque -> es un conjunto de dos o más árboles

#Ejemplo de árbol binario, cada nodo tiene como máximo dos hijos
from TDA.colas import Cola
class nodoArbol(object):
    """Clase nodo árbol"""

    def _init_(self, info):
        """Crea un nodo con la información cargada"""
        self.izq = None
        self.der = None
        self.info = info
    
    def eliminar_nodo(raiz, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra"""
        x = None
        if (raiz is not None):
            if(clave < raiz.info):
                raiz.izq, x = nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif(clave > raiz.info):
                raiz.der, x = nodoArbol(raiz.der, clave)
            else:
                x = raiz.info
                if(raiz.izq is None):
                    raiz = raiz.der
                elif(raiz.der is None):
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info = aux.info
        return raiz, x
    
    def insertar_nodo(raiz, dato):
        """Inserta un dato al árbol"""
        if(raiz is None):
            raiz = nodoArbol(dato)
        elif(dato < raiz.info):
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
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

    def imprimir_arbol(raiz, nivel=0):
        """Imprime por pantalla el arbol"""
        if raiz is not None:
            nodoArbol.imprimir_arbol(raiz.der, nivel + 1)
            print('    ' * nivel + str(raiz.info))
            nodoArbol.imprimir_arbol(raiz.izq, nivel + 1)