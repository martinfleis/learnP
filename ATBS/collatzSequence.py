def collatz(number):
    if number % 2 == 0:  # finds out if the number is even
        print(number // 2)  # prints the result of equation
        return number // 2  # return the result of equation as a value
    else:  # everything else is odd number
        print(3 * number + 1)
        return 3 * number + 1


print("Give me a number:")
try:  # try and exception when integer is not entered
    value = int(input())  # asks for a number and change it to integer from string

    if value <= 0:  # if you enter 0 or negative int
        print('Integer must be bigger than 0.')
    else:
        while value != 1:  # makes loop until value == 1
            value = collatz(value)  # redefines value by using it inside function collatz
except ValueError:
    print('You must enter integer.')
