import random

def getValidGuess():
    guessData = input('Enter a number: ')
    try:
        guess = int(guessData)
        return guess
    except ValueError:
        print('That wasn\'t a number try again!')
        return getValidGuess()

target = random.randint(0,100)
guess = -1
error = 0

while guess != target:
    guess = getValidGuess()
    if guess < target:
        print('Higher')
    elif guess > target:
        print('Lower')
print('You guessed the target', target)