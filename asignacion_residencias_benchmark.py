import timeit

cantidad_iteraciones = 1

execution_time = timeit.timeit(
stmt = "residencias.obtener_resultados()",
setup = """from asignacion_de_residencias import Residencias;
estudiantes = 1000;
hospitales = 1000;
vacantes = 3;
residencias = Residencias(False, estudiantes, hospitales, vacantes)""", 
number = cantidad_iteraciones)

print execution_time / cantidad_iteraciones

## N = M = 1, Vac = 3 --> 9.88594366876e-06 sec, 1000000 iteraciones
## N = M = 10, Vac = 3 --> 0.000229955009812 sec, 10000 iteraciones
## N = M = 100, Vac = 3 --> 0.0936539185934 sec, 50 iteraciones
## N = M = 1000, Vac = 3 --> 0.0936539185934 sec, 50 iteraciones
