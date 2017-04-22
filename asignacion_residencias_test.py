from asignacion_de_residencias import Residencias

def test (cant_estudiantes, pref_estudiantes,cant_hospitales, orden_merito, cant_vacantes, Q):
    residencias = Residencias(False, cant_estudiantes, cant_hospitales, cant_vacantes = cant_vacantes)
    residencias.E = pref_estudiantes
    residencias.H = orden_merito
    residencias.Q = Q
    resultado = residencias.obtener_resultados()
    return resultado
    
def check_result (obtenido, esperado, nombre_test="test"):
    if obtenido == esperado:
        print nombre_test, " correcto"
    else:
        print nombre_test, " fallido"
        
## Test 1
cant_vacantes = 1
cant_estudiantes = 5
cant_hospitales = 5
E = [[2, 1, 4, 3, 0], [0, 2, 3, 1, 4], [2, 3, 4, 1, 0], [1, 2, 0, 4, 3], [4, 0, 1, 2, 3]]
H = [[3, 4, 2, 1, 0], [0, 2, 3, 1, 4], [4, 1, 3, 0, 2], [0, 1, 2, 4, 3], [1, 2, 3, 0, 4]]
Q = [1, 1, 1, 1, 1]
solucion = [2, 0, 3, 1, 4]

result = test(cant_estudiantes, E, cant_hospitales,  H, cant_vacantes, Q)
check_result(result, solucion, "test 1")    

#Test 2 - test 1 con vacantes max 2, pero 1 en el hospital conflictivo
cant_vacantes = 2
cant_estudiantes = 5
cant_hospitales = 5
E = [[2, 1, 4, 3, 0], [0, 2, 3, 1, 4], [2, 3, 4, 1, 0], [1, 2, 0, 4, 3], [4, 0, 1, 2, 3]]
H = [[3, 4, 2, 1, 0], [0, 2, 3, 1, 4], [4, 1, 3, 0, 2], [0, 1, 2, 4, 3], [1, 2, 3, 0, 4]]
Q = [1, 2, 1, 2, 1]
solucion = [2, 0, 3, 1, 4]

result = test(cant_estudiantes, E, cant_hospitales,  H, cant_vacantes, Q)
check_result(result, solucion, "test 2")  

#Test 3 - N=M = 5 sin reestricciones de vacantes, todos van donde desean
cant_vacantes = 5
cant_estudiantes = 5
cant_hospitales = 5
E = [[2, 1, 4, 3, 0], [0, 2, 3, 1, 4], [2, 3, 4, 1, 0], [1, 2, 0, 4, 3], [4, 0, 1, 2, 3]]
H = [[3, 4, 2, 1, 0], [0, 2, 3, 1, 4], [4, 1, 3, 0, 2], [0, 1, 2, 4, 3], [1, 2, 3, 0, 4]]
Q = [5, 5, 5, 5, 5]
solucion = [2, 0, 2, 1, 4]

result = test(cant_estudiantes, E, cant_hospitales,  H, cant_vacantes, Q)
check_result(result, solucion, "test 3")  

#Test 4 - N=M = 10 con una sola vacante
cant_vacantes = 1
cant_estudiantes = 10
cant_hospitales = 10
E = [[8, 1, 5, 2, 7, 0, 9, 4, 6, 3], [5, 8, 0, 4, 1, 9, 7, 3, 2, 6], [3, 1, 0, 8, 2, 7, 4, 5, 6, 9], [5, 9, 1, 8, 7, 6, 2, 0, 3, 4], [7, 9, 2, 1, 0, 4, 8, 6, 3, 5], [1, 8, 9, 4, 7, 2, 6, 3, 0, 5], [2, 0, 5, 4, 1, 6, 7, 8, 3, 9], [5, 0, 3, 9, 2, 6, 1, 8, 4, 7], [2, 4, 7, 6, 9, 3, 1, 5, 8, 0], [4, 6, 5, 8, 0, 1, 3, 9, 2, 7]]
H = [[6, 5, 9, 3, 0, 8, 1, 7, 2, 4], [9, 0, 7, 5, 8, 4, 2, 6, 3, 1], [8, 3, 0, 2, 4, 5, 1, 9, 7, 6], [1, 3, 0, 8, 9, 4, 2, 6, 7, 5], [4, 3, 8, 9, 5, 0, 7, 2, 6, 1], [8, 9, 0, 2, 1, 4, 6, 7, 5, 3], [4, 0, 6, 7, 8, 1, 9, 5, 2, 3], [9, 6, 4, 3, 0, 8, 1, 7, 5, 2], [2, 8, 1, 7, 0, 3, 5, 6, 9, 4], [3, 5, 9, 2, 4, 8, 6, 1, 0, 7]]
Q = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
solucion = [8, 5, 3, 9, 7, 1, 0, 6, 2, 4]

result = test(cant_estudiantes, E, cant_hospitales,  H, cant_vacantes, Q)
check_result(result, solucion, "test 4")  

#Test 4 - N=M = 10 sin reestricciones de vacantes
cant_vacantes = 10
cant_estudiantes = 10
cant_hospitales = 10
E = [[8, 1, 5, 2, 7, 0, 9, 4, 6, 3], [5, 8, 0, 4, 1, 9, 7, 3, 2, 6], [3, 1, 0, 8, 2, 7, 4, 5, 6, 9], [5, 9, 1, 8, 7, 6, 2, 0, 3, 4], [7, 9, 2, 1, 0, 4, 8, 6, 3, 5], [1, 8, 9, 4, 7, 2, 6, 3, 0, 5], [2, 0, 5, 4, 1, 6, 7, 8, 3, 9], [5, 0, 3, 9, 2, 6, 1, 8, 4, 7], [2, 4, 7, 6, 9, 3, 1, 5, 8, 0], [4, 6, 5, 8, 0, 1, 3, 9, 2, 7]]
H = [[6, 5, 9, 3, 0, 8, 1, 7, 2, 4], [9, 0, 7, 5, 8, 4, 2, 6, 3, 1], [8, 3, 0, 2, 4, 5, 1, 9, 7, 6], [1, 3, 0, 8, 9, 4, 2, 6, 7, 5], [4, 3, 8, 9, 5, 0, 7, 2, 6, 1], [8, 9, 0, 2, 1, 4, 6, 7, 5, 3], [4, 0, 6, 7, 8, 1, 9, 5, 2, 3], [9, 6, 4, 3, 0, 8, 1, 7, 5, 2], [2, 8, 1, 7, 0, 3, 5, 6, 9, 4], [3, 5, 9, 2, 4, 8, 6, 1, 0, 7]]
Q = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
solucion = [8, 5, 3, 5, 7, 1, 2, 5, 2, 4]

result = test(cant_estudiantes, E, cant_hospitales,  H, cant_vacantes, Q)
check_result(result, solucion, "test 5")  