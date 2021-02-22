import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

games = pd.read_csv("games_stats.csv",
                    names=["Date", "Time", "Day", "League", "HomeTeam", "AwayTeam", "Score", "FTScore", "Odds",
                           "Bookie", "Type", "Result", "ROI"])

days_and_stats_dict = {
    'Monday': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'Tuesday': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'Wednesday': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'Thursday': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'Friday': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'Saturday': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'Sunday': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0}
}

bet_type_dict = {
    'OVER': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'UNDER': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0}
}

scores_and_stats_dict = {
    '0:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '1:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '2:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '1:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '2:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '2:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '3:0': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '3:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '3:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '0:1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '0:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '1:2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '0:3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '1:3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '2:3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0}
}

leagues_and_stats_dict = {
    '*ENGLISH PREMIER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                                'ROI': 0},
    'ENGLISH CHAMPIONSHIP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                             'ROI': 0},
    'ENGLISH FA CUP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '*GERMANY BUNDESLIGA': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                            'ROI': 0},
    'GERMANY BUNDESLIGA 2': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                             'ROI': 0},
    'GERMANY BUNDESLIGA 3': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                             'ROI': 0},
    'GERMANY CUP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '*ITALY SERIE A': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'ITALY CUP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '*SPAIN LA LIGA': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'SPAIN CUP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    '*UEFA CHAMPIONS LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                               'ROI': 0},
    '*UEFA EUROPA LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                            'ROI': 0},
    'AUSTRIA BUNDESLIGA': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'AUSTRIA ERSTE LIGA': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'BELGIUM FIRST DIVISION A': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                                 'ROI': 0},
    'BELGIUM FIRST DIVISION B': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                                 'ROI': 0},
    'BELGIUM CUP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'CZECH REPUBLIC FIRST LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                                    'ROI': 0},
    'DENMARK SUPER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                             'ROI': 0},
    'FRANCE LIGUE 1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'FRANCE CUP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'GEORGIA EROVNULI LIGA': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                              'ROI': 0},
    'GREECE SUPER LEAGUE 1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                              'ROI': 0},
    'HOLLAND EERSTE DIVISIE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                               'ROI': 0},
    'HOLLAND EREDIVISIE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'HOLLAND CUP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'NORTHERN IRELAND PREMIERSHIP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                                     'ROI': 0},
    'NORWAY ELITESERIEN': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'ROMANIA LIGA 1': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0, 'ROI': 0},
    'SWITZERLAND SUPER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                                 'ROI': 0},
    'SWITZERLAND CHALLENGE LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                                     'ROI': 0},
    'TURKEY SUPER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                            'ROI': 0},
    'TURKEY TFF FIRST LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                                'ROI': 0},
    'TURKEY CUP': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                   'ROI': 0},
    'UKRAINE PREMIER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                               'ROI': 0},
    'WALES PREMIER LEAGUE': {'Матчи': 0, 'Победы': 0, 'Поражения': 0, 'Win%': 0, 'Коэф.': float(0), 'Yield': 0,
                             'ROI': 0}
}


def overall(games_csv):
    print(games_csv.to_string())
    # print(games_csv.sort_values(by=['Odds']).to_string())
    print("Games:", games_csv.shape[0])
    print("Won:", int(games_csv[games_csv['Result'] == "Won"].shape[0]))
    print("Lost:", games_csv[games_csv['Result'] == "Lost"].shape[0])
    print("Win%:", round(int(games_csv[games_csv['Result'] == "Won"].shape[0]) * 100 / games_csv.shape[0], 2))
    print("WinOdds:", round(games.loc[games['Result'] == "Won", "Odds"].mean(), 3))
    # print("LostOdds:", round(games.loc[games['Result'] == "Lost", "Odds"].mean(), 3))
    # print("WinOddsMedian:", round(games.loc[games['Result'] == "Won", "Odds"].median(), 3))
    # print("WinOddsStd:", round(games.loc[games['Result'] == "Won", "Odds"].std(), 3))
    # print("WinOddsVar:", round(games.loc[games['Result'] == "Won", "Odds"].var(), 3))
    # https://www.quora.com/What-is-the-relation-between-the-Range-IQR-and-standard-deviation
    # q3 = round(games.loc[games['Result'] == "Won", "Odds"].quantile(0.75), 3)
    # q1 = round(games.loc[games['Result'] == "Won", "Odds"].quantile(0.25), 3)
    # print("WinOddsIQR:", round(q3 - q1, 3))
    print("Yield:", round(games_csv["ROI"].sum() * 100 / games_csv.shape[0], 2))
    # print("Yield Over:", round(games_csv.loc[games_csv["Type"] == "OVER", "ROI"].sum() * 100 / games_csv[games_csv["Type"] == "OVER"].shape[0], 2))
    # print("Yield Under:", round(games_csv.loc[games_csv["Type"] == "UNDER", "ROI"].sum() * 100 / games_csv[games_csv["Type"] == "UNDER"].shape[0], 2))
    print("ROI:", round(games_csv["ROI"].sum(), 2))


