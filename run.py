# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#Imports the "random" to get words for the game:
import random
import time
from word_list import word_list

#This is the display for the Hangman game:
HANGMAN = [
"""
This function will draw the hangman when the user answers the incorrect letter.
This is also directly related to the number of lives left
"""
   """
       +------------+
       |            |
       |
       |
       |
       |
       |
       +--------+
    """,
    """
       +------------+
       |            |
       |            O
       |
       |
       |
       |
       +--------+
    """,
    """
       +------------+
       |            |
       |            O
       |            |
       |
       |
       |
       +--------+
    """,
    """
       +------------+
       |            |
       |            O
       |            |
       |           /
       |
       |
       +--------+
    """,
    """
       +------------+
       |            |
       |            O
       |            |
       |           / \\
       |
       |
       +--------+
    """,
    """
       +------------+
       |            |
       |            O
       |            |\\
       |           / \\
       |
       |
       +--------+
    """,
    """
       +------------+
       |            |
       |            O
       |           /|\\
       |           / \\
       |
       |
       +--------+
    """
]

#Main Game
def game_display():
#This logo was taken with permission from previous student - Lee Martina.
#it will print the name of the game to the terminal:
    print("""
{}    {}    {}{}     {}    {}    {}}}}}    {}      {}    {}{}     {}    {}
{}    {}   {}  {}    {}}}  {}   {}    {}   {}}}  {{{}   {}  {}    {}}}  {}
{}{{}}{}  {}{{}}{}   {} {} {}   {}         {} {{}} {}  {}{{}}{}   {} {} {}
{}    {}  {}    {}   {}  {{{}   {}  {{{{   {}  {}  {}  {}    {}   {}  {{{}
{}    {}  {}    {}   {}    {}    {}}}}}    {}      {}  {}    {}   {}    {}
        """)
    print(HANGMAN[7])
    name = input("Please enter your name: \n")
    print("Welcome", name, "! Are you ready to play Hangman?")
    print("Try to guess the Irish county before your guesses run out. You have 7 guesses!")


def start_game():
    """
        This function signals the game to start.
        Its main purpose is to check the guesses left that the user has or,
        If the correct word is guessed to end the game or,
        If the hangman display is created then the game ends and teh user looses.
    """
#Main variables used:
    global word
    global current_guess
    global max_guesses
    global wrong_guesses
    global guessed_letters
    word = random.choice(word_list).upper()
    current_guess = "-" * len(word)
    max_guesses = 7
    wrong_guesses = 0
    guessed_letters = []
    while wrong_guesses < 7 and current_guess != word:
        print(HANGMAN[wrong_guesses])
        print("Letters that have been used so far: ", guessed_letters)
        print("Your guess so far: ", current_guess)
        user_guess = input("Type in your guess here: \n").upper()

""" 
The above command will make the guess uppercase.
The while statement below will check if the user selected multiple letters or numbers.
"""

        while user_guess.isdigit() or len(user_guess) != 1:
            user_guess = input("Numbers and multiple letters are not allowed. Please choose again: \n").upper()
"""
This while statement below checks if the letter has already been guessed which will through an error.
It will also add the letter to a list of letters previously used.
"""
        while user_guess in guessed_letters:
            print("You have already tried that letter:", user_guess)
            user_guess = input("Type another letter here: \n").upper()

        guessed_letters.append(user_guess)



