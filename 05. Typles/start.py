lang = ('Python', 'C#', "PHP", "Java", "TypeScript", "C#")

# print(len(lang))
# print(type(lang))
# print(lang)
# lang[5] = "C++"
# print(lang[5])

# fruits = ("Apple", "Banana", "Orange", "Cherry")
# print(f"Type: {type(fruits)}\nLength: {len(fruits)}\nData: {fruits}")
# fruits[0] = "Banana"  # Error

# print('Banana' in fruits)
# del fruits

# fruits = {"Apple", "Banana", "Orange", "Cherry"}
# print(f"Type: {type(fruits)}\nLength: {len(fruits)}\nData: {fruits}")
# print('Banana' in fruits)
# fruits.add("Lemon")
# print(f"Type: {type(fruits)}\nLength: {len(fruits)}\nData: {fruits}")
# print("---------------------Lemon===================")
# fruits.add("Lemon")
# fruits.add("Lemon")
# fruits.add("Apple")
# fruits.add("Lemon")
# print(f"Type: {type(fruits)}\nLength: {len(fruits)}\nData: {fruits}")
# fruits.remove("Orange")
# print(f"Type: {type(fruits)}\nLength: {len(fruits)}\nData: {fruits}")
# del fruits

input_string = input("Enter a string: ")

rotated_string = input_string[::-1]
print("Rotated string:", rotated_string)
