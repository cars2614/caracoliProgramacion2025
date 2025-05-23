try: 
    numero = int( input("Ingrese un numero: ") )
    print(f"El numero ingresado es: {numero}")
except Exception as e:
    print(f"El dato ingresado es incorrecto {e}")

else:
    print(f"El dato que ingreso es correcto: {numero}")

finally:
    print("Fin del programa, se libero la memoria ram")
