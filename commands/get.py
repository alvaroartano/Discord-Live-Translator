import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import time
from commands import translate


# Sheet 0 is Guilds
# Sheet 1 is Channels
# Sheet 2 is Admins
# Sheet 3 is Logs


# define the scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name(
    './google_sheets_api_key.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Database Hackapalooza Discord Translator')


def getguilds():
    # get the guilds sheet
    guilds_sheet = sheet.get_worksheet(0)
    # get the data from the sheet
    guilds_data = guilds_sheet.get_all_records()
    # return the dataframe
    return guilds_data


def addguild(guildId, guildName, usern):
    print("Added to guild! Adding to google Sheet...")
    # get current time
    current_time = time.strftime(f"%d/%m/%y %H:%M:%S")

    # get the guilds sheet
    guilds_sheet = sheet.get_worksheet(0)

    # append row containing data
    guilds_sheet.append_row([str(guildId), guildName, usern, current_time])
    print("Succesfully added channel!")


def addChannel(guildId, channelId, lang):
    print(lang)

    if checkChannel(channelId) != False:
        print("Channel already exists!")
        return

    for language in translate.getlanguages():
        if language['code'] == lang:

            print("New channel configured! Adding to google Sheet...")

            current_time = time.strftime(f"%d/%m/%y %H:%M:%S")

            # get the channels sheet
            channels_sheet = sheet.get_worksheet(1)

            # append row containing data
            channels_sheet.append_row(
                [str(guildId), str(channelId), lang, language['name'], current_time])
            print("Succesfully added channel!")
            return True
        else:
            print("no compared")
    return False


def checkChannel(channelId):
    print("starting")
    # get the channels sheet
    channels_sheet = sheet.get_worksheet(1)
    # get the data from the sheet
    channels_data = channels_sheet.get_all_records()
    print(channels_data)
    if channels_data:
        # return the dataframe
        for channel in channels_data:
            if channel['Channel ID'] == channelId:
                return channel['LangIso']
        return False
    return False
