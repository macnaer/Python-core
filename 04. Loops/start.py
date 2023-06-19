# people = ["John", "Adam", "Sara", "Paul", "Eva"]

# print(f"Index 'Sara' = {people.index('Sara')}")

# for person in people:
#     print(person)

# for item in people:
#     if item == "Sara":
#         print(item)

# for i in range(len(people)):
#     print(people[i])

# count = 1
# while count <= 10:
#     print(f"Count: {count}")
#     count += 1

# number = int(input("Enter number: "))

# print(number, type(number))

exit = False
# while not exit:
while exit != True:
    choise = int(input(f"Buy 36.57\tSale 37.45\n1. Buy\n2. Sale\n0. Exit "))
    if choise == 1:
        print("Buy")
    elif choise == 2:
        print("sale")
    elif choise == 0:
        exit = True
    else:
        print("Wrong choise")
