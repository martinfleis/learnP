# This program says hello and asks for my name.

print('Hello Glasgow!')
print('What is your name?')  # ask for their name
my_name = input()
print("It's good to meet you, " + my_name)
print("The lenght of your name is:")
print(len(my_name))
print("what is your age?")  # ask for their age
my_age = input()
# str makes string, int makes integer
print("You'll be " + str(int(my_age) + 1) + " in a year.")

# another way
age = int(my_age) + 1  # make integer and add one
sentence = "You'll be {} in a year"  # set variable with placeholder
# print variable sentence and fill placeholder with variable age
print(sentence.format(age))
# and another way how to do the same thing
print("You will be", age, "years old soon.")
