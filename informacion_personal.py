# 1) Crear diccionario con información ficticia
informacion_personal = {
    "nombre": "Daymer Guarnizo",
    "edad": 20,
    "ciudad": "Zumbi",
    "profesion": "Estudiante"
}

# 2) Acceder y modificar la ciudad
informacion_personal["ciudad"] = "Zumbi"  

# 3) Agregar/actualizar la profesion
informacion_personal["profesion"] = "Estudiante"

# 4) Verificar existencia de 'telefono' y agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+583987082110"

# 5) Eliminar la clave 'edad'
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# 6) Imprimir el diccionario final
print("Diccionario final:")
for k, v in informacion_personal.items():
    print(f"{k}: {v}")
