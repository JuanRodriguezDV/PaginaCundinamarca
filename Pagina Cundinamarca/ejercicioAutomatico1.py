num = int(input())

bandera = True
binaL = []


while bandera:
    if num == 0:
        bandera = False
    else:
        bina = num % 2
        binaL.append(bina)
        num = num // 2


new_trial = binaL[::-1]
for x in new_trial:
    print(x, end=(""))
