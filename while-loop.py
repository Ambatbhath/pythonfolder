import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#Assign a random number between 1 and 10 to number
number = random.randint(1,10)

#Set isGuessRight to False
isGuessRight = False

#Runs till the guess is true
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    
    if int(guess) == number:
        print(f"You guessed {guess}. That is correct! You win!")
        isGuessRight = True
    else:
        print(f"You guessed {guess}. Sorry, that isn’t it. Try again.")