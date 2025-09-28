# -*- coding: utf-8 -*-
"""
Ejemplo de uso de diccionarios en Python
"""

# 1) Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 28,
    "ciudad": "Quito",
    "profesion": "Diseñador gráfico"
}

print("Diccionario original:")
print(informacion_personal)
print("-" * 40)

# 2) Acceder y modificar el valor asociado con la clave "ciudad"
print("Ciudad antes:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Guayaquil"   # modificamos la ciudad
print("Ciudad después:", informacion_personal["ciudad"])
print("-" * 40)

# 3) Agregar una nueva clave-valor al diccionario para la profesión
informacion_personal["profesion_detalle"] = "Diseño digital y branding"
print("Se agregó la clave 'profesion_detalle'.")
print("-" * 40)

# 4) Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593 98 765 4321"  # número ficticio
    print("Se agregó la clave 'telefono'.")
else:
    print("La clave 'telefono' ya existe.")

print("-" * 40)

# 5) Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad", None)  # eliminamos la edad
print("La clave 'edad' ha sido eliminada.")
print("-" * 40)

# 6) Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)
