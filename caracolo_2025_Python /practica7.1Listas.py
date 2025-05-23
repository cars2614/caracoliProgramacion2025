"""Listas
Se pueden crear: 
    Homogeneas "contiene un solo tipo de dato"
    Heterogeneas "contienen varios tipos de datos"
"""
#Lista Heterogenea
listaDatosPersona = ["Carlos", "Ramirez", 80, True]
print(listaDatosPersona)
print(f" { listaDatosPersona[0:3] } *** { listaDatosPersona[1] } ")

#lista Homogenea
listaNombres = ["carlos", "Ana", "Pedro"]
print(listaNombres)
print(listaNombres[0])#primero de la lista
print(listaNombres[-1])#ultimo de la lista

#cambio de un valor a una lista
listaNombres[2] = "Robert"
print(f"cambio de valores de una lista: {listaNombres} " )

#Agregar elementos a la lista append()
listaNombres.append("Jose")
print(f"Lista con nuevo elemento: {listaNombres}")

#Agregar elemento en un orden en especifico
listaNombres.insert(0,"Isabella") #Aqui voy a colocar a Isabella en la 0
print(f"Lista con nuevo elemento ORDENADO: {listaNombres}")


#Eliminar uno o varios elementos de una lista
listaNombres.pop()#este metodo elimina el ultimo elemento de la lista
print(f"Ultimo elemento eliminado: {listaNombres}")
listaNombres.pop(0)
print(f"Primer elemento eliminado: {listaNombres}")

#Eliminar elemento con metodo remove
listaNombres.remove("carlos") #este metodo elimina 
print(f"elemento eliminado carlos: {listaNombres}")


print("*********************************")

for nombre in listaNombres:
    print(f"lista de nombres {nombre}")

