class nodoCola(object):

    """Clase nodoCola"""

    info, sig = None, None




class Cola(object):

    """Clase Cola"""

    def __init__(self) -> None:

        """Crea una cola vacía"""

        self.frente = None

        self.final = None

        self.tamanio = 0


    def arribo(cola, dato):

        """Arriba el dato al final de la cola"""
        nodo=nodoCola()
        nodo.info=dato
        if cola.frente == None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
            cola.final = nodo
            cola.tamanio += 1
        
    def atencion(cola):

        """Atiende el elemento que está en el frente de la cola"""

        if cola.cola_vacia():

            raise Exception("Cola vacía")  

        x = cola.frente.info

        cola.frente = cola.frente.sig

        # if cola.frente == None:

        #    cola.final = None

        cola.tamanio -= 1

        return x



    def cola_vacia(cola):

        """Verifica si la cola está vacía"""
        return cola.frente == None

    def tamanio(cola):

        """Devuelve el tamaño de la cola"""

        return cola.tamanio

    def en_frente(cola):

        """Devuelve el elemento que está en el frente de la cola"""

        if cola.cola_vacia():

            raise Exception("Cola vacía")

        return cola.frente.info

    def mover_al_final(cola):

        """Mueve el elemento que está en el frente de la cola al final"""

        if cola.cola_vacia():
            raise Exception("Cola vacía")

        x = cola.atencion()

        cola.arribo(x)
        return x

    def barrido(cola):

        """Muestra los elementos de la cola sin perder datos"""
        i=0
        while(i < cola.tamanio):
            dato=cola.mover_al_final()

            print(dato)
            i+=1

#experimentacion
cola=Cola()
cola.arribo(1)
cola.arribo(2)
cola.arribo(3)
cola.barrido()
cola.atencion()
cola.mover_al_final(5)