def scores_and_stats():
    for key, value in scores_and_stats_dict.items():
        for index, row in games.iterrows():
            if row["Score"] == key:
                value['Матчи'] += 1
                if row["Result"] == 'Won':
                    value['Победы'] += 1
                    value['ROI'] += round(row["ROI"], 2)
                    value["Коэф."] += row["Odds"]
                elif row["Result"] == 'Lost':
                    value['Поражения'] += 1
                    value['ROI'] += round(row["ROI"], 2)
    for key, value in scores_and_stats_dict.items():
        value['Win%'] = round(value['Победы'] * 100 / value['Матчи'], 2)
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['ROI'] = round(value['ROI'], 2)
        value['Yield'] = round(value['ROI'] * 100 / value['Матчи'], 2)
    for i in sorted(scores_and_stats_dict.items(), key=lambda item: item[1]['ROI'], reverse=True):
        print(i)
    # scores = pd.DataFrame.from_dict(scores_and_stats_dict, 'index')
    # scores = scores.sort_values("Win%")
    # fig, ax = plt.subplots()
    # ax.bar(scores.index, scores["Win%"])
    # ax.set_ylabel("Win%")
    # plt.show()


def scores_and_stats_and_bet(bet):
    for key, value in scores_and_stats_dict.items():
        for index, row in games.iterrows():
            if row["Score"] == key and row["Type"] == bet:
                value['Матчи'] += 1
                if row["Result"] == 'Won':
                    value['Победы'] += 1
                    value['ROI'] += round(row["ROI"], 2)
                    value["Коэф."] += row["Odds"]
                elif row["Result"] == 'Lost':
                    value['Поражения'] += 1
                    value['ROI'] += round(row["ROI"], 2)
    for key, value in scores_and_stats_dict.items():
        value['Win%'] = round(value['Победы'] * 100 / value['Матчи'], 2)
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['ROI'] = round(value['ROI'], 2)
        value['Yield'] = round(value['ROI'] * 100 / value['Матчи'], 2)
    for i in sorted(scores_and_stats_dict.items(), key=lambda item: item[1]['ROI'], reverse=True):
        print(i)


def leagues_and_stats():
    for key, value in leagues_and_stats_dict.items():
        for index, row in games.iterrows():
            if row["League"] == key:
                value['Матчи'] += 1
                if row["Result"] == 'Won':
                    value['Победы'] += 1
                    value['ROI'] += round(row["ROI"], 2)
                    value["Коэф."] += row["Odds"]
                elif row["Result"] == 'Lost':
                    value['Поражения'] += 1
                    value['ROI'] += round(row["ROI"], 2)
    for key, value in leagues_and_stats_dict.items():
        if value['Победы'] == 0:
            continue
        value['Win%'] = round(value['Победы'] * 100 / value['Матчи'], 2)
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['ROI'] = round(value['ROI'], 2)
        value['Yield'] = round(value['ROI'] * 100 / value['Матчи'], 2)
    for i in sorted(leagues_and_stats_dict.items(), key=lambda item: item[1]['ROI'], reverse=True):
        print(i)


def leagues_and_stats_and_date(time1, time2):
    for key, value in leagues_and_stats_dict.items():
        for index, row in games.iterrows():
            if row["League"] == key and time1 <= row['Date'] <= time2:
                value['Матчи'] += 1
                if row["Result"] == 'Won':
                    value['Победы'] += 1
                    value['ROI'] += round(row["ROI"], 2)
                    value["Коэф."] += row["Odds"]
                elif row["Result"] == 'Lost':
                    value['Поражения'] += 1
                    value['ROI'] += round(row["ROI"], 2)
    for key, value in leagues_and_stats_dict.items():
        if value['Победы'] == 0:
            continue
        value['Win%'] = round(value['Победы'] * 100 / value['Матчи'], 2)
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['ROI'] = round(value['ROI'], 2)
        value['Yield'] = round(value['ROI'] * 100 / value['Матчи'], 2)
    for i in sorted(leagues_and_stats_dict.items(), key=lambda item: item[1]['ROI'], reverse=True):
        print(i)
    print(games.loc[(games["Date"] >= time1) & (games["Date"] <= time2)].groupby("League")["ROI"].sum().sort_values(ascending=False))


def leagues_and_stats_and_type_and_difference(bet, *difference):
    goal_difference = []
    for i in difference:
        goal_difference.append(i)
    for key, value in leagues_and_stats_dict.items():
        for index, row in games.iterrows():
            if row["League"] == key and row['Type'] == bet and row['Score'] in goal_difference:
                value['Матчи'] += 1
                if row["Result"] == 'Won':
                    value['Победы'] += 1
                    value['ROI'] += round(row["ROI"], 2)
                    value["Коэф."] += row["Odds"]
                elif row["Result"] == 'Lost':
                    value['Поражения'] += 1
                    value['ROI'] += round(row["ROI"], 2)
    for key, value in leagues_and_stats_dict.items():
        if value['Победы'] == 0:
            continue
        value['Win%'] = round(value['Победы'] * 100 / value['Матчи'], 2)
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['ROI'] = round(value['ROI'], 2)
        value['Yield'] = round(value['ROI'] * 100 / value['Матчи'], 2)
    for i in sorted(leagues_and_stats_dict.items(), key=lambda item: item[1]['ROI'], reverse=True):
        print(i)


def leagues_and_stats_and_date_and_type(time1, time2, bet):
    for key, value in leagues_and_stats_dict.items():
        for index, row in games.iterrows():
            if row["League"] == key and time1 <= row['Date'] <= time2 and row['Type'] == bet:
                value['Матчи'] += 1
                if row["Result"] == 'Won':
                    value['Победы'] += 1
                    value['ROI'] += round(row["ROI"], 2)
                    value["Коэф."] += row["Odds"]
                elif row["Result"] == 'Lost':
                    value['Поражения'] += 1
                    value['ROI'] += round(row["ROI"], 2)
    for key, value in leagues_and_stats_dict.items():
        if value['Победы'] == 0:
            continue
        value['Win%'] = round(value['Победы'] * 100 / value['Матчи'], 2)
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['ROI'] = round(value['ROI'], 2)
        value['Yield'] = round(value['ROI'] * 100 / value['Матчи'], 2)
    for i in sorted(leagues_and_stats_dict.items(), key=lambda item: item[1]['ROI'], reverse=True):
        print(i)


