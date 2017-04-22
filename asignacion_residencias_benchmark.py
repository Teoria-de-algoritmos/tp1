import timeit

cantidad_iteraciones = 1
nombre_archivo_output = "problema1_benchmark_N1_M1.txt"

total_time = timeit.timeit(
stmt = "print residencias.obtener_resultados()",
setup = """from asignacion_de_residencias import Residencias;
estudiantes = 10;
hospitales = 10;
vacantes = 1;
residencias = Residencias(False, estudiantes, hospitales, vacantes)""", 
number = cantidad_iteraciones)

avg_time = total_time / cantidad_iteraciones
print avg_time

with open(nombre_archivo_output,"w") as archivo: 
    archivo.write("Tiempo de ejecucion con N = 1 y M = 1 --> " + str(avg_time) + " segundos \n")
