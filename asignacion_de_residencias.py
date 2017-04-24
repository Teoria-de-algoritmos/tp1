from random import shuffle, choice ## Shuffle desordena una lista, no devuelve nada. Choice devuelve un elemento random de una lista
from collections import defaultdict
from timeit import default_timer as timer

class Residencias:
    
    def __init__(self, pedir_input=False, cant_estudiantes=100, cant_hospitales=100, cant_vacantes=1):
        self.resultado = []
        if pedir_input:
            self.estudiantes = input("Ingresar la cantidad de estudiantes: ")
            self.hospitales = input("Ingresar la cantidad de hospitales: ")
            self.vacantes = input("Ingresar la cantidad de vacantes maxima: ")
        else :
            self.estudiantes = cant_estudiantes
            self.hospitales = cant_hospitales
            self.vacantes = cant_vacantes
        self.E = [self.mezclar_lista(range(self.hospitales)) for _ in xrange(self.estudiantes)] ## Preferencias de cada estudiante
        self.H = [self.mezclar_lista(range(self.estudiantes)) for _ in xrange(self.hospitales)] ## Orden de merito
        self.Q = [choice(range(1,self.vacantes+1)) for _ in xrange(self.hospitales)] ## Cantidad de vacantes por hospital    
        self.equivalencias = {}
        self.escribir_archivo("output_asignacion_de_residencias.txt")

    def mezclar_lista(self, l): ## Agarra una lista y la devuelve desordenada
        shuffle(l)
        return l

    def preferencias_estudiantes(self):
        return self.E

    def orden_merito(self):
        return self.H

    def vacantes(self):
        return self.Q

    def reducir(self):
        from copy import deepcopy
        hombres = defaultdict(list)
        mujeres = deepcopy(self.H)
        dic_m = defaultdict(list)
        m_cant = self.hospitales
        for m in xrange(self.hospitales):
            dic_m[m].append(m)
            for _ in xrange(1, self.Q[m]):
                dic_m[m].append(m_cant)
                mujeres.append(mujeres[m])
                self.equivalencias[m_cant] = m
                m_cant += 1
        for h in xrange(self.estudiantes):
            for m in xrange(self.hospitales):
                hombres[h].extend(dic_m[self.E[h][m]])
        return (self.estudiantes, m_cant, [hombres[h] for h in xrange(self.estudiantes)], mujeres)
     
    def gale_shapley(self, hombres, mujeres, pref_hombre, pref_mujer):
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
        return [pref_hombre[i][sig_prop_hombre[i]] for i in xrange(hombres)]
    
    def obtener_resultados(self):
        self.resultado = self.gale_shapley(*self.reducir())
        for i in xrange(len(self.resultado)):
            if self.resultado[i] in self.equivalencias:
                self.resultado[i] = self.equivalencias[self.resultado[i]]
        return self.resultado
    
    def escribir_archivo(self, ruta):
        with open("output_asignacion_de_residencias.txt","w") as archivo: 
            archivo.write(str(self.estudiantes) + "\n")
            for estudiante in self.E:
                archivo.write("".join(str(pref) + " " for pref in estudiante) + "\n")
            archivo.write(str(self.hospitales) + "\n")
            for hospital in self.H:
                archivo.write("".join(str(merito) + " " for merito in hospital) + "\n")
            archivo.write("".join(str(vac) + " " for vac in self.Q) + "\n")

from sys import setrecursionlimit

setrecursionlimit(10000)

start = timer()
residencias = Residencias(True)
print '\nResultado: ', residencias.obtener_resultados()
end = timer()
print("Tiempo de ejecucion: "+str((end - start)*1000.0)+" mseg")

is_curious = raw_input("\nDesea ver los valores relacionados al resultado generado? (Y/N)")

if is_curious == 'Y' or is_curious == 'y':
    print '\nValores relacionados al resultado anterior:\n'
    print 'Preferencia de cada estudiante: ', residencias.E
    print 'Orden de Merito: ', residencias.H
    print 'Vacantes por hospital: ', residencias.Q
