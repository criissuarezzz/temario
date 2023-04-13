class nodoArbol(object):
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None
        self.altura = 1

class ArbolAVL(object):
    def altura(raiz):
        if raiz is None:
            return 0
        return raiz.altura
    
    def actualizaraltura(raiz):
        if raiz is not None:
            alt_izq=ArbolAVL.altura(raiz.izq)
            alt_der=ArbolAVL.altura(raiz.der)
            raiz.altura=max(alt_izq if alt_izq > alt_der else alt_der)+1

    def rotar_simple(raiz, control):
        if control:   #control significa que es rotacion izquierda
            aux = raiz.izq
            raiz.izq = aux.der
            aux.der = raiz
        else:
            aux = raiz.der
            raiz.der = aux.izq
            aux.izq = raiz
        ArbolAVL.actualizaraltura(raiz)
        ArbolAVL.actualizaraltura(aux)
        raiz=aux
        return raiz
    
    def rotar_doble(raiz, control):
        if control:
            raiz.izq=ArbolAVL.rotar_simple(raiz.izq, False)
            raiz=ArbolAVL.rotar_simple(raiz, True)
        else:
            raiz.der=ArbolAVL.rotar_simple(raiz.der, True)
            raiz=ArbolAVL.rotar_simple(raiz, False)

    def balancear(raiz):
        if raiz is not None:
            alt_izq=ArbolAVL.altura(raiz.izq)
            alt_der=ArbolAVL.altura(raiz.der)
            if alt_izq-alt_der>1:
                if ArbolAVL.altura(raiz.izq.izq) > ArbolAVL.altura(raiz.izq.der):
                    raiz=ArbolAVL.rotar_simple(raiz, True)
                else:
                    raiz=ArbolAVL.rotar_doble(raiz, True)
            elif alt_der-alt_izq>1:
                if ArbolAVL.altura(raiz.der.der) > ArbolAVL.altura(raiz.der.izq):
                    raiz=ArbolAVL.rotar_simple(raiz, False)
                else:
                    raiz=ArbolAVL.rotar_doble(raiz, False)
        return raiz
    
    def insertar_nodo(raiz, dato, pos):
        if raiz is None:
            raiz = nodoArbol(dato)
        elif dato < raiz.info:
            raiz.izq = ArbolAVL.insertar_nodo(raiz.izq, dato, pos)
        elif dato > raiz.info:
            raiz.der= ArbolAVL.insertar_nodo(raiz.der, dato, pos)        
        ArbolAVL.actualizaraltura(raiz)
        raiz=ArbolAVL.balancear(raiz)
        return raiz
    
    def eliminar_nodo(raiz, clave):
        x= None
        if raiz is not None:
            if clave < raiz.info:
                raiz.izq, x = ArbolAVL.eliminar_nodo(raiz.izq, clave)
            elif clave > raiz.info:
                raiz.der, x = ArbolAVL.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if raiz.izq is None:
                    raiz = raiz.der
                elif raiz.der is None:
                    raiz = raiz.izq
                else:
                    x=raiz.info
                    if raiz.izq is None:
                        raiz=raiz.der
                    elif raiz.der is None:
                        raiz=raiz.izq
                    else:
                        raiz.izq, aux=ArbolAVL.remplazar(raiz.izq)
                        raiz.info, raiz.nrr =aux.info, aux.nrr
                raiz=ArbolAVL.balancear(raiz)
                ArbolAVL.actualizaraltura(raiz)
        return raiz, x
    
    def remplazar(raiz):
        if raiz.der is not None:
            raiz.der, aux = ArbolAVL.remplazar(raiz.der)
        else:
            aux = raiz
            raiz = raiz.izq
        return raiz, aux
    


            
