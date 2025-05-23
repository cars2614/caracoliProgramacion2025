def sumas(num1, num2):
    print("Vamos a realizar la suma: ")
    suma = num1+num2
    return suma

num1 = int( input("Ingrese el primer numero: ") )
num2 = int( input("Ingrese el segundo numero: ") )

notas = sumas(num1,num2)

print(f"la suma utilizando el return es: {notas}")

