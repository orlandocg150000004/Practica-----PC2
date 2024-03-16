# Solicitar al usuario la cantidad de alumnos
num_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Crear una lista para almacenar los datos de los alumnos
alumnos = []

# Solicitar y almacenar los datos de cada alumno
for i in range(num_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} del alumno {nombre}: "))
        notas.append(nota)
    alumno = {"Alumno": nombre, "Notas": notas}
    alumnos.append(alumno)

# Mostrar el listado completo de alumnos
print("\nListado completo de alumnos:")
for alumno in alumnos:
    print(alumno)