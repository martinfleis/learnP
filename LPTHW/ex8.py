# define variable with four placeholders
formatter = "{} {} {} {}"

# print 1 - 4 inside those placeholders
print(formatter.format(1, 2, 3, 4))
# print one - four inside placeholders
print(formatter.format("one", "two", "three", "four"))
# print booleans inside placeholders
print(formatter.format(True, False, False, True))
# print variable itself in all placeholders
print(formatter.format(formatter, formatter, formatter, formatter))
# print strings inside placeholders
print(formatter.format(
    "Odpoustim ti Rut,",
    "Ze nemas dnes den",
    "To se stava",
    "To znam"
))
