def operacionesBasicas(num1 , num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2

    return suma, resta, multiplicacion, division


resultado = operacionesBasicas(5,2)
print(f"Los resultados son: {resultado}")
print(f"El resultado de la suma: {resultado[0]}")
