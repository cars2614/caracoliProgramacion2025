#metodo para contar los caracteres
saludo = "hola que tal"
print( len(saludo) )

#
nombre = input("Ingrese su nombre: ")
#edad = int( input("Ingrese su edad: ") )

#metodo de impresion 
#print(f"hola {nombre} tu edad es {edad}")

#metodo para colocar la primera letra en mayuscula
nombre = nombre.title()
print(nombre)

#convierte las cadenas a minuscula -- lower
nombre = nombre.lower()
print(nombre)

#convierte las cadenas a MAYUSCULA -- 
nombre = nombre.upper()
print(nombre)


"""Ajusta el texto al centro

el metodo recibe un parametro el cual debe ser 
superior al caracter que deseemos centrar
"""
nombre = nombre.center(50,"*")
print(nombre)

x =saludo.center(50,"-")
print(x)


"""Ajusta el texto a la izquierda

el metodo recibe un parametro el cual debe ser 
superior al caracter que deseemos centrar
"""
sasaludo =saludo.ljust(50,"-")
print(sasaludo)

"""Ajusta el texto a la Derecha
el metodo recibe un parametro el cual debe ser 
superior al caracter que deseemos centrar
"""
sasaludo =saludo.rjust(100,"*")
print(sasaludo)


"""Buscar

el metodo me permite buscar con palabras claves y cuenta 
cuantas palabas o letras encuentra
"""
sasaludo_ = saludo.count("h")
print(f"cuenta cuantas veces encontro la letra h en {saludo} y la cantidad fue {sasaludo_}")



