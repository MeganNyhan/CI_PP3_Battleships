import random
import time

# Global variable for correctly guessed letter
correctly_guessed_letters = []

# Global variable for incorrectly guessed letter
incorrectly_guessed_letters = []

# Global variable for randomly guessed word
randomly_chosen_word = ""

# Global variable for lives left
lives_left = 6

# Global variable for game over
game_over = False


def draw_word():
    global correctly_guessed_letters
    global randomly_chosen_word

    for i in range(0, len(randomly_chosen_word)):
        letter = randomly_chosen_word[i]
        if letter in correctly_guessed_letters:
            print(letter, end=" ")
        else: 
            print("_", end=" ")
    print("")


def draw_hangman():
    """
        This function will draw the hangman when the user
        answers the incorrect letter.
        This is also directly related to the number of 
        lives left
    """
    global lives_left

    if lives_left == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+--------+")
    elif lives_left == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+--------+")
    elif lives_left == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+--------+")
    elif lives_left == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           /")
        print("|")
        print("|")
        print("+--------+")
    elif lives_left == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           / \\")
        print("|")
        print("|")
        print("+--------+")
    elif lives_left == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+--------+")
    elif lives_left == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+--------+")


def get_one_valid_letter():
    """
        This function will make sure the user only types in 1
        letter that hasn't previously been used.
        It will also prompt the user to input a letter.
    """
    is_letter_valid = False
    letter = ""
    while is_letter_valid is False:
        letter = input("Enter a letter: ")
        letter = letter.strip().lower()
        if len(letter) <= 0 or len(letter) > 1:
            print("Only one letter can be entered")
        elif letter.isalpha():
            if letter in correctly_guessed_letters or letter in incorrectly_guessed_letters:
                print("You have already guessed the letter " + letter + ", please try again")
            else:
                print("Your Letter must be (A-Z)")

    return letter
                


