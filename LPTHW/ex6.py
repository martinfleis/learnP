# set variable
types_of_people = 10
# set variable with another inside a string
x = f"There are {types_of_people} types of people."

# variable with simole string
binary = "binary"
# another one
do_not = "don't"
# variable made of a string using two prevous var.
y = f"Those who know {binary} and those who {do_not}."

# print var x
print(x)
# print var y
print(y)

# print string with var x
print(f"I said: {x}")
# print string with var y
print(f"I also said: '{y}'")

# set var to False
hilarious = False
# define var with a string and empty {} waiting to get proper var inside
joke_evaluation = "Isn't that joke so funny?! {}"

# print var joke_evaluation using var hilarious inside {}
print(joke_evaluation.format(hilarious))

# var as a simple string
w = "This is the left side of..."
# and again
e = "a string with a right side."

# print two vars together
print(w + e)
