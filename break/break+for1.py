#Tienes una lista de estudiantes. Recórrela e imprime cada nombre, pero detente inmediatamente cuando encuentres a "Juan":

estudiantes = ["Ana", "Luis", "Maria", "Juan", "Pedro", "Sofia"]

for estudiante in estudiantes:
    if estudiante == "Juan":
        print("Estudiante encontrado, deteniendo busqueda")
        break
    print(f"Revisando: {estudiante}")