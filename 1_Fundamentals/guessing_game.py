import math
import random

running = True

#Get Value helps to get input from the user and validate for presence
def getValue(val_name):
    print(f"Enter {val_name}: ")
    value = input()
    if(value == ""):
        print("Value Cannot Be Empty")
        getValue()
    else:
        return value
#Get Int uses getValue and then also validates for type int
def getInt(val_name):
    try:
        return int(getValue(val_name))
    except ValueError:
        print("Value Must Be a Number")
        return getInt(getValue(val_name))

def play_game():
    max = getInt("Enter the maximum integer: ")
    min = getInt("Enter the minimum integer: ")
    minTries =  math.ceil(math.log(max-min,2))
    tries = 0
    print(f"To guess the number between {min} and {max}, Computer has {minTries} tries.")
    while tries < minTries:
        try:
            guess = random.randint(min,max)
        except ValueError:
            print("Stop cheating!")
            print(f"Computer has guessed the number! It took {tries + 1} tries!")

        correct = input(f"Is {guess} the correct number? (y/n)").lower() == "y"
        if(not(correct)):
            highLow = input("Higher or Lower? (h/l)").lower() == "h"
            try:
                if(highLow):
                    min = guess + 1
                else:
                    max = guess - 1
            except ValueError:
                print("Stop cheating!")
                print(f"Computer has guessed the number! It took {tries + 1} tries!")
        else:
            print(f"Computer has guessed the number! It took {tries + 1} tries!")
            break
        tries += 1

    if(tries == minTries):
        print("Computer has run out of tries and failed to guess the number.")
        print(f"The number was between {min} and {max}")
        print("The human clearly cheated!")

def exit_game():
    global running
    running = False
    print("Exiting...")

def main_menu():
    print("Welcome to the Number Guessing Game!")
    print("1. Play Game")
    print("2. Exit")
    choice = getInt("Your choice")
    if choice == 1:
        play_game()
    elif choice == 2:
        exit_game()
    else:
        print("Invalid choice. Please try again.")

try:
    while running == True:
        main_menu()
except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting...")
    running = False