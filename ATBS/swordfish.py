while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello, Joe. What is your password?")
    password = input()
    if password == "swordfish":
        break
    else:
        print("Try it again.")
        password = input()
print("Access granted.")
