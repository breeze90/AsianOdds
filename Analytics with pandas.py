import pandas as pd

games = pd.read_csv("games.csv", names=["Date", "League", "Game", "Score", "FinalScore", "Odds", "Bookie", "Type",
                                        "Result", "+/-"])

scores_and_stats_dict = {
    '0:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '1:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '2:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '1:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '2:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '2:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '3:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '3:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '3:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '0:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '0:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '1:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '0:3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '1:3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '2:3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0}
}

leagues_and_stats_dict = {
    '*ENGLISH PREMIER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                                '+/-': 0},
    'ENGLISH CHAMPIONSHIP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '*GERMANY BUNDESLIGA': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'GERMANY BUNDESLIGA 2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'GERMANY BUNDESLIGA 3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '*ITALY SERIE A': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '*SPAIN LA LIGA': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    '*UEFA CHAMPIONS LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                               '+/-': 0},
    '*UEFA EUROPA LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'AUSTRIA BUNDESLIGA': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'AUSTRIA ERSTE LIGA': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'BELGIUM FIRST DIVISION A': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                                 '+/-': 0},
    'BELGIUM FIRST DIVISION B': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                                 '+/-': 0},
    'CZECH REPUBLIC FIRST LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                                    '+/-': 0},
    'DENMARK SUPER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'FRANCE LIGUE 1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'GEORGIA EROVNULI LIGA': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                              '+/-': 0},
    'GREECE SUPER LEAGUE 1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                              '+/-': 0},
    'HOLLAND EERSTE DIVISIE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                               '+/-': 0},
    'HOLLAND EREDIVISIE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'NORTHERN IRELAND PREMIERSHIP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                                     '+/-': 0},
    'NORWAY ELITESERIEN': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'ROMANIA LIGA 1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'SWITZERLAND SUPER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                                 '+/-': 0},
    'SWITZERLAND CHALLENGE LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                                     '+/-': 0},
    'TURKEY SUPER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
    'TURKEY TFF FIRST LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                                '+/-': 0},
    'UKRAINE PREMIER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0,
                               '+/-': 0},
    'WALES PREMIER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0}
}


def scores_and_stats():
    for key, value in scores_and_stats_dict.items():
        for index, row in games.iterrows():
            if row["Score"] == key:
                value['Матчи'] += 1
                if row["Result"] == 'Won':
                    value['Победы'] += 1
                    value['+/-'] += round(row["+/-"], 2)
                    value["Коэф."] += row["Odds"]
                elif row["Result"] == 'Lost':
                    value['Поражения'] += 1
                    value['+/-'] += round(row["+/-"], 2)
    for key, value in scores_and_stats_dict.items():
        value['Win%'] = round(value['Победы'] * 100 / value['Матчи'], 2)
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['+/-'] = round(value['+/-'], 2)
        value['ROI'] = round(value['+/-'] * 100 / value['Матчи'], 2)
    for key, value in scores_and_stats_dict.items():
        print(key, value)


def leagues_and_stats():
    for key, value in leagues_and_stats_dict.items():
        for index, row in games.iterrows():
            if row["League"] == key:
                value['Матчи'] += 1
                if row["Result"] == 'Won':
                    value['Победы'] += 1
                    value['+/-'] += round(row["+/-"], 2)
                    value["Коэф."] += row["Odds"]
                elif row["Result"] == 'Lost':
                    value['Поражения'] += 1
                    value['+/-'] += round(row["+/-"], 2)
    for key, value in leagues_and_stats_dict.items():
        if value['Победы'] == 0:
            continue
        value['Win%'] = round(value['Победы'] * 100 / value['Матчи'], 2)
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['+/-'] = round(value['+/-'], 2)
        value['ROI'] = round(value['+/-'] * 100 / value['Матчи'], 2)
    # for key, value in leagues_and_stats_dict.items():
    #     print(key, value)
    for i in sorted(leagues_and_stats_dict.items(), key=lambda item: item[1]['Матчи'], reverse=True):
        print(i)


