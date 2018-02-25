import sys  # import module sys

while True:  # make infinite loop
    print('Type exit to exit.')
    response = input()
    if response == 'exit':  # if input is 'exit'
        sys.exit()  # terminate program
        # break  # break the loop
    print('You typed ' + response + '.')
µ
