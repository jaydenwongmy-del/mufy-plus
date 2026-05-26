import random

# 1. Ask user their name
name = input("What is your name? ")

# 2 & 3. Create lists
adjectives = ["Sneaky", "Silent", "Brave", "Clever", "Fierce", "Mysterious"]
animals = ["Otter", "Panther", "Falcon", "Wolf", "Tiger", "Fox"]

# 4 & 5. Generate codename
codename = random.choice(adjectives) + " " + random.choice(animals)

# 6. Generate lucky number (1–99)
lucky_number = random.randint(1, 99)

# 7. Display result
print(f"Welcome Agent {name}!")
print(f"Your spy codename is: {codename}")
print(f"Your lucky number is: {lucky_number}")