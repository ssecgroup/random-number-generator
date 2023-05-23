import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")

    while True:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            break

guess_number()
