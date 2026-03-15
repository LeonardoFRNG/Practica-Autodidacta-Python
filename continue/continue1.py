#Tienes una lista de notas. Imprime solo las notas aprobadas (>= 3.0), saltando las reprobadas con continue:

notas = [4.5, 2.8, 3.0, 1.5, 4.0, 2.5, 3.7]

for nota in notas:
    if nota < 3:
        continue
    print(f"Nota arobada: {nota}")