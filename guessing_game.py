"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import statistics

guess_list = []


def authy(new_guess, new_answer):
    if new_guess > new_answer:
        print("too high")
    elif new_guess < new_answer:
        print("too low")


def guesses(new_guess):
    guess_list.append(new_guess)
    print(guess_list)


def start_game():
    print("Welcome to the guessing game")
    answer = random.randint(1, 100)
    print(answer)
    while True:
        try:
            guess = int(input("Enter a number: "))
            if guess < 1 or guess > 100:
                raise ValueError("Enter a number between 1 and 100")
        except ValueError as err:
            print(f'Please enter a valid number. {err}')

        else:
            authy(guess, answer)
            if guess == answer:
                print("You won")
                break

    play_again = input("Do you want to play again: y/n? ").lower()
    if play_again == "y":
        start_game()
    else:
        print("Good bye, hope you enjoyed the game")


start_game()

#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
