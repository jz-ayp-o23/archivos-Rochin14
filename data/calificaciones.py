# Leer el archivo de calificaciones
with open('data/calificaciones.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()

# Procesar las calificaciones y calcular los promedios
promedios = []
for line in lines:
    data = line.split()
    nombre = data[0]
    apellido = data[1]
    calificaciones = list(map(float, data[2:]))
    promedio = sum(calificaciones) / len(calificaciones)
    promedios.append((apellido.upper(), nombre, promedio))

# Escribir los resultados en un nuevo archivo
with open('data/promedios.txt', 'w', encoding="utf8") as file:
    for promedio in promedios:
        linea = f"{promedio[0]}, {promedio[1]}: {promedio[2]:.1f}\n"
        file.write(linea)