listaNombres = ["carlos","ana","felipe","andres"]

for nombre in listaNombres:
    if nombre == "felipe":
        print(f"{nombre} me debe dinero")
    elif nombre == "andres":
        print(f"{nombre} le debe 20.000")
    else:
        print(f"tu nombre es: {nombre}")