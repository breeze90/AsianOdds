import json

with open("games.json", "r") as json_file:
    games = json.load(json_file)

# CSVfor game in games:
# #     if game['PnlInfo'] == "Won" or game['PnlInfo'] == "Lost":
# #         print(
# #             f"{game['LeagueName']},{game['HomeName']} - {game['AwayName']},{game['HomeScore']}:{game['AwayScore']},"
# #             f"{game['FullTimeHomeScore']}:{game['FullTimeAwayScore']},{round(game['Odds'], 3)},{game['Bookie']},"
# #             f"{game['BetType']},{game['PnlInfo']}")
#

# Excel
for game in games:
    if game['PnlInfo'] == "Won":
        print(
            f"{game['LeagueName']},{game['HomeName']} - {game['AwayName']},{game['HomeScore']}:{game['AwayScore']},"
            f"{game['FullTimeHomeScore']}:{game['FullTimeAwayScore']},{round(game['Odds'], 3)},{game['Bookie']},"
            f"{game['BetType']},{game['PnlInfo']},{round(round(game['Odds'], 3) * 1 - 1, 2)}")
    elif game['PnlInfo'] == "Lost":
        print(
            f"{game['LeagueName']},{game['HomeName']} - {game['AwayName']},{game['HomeScore']}:{game['AwayScore']},"
            f"{game['FullTimeHomeScore']}:{game['FullTimeAwayScore']},{round(game['Odds'], 3)},{game['Bookie']},"
            f"{game['BetType']},{game['PnlInfo']},{-1}")
