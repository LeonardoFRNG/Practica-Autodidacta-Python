# #💡 Esto es una lista de **tuplas** — cada elemento tiene dos valores: nombre y nota. Puedes acceder a ellos así:
# > ```python
# > for nombre, nota in estudiantes:  # Python los separa automáticamente
# >     print(nombre)  # "Ana"
# >     print(nota)    # 4.5
# > ```

# ---

# ### Tu programa debe:

# **1.** Recorrer la lista e imprimir solo los estudiantes **aprobados** (`>= 3.0`), saltando los reprobados con `continue`:
# ```
# Aprobado: Ana con 4.5
# Aprobado: Maria con 3.0
# ...
# ```

# **2.** Buscar si `"Juan"` tiene nota **mayor a 3.0**. Si la tiene, imprimir `"Juan aprobó"` y parar con `break`. Si no, el `else` imprime `"Juan no aprobó"`.

# **3.** Contar cuántos estudiantes aprobaron usando una variable `contador` que empiece en `0` y sume `+1` por cada aprobado. Al final imprimir:
# ```
# Total aprobados: 4 de 7
# ```

# ---

# ### 💡 Pistas

# - Puedes resolver los 3 puntos en **bucles separados** — no tienes que hacerlo todo en uno
# - Para el punto 3, declara `contador = 0` **antes** del bucle
# - El total de estudiantes es `len(estudiantes)` — eso te da el `7`

# ---

# **Salida esperada completa:**
# ```
# --- Estudiantes aprobados ---
# Aprobado: Ana con 4.5
# Aprobado: Maria con 3.0
# Aprobado: Pedro con 4.0
# Aprobado: Carlos con 3.7

# --- Búsqueda de Juan ---
# Juan no aprobó

# --- Conteo final ---
# Total aprobados: 4 de 7

print("Notas de estudiantes\n")
estudiantes = [
    ("Ana", 4.5),
    ("Luis", 2.8),
    ("Maria", 3.0),
    ("Juan", 1.5),
    ("Pedro", 4.0),
    ("Sofia", 2.5),
    ("Carlos", 3.7)
]

# PUNTO 1 — continue filtra los reprobados 
for estudiante, nota in estudiantes:
    if nota < 3.0:
        continue # salta: Luis, Juan, Sofia
    print(f"Aprobado: {estudiante} con: {nota}")
# PUNTO 2 — break + else para buscar a Juan ✅
for estudiante, nota in estudiantes:
    if estudiante == "Juan" and nota > 3.0:
        print("Juan aprobo!") # Juan tiene 1.5 → else se ejecuta ✅
        break
else:
    print("Juan no aprobo.")

# PUNTO 3 — contador con += ✅
contador = 0

for estudiante, nota in estudiantes:
    if nota >= 3.0:
        contador += 1
print(f"Total aprobados: {contador} de {len(estudiantes)}")
    
    