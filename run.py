# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#Imports the "random" to get words for the game
import random
import time
from word_list import word_list

#This is the display for the Hangman game:
HANGMAN = [
   """
       This function will draw the hangman when the user
       answers the incorrect letter.
       This is also directly related to the number of
       lives left
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

