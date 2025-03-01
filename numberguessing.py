
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    target_number = random.randint(1, 10)  # Random number between 1 and 100
    attempts = 0

    while True:
        try:
            
            
            guess = int(input("Enter your guess (1-10): "))
            
            attempts += 1
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the number in", attempts, "attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()
