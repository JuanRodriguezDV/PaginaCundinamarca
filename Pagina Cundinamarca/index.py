# x = 500

# match x:
#     case 500 | 501:
#         print("soy un 500")

# y = ["chocolate", "manzana", "mandarina", "pescado"]

# for item in y:
#     print("tu comidas favoritas son.... ", item)

# count = 0

# while count < len(y):
#     print(" tu comida favorita es.....", y[count])
#     count += 1

# for i in range(10):
#     for j in range(10):
#         print("p", end=" ")
#     print()

# num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

# for index, item in enumerate(num_list):
#     print(f"indice:{index}, Numero{item}")

# del num_list
# print(num_list)

# num1 = int(input("Dame un entero: "))
# num2 = int(input("Dame otro numero: "))

# if num2 == 0:
#     print("No se puede dividir por CERO ")
# else:
#     print(f"el numero {num1} divido por el numero {num2} es {num1/num2}")

# num1 = int(input("Dame un entero: "))

# if num1 % 2 == 0:
#     print(f"tu numero {num1} es par")
# else:
#     print(f"tu numero {num1} es impar")

# edad = int(input("Tu edad por favor: "))
# ingresos = float(input("Cuantos son tus ingresos: "))

# if edad > 16 and ingresos >= 1000:
#     print("puedes tributar impuestos")
# else:
#     print("no puedes tributar")

# num1 = int(input("digite un numero entero: "))
# num2 = int(input("digite un segundo numero entero: "))
# num3 = int(input("digite un tercer numero entero: "))

# if num1 > num2 and num1 > num3:
#     print(f"{num1} es el mayor")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} es el mayor")
# else:
#     print(f"{num3} es el mayor")

# if num1 < num2 and num1 < num3:
#     print(f"{num1} es el numero menor")
# elif num2 < num1 and num2 < num3:
#     print(f"{num2} es el numero menor")
# else:
#     print(f"{num3} es el numero menor")

# if num1 < num2 and num1 > num3 or num1 > num2 and num1 < num3:
#     print(f"{num1} es el numero del medio")
# elif num2 < num1 and num2 > num3 or num2 > num1 and num2 < num3:
#     print(f"{num2} es el numero del medio")
# else:
#     print(f"{num3} es el numero del medio")

# produc1 = [
#     int(input("Digite cantidad: ")),
#     float(input("digite valor unitario: ")),
# ]

# produc2 = [
#     int(input("Digite cantidad: ")),
#     float(input("digite valor unitario: ")),
# ]

# produc3 = [
#     int(input("Digite cantidad: ")),
#     float(input("digite valor unitario: ")),
# ]

# totalP1 = produc1[0] * produc1[1]
# totalp2 = produc2[0] * produc2[1]
# totalP3 = produc3[0] * produc3[1]

# totalCompra = totalP1 + totalp2 + totalP3

# if totalCompra <= 20000:
#     print(
#         f"El total de tu compra es {totalCompra} tienes un descuento de 10% y \n
#         el total a pagar es {totalCompra * 0.10}"
#     )
# elif totalCompra >= 50000:
#     print(
#         f"El total de tu compra es {totalCompra} tienes un descuento de 20% y \n
#         el total a pagar es {totalCompra * 0.20}"
#     )
# else:
#     print(f"Tu compra tiene un valor de {totalCompra}")

# n = int(input("Ingrese un numero: "))
# fac = 1
# for x in range(1, (n + 1)):
#     fac = fac * x
#     print(fac)

# n = int(input("Ingrese un numero: "))
# r = int(input("Ingrese un numero: "))
# fac = 1

# for x in range(1, (n + 1)):
#     fac *= x

# fac2 = 1
# for y in range(1, (r + 1)):
#     fac2 *= y

# fac3 = 1
# for z in range(1, ((n - r) + 1)):
#     fac3 *= z

# h = fac / (fac2 * fac3)

# print(f"El resultado de la formula es {h}")
# for i in range(1, 10):
#     for j in range(1, 10 - 1):
#         print("p", end=" ")
#     print()
# menu = {
#     1: {"name": "espresso", "price": 1.99},
#     2: {"name": "coffee", "price": 2.50},
#     3: {"name": "cake", "price": 2.79},
#     4: {"name": "soup", "price": 4.50},
#     5: {"name": "sandwich", "price": 4.99},
# }

# names = [item["name"] for item in menu]

# print(names)

# try:
#     names = [item["name"] for item in menu]

#     print(names)
# except Exception as e:
#     print(e)

# import random as rdm

# file = open("../Pagina Cundinamarca/prueba.txt", mode="r")
# data = file.read()
# print(data)
# file.close

# file_name = "petnames.txt"

# with open(file_name) as file:
#     f = file.read()
#     f2 = f.split("\n")
#     print(rdm.choice(f2))
# pets = ["Ace", "Atlas", "Bailey", "Bear", "Blaze", "Boomer", "Buddy"]
# with open("prueba2.txt", "w") as file:
#     file.write(pets[0])


# def mi_funcion(lista):
#     for elemento in lista:
#         print(elemento)


# # Crear una lista
# mi_lista = [1, 2, 3, 4, 5]


# mi_funcion(mi_lista)


# n = int(input("Ingrese un numero: "))
# nume = 1
# deno = 1
# for x in range(1, (n + 1)):
#     nume *= x
#     deno *= 2
#     # if pot == n:
#     #     deno = expo**pot

# print(nume, deno)

for x in range(10) :
    for y in range (10):
        print(" * ",end="")
    print()