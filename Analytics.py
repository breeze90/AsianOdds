import json
import datetime

with open("games.json", "r") as json_file:
    games = json.load(json_file)

games_file = open("games_stats.csv", "w")

for game in games:
    if game['PnlInfo'] == "Won":
        games_file.write(
            f"{datetime.datetime.fromtimestamp(game['TicketDate'] / 1000.0, tz=datetime.timezone.utc).strftime('%d.%m.%Y')},"
            f"{game['LeagueName']},{game['HomeName']} - {game['AwayName']},{game['HomeScore']}:{game['AwayScore']},"
            f"{game['FullTimeHomeScore']}:{game['FullTimeAwayScore']},{round(game['Odds'], 3)},{game['Bookie']},"
            f"{game['BetType']},{game['PnlInfo']},{round(round(game['Odds'], 3) * 1 - 1, 2)}")
        games_file.write("\n")
    elif game['PnlInfo'] == "Lost":
        games_file.write(
            f"{datetime.datetime.fromtimestamp(game['TicketDate'] / 1000.0, tz=datetime.timezone.utc).strftime('%d.%m.%Y')},"
            f"{game['LeagueName']},{game['HomeName']} - {game['AwayName']},{game['HomeScore']}:{game['AwayScore']},"
            f"{game['FullTimeHomeScore']}:{game['FullTimeAwayScore']},{round(game['Odds'], 3)},{game['Bookie']},"
            f"{game['BetType']},{game['PnlInfo']},{-1}")
        games_file.write("\n")
