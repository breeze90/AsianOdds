import pandas as pd

games = pd.read_csv("games.csv", names=["League", "Game", "Score", "FinalScore", "Odds", "Bookie", "Type", "Result",
                                        "+/-"])

scores_and_stats_dict = {'0:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '1:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '2:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '1:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '2:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '2:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '3:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '3:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '3:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '0:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '0:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '1:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '0:3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '1:3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), 'ROI': 0, '+/-': 0},
                         '2:3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Коэф.': float(0), '+/-': 0}
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
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['+/-'] = round(value['+/-'], 2)
        value['ROI'] = round(value['+/-'] * 100 / value['Матчи'], 2)
    for key, value in scores_and_stats_dict.items():
        print(key, value)


def overall(games_csv):
    print(games_csv.to_string())
    print("Games:", games_csv.shape[0])
    print("Won:", int(games_csv[games_csv['Result'] == "Won"].shape[0]))
    print("Lost:", games_csv[games_csv['Result'] == "Lost"].shape[0])
    print("Win%:", round(int(games_csv[games_csv['Result'] == "Won"].shape[0]) * 100 / games_csv.shape[0], 2))
    print("WinOdds:", round(games.loc[games['Result'] == "Won", "Odds"].mean(), 3))
    print("ROI:", round(games_csv["+/-"].sum() * 100 / games_csv.shape[0], 2))
    print("+/-", round(games_csv["+/-"].sum(), 2))


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


overall(games)
# certain_period(196, 235)
# score_result("1:1")
# league_result("ENGLISH CHAMPIONSHIP")
# bet_type("OVER")
# bookie_stats("PIN")
# scores_and_stats()


# print(games.loc[(games['League'] == '*ENGLISH PREMIER LEAGUE') & (games['Score'] == "1:1"), "Odds"].mean())
