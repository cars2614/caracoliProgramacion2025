aprendices = [
    [1122, "carlos","ramirez",37,"Buga"],
    [1122, "carlos","ramirez",3,"Buga"],
    [1122, "carlos","ramirez",7,"Buga"],
    [1122, "carlos","ramirez",47,"Buga"],
    [1122, "carlos","ramirez",57,"Buga"],
]

for aprendiz in aprendices:
   # print(aprendiz[1],aprendiz[3])

    if aprendiz[3] >= 18:
        print(f"{aprendiz[1]}  Es mayor de edad")   