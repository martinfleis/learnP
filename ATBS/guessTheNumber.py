# Guess the number game
import random  # import module to get random answerNumber
secretNumber = random.randint(1, 20)  # randomly define secret number from range 1 - 20
print("I'm thinking of a number between 1 and 20.")

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):  # define a loop which goes 6 times
    print('Take a guess.')
    guess = int(input())  # asks for a guess

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # break the loop if the number is equal to secret one

if guess == secretNumber:  # if guess is correct, give correct message.
    print('Yay! You did it in', guessesTaken, 'guesses.')
else:  # if guess is wrong even after 6 tries (loop ends naturally)
    print('Nope, the number was ' + str(secretNumber) + '.')
