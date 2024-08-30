# file = open("prueba2.txt")
# data = file.readlines()

# # print(data)


# def isPalindrome(str):
#     startIndex = 0
#     endIndex = len(str) - 1
#     for x in str:
#         if str[startIndex] != str[endIndex]:
#             return False
#         return True

#     print(endIndex)


# print(isPalindrome("racecars"))


# coffees = ["Expresso", "Latte", "Ccappuccino"]


# def reverse(str):
#     return str[::-1]


# with open("petnames.txt") as file:
#     datos = file.readlines()


# reversed_coffes = map(reverse, datos)

# for x in reversed_coffes:
#     print(x)


# # Recursive function for Tower of Hanoi
# def hanoi(disks, source, helper, destination):
#     # Base Condition
#     if disks == 1:
#         print(
#             "Disk {} moves from tower {} to tower {}.".format(
#                 disks, source, destination
#             )
#         )
#         return

#     # Recursive calls in which function calls itself
#     hanoi(disks - 1, source, destination, helper)
#     print("Disk {} moves from tower {} to tower {}.".format(disks, source, destination))
#     hanoi(disks - 1, helper, source, destination)


# # Driver code
# disks = int(input("Number of disks to be displaced: "))
# """
# Tower names passed as arguments:
# Source: A
# Helper: B
# Destination: C
# """
# # Actual function call
# hanoi(disks, "A", "B", "C")

# trial = "Juancho"

# new_trial = trial[::-2]

# print(new_trial)

# data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# # Ex1: List comprehension: updating the same list
# data = [x + 3 for x in data]
# print("Updating the list: ", data)

# # # Ex2: List comprehension: creating a different list with updated values
# new_data = [x * 2 for x in data]
# print("Creating new list: ", new_data)

# # # Ex3: With an if-condition: Multiples of four:
# fourx = [x for x in new_data if x % 4 == 0]
# print("Divisible by four", fourx)

# # Ex4: Alternatively, we can update the list with the if condition as well
# fourxsub = [x - 1 for x in new_data if x % 4 == 0]
# print("Divisible by four minus one: ", fourxsub)

# # Ex5: Using range function:
# nines = [x for x in range(100) if x % 9 == 0]
# print("Nines: ", nines)

# Using range() function and no input list
# usingrange = {x: x * 2 for x in range(13)}
# print("Using range(): ", usingrange)

# # Lists
# months = [
#     "Jan",
#     "Feb",
#     "Mar",
#     "Apr",
#     "May",
#     "June",
#     "July",
#     "Aug",
#     "Sept",
#     "Oct",
#     "Nov",
#     "Dec",
# ]
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# # Using one input list
# numdict = {x: x**2 for x in number}
# print("Using one input list to create dict: ", numdict)

# # Using two input lists
# months_dict = {key: value for (key, value) in zip(number, months)}
# print("Using two lists: ", months_dict)

# data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# gen_obj = (x for x in data)
# print(gen_obj)
# print(type(gen_obj))
# for items in gen_obj:
#     print(items, end=" ")


# z = ["alpha", " bravo", " charlie"]
# new_z = [i[0] * 2 for i in z]
# print(new_z)
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"},
]


def mod(employee_list):
    temp = employee_list["name"] + "_" + employee_list["department"]
    return temp


datos = map(mod, employee_list)
list2 = [x for x in datos]

usernames = [x.replace(" ", "_") for x in list2]

id_empleado = {x["id"]: x["name"][0] for x in employee_list}

print(list2)
print(usernames)
print(id_empleado)


def sum(n):
    if n == 1:
        return 0
    return n + sum(n - 1)


a = sum(5)
print(a)
