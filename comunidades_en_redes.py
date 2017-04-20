from collections import defaultdict, deque ## diccionario con valor por default, cola optimizada

archivo = open("Archivos/Problema 3/d6.txt")
vertices = int(archivo.readline())
aristas = int(archivo.readline())
grafo = defaultdict(lambda : [[], []]) ## el valor por default son dos listas vacias (vecinos salientes, vecinos entrantes)

for _ in xrange(aristas):
    u, v = map(int, archivo.readline().split()) ## u -> v
    grafo[u][0].append(v) ## hay camino desde u hasta v
    grafo[v][1].append(u) ## hay camino hasta v desde u

def scc(grafo, vertices):
	## Devuelve la cantidad de componentes conexas
	## Utilizando el algoritmo de Kosaraju
    visitado = defaultdict(bool)
    L = deque([])
 
    def visitar(u):
        if not visitado[u]:
            visitado[u] = True
            for v in grafo[u][0]:
                visitar(v)
            L.appendleft(u)
 
    for u in xrange(1,vertices+1):
        visitar(u)
 
    asignado = defaultdict(lambda:-1)
 
    def asignar(u, raiz):
        if asignado[u] == -1:
            asignado[u] = raiz
            for v in grafo[u][1]:
                asignar(v, raiz)
    for u in L:
        asignar(u,u)

    return len(set(asignado[i] for i in xrange(vertices)))

print scc(grafo,vertices)