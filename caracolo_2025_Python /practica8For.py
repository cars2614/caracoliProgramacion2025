"""sumary_line
Este ciclo lee la cantidad de caracteres
que contiene la variable saludo
"""
saludos = input("Ingresa un saludo ")
for saludo in saludos:
    print(f"vamos en la vuelta {saludo} {saludos}")

"""For con range
este metodo me permite ingresar un rango 
el cual me brinda un limite te vueltas al 
ciclo, pero me descuenta 1
"""
numero = int(input("Ingrese un numero: "))
for indice in range(1,numero):
    print(f"vuelta numero {indice}")