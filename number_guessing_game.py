from random import randint
from art import logo

# Constants for the number of turns based on difficulty
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check the user's guess against the actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks the user's guess against the actual answer and returns the remaining turns."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return -1  # Indicates the game is over

# Function to set the difficulty level
def set_difficulty():
    """Sets the difficulty level and returns the number of turns."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Invalid input. Defaulting to 'easy'.")
        return EASY_LEVEL_TURNS

# Main game function
def game():
    print(logo)
    """Runs the Number Guessing Game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)  # Randomly generate the answer
    # Debugging line (optional): print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()  # Set the number of turns based on difficulty
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != answer:
        # Let the user guess a number
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Check the guess and update the number of turns
        turns = check_answer(guess, answer, turns)
        if turns == -1:  # Game over (correct guess)
            return
        elif turns == 0:  # No more turns left
            print("You've run out of guesses, you lose.")
            print(f"The correct answer was {answer}.")
            return
        else:
            print(f"You have {turns} attempts remaining to guess the number.")

# Run the game
game()
