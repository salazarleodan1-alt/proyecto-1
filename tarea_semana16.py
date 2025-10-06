# Tarea: Trabajo con Archivos de Texto
# Autor: [Daymer Guarnizo]
# Descripción: Tarea

with open("my_notes.txt", "w") as archivo:
    archivo.write("Nota 1: Hoy aprendí a trabajar con archivos en Python.\n")
    archivo.write("Nota 2: Los métodos open(), read() y write() son fundamentales.\n")
    archivo.write("Nota 3: Siempre debo cerrar los archivos después de usarlos.\n")

with open("my_notes.txt", "r") as archivo:
    
    print("Contenido del archivo my_notes.txt:\n")
    for linea in archivo:
        
        print(linea.strip())  

print("\nEl archivo ha sido leído y cerrado correctamente.")