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
        asignado = [-1] * vertices
     
        def visitar(u):                                     #recorrido DFS
            if not visitado[u]:                             #si no esta visitado el vertice
                visitado[u] = True                          #se lo marca como visitado
                for v in self.grafo.vecinos(u):   #se visitan sus hijos
                    visitar(v)
                L.appendleft(u)                             #al terminar se lo agrega al stack por tiempo de finalizacion
     
        def asignar(u, raiz):                               
            if asignado[u] == -1:                           #si el elemento no esta asignado
                asignado[u] = raiz                          #se lo define como la raiz
                for v in self.grafo.vecinos_entrantes(u):             #recorremos los hijos del elemento u
                    asignar(v, raiz)                        #se llama a asignar a dicho hijo v

        for u in xrange(vertices):                          #visitamos los elementos del grafo ordenando los elementos
            visitar(u)                                      #en el stack por tiempo de finalizacion
            
     
        for u in L:                                         #recorremos el grafo comenzando en orden de pop() del stack         
            asignar(u,u)
        
        for i in xrange(vertices):                          #para todo elemento del grafo
            self.componentes[asignado[i]].append(i)         #se crea un diccionario agrupando los elem. por componentes
                                                            #fuertemente conexas

    def cantidad_componentes(self):
        return len(self.componentes)
    
    def componente_dado_elemento(self, elemento):
        return self.componentes[self.asignado[elemento]]

# Ejemplo
from timeit import default_timer as timer

nombre_archivo = raw_input("Ingrese la ruta del archivo de Input")

start = timer()
k1 = Kosaraju(parse(Digrafo, nombre_archivo))
end = timer()

print k1.cantidad_componentes()

print("Vertices: "+str(k1.grafo.vertices()))
print("Tiempo: "+str((end - start)*1000)+" mseg")
