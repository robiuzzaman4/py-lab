# list 
fruits = ["apple", "banana", "cherry"]

capitalized_list = []

for index in range(len(fruits)):
    fruit = fruits[index]
    capitalized_list.append(fruit.capitalize())
    # print(index, "-", fruit.capitalize())

print(capitalized_list)