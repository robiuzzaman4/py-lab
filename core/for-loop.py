# for number in range(3):
#     print("Attempt", number + 1, (number + 1) * ".")

# for number in range(1, 4):
#     print("Attempt", number, number * ".")

# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")

success = True
for number in range(3):
    print("Seding Email... ⌛")
    if success:
        print("Email Sent ✅")
        break
else:
    print("Attemped 3 times and failed! ❌")