def days_and_stats():
    for key, value in days_and_stats_dict.items():
        for index, row in games.iterrows():
            if row["Day"] == key:
                value['Матчи'] += 1
                if row["Result"] == 'Won':
                    value['Победы'] += 1
                    value['ROI'] += round(row["ROI"], 2)
                    value["Коэф."] += row["Odds"]
                elif row["Result"] == 'Lost':
                    value['Поражения'] += 1
                    value['ROI'] += round(row["ROI"], 2)
    for key, value in days_and_stats_dict.items():
        if value['Победы'] == 0:
            continue
        value['Win%'] = round(value['Победы'] * 100 / value['Матчи'], 2)
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['ROI'] = round(value['ROI'], 2)
        value['Yield'] = round(value['ROI'] * 100 / value['Матчи'], 2)
    for i in sorted(days_and_stats_dict.items(), key=lambda item: item[1]['ROI'], reverse=True):
        print(i)


def bet_type_stats():
    for key, value in bet_type_dict.items():
        for index, row in games.iterrows():
            if row["Type"] == key:
                value['Матчи'] += 1
                if row["Result"] == 'Won':
                    value['Победы'] += 1
                    value['ROI'] += round(row["ROI"], 2)
                    value["Коэф."] += row["Odds"]
                elif row["Result"] == 'Lost':
                    value['Поражения'] += 1
                    value['ROI'] += round(row["ROI"], 2)
    for key, value in bet_type_dict.items():
        value['Win%'] = round(value['Победы'] * 100 / value['Матчи'], 2)
        value['Коэф.'] = round(value['Коэф.'] / value['Победы'], 3)
        value['ROI'] = round(value['ROI'], 2)
        value['Yield'] = round(value['ROI'] * 100 / value['Матчи'], 2)
    for i in sorted(bet_type_dict.items(), key=lambda item: item[1]['ROI'], reverse=True):
        print(i)


def certain_period(time1, time2):
    print(games.loc[(games['Date'] >= time1) & (games['Date'] <= time2)].head(1000).to_string())
    print("Games:", games.loc[(games['Date'] >= time1) & (games['Date'] <= time2)].shape[0])
    print("Won:", games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Result'] == "Won")]
          .shape[0])
    print("Lost:",
          games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Result'] == "Lost")]
          .shape[0])
    print("Win%:", round(int(
        games.loc[(games['Result'] == "Won") & (games['Date'] >= time1) & (games['Date'] <= time2)].shape[0]) * 100 /
                         games.loc[(games['Date'] >= time1) & (games['Date'] <= time2)].shape[0], 2))
    print("WinOdds:",
          round(games.loc[
                    (games['Date'] >= time1) & (games['Date'] <= time2) & (games['Result'] == "Won"), "Odds"].mean(),
                3))
    print("Yield:", round(games.loc[(games['Date'] >= time1) & (games['Date'] <= time2), "ROI"].sum() * 100 /
                          games.loc[(games['Date'] >= time1) & (games['Date'] <= time2)].shape[0], 2))
    print("ROI:", round(games.loc[(games['Date'] >= time1) & (games['Date'] <= time2), "ROI"].sum(), 3))


def certain_period_and_type(time1, time2, bet):
    print(
        games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet)].head(1000).to_string())
    print("Games:", games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet)].shape[0])
    print("Won:", games.loc[
        (games['Date'] >= time1) & (games['Date'] <= time2) & (games['Result'] == "Won") & (games['Type'] == bet)]
          .shape[0])
    print("Lost:",
          games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Result'] == "Lost") & (
                  games['Type'] == bet)]
          .shape[0])
    print("Win%:", round(int(
        games.loc[(games['Result'] == "Won") & (games['Date'] >= time1) & (games['Date'] <= time2) & (
                games['Type'] == bet)].shape[0]) * 100 /
                         games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet)].shape[
                             0], 2))
    print("WinOdds:",
          round(games.loc[
                    (games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet) & (
                            games['Result'] == "Won"), "Odds"].mean(),
                3))
    print("Yield:", round(
        games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet), "ROI"].sum() * 100 /
        games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet)].shape[0], 2))
    print("ROI:",
          round(games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet), "ROI"].sum(),
                3))


def certain_period_and_league(time1, time2, league):
    print(
        games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['League'] == league)].head(
            1000).to_string())
    print("Games:",
          games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['League'] == league)].shape[0])
    print("Won:", games.loc[
        (games['Date'] >= time1) & (games['Date'] <= time2) & (games['Result'] == "Won") & (games['League'] == league)]
          .shape[0])
    print("Lost:",
          games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Result'] == "Lost") & (
                  games['League'] == league)]
          .shape[0])
    print("Win%:", round(int(
        games.loc[(games['Result'] == "Won") & (games['Date'] >= time1) & (games['Date'] <= time2) & (
                games['League'] == league)].shape[0]) * 100 /
                         games.loc[
                             (games['Date'] >= time1) & (games['Date'] <= time2) & (games['League'] == league)].shape[
                             0], 2))
    print("WinOdds:",
          round(games.loc[
                    (games['Date'] >= time1) & (games['Date'] <= time2) & (games['League'] == league) & (
                            games['Result'] == "Won"), "Odds"].mean(),
                3))
    print("Yield:", round(
        games.loc[
            (games['Date'] >= time1) & (games['Date'] <= time2) & (games['League'] == league), "ROI"].sum() * 100 /
        games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['League'] == league)].shape[0], 2))
    print("ROI:",
          round(
              games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['League'] == league), "ROI"].sum(),
              3))


