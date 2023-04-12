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

class NodoArbol:
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

class ArbolBinario:
    def eliminar_nodo(raiz, clave):
        x= None
        if raiz is not None:
            if clave<raiz.info:
                raiz.izq, x= NodoArbol.eliminar_nodo(raiz.izq, clave)
            elif clave>raiz.info:
                raiz.der, x= NodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x= raiz.info
                if raiz.izq is None:
                    raiz= raiz.der
                elif raiz.der is None:
                    raiz= raiz.izq
                else:
                    raiz.izq, aux= NodoArbol.remplazar(raiz.izq)
                    raiz.info= aux.info
        return raiz, x
    
    def remplazar(raiz):
        aux= None
        if raiz.der is not None:
            aux= raiz
            raiz = raiz.izq
        else:
            raiz, aux= NodoArbol.remplazar(raiz.der)
        return raiz, aux
    
    def insertar_nodo(raiz, nodo):
        if raiz is None:
            raiz= NodoArbol(nodo.info)
        else:
            if nodo.info<raiz.info:
                    NodoArbol.insertar_nodo(raiz.izq, nodo)
            else:
                if raiz.der is None:
                    raiz.der= nodo
                elif nodo.info<raiz.info:
                    raiz.izq=NodoArbol.insertar_nodo(raiz.izq, nodo)
                else:
                    raiz.der= NodoArbol.insertar_nodo(raiz.der, nodo)
        return raiz
    
    def arbolvacio(raiz):
        return raiz is None
    
    def por_nivel(raiz):
        pendientes= Cola()
        Cola.arribo(pendientes, raiz)
        while not Cola.cola_vacia(pendientes):
            nodo= Cola.atencion(pendientes)
            print(nodo.info)
            if nodo.izq is not None:
                Cola.arribo(pendientes, nodo.izq)
            if nodo.der is not None:
                Cola.arribo(pendientes, nodo.der)

    def buscar(raiz, clave):
        pos= None
        if raiz is not None:
            if raiz.info==clave:
                pos= raiz
            elif clave<raiz.info:
                pos= NodoArbol.buscar(raiz.izq, clave)
            else:
                pos= NodoArbol.buscar(raiz.der, clave)
        return pos
    
    def inorden(raiz):
        if raiz is not None:
            NodoArbol.inorden(raiz.izq)
            print(raiz.info)
            NodoArbol.inorden(raiz.der)

    def preorden(raiz):
        if raiz is not None:
            print(raiz.info)
            NodoArbol.preorden(raiz.izq)
            NodoArbol.preorden(raiz.der)

    def postorden(raiz):
        if raiz is not None:
            NodoArbol.postorden(raiz.der)
            print(raiz.info)
            NodoArbol.postorden(raiz.izq)

    def cantidad_nodos(raiz):
        if raiz is None:
            return 0
        else:
            return 1+NodoArbol.cantidad_nodos(raiz.izq)+NodoArbol.cantidad_nodos(raiz.der)
        
    def cantidad_hojas(raiz):
        if raiz is None:
            return 0
        elif raiz.izq is None and raiz.der is None:
            return 1
        else:
            return NodoArbol.cantidad_hojas(raiz.izq)+NodoArbol.cantidad_hojas(raiz.der)
        

class Cola:
    def __init__(self):
        self.items=[]
    
    def arribo(self, dato):
        self.items.append(dato)
    
    def atencion(self):
        return self.items.pop(0)
    
    def cola_vacia(self):
        return len(self.items)==0