def overall(games_csv):
    print(games_csv.to_string())
    print("Games:", games_csv.shape[0])
    print("Won:", int(games_csv[games_csv['Result'] == "Won"].shape[0]))
    print("Lost:", games_csv[games_csv['Result'] == "Lost"].shape[0])
    print("Win%:", round(int(games_csv[games_csv['Result'] == "Won"].shape[0]) * 100 / games_csv.shape[0], 2))
    print("WinOdds:", round(games.loc[games['Result'] == "Won", "Odds"].mean(), 3))
    print("ROI:", round(games_csv["+/-"].sum() * 100 / games_csv.shape[0], 2))
    print("+/-", round(games_csv["+/-"].sum(), 2))


# def day_period(day):
#     print(games.to_string())
#     print("Games:", games_csv.shape[0])
#     print("Won:", int(games_csv[games_csv['Result'] == "Won"].shape[0]))
#     print("Lost:", games_csv[games_csv['Result'] == "Lost"].shape[0])
#     print("Win%:", round(int(games_csv[games_csv['Result'] == "Won"].shape[0]) * 100 / games_csv.shape[0], 2))
#     print("WinOdds:", round(games.loc[games['Result'] == "Won", "Odds"].mean(), 3))
#     print("ROI:", round(games_csv["+/-"].sum() * 100 / games_csv.shape[0], 2))
#     print("+/-", round(games_csv["+/-"].sum(), 2))


def certain_period(sample1, sample2):
    print(games.iloc[sample1: sample2].to_string())
    print('Games:', games.iloc[sample1: sample2].shape[0])
    current_games = games.iloc[sample1: sample2]
    print("Won:", int(current_games[current_games['Result'] == "Won"].shape[0]))
    print("Lost:", current_games[current_games['Result'] == "Lost"].shape[0])
    print("Win%:",
          round(int(current_games[current_games['Result'] == "Won"].shape[0]) * 100 / current_games.shape[0], 2))
    print("WinOdds:", round(current_games.loc[current_games['Result'] == "Won", "Odds"].mean(), 3))
    print("ROI:", round(current_games["+/-"].sum() * 100 / current_games.shape[0], 2))
    print("+/-", round(current_games["+/-"].sum(), 2))


def score_result(score):
    print(games[games["Score"] == score].head(1000).to_string())

    print("Games:", games[games['Score'] == score].shape[0])
    print("Won:", games.loc[(games['Score'] == score) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Score'] == score) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Score'] == score)].shape[0]) * 100 /
                games[games['Score'] == score].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['Score'] == score) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("ROI", round(games.loc[games['Score'] == score, "+/-"].sum() *
                       100 / games[games['Score'] == score].shape[0], 2))
    print("+/-:", round(games.loc[games['Score'] == score, "+/-"].sum(), 2))


def league_result(league):
    print(games[games['League'] == league].head(1000).to_string())

    print("Games:", games[games['League'] == league].shape[0])
    print("Won:", games.loc[(games['League'] == league) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['League'] == league) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['League'] == league)].shape[0]) * 100 /
                games[games['League'] == league].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['League'] == league) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("ROI", round(games.loc[games['League'] == league, "+/-"].sum() *
                       100 / games[games['League'] == league].shape[0], 2))
    print("+/-:", round(games.loc[games['League'] == league, "+/-"].sum(), 3))


def bet_type(bet):
    print(games[games['Type'] == bet].head(1000).to_string())
    print("Games:", games[games['Type'] == bet].shape[0])
    print("Won:", games.loc[(games['Type'] == bet) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Type'] == bet) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Type'] == bet)].shape[0]) * 100 /
                games[games['Type'] == bet].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['Type'] == bet) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("ROI", round(games.loc[games['Type'] == bet, "+/-"].sum() *
                       100 / games[games['Type'] == bet].shape[0], 2))
    print("+/-:", round(games.loc[games['Type'] == bet, "+/-"].sum(), 3))


