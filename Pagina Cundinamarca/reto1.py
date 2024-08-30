tornillo = float(input("Ingrese tamaño del tornillo: "))

match tornillo:
    case _ if 1 <= tornillo < 3:
        print("El tornillo es pequeno.")
    case _ if 3 <= tornillo < 5:
        print("El tornillo es mediano.")
    case _ if 5 <= tornillo < 6.5:
        print("El tornillo es grande.")
    case _ if 6.5 <= tornillo <= 8.5:
        print("El tornillo es muy grande.")
    case _ if 8.5 < tornillo:
        print("El tornillo es gigante.")
    case _:
        print("El tamano ingresado no es valido.")
