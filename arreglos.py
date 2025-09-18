# EMIR ALBERTO PINO MALDONADO

import random
import time

random.seed(0)

alumnos = [[random.randint(50, 100) for _ in range(6)] for _ in range(500)]

start_time = time.time()

alumno_num = 321
materia_num = 6  

calificacion = alumnos[alumno_num - 1][materia_num - 1]

print(f"{'Alumno':<10}", end="")
for j in range(1, 7):
    print(f"Materia {j:<12}", end="")
print()


for i, califs in enumerate(alumnos, start=1):
    print(f"{i:<10}", end="")
    for cal in califs:
        print(f"{cal:<12}", end="")
    print()

end_time = time.time()

print(f"\nLa calificación del alumno No.{alumno_num} en la materia {materia_num}: {calificacion}")
print(f"Tiempo de ejecución: {end_time - start_time:.10f} segundos")
