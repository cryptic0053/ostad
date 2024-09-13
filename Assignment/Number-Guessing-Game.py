import random

print("Welcome to the Number Guessing Game!\n"
      "Try to guess the number between 1 and 100\n")
comp_input = random.randint(1, 100)
user_input = None
counter = 0

while user_input != comp_input:
    try:
        user_input = int(input("Enter your guess: "))
        counter += 1
        if (user_input < comp_input):
            print("Too low!\n")
        elif (user_input > comp_input):
            print("Too high!\n")
        else:
            print(f"Congratulations! You've guessed the number in {counter} attempts.")
    except ValueError:
        print("Invalid input.Enter integer value.")
