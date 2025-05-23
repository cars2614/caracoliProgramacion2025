numeroSecreto = 7
numero = None

while numero != numeroSecreto:
    try:
        numero = int(input("Ingrese un numero: "))

    except Exception as e:

        print(f"El dato ingresado es incorrecto {e}")
    
    else:
        print(f"jajaja el numero ingresado NO ES: {numero}")

    finally:
        print("Vuelve a intentarlo")

print(f"Felicitaciones lo adivinaste el numero SECRETO ES {numero}")

