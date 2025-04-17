<<<<<<< HEAD
import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("🎮 Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
=======
import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("🎮 Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
>>>>>>> 0e0a4809e687b5737b2237adb0a9c1c67e0e34c0