def certain_period_and_type_and_score(time1, time2, bet, score):
    print(
        games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet) & (
                games['Score'] == score)].head(1000).to_string())
    print("Games:", games.loc[
        (games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet) & (games['Score'] == score)].shape[
        0])
    print("Won:", games.loc[
        (games['Date'] >= time1) & (games['Date'] <= time2) & (games['Result'] == "Won") & (games['Type'] == bet) & (
                games['Score'] == score)]
          .shape[0])
    print("Lost:",
          games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Result'] == "Lost") & (
                  games['Type'] == bet) & (games['Score'] == score)]
          .shape[0])
    print("Win%:", round(int(
        games.loc[(games['Result'] == "Won") & (games['Date'] >= time1) & (games['Date'] <= time2) & (
                games['Type'] == bet) & (games['Score'] == score)].shape[0]) * 100 /
                         games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet) & (
                                 games['Score'] == score)].shape[
                             0], 2))
    print("Yield:", round(
        games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet) & (
                games['Score'] == score), "ROI"].sum() * 100 /
        games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet) & (
                games['Score'] == score)].shape[0], 2))
    print("WinOdds:",
          round(games.loc[
                    (games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet) & (
                            games['Score'] == score) & (
                            games['Result'] == "Won"), "Odds"].mean(),
                3))
    print("ROI:",
          round(games.loc[(games['Date'] >= time1) & (games['Date'] <= time2) & (games['Type'] == bet) & (
                  games['Score'] == score), "ROI"].sum(),
                3))


def certain_time(time1, time2):
    print(games.loc[(games['Time'] >= time1) & (games['Time'] <= time2)].head(1000).to_string())
    print("Games:", games.loc[(games['Time'] >= time1) & (games['Time'] <= time2)].shape[0])
    print("Won:", games.loc[(games['Time'] >= time1) & (games['Time'] <= time2) & (games['Result'] == "Won")]
          .shape[0])
    print("Lost:",
          games.loc[(games['Time'] >= time1) & (games['Time'] <= time2) & (games['Result'] == "Lost")]
          .shape[0])
    print("Win%:", round(int(
        games.loc[(games['Result'] == "Won") & (games['Time'] >= time1) & (games['Time'] <= time2)].shape[0]) * 100 /
                         games.loc[(games['Time'] >= time1) & (games['Time'] <= time2)].shape[0], 2))
    print("Yield:", round(games.loc[(games['Time'] >= time1) & (games['Time'] <= time2), "ROI"].sum() * 100 /
                          games.loc[(games['Time'] >= time1) & (games['Time'] <= time2)].shape[0], 2))
    print("ROI:", round(games.loc[(games['Time'] >= time1) & (games['Time'] <= time2), "ROI"].sum(), 3))


def score_result(score):
    print(games[games["Score"] == score].head(1000).to_string())
    # print(games[games["Score"] == score].sort_values(by=['Odds']).to_string())
    print("Games:", games[games['Score'] == score].shape[0])
    print("Won:", games.loc[(games['Score'] == score) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Score'] == score) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Score'] == score)].shape[0]) * 100 /
                games[games['Score'] == score].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['Score'] == score) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(games.loc[games['Score'] == score, "ROI"].sum() *
                          100 / games[games['Score'] == score].shape[0], 2))
    print("ROI:", round(games.loc[games['Score'] == score, "ROI"].sum(), 2))


def league_result(league):
    print(games[games['League'] == league].head(1000).to_string())
    print("Games:", games[games['League'] == league].shape[0])
    print("Won:", games.loc[(games['League'] == league) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['League'] == league) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['League'] == league)].shape[0]) * 100 /
                games[games['League'] == league].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['League'] == league) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(games.loc[games['League'] == league, "ROI"].sum() *
                          100 / games[games['League'] == league].shape[0], 2))
    print("ROI:", round(games.loc[games['League'] == league, "ROI"].sum(), 3))


def score_and_league(score, league):
    print(games.loc[(games['League'] == league) & (games['Score'] == score)].head(1000).to_string())
    print("Games:", games.loc[(games['League'] == league) & (games['Score'] == score)].shape[0])
    print("Won:",
          games.loc[(games['League'] == league) & (games['Score'] == score) & (games['Result'] == "Won")].shape[0])
    print("Lost:",
          games.loc[(games['League'] == league) & (games['Score'] == score) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(
              games.loc[(games['Result'] == "Won") & (games['League'] == league) & (games['Score'] == score)].shape[
                  0]) * 100 /
                games.loc[(games['Score'] == score) & (games['League'] == league)].shape[0], 2))
    print("WinOdds:", round(
        games.loc[(games['League'] == league) & (games['Score'] == score) & (games['Result'] == "Won"), "Odds"].mean(),
        3))
    print("Yield:", round(games.loc[(games['League'] == league) & (games['Score'] == score), "ROI"].sum() *
                          100 / games.loc[(games['League'] == league) & (games['Score'] == score)].shape[0], 2))
    print("ROI:", round(games.loc[(games['League'] == league) & (games['Score'] == score), "ROI"].sum(), 3))


