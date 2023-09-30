import random

# Global variables to store game state
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10
guesses = []

def get_user_guess():
    try:
        guess = int(input("Enter your guess (1-100): "))
        return guess
    except ValueError:
        print("Please enter a valid number.")
        return get_user_guess()

def play_game():
    global attempts
    global guesses

    if attempts < max_attempts:
        guess = get_user_guess()
        guesses.append(guess)

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts + 1} attempts.")
            print("Your guesses:", guesses)
        elif guess < number_to_guess:
            print("Try higher.")
            attempts += 1
            play_game()
        else:
            print("Try lower.")
            attempts += 1
            play_game()
    else:
        print(f"Sorry, you've reached the maximum number of attempts ({max_attempts}). The number was {number_to_guess}.")
        print("Your guesses:", guesses)

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("I've selected a random number between 1 and 100. Try to guess it.")
    play_game()
