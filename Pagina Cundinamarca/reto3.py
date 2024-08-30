num = int(input())

for x in range(1, num + 1):
    if x % 2 != 0:
        print(x, end="  ")
        for y in range(1, x):
            x2 = x - y
            if x2 % 2 != 0:
                print(x2, end="  ")
        print()
