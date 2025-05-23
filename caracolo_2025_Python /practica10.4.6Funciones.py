def datosPersona(nombre,apellido,edad):
    edadActual = 2024 - edad   

    return nombre, apellido , edadActual


inicio = 1
while inicio <= 3:

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int( input("Ingrese su edad: ") )

    resul = datosPersona(nombre,apellido,edad)

    if resul[0] == "carlos":
        print(f" Instru, su nombre es: {resul[0] }  apellido: {resul[1]} edad es: {resul[2]}")

    else:
        print(f"su nombre es: {resul[0] }  apellido: {resul[1]} edad es: {resul[2]}") 
        
    inicio+=1


    