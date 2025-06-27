# list 
fruits = ["apple", "banana", "cherry"]

capitalizedList = []

for index in range(len(fruits)):
    fruit = fruits[index]
    capitalizedList.append(fruit.capitalize())
    # print(index, "-", fruit.capitalize())

print(capitalizedList)