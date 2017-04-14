from random import shuffle, choice ## Shuffle desordena una lista, no devuelve nada
## Choice devuelve un elemento random de una lista
from pprint import pprint ## Agarra una matriz y la imprime linda
## Agarra una lista y la devuelve desordenada
def shuffled_list(l):
    shuffle(l)
    return l

students_quant = input("Ingresar la cantidad de estudiantes: ")
hospitals_quant = input("Ingresar la cantidad de hospitales: ")
vacancies_quant = input("Ingresar la cantidad de vacantes maxima: ")

## Con students_quant = hospitals_quant = 100000 esto llena la ram y traba la maquina, ni se gasten
## El limite es students_quant * hospitals_quant <= 10**8
E = [shuffled_list(range(hospitals_quant)) for _ in xrange(students_quant)] ## Preferencias de cada estudiante
H = [shuffled_list(range(students_quant)) for _ in xrange(hospitals_quant)] ## Orden de merito
Q = [choice(range(1,vacancies_quant+1)) for _ in xrange(hospitals_quant)] ## Cantidad de vacantes por hospital
                                                                          ## 
print("Preferencia de estudiantes:")                                                                          
pprint(E)
print("Orden de merito:")
pprint(H)