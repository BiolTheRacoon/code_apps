import random as rnd
import os
import time

# Difficulty settings
hard = 6
medium = 8
easy = 10

# Default difficulty
dificulty = medium
max_guesses = dificulty

def clear_screen():
    os.system('clear')  # Use 'cls' on Windows

def exit_animation():
    for i in range(4):
        dots = '.' * i + ' ' * (3 - i)
        print(f"Exiting the game  [{dots}]")
        time.sleep(1)
        clear_screen()
    os._exit(0)

def change_dif():
    global dificulty, max_guesses
    print("[hard] [medium] [easy]")
    choice = input("Choose difficulty: ").lower()
    if choice == "hard":
        dificulty = hard
    elif choice == "medium":
        dificulty = medium
    elif choice == "easy":
        dificulty = easy
    else:
        print("Error: invalid input, keeping previous difficulty.")
        return
    max_guesses = dificulty
    print(f"Difficulty set to {choice} ({dificulty} guesses)")

def number_guess():
    number = rnd.randint(1, 100)
    change_dif()
    count = 0

    while True:
        guess = input("Guess a number between 1 and 100: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)

        count += 1

        if guess > number:
            print("Guess lower!")
        elif guess < number:
            print("Guess higher!")
        else:
            print("Correct!")
            break

        if count >= max_guesses:
            print(f"Too bad, you failed. The number was {number}.")
            break

    print(f"You guessed the number in {count} tries!")
    time.sleep(2)
    clear_screen()

# Main loop
while True:
    number_guess()

    play_again = input("Wish to play again? [y/n]: ").lower()
    if play_again == "y":
        clear_screen()
        continue
    elif play_again == "n":
        exit_animation()
    else:
        print("Invalid input. Exiting.")
        exit_animation()
