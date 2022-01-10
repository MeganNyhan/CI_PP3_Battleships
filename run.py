# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Imports words from word_list.py
from words import word_list 
import random  # Imports random library to generate random word.

# Get word function which will get a word for the game to run.
# This function will use words from the words.py file I created.
def get_word():
    word = random.choice(word_list)
    return word.upper ()  # Returns word in uppercase


def play(word):
    # The play function holds most of the functionality of the game.
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 7
    # This part of the function will guide the user through the game.
    print("Are you ready to play hangman?")
    print(display_hangman(tries))


# Display Hangman function displays what the user will see as the game.
def display_hangman(tries):
    stages = [ """ 
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
return stages[tries]
