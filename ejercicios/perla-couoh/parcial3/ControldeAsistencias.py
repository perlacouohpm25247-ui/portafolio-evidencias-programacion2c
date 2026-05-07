#Control de asistencias

#En una escuela se desea crear un pequeño sistema para registrar:
#1. Nombre de alumnos que asistieron a clases.
#2. Materias favoritas de cada alumno.

#Sin embargo algunos alumnos escribieron su nombre más de una vez por error.

#Tu tarea será organizar la información utilizando diferentes estructuras de datos.
# Datos de entrada: algunos nombres están repetidos por error
alumnos = ["Angel", "Emilio", "Andrea", "Angel", "Andrea", "Emilio"]

# 1. Usamos un SET para eliminar duplicados automáticamente, un set no permite elementos repetidos.
alumnos_presentes= set(alumnos)
print("1. Nombres de alumnos presentes:", alumnos_presentes)

# 2. Usamos un dict para guardar la materia favorita de cada alumno.
materias_favoritas = { "Angel": "Matemáticas", "Emilio": "Historia", "Andrea": "Programación" }

organizacion= []
for alumno in alumnos_presentes:
    materia = materias_favoritas.get(alumno, "No registrada") 
    organizacion.append((alumno, materia))

# 4. Mostramos el resultado organizado
print("\n2. Reporte final de asistencia y materias:")
for alumno, materia in organizacion:
    print(f"Alumno: {alumno} | Materia favorita: {materia}")