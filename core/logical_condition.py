# conditions - temperature

temperature = 25
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cool")


# and, or, not logical operators
high_income = True
good_credit = False
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# age shoule be between 18 and 65
age = 22
# if age >= 18 and age < 65:
if 18 <= age < 65: # shortcut
    print("Adult")
else:
    print("Child")
