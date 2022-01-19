import gspread

sa = gspread.service_account(filename="creds.json")
sh = sa.open("pp3_hangman")

wks = sh.worksheet("user")

# print('rows: ', wks.row_count)
# print('cols: ', wks.col_count)

print(wks.acell('A1').value)
