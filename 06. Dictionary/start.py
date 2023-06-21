person = {
    "FirstName": "Bill",
    "LastName": "Gates",
    "Age": 24,
}

# print(
#     f"Type: {type(person)}\nName: {person['FirstName']}\nSurname: {person['LastName']}\nAge: {person['Age']}")
print(person.get('LastName'))

# print(person.keys())
# print(person.items())

person2 = person.copy()
person2['Age'] = 30
# print(person.get('Age'))

peopleList = [person, person2]

# print(peopleList)
# print(peopleList[0].get('Age'))
# print(peopleList[0]['Age'])
# print("========================")
# print(peopleList[1].get('Age'))
# print(peopleList[1]['Age'])


for item in peopleList:
    print(item['Age'])