def bet_type_and_score(bet, score):
    print(games.loc[(games['Type'] == bet) & (games['Score'] == score)].head(1000).to_string())
    print("Games:", games.loc[(games['Type'] == bet) & (games['Score'] == score)].shape[0])
    print("Won:", games.loc[(games['Type'] == bet) & (games['Score'] == score) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Type'] == bet) & (games['Score'] == score) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Type'] == bet) & (games['Score'] == score)].shape[
                        0]) * 100 /
                games[games['Type'] == bet].shape[0], 2))
    print("WinOdds:", round(
        games.loc[(games['Type'] == bet) & (games['Score'] == score) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("ROI", round(games.loc[(games['Type'] == bet) & (games['Score'] == score), "+/-"].sum() *
                       100 / games[games['Type'] == bet].shape[0], 2))
    print("+/-:", round(games.loc[(games['Type'] == bet) & (games['Score'] == score), "+/-"].sum(), 3))


def bookie_stats(bookie):
    print(games[games['Bookie'] == bookie].head(1000).to_string())
    print("Games:", games[games['Bookie'] == bookie].shape[0])
    print("Won:", games.loc[(games['Bookie'] == bookie) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Bookie'] == bookie) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Bookie'] == bookie)].shape[0]) * 100 /
                games[games['Bookie'] == bookie].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['Bookie'] == bookie) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("ROI", round(games.loc[games['Bookie'] == bookie, "+/-"].sum() *
                       100 / games[games['Bookie'] == bookie].shape[0], 2))
    print("+/-:", round(games.loc[games['Bookie'] == bookie, "+/-"].sum(), 3))
    print('По сравнению со средним коэффициентом во всех конторах:')
    print("OddsAll:", round(games.loc[(games['Bookie'] == "PIN") & (games['Result'] == "Won") |
                                      (games['Bookie'] == "SIN") & (games['Result'] == "Won") |
                                      (games['Bookie'] == "P88") & (games['Result'] == "Won"), "Odds"].mean(), 3))


def more_odds(game_odds):
    print(games[games['Odds'] >= game_odds].head(1000).to_string())
    print("Games:", games[games['Odds'] >= game_odds].shape[0])
    print("Won:", games.loc[(games['Odds'] >= game_odds) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Odds'] >= game_odds) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Odds'] >= game_odds)].shape[0]) * 100 /
                games[games['Odds'] >= game_odds].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['Odds'] >= game_odds) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("ROI", round(games.loc[games['Odds'] >= game_odds, "+/-"].sum() *
                       100 / games[games['Odds'] >= game_odds].shape[0], 2))
    print("+/-:", round(games.loc[games['Odds'] >= game_odds, "+/-"].sum(), 3))


def less_odds(game_odds):
    print(games[games['Odds'] <= game_odds].head(1000).to_string())
    print("Games:", games[games['Odds'] <= game_odds].shape[0])
    print("Won:", games.loc[(games['Odds'] <= game_odds) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Odds'] <= game_odds) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Odds'] <= game_odds)].shape[0]) * 100 /
                games[games['Odds'] <= game_odds].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['Odds'] <= game_odds) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("ROI", round(games.loc[games['Odds'] <= game_odds, "+/-"].sum() *
                       100 / games[games['Odds'] <= game_odds].shape[0], 2))
    print("+/-:", round(games.loc[games['Odds'] <= game_odds, "+/-"].sum(), 3))


def between_odds(game_odds1, game_odds2):
    print(games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2)].head(1000).to_string())
    print("Games:", games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2)].shape[0])
    print("Won:", games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2) & (games['Result'] == "Won")]
          .shape[0])
    print("Lost:",
          games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2) & (games['Result'] == "Lost")]
          .shape[0])
    print("Win%:", round(int(
        games.loc[(games['Result'] == "Won") & (games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2)].shape[
            0]) * 100 / games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2)].shape[0], 2))
    print("ROI", round(games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2), "+/-"].sum() * 100 /
                       games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2)].shape[0], 2))
    print("+/-:", round(games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2), "+/-"].sum(), 3))


# overall(games)
# certain_period(315, 400)
# score_result("3:0")
# league_result("*SPAIN LA LIGA")
# bet_type_and_score('UNDER', "1:1")
# bet_type("OVER")
# bookie_stats("PIN")
# scores_and_stats()
# leagues_and_stats()
# more_odds(2.5)
# less_odds(2)
# between_odds(2, 2.1)

# print(games.loc[(games['League'] == '*ENGLISH PREMIER LEAGUE') & (games['Score'] == "1:1"), "Odds"].mean())
