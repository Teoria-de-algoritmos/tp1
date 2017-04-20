# Puntos de articulacion en un grafo no direccionado
from GrafoUtils import Grafo

grafo = Grafo.parse("Archivos/Problema 2/g1.txt")
tiempo = 0                   #Tiempo de encuentro
puntos_articulacion = []           #Lista de puntos de articulacion del grafo


def puntos_de_articulacion(grafo):
    visitado = [False] * (grafo.vertices())                #Lista de flags para saber si el elemento fue visitado o no
    tiempo_de_descubrimiento = [float("Inf")] * (grafo.vertices())  #Lista de tiempos de descubrimiento
    tiempo_de_baja = [float("Inf")] * (grafo.vertices())        #Lista de tiempos de baja
    padre = [-1] * (grafo.vertices())                    #Lista de padres
    ap_flag = [False] * (grafo.vertices())                #Lista de flags que determinan si es o no un punto de articulacion

    # Funcion que encuentra puntos de articulacion utilizando DFS.
    def visitar(u):
        hijos = 0          
        visitado[u] = True                
        tiempo_de_descubrimiento[u] = tiempo   
        tiempo_de_baja[u] = tiempo         
        tiempo += 1                 
        for v in grafo[u]:         #Se recorren todos los vertices adyacentes
            if not visitado[v] :    
                padre[v] = u           #Se incide que es un hijo del vertice u en el arbol DFS
                hijos += 1  
                visitar(v) #Llamada recursiva de la funcion
                tiempo_de_baja[u] = min(tiempo_de_baja[u], tiempo_de_baja[v])     #Chequea los ancestros del subarbol comparando los tiempos de baja minima
                # u es un punto de articulacion si se cumple los siguientes casos
                if padre[u] == -1 and hijos > 1:                   # (1) u es la raiz del arbol DFS y tiene al menos dos hijos.       
                    ap_flag[u] = True
                 #(2) Si el valor de baja de alguno de sus hijos es mayor al tiempo de descubrimiento de u
                if padre[u] != -1 and tiempo_de_baja[v] >= tiempo_de_descubrimiento[u]:       
                    ap_flag[u] = True   

            elif v != padre[u]:        #Si el vertice v ha sido visitado y no es el padre de u
                tiempo_de_baja[u] = min(tiempo_de_baja[u], tiempo_de_descubrimiento[v])
    
    
    for i in xrange(grafo.vertices()):                    #Se recorre la cantidad de elementos del grafo
        if not visitado[i]:                      #Si el elemento no fue visitado, se llama la funcion
            visitar(i)

    for indice, valor in enumerate (ap_flag):    #Se itera en la lista de puntos de articulacion, analizando su indice y su estado
        if valor: puntos_articulacion.append(indice)    #Si es un punto de articulacion, se almacena en al lista de AP
    
    return puntos_articulacion
  
print("Puntos de articulacion: " + str(puntos_de_articulacion(grafo)))   
