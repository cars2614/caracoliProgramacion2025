print ("Vamos a ver el listado de las pelCanciones disponibles")
canciones = {
    "un dia": "Cosculluela",
    "y si la ves": "Ñejo",
    "dale don dale": "Don Omar",
    "malo h": "leandro y Pirlo",
    "yogurcito": "Blessd",
    "flow hp": "Don Omar y Residente",
    "un beso": "Luigi 21 Plus"
}


print("Estas son las canciones de mi listado: ")
for cancion in canciones:
    print(f"=> {cancion}")

intento = 1

while intento <= 3 :

    entreda = input("Ingrese la cancion que desea saber quien la canta: ")

    if entreda =="un dia":
            print("La canta cosculluela") 
            
    elif entreda == "y si la ves":
        print("La canta ñejo") 

    elif entreda == "dale don dale":
        print("La canta don omar")

    elif entreda == "malo h":
        print("La canta pirlo")

    elif entreda == "yogurcito":
        print("La canta blessd")

    elif entreda == "flow hp":
        print("La canta don omay y residente")

    elif entreda == "un beso":
        print("La canta luigi 21 plus")

    else:
        print("Cancion no identificada")

    intento += 1
                

