# Lista de edades
edades = [
21,20,20,19,28,21,18,21,25,19,20,20,21,19,19,21,19,25,25,19,
19,20,21,20,19,24,22,19,34,20,26,27,20,20,25,25,19,19,24,19,
23,19,19,19,30,20,22
]

# Cantidad de datos
n = len(edades)

# -------------------
# MEDIA
# -------------------
suma = 0
for edad in edades:
    suma += edad

media = suma / n

# -------------------
# MEDIANA
# -------------------
edades_ordenadas = sorted(edades)

if n % 2 == 0:
    mediana = (edades_ordenadas[n//2 - 1] + edades_ordenadas[n//2]) / 2
else:
    mediana = edades_ordenadas[n//2]

# -------------------
# MODA
# -------------------
frecuencias = {}

for edad in edades:
    if edad in frecuencias:
        frecuencias[edad] += 1
    else:
        frecuencias[edad] = 1

max_frecuencia = 0
moda = None

for edad in frecuencias:
    if frecuencias[edad] > max_frecuencia:
        max_frecuencia = frecuencias[edad]
        moda = edad

# -------------------
# VARIANZA
# -------------------
suma_varianza = 0

for edad in edades:
    suma_varianza += (edad - media) ** 2

varianza = suma_varianza / (n - 1)

# -------------------
# DESVIACIÓN ESTÁNDAR
# -------------------
desviacion = varianza ** 0.5

# -------------------
# RESULTADOS
# -------------------
print("Cantidad de datos:", n)
print("Media:", round(media, 2))
print("Mediana:", mediana)
print("Moda:", moda)
print("Varianza:", round(varianza, 2))
print("Desviación estándar:", round(desviacion, 2))