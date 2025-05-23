cantidad = 0

while cantidad <3:
    def suma(numero1,numero2):
        res = numero1 + numero2
        print(f"la suma es: {res}")

    numero1 = int(input("Ingrese el numero 1: "))
    numero2 = int(input("Ingrese el numero 2: "))

    suma(numero1, numero2)

    cantidad+=1