"""
La mecánica de funcionamiento de los algoritmos voraces es en pasos. En cada paso se toma una
decisión que parece ser buena sin considerar las consecuencias futuras es decir se selecciona el
que se considera en ese momento el mejor candidato del conjunto de candidatos, esto significa
que se elige un óptimo local. Cuando el algoritmo termina de ejecutarse, se espera que el óptimo
local sea igual al óptimo global, de no ser así habremos hallado una solución subóptima,es decir,
una solución factible. El nombre voraz proviene de la estrategia de “tomar lo que sea mejor ahora”
en cada etapa.
"""

def seleccion_actividades(actividades):
    """Implementación del algoritmo voraz de selección de actividades."""
    actividades.sort(key=lambda x: x[1])  # Ordena las actividades por tiempo de finalización
    seleccionadas = [actividades[0]]  # Selecciona la primera actividad
    for i in range(1, len(actividades)):
        if actividades[i][0] >= seleccionadas[-1][1]:  # Si la actividad actual no se solapa con la última seleccionada
            seleccionadas.append(actividades[i])  # La selecciona
    return seleccionadas


"""
Básicamente estos algoritmos están compuestos por los siguientes elementos:
Conjunto de candidatos que almacena todos los elementos que pueden formar parte de la solución;
Conjunto solución, inicialmente está vacío y en cada paso del algoritmo se intenta agregar “el mejor
elemento del conjunto de candidatos” basado en alguna función de optimización denominada función de selección;
Función de selección del mejor candidato, se encarga de determinar cuál es el elemento más prometedor del conjunto de candidatos en cada etapa del algoritmo;
[239]
Función de factibilidad, se utiliza para determinar si un elemento candidato elegido por la función de
selección es factible para formar parte de la solución. Si es factible dicho elemento, se agrega al conjunto solución y permanecerá siempre en él, caso contrario es descartado y no vuelve a ser considerado;
Función solución, su objetivo es determinar si los elementos en el conjunto solución son una solución factible del problema o no, independientemente de que sea la óptima o no.
"""



def es_solucion(solucion, valor_devolver):
    total=0
    for moneda in solucion:
        total=round(total+(moneda[0]*moneda[1]),2) #redondeamos a 2 decimales 
    if total==valor_devolver:
        return True
    else:
        return False

def cambio(monedas, valor_devolver):
    solucion=[]
    monedas.sort(reverse=True) #ordenamos de mayor a menor
    for moneda in monedas:
        if moneda<=valor_devolver:
            cantidad=valor_devolver//moneda
            solucion.append((cantidad, moneda))
            valor_devolver=valor_devolver%moneda
        if es_solucion(solucion, valor_devolver):
            return solucion
    return solucion
    
monedas = [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2]
vuelto=cambio(monedas, 3.81)


if __name__=='__main__':
    actividades = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    print("Las actividades seleccionadas son:"+str(actividades), "donde el primer elemento es el tiempo de inicio y el segundo el tiempo de finalización")
    print(seleccion_actividades(actividades))
    """
    El algoritmo primero ordena las actividades por hora de finalización
    y luego itera por ellas, seleccionando cada actividad que no se solape 
    con la última seleccionada (es decir, que tenga una hora de inicio 
    mayor o igual a la hora de finalización de la última actividad 
    seleccionada). El resultado es una lista de actividades seleccionadas 
    que no se solapan y que se espera que maximicen el número total de actividades 
    realizadas.
"""

