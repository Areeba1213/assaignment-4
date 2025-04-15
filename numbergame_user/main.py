def computer_guesses():
    print("🎮 Think of a number between 1 and 100, and I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        if low > high:
            print("Hmm 🤔 something's not right. Are you sure you're giving correct hints?")
            break

        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == 'c':
            print(f"🎉 Yay! I guessed it in {attempts} attempts.")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Please type 'H', 'L', or 'C'.")

computer_guesses()
