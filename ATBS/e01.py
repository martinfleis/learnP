# This program says hello and asks for my name.

print('Hello Glasgow!')
print('What is your name?')  # ask for their name
my_name = input()
print("It's good to meet you, " + my_name)
print("The lenght of your name is:")
print(len(my_name))
print("what is your age?")  # ask for their age
my_age = input()
print("You'll be " + str(int(my_age) + 1) + " in a year.")
print(type(my_age))
