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

