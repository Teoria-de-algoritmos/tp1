from random import shuffle, choice ## Shuffle desordena una lista, no devuelve nada
## Choice devuelve un elemento random de una lista
from pprint import pprint ## Agarra una matriz y la imprime linda
## Agarra una lista y la devuelve desordenada
def shuffled_list(l):
    shuffle(l)
    return l
n, m = 10, 2 ## n = estudiantes, m = hospitales
v = 3 ## Maxima cantidad de vacantes
## Con n = m = 100000 esto llena la ram y traba la maquina, ni se gasten
## El limite es n*m <= 10**8
E = [shuffled_list(range(m)) for _ in xrange(n)] ## Preferencias de cada estudiante
H = [shuffled_list(range(n)) for _ in xrange(m)] ## Orden de merito
Q = [choice(range(1,v+1)) for _ in xrange(m)] ## Cantidad de vacantes por hospital
pprint(E)
pprint(H)