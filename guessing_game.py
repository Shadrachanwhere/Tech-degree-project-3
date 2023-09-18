"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import statistics

guess_list = []


def stats(stats_of_guess):
    print("=+Overall statistics+=")
    print(f"mean : {round(statistics.mean(stats_of_guess))}")
    print(f"mode: {statistics.mode(stats_of_guess)}")
    print(f"median: {statistics.median(stats_of_guess)}")


def guesses(new_guess):
    guess_list.append(new_guess)


def start_game():
    high_score = 0
    print("Welcome to **Guess** **That** **Number**")
    print("Guess a number between 1 and 100")
    answer = random.randint(1, 100)
    print(answer)
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess > 100 or guess < 1:
                raise ValueError("Try entering  a number between 1 and 100")
        except ValueError as err:
            print(f"{err}")
        else:
            guesses(guess)
            if guess < answer:
                print("Too low. Try again")
            elif guess > answer:
                print("Too high. Try again")
            elif guess == answer:
                print("You got it")
                break

    attempts = len(guess_list)
    high_score = attempts
    print(f"Way to go, you guessed it in {attempts} tries")
    stats(guess_list)
    play_again = input("Would you like to play again? [y/n]? ").lower()
    if play_again == "y":
        print(f"can you beat the high score of {high_score}")
        guess_list.clear()
        start_game()
    else:
        print("Closing the game! Thanks for playing")


start_game()


