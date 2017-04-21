# Puntos de articulacion en un grafo no direccionado
from GrafoUtils import Grafo

class Tarjan:
    def __init__(self, ruta):
        grafo = Grafo.parse(ruta)
        visitado = [False] * (grafo.vertices())                #Lista de flags para saber si el elemento fue visitado o no
        tiempo_de_descubrimiento = [float("Inf")] * (grafo.vertices())  #Lista de tiempos de descubrimiento
        tiempo_de_baja = [float("Inf")] * (grafo.vertices())        #Lista de tiempos de baja
        padre = [-1] * (grafo.vertices())                    #Lista de padres
        punto_articulacion = [False] * (grafo.vertices())                #Lista de flags que determinan si es o no un punto de articulacion
        self.tiempo = 0                   #Tiempo de encuentro
        # Funcion que encuentra puntos de articulacion utilizando DFS.
        def visitar(u):
            hijos = 0          
            visitado[u] = True                
            tiempo_de_descubrimiento[u] = self.tiempo   
            tiempo_de_baja[u] = self.tiempo         
            self.tiempo += 1                 
            for v in grafo.vecinos(u):         #Se recorren todos los vertices adyacentes
                if not visitado[v] :    
                    padre[v] = u           #Se incide que es un hijo del vertice u en el arbol DFS
                    hijos += 1  
                    visitar(v) #Llamada recursiva de la funcion
                    tiempo_de_baja[u] = min(tiempo_de_baja[u], tiempo_de_baja[v])     #Chequea los ancestros del subarbol comparando los tiempos de baja minima
                    # u es un punto de articulacion si se cumple los siguientes casos
                    if padre[u] == -1 and hijos > 1:                   # (1) u es la raiz del arbol DFS y tiene al menos dos hijos.       
                        punto_articulacion[u] = True
                     #(2) Si el valor de baja de alguno de sus hijos es mayor al tiempo de descubrimiento de u
                    if padre[u] != -1 and tiempo_de_baja[v] >= tiempo_de_descubrimiento[u]:       
                        punto_articulacion[u] = True   
    
                elif v != padre[u]:        #Si el vertice v ha sido visitado y no es el padre de u
                    tiempo_de_baja[u] = min(tiempo_de_baja[u], tiempo_de_descubrimiento[v])
        
        for i in xrange(grafo.vertices()):                    #Se recorre la cantidad de elementos del grafo
            if not visitado[i]:                      #Si el elemento no fue visitado, se llama la funcion
                visitar(i)
        #Lista de puntos de articulacion del grafo        
        #Se itera en la lista de puntos de articulacion, analizando su indice y su estado
        #Si es un punto de articulacion, se almacena en al lista de AP
        self.puntos_articulacion = [indice for indice in xrange(grafo.vertices()) if punto_articulacion[indice]]
    
    def get_puntos_articulacion(self):
        return self.puntos_articulacion

t1 = Tarjan("Archivos/Problema 2/g1.txt")    

print "Puntos de articulacion: " + "".join(str(x) + " " for x in t1.get_puntos_articulacion())