def mulitiple_scores_and_type(bet, *scores):
    my_scores = []
    for i in scores:
        my_scores.append(i)
    print(games.loc[
              (games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores)))].to_string())
    print("Games:",
          games.loc[(games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores)))].shape[
              0])
    print("Won:", games.loc[
        (games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores))) & (
                games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[
        (games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores))) & (
                games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(
              games.loc[(games['Result'] == "Won") & (games['Type'] == bet) & (
                  games['Score'].str.contains("|".join(my_scores)))].shape[0]) * 100 /
                games.loc[
                    (games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores)))].shape[
                    0], 2))
    print("WinOdds:",
          round(games.loc[
                    (games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores))) & (
                            games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(
        games.loc[(games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores))), "ROI"].sum() *
        100 / games.loc[(games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores)))].shape[0], 2))
    print("ROI:", round(
        games.loc[(games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores))), "ROI"].sum(), 3))


def mulitiple_scores_and_league_and_type(league, bet, *scores):
    my_scores = []
    for i in scores:
        my_scores.append(i)
    print(games.loc[
              (games['League'] == league) & (games['Type'] == bet) & (
                  games['Score'].str.contains("|".join(my_scores)))].to_string())
    print("Games:",
          games.loc[(games['League'] == league) & (games['Type'] == bet) & (
              games['Score'].str.contains("|".join(my_scores)))].shape[
              0])
    print("Won:", games.loc[
        (games['League'] == league) & (games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores))) & (
                games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[
        (games['League'] == league) & (games['Type'] == bet) & (games['Score'].str.contains("|".join(my_scores))) & (
                games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(
              games.loc[(games['Result'] == "Won") & (games['Type'] == bet) & (games['League'] == league) & (
                  games['Score'].str.contains("|".join(my_scores)))].shape[0]) * 100 /
                games.loc[
                    (games['League'] == league) & (games['Type'] == bet) & (
                        games['Score'].str.contains("|".join(my_scores)))].shape[
                    0], 2))
    print("WinOdds:",
          round(games.loc[
                    (games['League'] == league) & (games['Type'] == bet) & (
                        games['Score'].str.contains("|".join(my_scores))) & (
                            games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(
        games.loc[(games['League'] == league) & (games['Type'] == bet) & (
            games['Score'].str.contains("|".join(my_scores))), "ROI"].sum() *
        100 / games.loc[(games['League'] == league) & (games['Type'] == bet) & (
            games['Score'].str.contains("|".join(my_scores)))].shape[0], 2))
    print("ROI:", round(
        games.loc[(games['League'] == league) & (games['Type'] == bet) & (
            games['Score'].str.contains("|".join(my_scores))), "ROI"].sum(), 3))


def mulitiple_scores_and_leagues(league, *scores):
    my_scores = []
    for i in scores:
        my_scores.append(i)
    print(games.loc[
              (games['League'] == league) & (games['Score'].str.contains("|".join(my_scores)))].to_string())
    print("Games:",
          games.loc[(games['League'] == league) & (games['Score'].str.contains("|".join(my_scores)))].shape[
              0])
    print("Won:", games.loc[
        (games['League'] == league) & (games['Score'].str.contains("|".join(my_scores))) & (
                games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[
        (games['League'] == league) & (games['Score'].str.contains("|".join(my_scores))) & (
                games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(
              games.loc[(games['Result'] == "Won") & (games['League'] == league) & (
                  games['Score'].str.contains("|".join(my_scores)))].shape[0]) * 100 /
                games.loc[
                    (games['League'] == league) & (games['Score'].str.contains("|".join(my_scores)))].shape[
                    0], 2))
    print("WinOdds:",
          round(games.loc[
                    (games['League'] == league) & (games['Score'].str.contains("|".join(my_scores))) & (
                            games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(
        games.loc[(games['League'] == league) & (games['Score'].str.contains("|".join(my_scores))), "ROI"].sum() *
        100 / games.loc[(games['League'] == league) & (games['Score'].str.contains("|".join(my_scores)))].shape[0], 2))
    print("ROI:", round(
        games.loc[(games['League'] == league) & (games['Score'].str.contains("|".join(my_scores))), "ROI"].sum(), 3))


def type_and_league(bet, league):
    print(games.loc[(games['League'] == league) & (games['Type'] == bet)].head(1000).to_string())
    print("Games:", games.loc[(games['League'] == league) & (games['Type'] == bet)].shape[0])
    print("Won:",
          games.loc[(games['League'] == league) & (games['Type'] == bet) & (games['Result'] == "Won")].shape[0])
    print("Lost:",
          games.loc[(games['League'] == league) & (games['Type'] == bet) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(
              games.loc[(games['Result'] == "Won") & (games['League'] == league) & (games['Type'] == bet)].shape[
                  0]) * 100 /
                games.loc[(games['Type'] == bet) & (games['League'] == league)].shape[0], 2))
    print("WinOdds:", round(
        games.loc[(games['League'] == league) & (games['Type'] == bet) & (games['Result'] == "Won"), "Odds"].mean(),
        3))
    print("Yield:", round(games.loc[(games['League'] == league) & (games['Type'] == bet), "ROI"].sum() *
                          100 / games.loc[(games['League'] == league) & (games['Type'] == bet)].shape[0], 2))
    print("ROI:", round(games.loc[(games['League'] == league) & (games['Type'] == bet), "ROI"].sum(), 3))


def teams_stats(team, minus_word, *teams):
    my_teams = [team]
    for i in teams:
        my_teams.append(i)
    print(games.loc[
              (games["HomeTeam"].str.contains("|".join(my_teams))) & (~games["HomeTeam"].str.contains(minus_word)) | (
                  games["AwayTeam"].str.contains("|".join(my_teams))) & (
                  ~games["AwayTeam"].str.contains(minus_word))].to_string())
    print("Games:", games.loc[
        (games["HomeTeam"].str.contains("|".join(my_teams))) & (~games["HomeTeam"].str.contains(minus_word)) | (
            games["AwayTeam"].str.contains("|".join(my_teams))) & (~games["AwayTeam"].str.contains(minus_word))].shape[
        0])
    print("Won:", games.loc[
        (games["HomeTeam"].str.contains("|".join(my_teams))) & (~games["HomeTeam"].str.contains(minus_word)) & (
                games['Result'] == "Won") | (games["AwayTeam"].str.contains("|".join(my_teams))) & (
            ~games["AwayTeam"].str.contains(minus_word)) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[
        (games["HomeTeam"].str.contains("|".join(my_teams))) & (~games["HomeTeam"].str.contains(minus_word)) & (
                games['Result'] == "Lost") | (games["AwayTeam"].str.contains("|".join(my_teams))) & (
            ~games["AwayTeam"].str.contains(minus_word)) & (games['Result'] == "Lost")].shape[0])
    print("Win%:", round(int(games.loc[(games["HomeTeam"].str.contains("|".join(my_teams))) & (
        ~games["HomeTeam"].str.contains(minus_word)) & (games['Result'] == "Won") | (
                                           games["AwayTeam"].str.contains("|".join(my_teams))) & (
                                           ~games["AwayTeam"].str.contains(minus_word)) & (
                                               games['Result'] == "Won")].shape[0]) * 100 / games.loc[
                             (games["HomeTeam"].str.contains("|".join(my_teams))) & (
                                 ~games["HomeTeam"].str.contains(minus_word)) | (
                                 games["AwayTeam"].str.contains("|".join(my_teams))) & (
                                 ~games["AwayTeam"].str.contains(minus_word))].shape[0], 2))
    print("WinOdds:", round(games.loc[(games["HomeTeam"].str.contains("|".join(my_teams))) & (
        ~games["HomeTeam"].str.contains(minus_word)) & (games['Result'] == "Won") | (
                                          games["AwayTeam"].str.contains("|".join(my_teams))) & (
                                          ~games["AwayTeam"].str.contains(minus_word)) & (
                                              games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(games.loc[(games["HomeTeam"].str.contains("|".join(my_teams))) & (
        ~games["HomeTeam"].str.contains(minus_word)) | (games["AwayTeam"].str.contains("|".join(my_teams))) & (
                                        ~games["AwayTeam"].str.contains(minus_word)), "ROI"].sum() * 100 / games.loc[
                              (games["HomeTeam"].str.contains("|".join(my_teams))) & (
                                  ~games["HomeTeam"].str.contains(minus_word)) | (
                                  games["AwayTeam"].str.contains("|".join(my_teams))) & (
                                  ~games["AwayTeam"].str.contains(minus_word))].shape[0], 2))
    print("ROI:", round(games.loc[(games["HomeTeam"].str.contains("|".join(my_teams))) & (
        ~games["HomeTeam"].str.contains(minus_word)) | (games["AwayTeam"].str.contains("|".join(my_teams))) & (
                                      ~games["AwayTeam"].str.contains(minus_word)), "ROI"].sum(), 3))


def bet_type(bet):
    print(games[games['Type'] == bet].head(1000).to_string())
    print("Games:", games[games['Type'] == bet].shape[0])
    print("Won:", games.loc[(games['Type'] == bet) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Type'] == bet) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Type'] == bet)].shape[0]) * 100 /
                games[games['Type'] == bet].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['Type'] == bet) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(games.loc[games['Type'] == bet, "ROI"].sum() *
                          100 / games[games['Type'] == bet].shape[0], 2))
    print("ROI:", round(games.loc[games['Type'] == bet, "ROI"].sum(), 3))


def bet_type_and_score(bet, score):
    print(games.loc[(games['Type'] == bet) & (games['Score'] == score)].head(1000).to_string())
    print("Games:", games.loc[(games['Type'] == bet) & (games['Score'] == score)].shape[0])
    print("Won:", games.loc[(games['Type'] == bet) & (games['Score'] == score) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Type'] == bet) & (games['Score'] == score) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Type'] == bet) & (games['Score'] == score)].shape[
                        0]) * 100 /
                games.loc[(games['Type'] == bet) & (games['Score'] == score)].shape[0], 2))
    print("WinOdds:", round(
        games.loc[(games['Type'] == bet) & (games['Score'] == score) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(games.loc[(games['Type'] == bet) & (games['Score'] == score), "ROI"].sum() *
                          100 / games.loc[(games['Type'] == bet) & (games['Score'] == score)].shape[0], 2))
    print("ROI:", round(games.loc[(games['Type'] == bet) & (games['Score'] == score), "ROI"].sum(), 3))


def bookie_stats(bookie):
    print(games[games['Bookie'] == bookie].head(1000).to_string())
    print("Games:", games[games['Bookie'] == bookie].shape[0])
    print("Won:", games.loc[(games['Bookie'] == bookie) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Bookie'] == bookie) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Bookie'] == bookie)].shape[0]) * 100 /
                games[games['Bookie'] == bookie].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['Bookie'] == bookie) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(games.loc[games['Bookie'] == bookie, "ROI"].sum() *
                          100 / games[games['Bookie'] == bookie].shape[0], 2))
    print("ROI:", round(games.loc[games['Bookie'] == bookie, "ROI"].sum(), 3))
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
    print("Yield:", round(games.loc[games['Odds'] >= game_odds, "ROI"].sum() *
                          100 / games[games['Odds'] >= game_odds].shape[0], 2))
    print("ROI:", round(games.loc[games['Odds'] >= game_odds, "ROI"].sum(), 3))


def less_odds(game_odds):
    print(games[games['Odds'] <= game_odds].head(1000).to_string())
    print("Games:", games[games['Odds'] <= game_odds].shape[0])
    print("Won:", games.loc[(games['Odds'] <= game_odds) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Odds'] <= game_odds) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Odds'] <= game_odds)].shape[0]) * 100 /
                games[games['Odds'] <= game_odds].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['Odds'] <= game_odds) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(games.loc[games['Odds'] <= game_odds, "ROI"].sum() *
                          100 / games[games['Odds'] <= game_odds].shape[0], 2))
    print("ROI:", round(games.loc[games['Odds'] <= game_odds, "ROI"].sum(), 3))


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
    print("Yield:", round(games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2), "ROI"].sum() * 100 /
                          games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2)].shape[0], 2))
    print("ROI:", round(games.loc[(games['Odds'] >= game_odds1) & (games['Odds'] <= game_odds2), "ROI"].sum(), 3))


