# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Imports words from word_list.py
from words import word_list 
import random  # Imports random library to generate random word.

"""Get word function which will get a word for the game to run.
This function will use words from the words.py file I created."""


def get_word():
    word = random.choice(word_list)
    return word.upper()  # Returns word in uppercase


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
    print(word_completion)
    print("\n")
# This is the main chunk of code here and will run until the game ends.
    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
# This will check which letters have been guessed or if the letter is valid.
            if guess in guessed_letters:
                print("You have already guessed this letter", guess)
            elif guess not in word:
                print("Your", guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else: 
                print("Great Guess", guess, "is correct!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == 
                           guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion: 
                    guessed = True
# This makes sure only letters are selected.
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guess this letter", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1 
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess. Please guess again.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
# This part of the function will let the user know if their correct or not.
    if guessed:
        print("Congratulations! You guessed the word, you Win!!")
    else:
        print("Sorry, you have run out of tries. The word was " + word + 
              ". Maybe next time!")


# Display Hangman function displays what the user will see as the game.
def display_hangman(tries):
    stages = [
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
return stages[tries]


# This is the main function that will tie the game together and allow it to 
# function.
def main():
    word = get_word()
    play(word)
# This part will allow the user to replay the game if they want.
    while input("Play Again? (Yes / No) ").upper() == "Yes":
        word = get_word()
        play(word)
# The game will no continue to run again, aslong as the user types YES.

# This part of code will make sure the game will run on the command line.
if __name__ == "__main__":
    main()
