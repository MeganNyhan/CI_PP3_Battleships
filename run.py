"""
Imports
"""
import random
import gspread

from words import word_list
sa = gspread.service_account(filename="creds.json")
sh = sa.open("pp3_hangman")

wks = sh.worksheet("user")


def get_word():
    """
    Get word function.
    This will generate random words from my words.py list.
    It will also return the users input with an uppercase.
    """
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    Play function.
    This is the main function that will run the game.
    This is also the introduction to the game for the user.
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    # This is the introduction for the user.
    print("Are you ready to play Hangman, the Irish county edition?")
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
        print("Congratulations, you guessed the CORRECT word. You WON!")
    else:
        print("Sorry, you have run out of tries"
              "the word was " + word + ". Why not try again!")


def display_hangman(tries):
    """
    This function will display the main hangman game.
    As the user plays each stage will appear depending on the guess.
    """
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
    """
    This will prin the logo for the game.
    This appears in the main introduction before the game starts.
    """
    print("""
{}    {}    {}{}     {}    {}    {}}}}}    {}      {}    {}{}     {}    {}
{}    {}   {}  {}    {}}}  {}   {}    {}   {}}}  {{{}   {}  {}    {}}}  {}
{}{{}}{}  {}{{}}{}   {} {} {}   {}         {} {{}} {}  {}{{}}{}   {} {} {}
{}    {}  {}    {}   {}  {{{}   {}  {{{{   {}  {}  {}  {}    {}   {}  {{{}
{}    {}  {}    {}   {}    {}    {}}}}}    {}      {}  {}    {}   {}    {}
        """)
    name = input("Enter your name: \n")
    print("Welcome", name, "!")

    word = get_word()
    play(word)
    # This function runs the game or allows the user to replay.
    while input("Play Again? (YES / NO) ").upper() == "YES":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()

# Google documentation
# from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Generate the credentials needed for code
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1Kv6gYod8qPLaEcLNhIDdd2mJUdZzBqcSu1wEqHsS4YQ'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="user!a3:b3").execute()
values = result.get('values', [])

name = [{name}]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                            range="user!a3:b4", valueInputOption="USER_ENTERED", body={"values": name}).execute()

print(values)
