"""cual es el numero mayor

desarrolle una aplicacion que me permita ingresar 3 notas por teclado
las cuales la aplicacion debe identificar ¿Cual es la nota mayor?

1>2 1>3
  2>3
  3
"""
nombre = input("Ingrese su nombre: ")

nota1 = int(input(nombre + " Ingrese la primera nota: "))
nota2 = int(input(nombre + " Ingrese la segunda nota: "))
nota3 = int(input(nombre + " Ingrese la tercera nota: "))

if nota1 > nota2 and nota1 >nota3:
        
    print("La nota mas alta es la nota 1: ", nota1)

elif nota2 > nota3:
    print("La nota mas alta es la nota 2: ", nota2)
else:
    print("La nota mas alta es la nota 3: ", nota3)
