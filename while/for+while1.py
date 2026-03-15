#Situación A — ¿for o while?
#Tienes esta lista de notas y quieres imprimir solo las que sean mayores o iguales a 3.0:

notas = [4.5, 2.8, 3.0, 1.5, 4.0, 2.5, 3.7]

for nota in notas:
    if nota >= 3.0:
        print(f"Su nota es: {nota}")