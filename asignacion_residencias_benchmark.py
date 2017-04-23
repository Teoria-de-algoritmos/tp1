import timeit

cantidad_iteraciones = 1
nombre_archivo_output = "problema1_benchmark_N1_M1.txt"

total_time = timeit.timeit(
stmt = "print residencias.obtener_resultados()",
setup = """from asignacion_de_residencias import Residencias;
estudiantes = 100;
hospitales = 100;
vacantes = 1;
residencias = Residencias(False, estudiantes, hospitales, vacantes)""", 
number = cantidad_iteraciones)

avg_time = total_time / cantidad_iteraciones
print avg_time

