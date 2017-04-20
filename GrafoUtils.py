from collections import defaultdict
#Clase grafo direccionado usando una representacion de listas adyacentes   
class Digrafo:
    # Inicializador
    def __init__(self, vertices):
        self.V = vertices #Numero de vertices.
        self.grafo = defaultdict(lambda:([],[])) #Diccionario default para almacenar el grafo como tuplas de dos listas
    # Funcion para agregar un elemento al grafo direccionado
    def eje(self, u, v):
        self.grafo[u][0].append(v)
        self.grafo[v][1].append(u)
    
    def vertices(self):
        return self.V
    
    def vecinos_salientes(self, u):
        for v in self.grafo[u][0]:
            yield v
    
    def vecinos_entrantes(self, u):
        for v in self.grafo[u][1]:
            yield v
    @classmethod        
    def parse(self, ruta_archivo):
        archivo = open(ruta_archivo)
        grafo = Digrafo(int(archivo.readline())) 
        for a in xrange(int(archivo.readline())):
            u, v = map(int, archivo.readline().split())
            grafo.eje(u, v)
        return grafo
            
#Clase grafo no direccionado usando una representacion de listas adyacentes            
class Grafo:
    # Inicializador
    def __init__(self, vertices):
        self.V = vertices #Numero de vertices.
        self.grafo = defaultdict(list) #Diccionario default para almacenar el grafo
    # Funcion para agregar un elemento al grafo no direccionado
    def eje(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)
    
    def vertices(self):
        return self.V

    def vecinos(self, u):
        for v in self.grafo[u]:
            yield v
            
    @classmethod        
    def parse(self, ruta_archivo):
        archivo = open(ruta_archivo)
        grafo = Grafo(int(archivo.readline()))
        for a in xrange(int(archivo.readline())):
            u, v = map(int, archivo.readline().split())
            grafo.eje(u, v)
        return grafo