class Heap(object):
    """Crea  un montículo"""
    def __init__(self):
        self.tamanio = 0
        self.vector = [None]*self.tamanio

class Arbol:
    def agregar(heap, dato):
        """Agrega un dato en el montículo"""
        heap.vecctor[heap.tamanio]=dato
        Arbol.flotar(heap, heap.tamanio)
        heap.tamanio+=1

    def quitar(heap):
        """Quita el dato en la cima del montículo"""
        Arbol.intercambio(heap.vector, 0, heap.tamanio-1)
        heap.tamanio-=1
        Arbol.hundir(heap, 0)
        return heap.vector[heap.tamanio]
    
    def cantidad_elementos(heap):
        """Devuelve la cantidad de elementos en el montículo"""
        return heap.tamanio
    
    def monticulo_vacio(heap):
        """Devuelve True si el montículo está vacío"""
        return heap.tamanio==0

    def flotar(heap, indice):
        """Flota el elemento en la posición índice"""
        while(indice>0 and heap.vector[indice]>heap.vector[(indice-1)//2]):
            padre=(indice-1)//2
            Arbol.intercambio(heap.vector, indice, padre)
            indice=padre

    def hundir(heap, indice):
        """Hunde el elemento en la posición índice"""
        hijo_izq=(indice*2)+1
        control=True
        while(control and hijo_izq<heap.tamanio ):
            hijo_der=hijo_izq +1
            aux=hijo_izq
            if(hijo_der<heap.tamanio):
                if(heap.vector[hijo_der]>heap.vector[hijo_izq]):
                    aux=hijo_der
            if(heap.vector[indice]<heap.vector[aux]):
                Arbol.intercambio(heap.vector, indice, aux)
                indice=aux
                hijo_izq=(indice*2)+1
            else:
                control=False
    
    def intercambio(vector, indice1, indice2):
        """Intercambia dos elementos de posición"""
        aux=vector[indice1]
        vector[indice1]=vector[indice2]
        vector[indice2]=aux

    def monticulizar(heap):
        """Convierte un vector en un montículo"""
        for i in range(len(heap.vector)):
            Arbol.flotar(heap, i)

    def heapsort(heap):
        """Ordena un vector utilizando el método heapsort"""
        Arbol.monticulizar(heap)
        for i in range(len(heap.vector)-1, 0, -1):
            Arbol.intercambio(heap.vector, 0, i)
            Arbol.hundir(heap, 0)
        return heap.vector
    
    def arribo(heap, dato, prioridad):
        """Agrega un dato en el montículo utilizando prioridades"""
        heap.vector[heap.tamanio]=dato
        Arbol.flotar(heap, heap.tamanio)
        heap.tamanio+=1

    def atencion(heap):
        """Atiende el elemento en el frente de la cola y lo devuelve"""
        Arbol.intercambio(heap.vector, 0, heap.tamanio-1)
        heap.tamanio-=1
        Arbol.hundir(heap, 0)
        return heap.vector[heap.tamanio]
    
    def cambiar_prioridad(heap, indice, prioridad):
        """Cambia la prioridad de un elemento del montículo"""
        prioridad_anterior=heap.vector[indice][0]
        prioridad=heap.vector[indice][0]
        if(prioridad>prioridad_anterior):
            Arbol.flotar(heap, indice)
        else:
            Arbol.hundir(heap, indice)

    def heap_lleno(heap):
        """Verifica si el montículo está lleno"""
        if heap.tamanio==len(heap.vector):
            return True
        else:
            return False
    
    def agregar(heap, dato):
        """Agrega un dato en el montículo"""
        heap.vector[heap.tamanio]=dato
        Arbol.flotar(heap, heap.tamanio)
        heap.tamanio+=1

    def heap_vacio(heap):
        """Verifica si el montículo está vacío"""
        if heap.tamanio==0:
            return True
        else:
            return False
        
    def apilar(heap, dato):
        """Apila un dato en el montículo"""
        heap.vector[heap.tamanio]=dato
        Arbol.flotar(heap, heap.tamanio)
        heap.tamanio+=1
    
    def vacio(heap):
        """Verifica si el montículo está vacío"""
        if heap.tamanio==0:
            return True
        else:
            return False
        
import random
heap=Heap()
heap.tamanio=10
while not Arbol.heap_lleno(heap):
    num=random.randint(0, 500)
    prioridad=random.randint(1,3)
    Arbol.agregar(heap, (prioridad, num))
print(heap.vector)
print(Arbol.heapsort(heap))
while not Arbol.heap_vacio(heap):
    dato=Arbol.atencion(heap)
    print(dato)


