import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
isGuessRight = False
while isGuessRight !=True:
    guess=input("Guess a number between 1 to 10 ")
    number = random.randint(1,10)
    if int(guess)==number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. the number was {} Try again.".format(guess,number))
        