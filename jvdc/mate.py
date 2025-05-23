""" 
Tengo un servido web que tiene un espacio de 10GB 'Gigabyte', y cargo siardiariamente 600MB 'Megabyte'

cuantos dias me queda para llenar el servidor, y si lo lleno que me diga cuanta capacidad me queda.

datos: 
Espacio en servidor => 10GB
10GB = 10240MB
1GB = 1024MB
600MB = 0.6GB
"""

espacio_servidor = 10 * 1024 # Convertir GB a MB
carga_diaria = 600 # MB
dias = espacio_servidor / carga_diaria
capacidad_restante = espacio_servidor - (carga_diaria * dias)

print("Espacio total en el servidor:", espacio_servidor, "MB")
print("Dias para llenar el servidor:", dias)
print("Capacidad restante:", capacidad_restante, "MB")


 
