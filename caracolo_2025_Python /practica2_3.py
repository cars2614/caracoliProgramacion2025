""" 
Desarrolla una aplicacion que me pida:
#El nombre del estudiante.
# 3 notas del 1 al 5 y me las promedie

si es de 0 a 3.4 perdio
si es de 3.5 a 4.4 aprobo
si es de 4.5 a 5 aprobo con excelencia

si el estudiente es igual a carlos que me envie el siguiente mensaje:

"Carlos eres una maquina y l anota 4.5 a 5"

"""

nombre = input("Ingrese su nombre: ")
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 0 and promedio <= 3.4:
    print(nombre, "Perdiste, tu promedio es: ", promedio)

elif promedio >= 3.5 and promedio <= 4.4:
    print(nombre, "Aprobaste, tu promedio es: ", promedio)
    
elif promedio >= 4.5 and promedio <= 5:
    if nombre.lower() == "carlos":
        print(nombre, " Eres una máquina y la nota es: ", promedio)
    else:
        print(nombre, "Aprobaste con excelencia, tu promedio es: ", promedio)  
else:
    print("Error, el promedio no es válido")
