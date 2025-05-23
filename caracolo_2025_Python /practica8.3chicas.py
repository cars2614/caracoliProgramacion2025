"""ejercicio

realiza una lista de comidas 

la cual se debe recorrer por medio de un ciclo FOR 
el cual me indique cuando sea una comida saludable 
y cuando sea una comida chatarra 

8 comidas
"""

lista_comidas = [
    "perro caliente", "hamburguesas", "sopa", "arroz con pollo",
    "pescado","carne","atun","sandwich"  
    ]

for comida in lista_comidas:
    if comida == "perro caliente" or comida == "hamburguesas":
        print(f"{comida} no es saludable :( ")
        
    else:
        print(f"{comida} SI es saludable :) ")
        
    print(" ")
