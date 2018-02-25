def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


print('Enter number:')
try:
    value = int(input())
    if value <= 0:
        print('Number have to be bigger than zero.')
    else:
        while value != 1:
            value = collatz(value)

except ValueError:
    print('You must enter integer.')
