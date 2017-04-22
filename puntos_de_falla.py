# Puntos de articulacion en un grafo no direccionado
from GrafoUtils import Grafo, parse

#Clase grafo no direccionado usando una representacion de listas adyacentes

##
## @brief      Class for tarjan.
##
class Tarjan:
    ##
    ## @brief      Constructs the object.
    ##
    ## @param      self   The object
    ## @param      graph  The graph
    ##
    def __init__(self, graph):

        visited_flags = [False] * (graph.vertices())                
        discovered_time = [float("Inf")] * (graph.vertices())  
        low_time = [float("Inf")] * (graph.vertices())        
        father_v = [-1] * (graph.vertices())                  
        ap_list = [False] * (graph.vertices())              
        self.appear_time = 0     
                                        
        ##
        ## @brief      Visit vertex and find articulation points
        ##
        ## @param      u     A vertex
        ##
        ## @return     None
        ##
        def visit_vertex(u):

            sons_quant = 0          
            visited_flags[u] = True                
            discovered_time[u] = self.appear_time   
            low_time[u] = self.appear_time         
            self.appear_time += 1  

            for v in graph.vecinos(u):                              #Se recorren todos los vertices adyacentes
                                               
                if not visited_flags[v] : 

                    father_v[v] = u                                 #Se incide que es un hijo del vertice u en el arbol DFS
                                                                    
                    sons_quant += 1                                 #Incrementa la cantidad de hijos

                    visit_vertex(v)                                 #Llamada recursiva de la funcion
                                                                    
                    low_time[u] = min(low_time[u], low_time[v])     #Chequea los ancestros del subarbol comparando los tiempos de baja minima
                    
                    # u es un punto de articulacion si se cumple los siguientes casos:
                    # 
                    #       (1) u es la raiz del arbol DFS y tiene al menos dos hijos. 
                    #
                    #       (2) Si el valor de baja de alguno de sus hijos es mayor al tiempo de descubrimiento de u    
                    #
                    if father_v[u] == -1 and sons_quant > 1:                      
                                                                                
                        ap_list[u] = True
                     
                    if father_v[u] != -1 and low_time[v] >= discovered_time[u]:

                        ap_list[u] = True   
    
                elif v != father_v[u]:                              #Si el vertice v ha sido visitado y no es el padre de u

                    low_time[u] = min(low_time[u], discovered_time[v])
        
        for v in xrange(graph.vertices()):  

            if not visited_flags[v]:    

                visit_vertex(v)

        self.ap_result = [v for v in xrange(graph.vertices()) if ap_list[v]]
    

    ##
    ## @brief      Gets the articulation points.
    ##
    ## @param      self  The object
    ##
    ## @return     The articulation points.
    ##
    def get_articulation_points(self):

        return self.ap_result



##---------------------------------------Example-----------------------------------------------


t1 = Tarjan(parse(Grafo, "Archivos/Problema 2/g1.txt"))    
print "Puntos de articulacion: " + "".join(str(v) + " " for v in t1.get_articulation_points())
print str(t1.get_articulation_points())