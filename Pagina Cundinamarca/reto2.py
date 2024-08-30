import math

nLatas = int(input())

formula = (-1 + (math.sqrt(1 + (8 * nLatas)))) / 2


if formula.is_integer():
    print(f"{nLatas} es adecuado para apilar.")
else:
    print(f"{nLatas} no es adecuado para apilar.")
