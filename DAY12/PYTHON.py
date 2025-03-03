from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
    """Check if the guess is correct and return updated turns."""
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You guessed correctly! The answer is {answer}")
        return 0  # Indicating the game is won

def set_difficulty():
    """Set difficulty level based on user input."""
    level = input("Do you want it 'easy' or 'hard'? ").lower()
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL
    else:
        print("Invalid choice! Defaulting to 'easy'.")
        return EASY_LEVEL

def game():
    """Main game loop."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)  # Random number
    turns = set_difficulty()  # Get difficulty level
    guess = -1

    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining.")
        try:
            guess = int(input("Enter your guess: "))  # Ensure input is a number
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        turns = check_answer(guess, answer, turns)

        if turns == 0 and guess != answer:
            print(f"You lost! The correct answer was {answer}.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        game()  # Restart the game
    else:
        print("Thanks for playing! Goodbye.")

game()  # Start the game
