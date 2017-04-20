# Puntos de articulacion en un grafo no direccionado
  

from GrafoUtils import Grafo

grafo = Grafo.parse("Archivos/Problema 2/g1.txt")

tiempo = 0                   #Tiempo de encuentro
puntos_articulacion = []           #Lista de puntos de articulacion del grafo

# Funcion que encuentra puntos de articulacion utilizando DFS.
def visitar(u, visitado, ap_flag, padre, tiempo_de_baja, tiempo_de_descubrimiento):

    hijos = 0           #Cantidad de hijos del nodo
    visitado[u] = True                #Se avisa que se visito el nodo.

    tiempo_de_descubrimiento[u] = tiempo   #Inicializador del tiempo de descubrimiento
    tiempo_de_baja[u] = tiempo         #Inicializador del tiempo de baja
    tiempo += 1                  #Se incrementa en 1 el tiempo actual
    
    for v in grafo[u]:         #Se recorren todos los vertices adyacentes
        if not visitado[v] :    #Si el vertice v no ha sido visitado
            padre[v] = u           #Se incide que es un hijo del vertice u en el arbol DFS
            hijos += 1  #Se incrementa en 1 la cantidad de hijos
            visitar(v, visitado, ap_flag, padre, tiempo_de_baja, tiempo_de_descubrimiento) #Llamada recursiva de la funcion
            tiempo_de_baja[u] = min(tiempo_de_baja[u], tiempo_de_baja[v])     #Chequea los ancestros del subarbol comparando los tiempos de baja minima

            # u es un punto de articulacion si se cumple los siguientes casos
            
            if padre[u] == -1 and hijos > 1:                   # (1) u es la raiz del arbol DFS y tiene al menos dos hijos.
                
                ap_flag[u] = True


            if padre[u] != -1 and tiempo_de_baja[v] >= tiempo_de_descubrimiento[u]:        #(2) Si el valor de baja de alguno de sus hijos es mayor al
                                                                            # tiempo de descubrimiento de u
                ap_flag[u] = True   
                 
             
        elif v != padre[u]:        #Si el vertice v ha sido visitado y no es el padre de u
            
            tiempo_de_baja[u] = min(tiempo_de_baja[u], tiempo_de_descubrimiento[v])


#The function to do DFS traversal. It uses recursive APUtil()
def AP(grafo):
    visitado = [False] * (grafo.vertices())                #Lista de flags para saber si el elemento fue visitado o no
    tiempo_de_descubrimiento = [float("Inf")] * (grafo.vertices())  #Lista de tiempos de descubrimiento
    tiempo_de_baja = [float("Inf")] * (grafo.vertices())        #Lista de tiempos de baja
    padre = [-1] * (grafo.vertices())                    #Lista de padres
    ap_flag = [False] * (grafo.vertices())                #Lista de flags que determinan si es o no un punto de articulacion

    for i in xrange(grafo.vertices()):                    #Se recorre la cantidad de elementos del grafo
        if not visitado[i]:                      #Si el elemento no fue visitado, se llama la funcion
            visitar(i, visitado, ap_flag, padre, tiempo_de_baja, tiempo_de_descubrimiento)

    for indice, valor in enumerate (ap_flag):    #Se itera ern la lista de puntos de articulacion, analizando su indice y su estado
        if valor: puntos_articulacion.append(indice)    #Si es un punto de articulacion, se almacena en al lista de AP

#Funcion que retorna una lista de puntos de articulacion
def puntos_de_articulacion(grafo):
    AP(grafo)                                   #Se calcula los puntos de articulacion
    return puntos_articulacion

#Se imprimen los puntos de articulacion calculados por la rutina del objeto graph
print("Puntos de articulacion: " + str(puntos_de_articulacion(grafo)))   