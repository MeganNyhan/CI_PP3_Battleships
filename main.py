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


def draw_word()
    global correctly_guessed_letters
    global randomly_chosen_word

    for i in range(0, len(randomly_chosen_word)):
        letter - randomly_chosen_word[i]
        if letter in correctly_guessed_letters:
            print(letter, end= " ")
        else: 
            print("_", end=" ")
    print("")