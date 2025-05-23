#funciones basicas
def saludo():
    print("Hola que tal?")

saludo()

#funciones con argumentos o parametros

#se recibe como parametro
def saludo2(nombre):
    print(f"bienvenido {nombre}")


#se envia como argumento
saludo2("carlos")

#segunda forma para enviar argumentos
nom = input("ingrese su nombre: ")
saludo2(nom)






