edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad <= 10:
    if edad == 0:
        print("Eres un bebé, Tu edad es:" , edad, "Años")
    else:
        print("Eres un niño, Tu edad es:" , edad, "Años")    

elif edad >= 11 and edad <= 17:
    print("Eres un adolescente, Tu edad es:" , edad, "Años")

elif edad >= 18 and edad <= 35:
    if edad == 18:
        print("Felicitaciones.... Eres un adulto, Tu edad es:" , edad, "Años")
    else:
        print("Eres un adulto joven, Tu edad es:" , edad, "Años")    

elif edad >= 36 and edad <= 60:
    if edad == 60:
        print("Estas cascadito, Tu edad es:" , edad, "Años")
    else:
        print("Eres un adulto, Tu edad es:" , edad, "Años") 

elif edad >= 61 and edad <= 120:  
    if edad == 120:
        print("Eres legendario, Tu edad es:" , edad, "Años")  
    else:
        print("Eres un adulto mayor, Tu edad es:" , edad, "Años")

else:
    print("Edad no válida")