def winning_odds(games_csv):
    list_of_winning_odds = []
    # list_of_loosing_odds = []
    list_of_time = []
    for i in games_csv[games_csv['Result'] == "Won"]["Odds"]:
        list_of_winning_odds.append(round(i, 3))
    # for i in games_csv[games_csv['Result'] == "Lost"]["Odds"]:
    #     list_of_loosing_odds.append(round(i, 3))
    for i in games_csv[games_csv['Result'] == "Won"]["Time"]:
        list_of_time.append(int(i.replace(':', '')) + 300)
    plt.hist(list_of_winning_odds, bins=20)
    # plt.scatter(list_of_winning_odds, list_of_time)
    plt.title("Гистограмма")
    plt.xlabel("Коэффициент")
    plt.ylabel("Количество побед")
    # plt.yticks([50, 60, 70, 80, 90, 100], [50, 60, 70, 80, 80, 100])
    plt.show()


def week_day(day):
    print(games[games["Day"] == day].head(1000).to_string())
    # print(games[games["Day"] == score].sort_values(by=['Odds']).to_string())
    print("Games:", games[games['Day'] == day].shape[0])
    print("Won:", games.loc[(games['Day'] == day) & (games['Result'] == "Won")].shape[0])
    print("Lost:", games.loc[(games['Day'] == day) & (games['Result'] == "Lost")].shape[0])
    print("Win%:",
          round(int(games.loc[(games['Result'] == "Won") & (games['Day'] == day)].shape[0]) * 100 /
                games[games['Day'] == day].shape[0], 2))
    print("WinOdds:", round(games.loc[(games['Day'] == day) & (games['Result'] == "Won"), "Odds"].mean(), 3))
    print("Yield:", round(games.loc[games['Day'] == day, "ROI"].sum() *
                          100 / games[games['Day'] == day].shape[0], 2))
    print("ROI:", round(games.loc[games['Day'] == day, "ROI"].sum(), 2))


