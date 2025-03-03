from random import randint
easy_level = 10
hard_level = 5

def check_answer(guess, answer, turn):
    if guess > answer:
        print("too high")
        return turn -1
    elif guess< answer:
        print("too low")
        return turn -1
    else:
        print(f"u guesses correctly answer is {answer}")
        return 0







def set_deiff_lvl():
    level = input("do you want it easy or hard: ").lower()
    if level == "easy":
        return easy_level
    elif level == "hard":
        return hard_level
    else:
        print("Invalid choice! Defaulting to 'easy'.")
        return easy_level
    



def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    guess = -1
    turn = set_deiff_lvl()
    while guess != answer and turn > 0:
        print(f"u have {turn} left guess ")
        guess = int(input("write ur guess: "))
        turn = check_answer(guess, answer, turn)
        if turn == 0 and guess != answer:
            print(f"u lost try again the correct answer was {answer}")
            1
        elif turn > 0 and guess!= answer:
            print("guess again")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        game()  # Restart the game
    else:
        print("Thanks for playing! Goodbye.")
game()


