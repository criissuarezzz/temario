#1.	Cada nodo en el árbol debe ser rojo o negro.

#2.	El nodo raíz del árbol debe ser siempre negro.

#3.	Dos nodos rojos nunca pueden aparecer consecutivamente, uno tras otro. Es decir un nodo rojo siempre debe tener un nodo padre negro e hijos negros.

#4.	Cada ruta de bifurcación del árbol desde el nodo raíz a un nodo hoja vacío (o nulo) debe pasar por el mismo número exacto de nodos negros. Los nodos hojas vacíos también se deben consi- derar como un nodo negro del camino, ya que representa la ruta que se tomará si se busca un nodo que no existe dentro del árbol.

class nodoArbolRN(object):
    """Clase nodo árbol rojo-negro"""
    def __init__(self, info):
        self.padre= None
        self.izq=None
        self.der=None
        self.info=info
        self.color=1  #0=negro y 1=rojo

    def insertar_nodo(raiz, dato):
        """Inserta un dato al árbol"""
        ant=None
        act=raiz
        nodo=nodoArbolRN(dato)
        while (act is not None):
            ant=act
            if (nodo.info<act.info):
                act=act.izq
            else:
                act=act.der
        nodo.padre=ant
        if ant is not None:
            raiz= nodo
        elif (nodo.info<ant.info):
            ant.izq = nodo
        else:
            ant.der=nodo
        raiz=nodoArbolRN.reparar_insertar(nodo)
        return raiz
    
    
    def reparar_insertar(nodo):
        """Repara el equilibrio del árbol luego de insertar un nodo"""
        aux=None
        while nodo.padre is not None and nodo.padre.color==1:
            abuelo=nodo.padre.padre
            if abuelo is not None and nodo.padre==nodo.padre.padre.izq:
                aux=nodo.padre.padre.der
                if aux is not None and aux.color ==1:  #caso 1
                    nodo.padre.color=0
                    aux.color=0
                    nodo.padre.padre.color=1
                    nodo=nodo.padre.padre
                elif nodo==nodo.padre.der: #caso 2
                    nodo=nodo.padre
                    nodoArbolRN.rotar_izquierda(nodo)
                else: #caso 3
                    nodo.padre.color=0
                    nodo.padre.padre.color=1
                    nodoArbolRN.rotar_derecha(nodo.padre.padre)
            elif(nodo.padre.padre is not None):
                aux=nodo.padre.padre.izq
                if aux is not None and aux.color==1: #caso 1
                    nodo.padre.color=0
                    aux.color=0
                    nodo.padre.padre.color=1
                    nodo=nodo.padre.padre
                elif nodo==nodo.padre.izq: #caso 2
                    nodo=nodo.padre
                    nodoArbolRN.rotar_derecha(nodo)
                else: #caso 3
                    nodo.padre.color=0
                    nodo.padre.padre.color=1
                    nodoArbolRN.rotar_izquierda(nodo.padre.padre)
            else:
                nodo=nodo.padre
        if nodo.padre is None:
            nodo.color=0
        else:
            while nodo.padre is not None:
                nodo=nodo.padre
        return nodo
    
    def rotar_derecha(nodo):
        """Rotar nodo a la derecha"""
        aux=nodo.izq
        nodo.izq=aux.der
        if aux.der is not None:
            aux.der.padre=nodo
        aux.padre=nodo.padre

        if nodo.padre is not None:
            if nodo.padre.der == nodo:
                nodo.padre.der=aux
            else:
                nodo.padre.izq=aux
        aux.der=nodo
        nodo.padre=aux

    def rotar_izquierda(nodo):
        """Rotar nodo a la izquierda"""
        aux=nodo.der
        nodo.der=aux.izq
        if aux.izq is not None:
            aux.izq.padre=nodo
        aux.padre=nodo.padre

        if nodo.padre is not None:
            if nodo.padre.izq == nodo:
                nodo.padre.izq=aux
            else:
                nodo.padre.der=aux
        aux.izq=nodo
        nodo.padre=aux

    def eliminar_nodo(raiz, dato):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra"""
        dato=None
        if raiz is not None:
            aux=raiz
            while aux is not None and aux.info!=dato:
                if dato<aux.info:
                    aux=aux.izq
                else:
                    aux=aux.der
            if aux is not None:
                dat=aux.info
                x=None
                y=None

                if aux.izq is None or aux.der is None:
                    y=aux
                else:
                    y=nodoArbolRN.remplazar(aux.izq)
                if y.izq is not None:
                    x=y.izq
                else:
                    x=y.der

                if y.padre is not None:
                    if y.padre.izq is not None and y.padre.izq == y:
                        y.padre.izq=x
                    elif y.padre.der is not None and y.padre.der == y:
                        y.padre.der=x
                
                if x is None and y.padre is not None and y.color==0:
                    x= nodoArbolRN(0)
                    x.color=y.color
                if x is not None:
                    x.padre=y.padre
                if y!=aux:
                    aux.info=y.info
                
                if y.padre is None and y.izq is None and y.der is None:
                    raiz=x
                    return raiz, dato
                if y.color==0:
                    aux=nodoArbolRN.reparar_eliminar(x)
                    if aux is not None:
                        raiz=aux
            return raiz, dato
        
        def remplazar(nodo):
            """Remplaza un nodo"""
            aux1=nodo
            aux2=None
            while aux1 is not None:
                aux2=aux1
                aux1=aux1.der
            return aux2
#ejemplo de uso
def main():
    raiz=None
    raiz=nodoArbolRN.insertar_nodo(raiz, 10)
    raiz=nodoArbolRN.insertar_nodo(raiz, 20)
    raiz=nodoArbolRN.insertar_nodo(raiz, 30)
    raiz=nodoArbolRN.insertar_nodo(raiz, 40)
    raiz=nodoArbolRN.insertar_nodo(raiz, 50)
    raiz=nodoArbolRN.insertar_nodo(raiz, 60)
    raiz=nodoArbolRN.insertar_nodo(raiz, 70)
    raiz=nodoArbolRN.insertar_nodo(raiz, 80)
    raiz=nodoArbolRN.insertar_nodo(raiz, 90)
    raiz=nodoArbolRN.insertar_nodo(raiz, 100)
    raiz=nodoArbolRN.insertar_nodo(raiz, 110)
    raiz=nodoArbolRN.insertar_nodo(raiz, 120)
    raiz=nodoArbolRN.insertar_nodo(raiz, 130)
    raiz=nodoArbolRN.insertar_nodo(raiz, 140)
    raiz=nodoArbolRN.insertar_nodo(raiz, 150)
    raiz=nodoArbolRN.insertar_nodo(raiz, 160)
    raiz=nodoArbolRN.insertar_nodo(raiz, 170)
    raiz=nodoArbolRN.insertar_nodo(raiz, 180)
    raiz=nodoArbolRN.insertar_nodo(raiz, 190)
    raiz=nodoArbolRN.insertar_nodo(raiz, 200)
    raiz=nodoArbolRN.insertar_nodo(raiz, 210)
    raiz=nodoArbolRN.insertar_nodo(raiz, 220)
    raiz=nodoArbolRN.insertar_nodo(raiz, 230)
    raiz=nodoArbolRN.insertar_nodo(raiz, 240)
    raiz=nodoArbolRN.insertar_nodo(raiz, 250)
    raiz=nodoArbolRN.insertar_nodo(raiz, 260)
    raiz=nodoArbolRN.insertar_nodo(raiz, 270)
    raiz=nodoArbolRN