def roi_graph():
    games["ROI overall"] = games["ROI"].cumsum()
    for i, r in games.iterrows():
        if r["Type"] == "OVER":
            games.loc[i, "ROI OVER"] = r["ROI"]
            games.loc[i, "ROI UNDER"] = 0
        elif r["Type"] == "UNDER":
            games.loc[i, "ROI OVER"] = 0
            games.loc[i, "ROI UNDER"] = r["ROI"]
    games["ROI over"] = games["ROI OVER"].cumsum()
    games["ROI under"] = games["ROI UNDER"].cumsum()
    games["Date"] = pd.to_datetime(games['Date'])
    # Matplotlib
    # ax = games.plot(x="Date", y="ROI overall", kind="line", title="ROI over time", xlabel="Date", ylabel="ROI")
    # games.plot(x="Date", y="ROI over", kind="line", ax=ax)
    # games.plot(x="Date", y="ROI under", kind="line", ax=ax)
    # plt.legend(["ROI", "ROI over", "ROI under"])

    # Seaborn
    sns.lineplot(x="Date", y="ROI overall", data=games, label="ROI")
    sns.lineplot(x="Date", y="ROI over", data=games, label="ROI over")
    sns.lineplot(x="Date", y="ROI under", data=games, label="ROI under")
    plt.xlabel('Date')
    plt.ylabel('ROI')
    plt.title('ROI over time')
    plt.show()


def yield_graph():
    games["ROI overall"] = games["ROI"].cumsum()
    for i, r in games.iterrows():
        if r["Type"] == "OVER":
            games.loc[i, "ROI OVER"] = r["ROI"]
            games.loc[i, "ROI UNDER"] = 0
        elif r["Type"] == "UNDER":
            games.loc[i, "ROI OVER"] = 0
            games.loc[i, "ROI UNDER"] = r["ROI"]
    games["ROI over"] = games["ROI OVER"].cumsum()
    games["ROI under"] = games["ROI UNDER"].cumsum()
    games["Date"] = pd.to_datetime(games['Date'])
    roi = games.groupby("Date")["ROI"].sum().to_frame(name='ROI').reset_index()
    roi_over = games.groupby("Date")["ROI OVER"].sum().to_frame(name='ROI_Over').reset_index()
    roi_under = games.groupby("Date")["ROI UNDER"].sum().to_frame(name='ROI_Under').reset_index()
    games_aggregate = roi.merge(roi_over).merge(roi_under)
    games_aggregate['Date'] = pd.to_datetime(games_aggregate['Date'])
    games_aggregate.set_index('Date', inplace=True)
    # print(games_aggregate)
    # fig, ax = plt.subplots(2, 1)
    # ax[0].plot(games_aggregate.index, games_aggregate["ROI"])
    # ax[1].plot(games_aggregate.index, games_aggregate["ROI_Over"])
    # ax[1].plot(games_aggregate.index, games_aggregate["ROI_Under"])
    # # yield  ax.plot(games_aggregate.index, round(games.groupby("Date")["ROI"].sum() * 100 / games.groupby("Date")["ROI"].count(), 2))
    # plt.show()


