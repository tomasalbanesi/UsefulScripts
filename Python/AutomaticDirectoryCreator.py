import os

# Ruta base donde se crearán los directorios
ruta_base = r"C:\Users\tomas\OneDrive - UTN.BA\UBA\FILO\Latin I Cát. Pégolo 2021\TPs"

# Número de directorios que deseas crear
num_directorios = 14

# Utiliza un bucle para crear directorios con un índice incremental
for i in range(1, num_directorios + 1):
    
    # Path del nuevo directorio
    directorio_nuevo = f"{ruta_base}\Practico_{i}"
    
    # Verifica si el directorio ya existe antes de crearlo
    if not os.path.exists(directorio_nuevo):
        os.makedirs(directorio_nuevo)
        print(f"Directorio '{directorio_nuevo}' creado exitosamente.")
    else:
        print(f"El directorio '{directorio_nuevo}' ya existe.")