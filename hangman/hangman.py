<<<<<<< HEAD
import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'project', 'developer']
    word = random.choice(words)
    guessed_letters = []

    # Choose difficulty
    difficulty = input("Choose difficulty (easy/hard): ").lower()
    if difficulty == 'easy':
        attempts = 11
    else:
        attempts = 6

    print("🎮 Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(" Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(" Good guess!")
        else:
            attempts -= 1
            print(f" Wrong guess! Attempts left: {attempts}")

        # Show current state of the word
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(" ".join(display_word))

        if '_' not in display_word:
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f" Game over! The word was '{word}'.")

hangman()
=======
import random

def hangman():
    words = ['python', 'hangman', 'challenge', 'project', 'developer']
    word = random.choice(words)
    guessed_letters = []

    # Choose difficulty
    difficulty = input("Choose difficulty (easy/hard): ").lower()
    if difficulty == 'easy':
        attempts = 11
    else:
        attempts = 6

    print("🎮 Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(" Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(" Good guess!")
        else:
            attempts -= 1
            print(f" Wrong guess! Attempts left: {attempts}")

        # Show current state of the word
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(" ".join(display_word))

        if '_' not in display_word:
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f" Game over! The word was '{word}'.")

hangman()
>>>>>>> 0e0a4809e687b5737b2237adb0a9c1c67e0e34c0
