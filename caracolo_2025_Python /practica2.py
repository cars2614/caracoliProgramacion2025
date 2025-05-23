"""Practica 2

realiza una aplicacion la cual me brinde la 
informacion si voy bien de tiempo
"""

print("Ingrese en hora militar: ")
hora = int(input("Ingrese la hora: "))

if hora >500 and hora <515:
    print("Estamos bien de tiempo, son las ", hora)

elif hora >516 and hora <530:
    print("Estamos Tarde, son las ", hora)

elif hora >531 and hora <600:
    print("Pela fija, son las ", hora)
else:
    print("error")