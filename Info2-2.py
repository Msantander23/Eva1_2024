numvlan = int(input("Cual es el número de la vlan? "))
if numvlan >= 1 and numvlan <= 1005:
    print("Esta es una VLAN normal .")
elif numvlan >=1006 and numvlan <= 4095:
    print("Esta es una VLAN extendida")
else:
    print("Esta VLAN no corresponde a las de rango normal ni extendidas.")