def odds_stats():
    def ecdf(data):
        n = len(data)
        x = np.sort(data)
        y = np.arange(1, n + 1) / n
        return x, y

    x_vers, y_vers = ecdf(games["Odds"])
    _ = plt.xlabel('Odds')
    _ = plt.ylabel('Empirical distribution function')
    _ = plt.plot(x_vers, y_vers, '.')
    percentiles = np.array([2.5, 25, 50, 75, 97.5])
    odds_vers = np.percentile(games["Odds"], percentiles)
    _ = plt.plot(odds_vers, percentiles / 100, marker='D', color='orange', linestyle='none')
    plt.show()


with open("games.json", "r") as json_file:
    games_json = json.load(json_file)

games_file = open("games_stats.csv", "w")

for game in games_json:
    if game['PnlInfo'] == "Won":
        games_file.write(
            f"{datetime.datetime.fromtimestamp(game['TicketDate'] / 1000.0, tz=datetime.timezone.utc).strftime('%Y-%m-%d,%H:%M,%A')},"
            f"{game['LeagueName']},{game['HomeName']},{game['AwayName']},{game['HomeScore']}:{game['AwayScore']},"
            f"{game['FullTimeHomeScore']}:{game['FullTimeAwayScore']},{round(game['Odds'], 3)},{game['Bookie']},"
            f"{game['BetType']},{game['PnlInfo']},{round(round(game['Odds'], 3) * 1 - 1, 2)}")
        games_file.write("\n")
    elif game['PnlInfo'] == "Lost":
        games_file.write(
            f"{datetime.datetime.fromtimestamp(game['TicketDate'] / 1000.0, tz=datetime.timezone.utc).strftime('%Y-%m-%d,%H:%M,%A')},"
            f"{game['LeagueName']},{game['HomeName']},{game['AwayName']},{game['HomeScore']}:{game['AwayScore']},"
            f"{game['FullTimeHomeScore']}:{game['FullTimeAwayScore']},{round(game['Odds'], 3)},{game['Bookie']},"
            f"{game['BetType']},{game['PnlInfo']},{-1}")
        games_file.write("\n")


# overall(games)
# certain_period('2021-02-21', '2021-02-21')
certain_period('2021-02-01', '2021-02-28')
# certain_period_and_type('2021-02-20', '2021-02-20', "OVER")
# certain_period_and_league('2021-01-30', '2021-02-31', "GERMANY BUNDESLIGA 3")
# certain_period_and_type_and_score('2020-01-01', '2021-01-31', "UNDER", "2:2")
# certain_time('18:00', '18:59')
# score_result("1:0")
# league_result("GERMANY BUNDESLIGA 3")
# score_and_league("0:0", "*SPAIN LA LIGA")
# mulitiple_scores_and_type("OVER", "1:0", "2:1", "3:2", "0:1", "1:2", "2:3")
# mulitiple_scores_and_type("OVER", "2:0", "3:1", "3:0", "0:2", "0:3", "1:3")
# mulitiple_scores_and_leagues("FRANCE LIGUE 1", "1:0", "2:1", "3:2", "0:1", "1:2", "2:3")
# mulitiple_scores_and_leagues("FRANCE LIGUE 1", "2:0", "3:1", "3:0", "0:2", "0:3", "1:3")
# mulitiple_scores_and_leagues("FRANCE LIGUE 1", "0:0", "1:1", "2:2")
# mulitiple_scores_and_league_and_type("FRANCE LIGUE 1", "OVER", "1:0", "2:1", "3:2", "0:1", "1:2", "2:3")
# mulitiple_scores_and_league_and_type("FRANCE LIGUE 1", "OVER", "2:0", "3:1", "3:0", "0:2", "0:3", "1:3")
# mulitiple_scores_and_league_and_type("TURKEY SUPER LEAGUE", "OVER", "0:0", "1:1", "2:2")
# type_and_league("UNDER", "*ITALY SERIE A")
# bet_type_and_score('OVER', "3:1")
# bet_type("UNDER")
# bookie_stats("SIN")
# scores_and_stats()
# scores_and_stats_and_bet("OVER")
# leagues_and_stats()
# leagues_and_stats_and_date('2021-02-20', '2021-02-20')
# leagues_and_stats_and_type_and_difference("OVER", "0:0", "1:1", "2:2")
# leagues_and_stats_and_type_and_difference("OVER", "1:0", "2:1", "3:2", "0:1", "1:2", "2:3")
# leagues_and_stats_and_date_and_type('2021-02-01', '2021-02-28', "UNDER")
# days_and_stats()
# bet_type_stats()
# teams_stats("Lille OSC", "none")
# more_odds(2.5)
# less_odds(2)
# between_odds(1.9, 1.9)
# winning_odds(games)
# week_day("Monday")
# roi_graph()
# yield_graph()
# odds_stats()

