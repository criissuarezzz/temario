class Nodo:
    def __init__(self, freq, simbolo=None, izquierda=None, derecha=None):
        self.freq = freq
        self.simbolo = simbolo
        self.izquierda = izquierda
        self.derecha = derecha
        self.codigo = ''

    def __lt__(self, otro):
        return self.freq < otro.freq

    def es_hoja(self):
        return self.izquierda is None and self.derecha is None


def arbol_huffman(freq):
    nodos = [Nodo(freq[key], key) for key in freq]
    while len(nodos) > 1:
        nodos.sort()
        izquierda = nodos.pop(0)
        derecha = nodos.pop(0)
        nodo = Nodo(izquierda.freq + derecha.freq, izquierda.simbolo + derecha.simbolo, izquierda, derecha)
        nodos.append(nodo)
    raiz = nodos[0]
    
    codigos = {}
    def buscar_codigo(nodo, ruta):
        if nodo is not None:
            if nodo.es_hoja():
                codigos[nodo.simbolo] = ruta
            else:
                buscar_codigo(nodo.izquierda, ruta + "0")
                buscar_codigo(nodo.derecha, ruta + "1")

    buscar_codigo(raiz, "")
    
    tabla_frecuencias = {key: codigos[key] for key in freq}
    
    return raiz, tabla_frecuencias


def codificar(cadena, raiz):
    codigos = {}

    def buscar_codigo(nodo, ruta):
        if nodo is not None:
            if nodo.es_hoja():
                codigos[nodo.simbolo] = ruta
            else:
                buscar_codigo(nodo.izquierda, ruta + "0")
                buscar_codigo(nodo.derecha, ruta + "1")

    buscar_codigo(raiz, "")

    cadena_codificada = ""
    for caracter in cadena:
        cadena_codificada += codigos[caracter]
    return cadena_codificada


def decodificar(cadena_codificada, raiz):
    cadena_decodificada = ""
    nodo_actual = raiz

    for bit in cadena_codificada:
        if bit == '0':
            nodo_actual = nodo_actual.izquierda
        elif bit == '1':
            nodo_actual = nodo_actual.derecha

        if nodo_actual.es_hoja():
            cadena_decodificada += nodo_actual.simbolo
            nodo_actual = raiz

    return cadena_decodificada


if __name__ == "__main__":
    freq = {'a': 10, 'b': 2, 'c': 1, 'd': 4, 'e': 3, 'f': 5}
    raiz, tabla_codigos = arbol_huffman(freq)

    print("Tabla de códigos de cada clave:")
    for key in tabla_codigos:
        print(f"{key}: {tabla_codigos[key]}")

    cadena = "ababaefdceddfe"

    cadena_codificada = codificar(cadena, raiz)
    print("Cadena codificada con Huffman:", cadena_codificada)

    cadena_decodificada = decodificar(cadena_codificada, raiz)
    print("Cadena decodificada con Huffman:", cadena_decodificada)  

