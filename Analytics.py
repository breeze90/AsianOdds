import json
import datetime

with open("games.json", "r") as json_file:
    games = json.load(json_file)

for game in games:
    if game['PnlInfo'] == "Won":
        print(
            f"{datetime.datetime.fromtimestamp(game['TicketDate'] / 1000.0, tz=datetime.timezone.utc).strftime('%d.%m.%Y')},"
            f"{game['LeagueName']},{game['HomeName']} - {game['AwayName']},{game['HomeScore']}:{game['AwayScore']},"
            f"{game['FullTimeHomeScore']}:{game['FullTimeAwayScore']},{round(game['Odds'], 3)},{game['Bookie']},"
            f"{game['BetType']},{game['PnlInfo']},{round(round(game['Odds'], 3) * 1 - 1, 2)}")
    elif game['PnlInfo'] == "Lost":
        print(
            f"{datetime.datetime.fromtimestamp(game['TicketDate'] / 1000.0, tz=datetime.timezone.utc).strftime('%d.%m.%Y')},"
            f"{game['LeagueName']},{game['HomeName']} - {game['AwayName']},{game['HomeScore']}:{game['AwayScore']},"
            f"{game['FullTimeHomeScore']}:{game['FullTimeAwayScore']},{round(game['Odds'], 3)},{game['Bookie']},"
            f"{game['BetType']},{game['PnlInfo']},{-1}")
