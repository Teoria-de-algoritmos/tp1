from GrafoUtils import Grafo, parse

##
## @brief      Class for tarjan.
##
class Tarjan:

    ##
    ## @brief      Construye el objeto.
    ##
    ## @param      self   El objeto
    ## @param      grafo  El grafo a analizar
    ##
    def __init__(self, grafo):
        visitado = [False] * (grafo.vertices())                
        tiempo_de_descubrimiento = [float("Inf")] * (grafo.vertices())  
        tiempo_de_baja = [float("Inf")] * (grafo.vertices())        
        padre = [-1] * (grafo.vertices())                  
        punto_articulacion = [False] * (grafo.vertices())              
        self.tiempo = 0                   #Tiempo de encuentro

        ##
        ## @brief      Visita un vertice y actualiza los tiempos
        ## @param      u     vertice
        ## @return     None
        ##
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
                                        
                    # u es un punto de articulacion si se cumple los siguientes casos:
                    #(1) u es la raiz del arbol DFS y tiene al menos dos hijos. 
                    #(2) Si el valor de baja de alguno de sus hijos es mayor al tiempo de descubrimiento de u    
                    #
                    if padre[u] == -1 and hijos > 1:               
                        punto_articulacion[u] = True

                    if padre[u] != -1 and tiempo_de_baja[v] >= tiempo_de_descubrimiento[u]:       
                        punto_articulacion[u] = True   
    
                elif v != padre[u]:        # Si el vertice v ha sido visitado y no es el padre de u
                    tiempo_de_baja[u] = min(tiempo_de_baja[u], tiempo_de_descubrimiento[v])
        
        for v in xrange(grafo.vertices()):                   
            
            if not visitado[v]:                    
                visitar(v)

        self.puntos_articulacion = [v for v in xrange(grafo.vertices()) if punto_articulacion[v]]
    
    ##
    ## @brief      Gets the puntos articulacion.
    ## @param      self  El objeto
    ## @return     Los puntos articulacion.
    ##
    def get_puntos_articulacion(self):
        return self.puntos_articulacion

# Ejemplo
from timeit import default_timer as timer

start = timer()

from sys import setrecursionlimit

setrecursionlimit(10000)

t1 = Tarjan(parse(Grafo, "Archivos/Problema 2/g5.txt"))    
print "Puntos de articulacion: " + "".join(str(v) + " " for v in t1.get_puntos_articulacion())

end = timer()

print(str((end - start)*1000)+" mseg")