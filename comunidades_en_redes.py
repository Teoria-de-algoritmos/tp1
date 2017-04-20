from collections import defaultdict, deque ## diccionario con valor por default, cola optimizada
from GrafoUtils import Digrafo

grafo = Digrafo.parse("Archivos/Problema 3/d3.txt")
    
def componentes_fuertemente_conexas(grafo, vertices):
    ## Devuelve la cantidad de componentes conexas
    ## Utilizando el algoritmo de Kosaraju
    visitado = defaultdict(bool)
    L = deque([])
 
    def visitar(u):
        if not visitado[u]:
            visitado[u] = True
            for v in grafo.vecinos_entrantes(u):
                visitar(v)
            L.appendleft(u)
 
    for u in xrange(vertices):
        visitar(u)
 
    asignado = defaultdict(lambda:-1)
 
    def asignar(u, raiz):
        if asignado[u] == -1:
            asignado[u] = raiz
            for v in grafo.vecinos_salientes(u):
                asignar(v, raiz)
    for u in L:
        asignar(u,u)

    return len(set(asignado[i] for i in xrange(vertices)))

print componentes_fuertemente_conexas(grafo, grafo.vertices())