# Ejemplo: Temperaturas diarias en varias ciudades durante varias semanas

# Definimos los datos:
# 3 ciudades, 7 días por semana, 2 semanas
temperaturas = [
    [  # Ciudad 1
        [25, 26, 24, 23, 25, 26, 27],  # Semana 1
        [26, 27, 25, 24, 26, 27, 28]   # Semana 2
    ],
    [  # Ciudad 2
        [30, 31, 29, 28, 30, 31, 32],  # Semana 1
        [31, 32, 30, 29, 31, 32, 33]   # Semana 2
    ],
    [  # Ciudad 3
        [20, 21, 19, 18, 20, 21, 22],  # Semana 1
        [21, 22, 20, 19, 21, 22, 23]   # Semana 2
    ]
]

# Nombres de ciudades y semanas para mostrar resultados
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]
semanas = ["Semana 1", "Semana 2"]

# Calcular el promedio de temperaturas por ciudad y semana
for i in range(len(temperaturas)):  # Recorre ciudades
    print(f"\nPromedios de {ciudades[i]}:")
    for j in range(len(temperaturas[i])):  # Recorre semanas
        suma = 0
        for k in range(len(temperaturas[i][j])):  # Recorre días
            suma += temperaturas[i][j][k]
        promedio = suma / len(temperaturas[i][j])
        print(f"{semanas[j]}: {promedio:.2f} °C")
