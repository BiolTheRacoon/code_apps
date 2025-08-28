import random as rnd
import os
import time

def number_guess():
    number = rnd.randint(1, 100)
    count = 0

    while True:
        guess = input("Guess a number between 1 and 100: ")
        guess = int(guess)

        if guess > number:
            print("Guess lower!")
            count += 1

        elif guess < number:
            print("Guess higher!")
            count += 1

        else:
            print("Correct!")
            time.sleep(2)
            os.system('clear')
            break


    print(f"You guessed the number in {count} tries!")
    time.sleep(2)
    os.system('clear')

while True:
    number_guess()

    print("wish to play again?")
    play_again = input("[y/n]: ")

    if play_again == "y":
        os.system('clear')
        continue
    elif play_again == "n":
        print("Thanks for playing!")
        os.system('clear')
        print("Exiting the game  [   ]")
        time.sleep(1)
        os.system('clear')
        print("Exiting the game  [.  ]")
        time.sleep(1)
        os.system('clear')
        print("Exiting the game  [.. ]")
        time.sleep(1)
        os.system('clear')
        print("Exiting the game  [...]")
        time.sleep(1)
        os.system('clear')
        os._exit(0)
    else:
        print("Invalid input.")
        time.sleep(2)
        os.system('clear')
        print("Exiting the game  [   ]")
        time.sleep(1)
        os.system('clear')
        print("Exiting the game  [.  ]")
        time.sleep(1)
        os.system('clear')
        print("Exiting the game  [.. ]")
        time.sleep(1)
        os.system('clear')
        print("Exiting the game  [...]")
        time.sleep(1)
        os.system('clear')
        os._exit(0) 
 

