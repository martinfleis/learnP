# name = ""
#
# while name != "your name":
#     print("Please type your name.")
#     name = input()
# print('Thank you.')

# anothe way of doing it
while True:  # infinite loop
    print("Please type your name.")
    name = input()
    if name == "your name":
        break  # escape from loop
print("Thank you.")
