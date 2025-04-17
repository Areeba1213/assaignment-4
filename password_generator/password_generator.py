<<<<<<< HEAD
import random
import string

def generate_password(length=12):
    if length < 4:
        return "Too short!"
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

try:
    user_length = int(input("Enter desired password length: "))
    amount = int(input("How many passwords do you want? (at least 10): "))

    if amount < 10:
        print(" Please enter at least 10.")
    else:
        print(f"\n Generating {amount} passwords of length {user_length}...\n")
        for i in range(1, amount + 1):
            print(f"{i}. {generate_password(user_length)}")

except ValueError:
    print(" Please enter valid numbers.")

=======
import random
import string

def generate_password(length=12):
    if length < 4:
        return "Too short!"
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

try:
    user_length = int(input("Enter desired password length: "))
    amount = int(input("How many passwords do you want? (at least 10): "))

    if amount < 10:
        print(" Please enter at least 10.")
    else:
        print(f"\n Generating {amount} passwords of length {user_length}...\n")
        for i in range(1, amount + 1):
            print(f"{i}. {generate_password(user_length)}")

except ValueError:
    print(" Please enter valid numbers.")

>>>>>>> 0e0a4809e687b5737b2237adb0a9c1c67e0e34c0
