# Step 1: Welcome message
print("Welcome to the Mad Libs Game!")

# Step 2: User se inputs lo
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")

# Step 3: Story create karo using user inputs
story = f"""
Once upon a time in {place}, there was a {adjective} {noun}.
Every day, it would {verb} all around the town and make everyone laugh.
It became the hero of {place}!
"""

# Step 4: Story display karo
print("\nHere's your Mad Libs story!")
print(story)
