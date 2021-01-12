import json
import datetime

with open("games1.json", "r") as json_file:
    games = json.load(json_file)


for game in games:
    if 'result' in game:
        if game['result'] == "Won":
            print(
                f"{game['startTime']},"
                f"{game['leagueName']},{game['homeName']} - {game['awayName']},{game['homeTeamRedCards']}:{game['awayTeamRedCards']},{game['homeScore']}:{game['awayScore']},"
                f"{game['fullTimeHomeScore']}:{game['fullTimeAwayScore']},{round(game['odds'], 3)},{game['bookie']},"
                f"{game['minute']},{game['betType']},{game['result']},{round(round(game['odds'], 3) * 1 - 1, 2)}")
        elif game['result'] == "Lost":
            print(
                f"{game['startTime']},"
                f"{game['leagueName']},{game['homeName']} - {game['awayName']},{game['homeTeamRedCards']}:{game['awayTeamRedCards']},{game['homeScore']}:{game['awayScore']},"
                f"{game['fullTimeHomeScore']}:{game['fullTimeAwayScore']},{round(game['odds'], 3)},{game['bookie']},"
                f"{game['minute']},{game['betType']},{game['result']},{-1}")
