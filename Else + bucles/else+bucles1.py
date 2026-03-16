#Tienes una lista de productos. Busca si "leche" está en la lista. Si la encuentras, imprime "Leche disponible" y para. Si recorres toda la lista sin encontrarla, imprime "Leche agotada"

productos = ["pan", "huevos", "arroz", "cafe", "azucar"]

for producto in productos:
    if producto == "leche": #nunca se cumple, leche no esta.
        print("Leche disponible")
        break #nunca se ejecuta
else:
    #el for termino sin break => else se ejecuta.
    print("Leche agotada")


