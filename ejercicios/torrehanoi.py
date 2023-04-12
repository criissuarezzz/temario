class Disco:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.siguiente = None


class Torre:
    def __init__(self):
        self.top = None
        self.altura = 0

    def apilar(self, disco):
        disco.siguiente = self.top
        self.top = disco
        self.altura += 1

    def desapilar(self):
        if self.top is None:
            return None

        disco = self.top
        self.top = disco.siguiente
        self.altura -= 1
        return disco

    def obtener_top(self):
        return self.top

    def obtener_altura(self):
        return self.altura

    def mover_disco(origen, destino):
        disco = origen.desapilar()
        destino.apilar(disco)

def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        Torre.mover_disco(origen, destino)
    else:
        torres_hanoi(n-1, origen, auxiliar, destino)
        Torre.mover_disco(origen, destino)
        torres_hanoi(n-1, auxiliar, destino, origen)

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0
    
    def arribo(self, dato):
        nodo = Disco()
        nodo.info = dato
        if self.frente == None:
            self.frente = nodo
        else:
            self.final.siguiente = nodo
            self.final = nodo
            self.tamanio += 1

    def atencion(self):
        if self.cola_vacia():
            raise Exception("Cola vacía")

        x = self.frente.info
        self.frente = self.frente.siguiente
        self.tamanio -= 1
        return x
    
    def cola_vacia(self):
        return self.frente == None
    
    def en_frente(self):
        return self.frente == None
    
    def tamanio(self):
        return self.tamanio
    
    def mover_al_final(self):
        if self.cola_vacia():
            raise Exception("Cola vacía")

        x = self.frente.info
        self.frente = self.frente.siguiente
        self.arribo(x)
        return x
    
    def mover_n_elementos(self, n):
        for i in range(n):
            self.mover_al_final()

    def __str__(self):
        cadena = ""
        nodo = self.frente
        while nodo != None:
            cadena += str(nodo.info) + " "
            nodo = nodo.siguiente
        return cadena

def main():
    origen = Torre()
    destino = Torre()
    auxiliar = Cola()

    for i in range(74, 0, -1):
        disco = Disco(i)
        origen.apilar(disco)

    torres_hanoi(origen.obtener_altura(), origen, destino, auxiliar)

    print("Torre de origen: ", origen.obtener_altura())
    print("Torre auxiliar: ", auxiliar.obtener_altura())
    print("Torre de destino: ", destino.obtener_altura())

main()