"""tabla de multiplicar
desarrolle una tabla de multiplicar de un numero X que el usuario
ingrese por teclado
"""
tabla = int(input("Ingrese un numero: "))

for num in range(1,11):
    print(f"{tabla} * {num} = {tabla * num} ")