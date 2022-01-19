import gspread

sa = gspread.service_account(filename="creds.json")
sh = sa.open("pp3_hangman")

wks = sh.worksheet("user")


