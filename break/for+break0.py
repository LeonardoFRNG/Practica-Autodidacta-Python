numeros = [3, 7, 1, 9, 4, 6]

for numero in numeros:
    #si encontramos el 9, no necesitamos seguir.
    if numero == 9:
        break #sale del bucle inmediatamente
print(f"Encontre el:  {numero}!")

#No se va a imprimir el 4 ni el 6.
