numeros = [1, 2, 3, 4, 5, 6]

for numero in numeros:
    if numero % 2 == 0: #si el numero es impar
        continue #salta esta vuelta, ve al siguiente.
    print(f"{numero} es impar") #esta linea solo se ejecuta si no hubo continue
    
#los pares 2, 4, 6 fueron ignorados, el continue salto su vuelta antes de llegar al print.