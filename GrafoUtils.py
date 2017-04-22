from collections import defaultdict    

def parse(clase, ruta_archivo):
    archivo = open(ruta_archivo)
    grafo = clase(int(archivo.readline())) 
    for _ in xrange(int(archivo.readline())):
        grafo.eje(*map(int, archivo.readline().split()))
    return grafo

class Digrafo():
    # Inicializador
	def __init__(self, vertices):
		self.V = vertices
		self.grafo = defaultdict(lambda:([],[])) #Diccionario default para almacenar el grafo como tuplas de dos listas
    # Funcion para agregar un elemento al grafo
	def eje(self, u, v):
	    self.grafo[u][0].append(v)
	    self.grafo[v][1].append(u)

	def vertices(self):
 		return self.V

	def vecinos(self, u):
	    for v in self.grafo[u][0]:
	        yield v
    
	def vecinos_entrantes(self, u):
	    for v in self.grafo[u][1]:
	        yield v
            
class Grafo(Digrafo):
    def eje(self, u, v):
    	Digrafo.eje(self, u, v)
    	Digrafo.eje(self, v, u)
