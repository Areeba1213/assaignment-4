<<<<<<< HEAD
import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    print("🎮 Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
        if user_choice == 'q':
            print("Thanks for playing! 👋")
            break
        if user_choice not in options:
            print("Invalid choice. Try again!")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a draw! 😐")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win! 🏆")
        else:
            print("You lose! 💀")

        print()  # Empty line for spacing

rock_paper_scissors()
=======
import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    print("🎮 Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
        if user_choice == 'q':
            print("Thanks for playing! 👋")
            break
        if user_choice not in options:
            print("Invalid choice. Try again!")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a draw! 😐")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win! 🏆")
        else:
            print("You lose! 💀")

        print()  # Empty line for spacing

rock_paper_scissors()
>>>>>>> 0e0a4809e687b5737b2237adb0a9c1c67e0e34c0
