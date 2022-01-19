"""
Imported code
"""
import gspread

sa = gspread.service_account(filename="keys.json")
sh = sa.open("pp3_hangman")

wks = sh.worksheet("user")

wks.update('A5', 'Maia')

