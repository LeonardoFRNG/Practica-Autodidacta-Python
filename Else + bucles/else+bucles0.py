# #si juan no estuviera en la lista
# estudiantes = ["Ana", "Luis", "Maria", "Pedro"]

# #buscamos a juan en la lista

# for estudiante in estudiantes:
#     if estudiante == "Juan":
#         print("Estudiante encontrado!")
#         break #si lo encuentra para aqui
# else:
#         #solo llega aqui si el for termino sin ejecutar break
#         print("Juan no esta en la lista.")

#si juan estuviera en la lista
estudiantes = ["Ana", "Juan", "Maria"]
for estudiante in estudiantes:
    if estudiante == "Juan":
        print("Estudiante encontrado!")
        break
else:
    print("Juan no esta en la lista.")