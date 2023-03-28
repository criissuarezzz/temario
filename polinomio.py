#explicado:
class datoPolinomio:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente

class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class Polinomio:
    def __init__(self):
        self.termino_mayor=None
        self.grado=-1

    def agregar_termino(self, coeficiente, exponente):
        if self.grado < exponente:
            self.grado = exponente
        if self.termino_mayor is None:
            self.termino_mayor = Nodo(datoPolinomio(coeficiente, exponente))
        else:
            self.termino_mayor = Nodo(datoPolinomio(coeficiente, exponente), self.termino_mayor)

    def mostrar(self):
        if self.termino_mayor is None:
            print("Polinomio vacio")
        else:
            aux = self.termino_mayor
            while aux is not None:
                print(aux.dato.coeficiente, "x^", aux.dato.exponente, end=" ")
                aux = aux.siguiente
            print()

    def evaluar(self, x):
        if self.termino_mayor is None:
            print("Polinomio vacio")
        else:
            aux = self.termino_mayor
            resultado = 0
            while aux is not None:
                resultado += aux.dato.coeficiente * (x**aux.dato.exponente)
                aux = aux.siguiente
            return resultado
        
    
    def sumar(self, otro):
        if self.grado < otro.grado:
            self.grado = otro.grado
        if self.termino_mayor is None:
            self.termino_mayor = otro.termino_mayor
        else:
            aux = self.termino_mayor
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = otro.termino_mayor
    def multiplicar(self, otro):
        if self.grado < otro.grado:
            self.grado = otro.grado
        if self.termino_mayor is None:
            self.termino_mayor = otro.termino_mayor
        else:
            aux = self.termino_mayor
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = otro.termino_mayor
