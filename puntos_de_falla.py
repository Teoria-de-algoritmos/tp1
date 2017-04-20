# Puntos de articulacion en un grafo no direccionado
  
from collections import defaultdict
  
#Clase grafo no direccionado usando una representacion de listas adyacentes
class Graph:
  
    # Inicializador
    def __init__(self,vertices):
        self.V = vertices               #Numero de vertices.
        self.graph = defaultdict(list)  #Diccionario default para almacenar el grafo
        self.Time = 0                   #Tiempo de encuentro
        self.ap_list = []           #Lista de puntos de articulacion del grafo
  
    # Funcion para agregar un elemento al grafo no direccionado
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
  

    # Funcion que encuentra puntos de articulacion utilizando DFS.
    def APUtil(self, u, visited, ap_flag, parent, low_time, discovery_time):
 
        children_quantity = 0           #Cantidad de hijos del nodo
        visited[u]= True                #Se avisa que se visito el nodo.
 
        discovery_time[u] = self.Time   #Inicializador del tiempo de descubrimiento
        low_time[u] = self.Time         #Inicializador del tiempo de baja
        self.Time += 1                  #Se incrementa en 1 el tiempo actual
 
        
        for v in self.graph[u]:         #Se recorren todos los vertices adyacentes

            if visited[v] == False :    #Si el vertice v no ha sido visitado
                
                parent[v] = u           #Se incide que es un hijo del vertice u en el arbol DFS
                children_quantity += 1  #Se incrementa en 1 la cantidad de hijos

                self.APUtil(v, visited, ap_flag, parent, low_time, discovery_time) #Llamada recursiva de la funcion
 
                low_time[u] = min(low_time[u], low_time[v])     #Chequea los ancestros del subarbol comparando los tiempos de baja minima
 
                # u es un punto de articulacion si se cumple los siguientes casos
                
                if parent[u] == -1 and children_quantity > 1:                   # (1) u es la raiz del arbol DFS y tiene al menos dos hijos.
                    
                    ap_flag[u] = True
 

                if parent[u] != -1 and low_time[v] >= discovery_time[u]:        #(2) Si el valor de baja de alguno de sus hijos es mayor al
                                                                                # tiempo de descubrimiento de u
                    ap_flag[u] = True   
                     
                 
            elif v != parent[u]:        #Si el vertice v ha sido visitado y no es el padre de u
                
                low_time[u] = min(low_time[u], discovery_time[v])
 
 
    #The function to do DFS traversal. It uses recursive APUtil()
    def AP(self):
  
        visited = [False] * (self.V)                #Lista de flags para saber si el elemento fue visitado o no
        discovery_time = [float("Inf")] * (self.V)  #Lista de tiempos de descubrimiento
        low_time = [float("Inf")] * (self.V)        #Lista de tiempos de baja
        parent = [-1] * (self.V)                    #Lista de padres
        ap_flag = [False] * (self.V)                #Lista de flags que determinan si es o no un punto de articulacion

        for i in xrange(self.V):                    #Se recorre la cantidad de elementos del grafo

            if not visited[i]:                      #Si el elemento no fue visitado, se llama la funcion

                self.APUtil(i, visited, ap_flag, parent, low_time, discovery_time)
 
        for index, value in enumerate (ap_flag):    #Se itera ern la lista de puntos de articulacion, analizando su indice y su estado

            if value: self.ap_list.append(index)    #Si es un punto de articulacion, se almacena en al lista de AP

    #Funcion que retorna una lista de puntos de articulacion
    def AP_list_get(self):
        self.AP()                                   #Se calcula los puntos de articulacion
        return self.ap_list


with open("Archivos/Problema 2/g1.txt","r") as file:               #Se abre el archivo en modo lectura

    print("Tamano del grafo: " + str(file.readline().strip()))  #Se imprime por pantalla la cantidad de vertices del grafo, o tamano del mismo
    
    graph = Graph(int(file.readline()))                 #Se lee almacena como entero el dato impreso previamente

    for line in file:                                   #Se itera en todas las lineas del archivo
       
        u, v = map(int, line.strip().split())           #Se separa cada linea leida en dos elementos, los cuales son convertidos a int.
        graph.addEdge(u, v)                             #Se agrega dicha arista o vertices conectados
    
    #Se cierra el archivo

#Se imprimen los puntos de articulacion calculados por la rutina del objeto graph
print("Puntos de articulacion: " + (str(graph.AP_list_get())))                       

