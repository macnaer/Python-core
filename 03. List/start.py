
prog_lang = ["C#", "Rast", "Java", "Python", "JavaScript", "Go"]
''' 
print(type(prog_lang))
print(type(prog_lang[0]))
print(prog_lang[- 1])
print(len(prog_lang))
prog_lang.append("TypeScript")
print("============append===================")
print(prog_lang)
print("============remove===================")
prog_lang.remove("TypeScript")
print(prog_lang)
print("============incert===================")
prog_lang.insert(2, "C++")
print(prog_lang)
print("============pop===================")
prog_lang.pop(1)
print(prog_lang)
print("============reverse===================")
prog_lang.reverse()
print(prog_lang)
print("============sort===================")
prog_lang.sort()
print(prog_lang)
print("============sort reverse===================")
prog_lang.sort(reverse=True)
print(prog_lang)
'''
# ================================

mix_list = [2, 65, -6, "Apple", [55, ["Test", False], "Banana"], False]
# print(type(mix_list))
# print(type(mix_list[4][1][1]))
# print(mix_list)
# print(len(mix_list[4]))
# print(len(mix_list[4][1]))
# print("================Reverse================")
# mix_list.reverse()
# print(mix_list)
# print(mix_list)
# print("================Sort================")
# mix_list.sort()  # Error not supported between instances of 'list' and 'bool'
# print(mix_list)
mix_list.extend(prog_lang)
# print(mix_list)

# tmp_list = mix_list
# tmp_list = mix_list.copy()
# print(
#     f"\n---------------\nMix list {mix_list}\nTmp list {tmp_list}")
# tmp_list[0] = 22222222
# print(
#     f"\n---------------\nMix list {mix_list}\nTmp list {tmp_list}")

''' 
Користувач із клавіатури вводить елементи списку цілих. Необхідно порахувати суму всіх елементів та їхнє середньоарифметичне. Результати вивести на екран
'''
numbers = []

num1 = int(input("Enter first number: "))
numbers.append(num1)

num2 = int(input("Enter second number: "))
numbers.append(num2)

num3 = int(input("Enter third number: "))
numbers.append(num3)

print(numbers)

count = len(numbers)
print(f"Count = {count}")
print("============================")
avg = (numbers[0] + numbers[1] + numbers[2]) / count
print(f"AVG  : {avg}")
print("============================")
sum = numbers[0] + numbers[1] + numbers[2]
print(f"SUM  : {sum}")