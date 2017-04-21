import timeit
from random import shuffle, choice ## Shuffle desordena una lista, no devuelve nada. Choice devuelve un elemento random de una lista
from pprint import pprint ## Agarra una matriz y la imprime linda

def shuffled_list(l): ## Agarra una lista y la devuelve desordenada
    shuffle(l)
    return l
pedir_input = True
if pedir_input:
    students_quant = input("Ingresar la cantidad de estudiantes: ")
    hospitals_quant = input("Ingresar la cantidad de hospitales: ")
    vacancies_quant = input("Ingresar la cantidad de vacantes maxima: ")
else :
    students_quant = 5
    hospitals_quant = 5
    vacancies_quant = 3

## Con students_quant = hospitals_quant = 100000 esto llena la ram y traba la maquina, ni se gasten
## El limite es students_quant * hospitals_quant <= 10**8
E = [shuffled_list(range(hospitals_quant)) for _ in xrange(students_quant)] ## Preferencias de cada estudiante
H = [shuffled_list(range(students_quant)) for _ in xrange(hospitals_quant)] ## Orden de merito
Q = [choice(range(1,vacancies_quant+1)) for _ in xrange(hospitals_quant)] ## Cantidad de vacantes por hospital
                                                                          ## 
print("Preferencia de estudiantes:")                                                                          
print(E)
print("Orden de merito:")
print(H)
print("Cantidad de vacantes por hospital:")
print Q
 
def gale_shapley():
    from collections import defaultdict
    hospitals = defaultdict(list)
    engaged = [False] * students_quant
    students = [0] * students_quant
    while False in engaged:
        print engaged
        print hospitals
        for stud in xrange(students_quant):
            if not engaged[stud]:
                hospitals[E[stud][students[stud]]].append(stud)
        for hosp in xrange(hospitals_quant):
            hosp_props = hospitals[hosp]
            hosp_props.sort(key = lambda x : H[hosp].index(x))
            for i in xrange(min(Q[hosp],len(hosp_props))):
                engaged[hosp_props[i]] = True
            for i in xrange(Q[hosp], len(hosp_props)):
                students[hosp_props[i]] += 1
            hosp_props = hosp_props[:min(len(hosp_props),Q[hosp])]
    return [(i, E[i][students[i]]) for i in xrange(students_quant)]

startTime = timeit.default_timer() ## tiempo en que empieza ejecutar gale_shapley

print gale_shapley()

elapsedTime = timeit.default_timer() - startTime

print 'execution time = ', elapsedTime, 'ms'

with open("output_asignacion_de_residencias.txt","w") as file: 

    file.write(str(students_quant) + "\n")

    for student in E:
        file.write("".join(str(pref) + " " for pref in student) + "\n")

    file.write(str(hospitals_quant) + "\n")

    for hosp in H:
        file.write("".join(str(merit) + " " for merit in hosp) + "\n")

    file.write("".join(str(vac) + " " for vac in Q) + "\n")
