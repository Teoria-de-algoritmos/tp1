from collections import deque ## cola optimizada
from collections import defaultdict
from GrafoUtils import Digrafo, parse

class Kosaraju:
    
    def __init__(self, grafo):
        self.grafo = grafo
        self.componentes = defaultdict(list)
        self.componentes_fuertemente_conexas(self.grafo.vertices())
        
    def componentes_fuertemente_conexas(self, vertices):
        ## Devuelve la cantidad de componentes conexas
        ## Utilizando el algoritmo de Kosaraju
        visitado = [False] * vertices
        L = deque([])
     
        def visitar(u):
            if not visitado[u]:
                visitado[u] = True
                for v in self.grafo.vecinos_entrantes(u):
                    visitar(v)
                L.appendleft(u)
     
        for u in xrange(vertices):
            visitar(u)
     
        asignado = [-1] * vertices
     
        def asignar(u, raiz):
            if asignado[u] == -1:
                asignado[u] = raiz
                for v in self.grafo.vecinos(u):
                    asignar(v, raiz)
        for u in L:
            asignar(u,u)
        
        for i in xrange(vertices):
            self.componentes[asignado[i]].append(i)

    def cantidad_componentes(self):
        return len(self.componentes)
    
    def componente_dado_elemento(self, elemento):
        return self.componentes[self.asignado[elemento]]
    
k1 = Kosaraju(parse(Digrafo, "Archivos/Problema 3/d2.txt"))
print k1.cantidad_componentes()
