# This is a guess the number game
import random
print('Hello.  What is your first name?')
name = input()
secretNumber = random.randint(1, 20)
print('Well, ' + name + ", I am thinking of a whole number between 1 and 20.  I'll give you 6 tries to get it right.  Take a guess")

print('DEBUG: The secret number is ' + str(secretNumber))

# Ask the player to guess up to 6 times.
for guessesTaken in range(1, 7):
    try:
        print('Take a guess.')
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break # This condition is the correct guess!
    except ValueError:
        print('You did not enter an integer!')

if guess == secretNumber:
    print('Good job, ' + name + '!  You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope.  The number I was thinking of was ' + str(secretNumber))
