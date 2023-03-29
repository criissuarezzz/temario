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



# Ejemplo de uso:
origen = Torre()
destino = Torre()
auxiliar = Torre()



# Apilando discos en la torre de origen
for i in range(6, 0, -1):
    print("Se ha movido el disco", i)
    disco = Disco(i)
    origen.apilar(disco)


# Resolviendo la Torre de Hanoi
torres_hanoi(origen.obtener_altura(), origen, destino, auxiliar)


# Imprimiendo el resultado final
print("Torre de origen: ", origen.obtener_altura())
print("Torre auxiliar: ", auxiliar.obtener_altura())
print("Torre de destino: ", destino.obtener_altura())