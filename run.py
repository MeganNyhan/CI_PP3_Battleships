# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#Imports the "random" to get words for the game
import random
import time
from word_list import word_list

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


def choose_random_word():
    """
        This will choose a random word selected from the list
        below.
    """
    global randomly_chosen_word

    acceptable_words = [
        "Donegal",
        "Derry",
        "Offlay",
        "Loais",
        "Cavan",
        "Dublin"
    ]

    random.seed(time.time())
    randomly_chosen_word = random.choice(acceptable_words)
    randomly_chosen_word = randomly_chosen_word.lower()


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
                

def guess_letter():
    """
        This function will check if the letter is correct or wrong,
        and update global variabled based on the result.
    """
    global correctly_guessed_letters
    global incorrectly_guessed_letters
    global lives_left

    letter = get_one_valid_letter()
    if letter in randomly_chosen_word:
        correctly_guessed_letters.append(letter)
    else:
        incorrectly_guessed_letters.append(letter)
        lives_left -= 1


def check_for_game_over():
    """
    This function check to see if the user has lost
    """
    global lives_left
    global game_over
    global correctly_guessed_letters

    if lives_left <= 0:
        game_over = True
        draw_hangman()
        print(
              "You lost! The word was ", + randomly_chosen_word +, ". " Try again next time! ")


    else:
        guessed_all_letters = True
        for letter in randomly_chosen_word:
            if letter not in correctly_guessed_letters:
                guessed_all_letters = False
                break
        if guessed_all_letters:
            game_over = True
            print("Congratulations! You have won! Feel free to play again.")


def main():
    """
        The entry point of the application.
        This will call all other functions in the game loop"
    """
    global game_over

    print("-------- Welcome to the Irish County Hangman Challenge!!! --------")
    choose_random_word()

    while game_over is False:
        draw_hangman()
        draw_word()

        if len(incorrectly_guessed_letters) > 0:
            print("Incorrect Guess: ")
            print(incorrectly_guessed_letters)

        guess_letter()
        check_for_game_over()


# if __name__ == '__main__':
#     """ 
#     This will only be called when you run the python program from the termanial or an IDE like PyCharms
#     """

