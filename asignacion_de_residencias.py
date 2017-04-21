from random import shuffle, choice ## Shuffle desordena una lista, no devuelve nada. Choice devuelve un elemento random de una lista
#from pprint import pprint ## Agarra una matriz y la imprime linda
import timeit
class Residencias:
    
    def mezclar_lista(self, l): ## Agarra una lista y la devuelve desordenada
        shuffle(l)
        return l
    
    def __init__(self, pedir_input):
        self.time = timeit.default_timer()
        #print self.time
        if pedir_input:
            self.students_quant = input("Ingresar la cantidad de estudiantes: ")
            self.hospitals_quant = input("Ingresar la cantidad de hospitales: ")
            self.vacancies_quant = input("Ingresar la cantidad de vacantes maxima: ")
        else :
            self.students_quant = 500
            self.hospitals_quant = 500
            self.vacancies_quant = 3
        
        ## Con students_quant = hospitals_quant = 100000 esto llena la ram y traba la maquina, ni se gasten
        ## El limite es students_quant * hospitals_quant <= 10**8
        self.E = [self.mezclar_lista(range(self.hospitals_quant)) for _ in xrange(self.students_quant)] ## Preferencias de cada estudiante
        self.H = [self.mezclar_lista(range(self.students_quant)) for _ in xrange(self.hospitals_quant)] ## Orden de merito
        self.Q = [choice(range(1,self.vacancies_quant+1)) for _ in xrange(self.hospitals_quant)] ## Cantidad de vacantes por hospital    
        #print("Preferencia de estudiantes:")                                                                          
        #pprint(E)
        #print("Orden de merito:")
        #pprint(H)
        #print("Cantidad de vacantes por hospital:")
        #print Q
        self.equivalencias = {}
        self.escribir_archivo("output_asignacion_de_residencias.txt")
        #print timeit.default_timer() - self.time
    def reducir(self):
        h = self.hospitals_quant
        for hosp in xrange(self.hospitals_quant):
            for _ in xrange(1, self.Q[hosp]):
                for s in xrange(self.students_quant):
                    self.E[s].insert(self.E[s].index(hosp), h)
                self.H.append(self.H[hosp])
                self.equivalencias[h] = hosp
                h += 1
        return (self.students_quant, h, self.E, self.H)
     
    def gale_shapley(self, hombres, mujeres, pref_hombre, pref_mujer):
        from collections import defaultdict
        prop_mujer = defaultdict(list)
        pareja_hombre = [-1] * hombres
        sig_prop_hombre = [0] * hombres
        while -1 in pareja_hombre:
            for h in xrange(hombres):
                if pareja_hombre[h] == -1:
                    prop_mujer[pref_hombre[h][sig_prop_hombre[h]]].append(h)
            for m in xrange(mujeres):
                props_m = prop_mujer[m]
                if props_m:
                    props_m.sort(key = lambda x : pref_mujer[m].index(x))
                    pareja_hombre[props_m[0]] = m
                    for i in xrange(1, len(props_m)):
                        pareja_hombre[props_m[i]] = -1
                        sig_prop_hombre[props_m[i]] += 1
                    prop_mujer[m] = [props_m[0]]
        #print timeit.default_timer()-self.time
        return [pref_hombre[i][sig_prop_hombre[i]] for i in xrange(hombres)]
    
    def obtener_resultados(self):
        resultado = self.gale_shapley(*self.reducir())
        for i in xrange(len(resultado)):
            if resultado[i] in self.equivalencias:
                resultado[i] = self.equivalencias[resultado[i]]
        return resultado
    
    def escribir_archivo(self, ruta):
        with open("output_asignacion_de_residencias.txt","w") as archivo: 
            archivo.write(str(self.students_quant) + "\n")
            for student in self.E:
                archivo.write("".join(str(pref) + " " for pref in student) + "\n")
            archivo.write(str(self.hospitals_quant) + "\n")
            for hosp in self.H:
                archivo.write("".join(str(merit) + " " for merit in hosp) + "\n")
            archivo.write("".join(str(vac) + " " for vac in self.Q) + "\n")
    
#r1 = Residencias(False)
#print r1.obtener_resultados()
