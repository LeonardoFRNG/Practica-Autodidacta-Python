# **Situación B — ¿`for` o `while`?**
# Un cajero automático permite intentar la clave **máximo 3 veces**. Simula eso imprimiendo:
# ```
# Intento 1 de 3
# Intento 2 de 3
# Intento 3 de 3
# Acceso bloqueado

clave = 1

while clave <= 3:
    print(f"Intento {clave} de 3")
    clave += 1
print("Acceso bloqueado")