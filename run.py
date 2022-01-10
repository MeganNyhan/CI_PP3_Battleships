# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import word_list


# Get word function.
# This will generate random words from my words.py list.
# It will also return the users input with an uppercase.
def get_word():
    word = random.choice(word_list)
    return word.upper()

# Play function.
# This is the main function that will run the game.
# This is also the introduction to the game for the user.


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    # This is the introduction for the user.
    print("Are you ready to play Hangman?")
    print(display_hangman(tries))
    print(word_completion)
    print(" \n")
    while not guessed and tries > 0:
        # This is the input for the users guesses.
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter", guess)
            elif guess not in word:
                # This will let the user know if the guess they have guessed 
                # is incorrect.
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                # This will let the user know if the guess they have guessed 
                # is correct.
                print("Great guess,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == 
                           guess]
                for index in indices:
                    word_as_list[index] = guess 
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guess this word", guess)
                # This will let the user know that they have already guessed 
                # word and need to replay the game.
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Sorry the guess you entered is not valid")
            # This will come up if the guess is invalid as in a number.
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the CORRECT word. \
              You are the winner!")
    else:
        print("Sorry, you have run out of tries"
              "the word was" + word + ". Why not try again!")
        
    
def display_hangman(tries):
    stages = [  # This is the hangman visual. Final state = full body.
                """
      +------------+
      |            |
      |            O
      |           /|\\
      |           / \\
      |
      |
      +--------+
   """,
                # This is the second last state with just the arm missing.
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
                # This state has everything but both arms.
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
                # This state has everything but both arms and a leg.
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
                # This state has only the head and body.
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
                # This state has only the head.
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
                # This state has only the noose.
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
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    # This function runs the game or allows the user to replay.
    while input("Play Again? (YES / NO) ").upper() == "YES":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()



