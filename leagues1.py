import grequests
import requests
from bs4 import BeautifulSoup


class Match:
    def __init__(self, home_team, away_team, home_score, away_score, home_goals, away_goals, home_cards, away_cards):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.home_cards = home_cards
        self.away_cards = away_cards

    def __str__(self):
        return "{} - {} {}:{}, goals: {} - {}".format(self.home_team, self.away_team, self.home_score,
                                                      self.away_score, self.home_goals, self.away_goals,
                                                      self.home_cards, self.away_cards)


HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0',
           'accept': '*/*'}

URL = ["Https://soccer365.ru/competitions/16/results/", "Https://soccer365.ru/competitions/17/results/", "Https://soccer365.ru/competitions/587/results/",
       "Https://soccer365.ru/competitions/715/results/", "Https://soccer365.ru/competitions/721/results/", "Https://soccer365.ru/competitions/723/results/",
       "Https://soccer365.ru/competitions/596/results/", "Https://soccer365.ru/competitions/595/results/", "Https://soccer365.ru/competitions/554/results/",
       "Https://soccer365.ru/competitions/474/results/", "Https://soccer365.ru/competitions/473/results/", "Https://soccer365.ru/competitions/667/results/"]
#  "Https://soccer365.ru/competitions/485/results/" Бельгия
# "Https://soccer365.ru/competitions/487/results/" Бельгия 2
#  "Https://soccer365.ru/competitions/585/results/" Грузия
#  "Https://soccer365.ru/competitions/606/results/" Исландия
#  "Https://soccer365.ru/competitions/436/results/" США


links = []
games = []

for url in URL:
    r = requests.get(url, headers=HEADERS, params=None)
    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find_all(class_='game_block')
    for item in items:
        links.append('https://soccer365.ru' + item.find('a').get('href'))

asy = (grequests.get(link) for link in links)
asa = grequests.map(asy)

for r in asa:
    home_goals, away_goals = [], []
    home_team, away_team = '', ''
    home_score, away_score = 0, 0
    home_cards, away_cards = 0, 0
    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find_all(id='game_events')
    events_ht = soup.find_all(class_="event_ht")
    events_at = soup.find_all(class_="event_at")
    events_min = soup.find_all(class_="event_min")
    home_goal_types = ["event_ht_icon live_goal", "event_ht_icon live_pengoal", "event_ht_icon live_owngoal"]
    away_goal_types = ["event_at_icon live_goal", "event_at_icon live_pengoal", "event_at_icon live_owngoal"]
    home_red_cards = ["event_ht_icon live_redcard", "event_ht_icon live_yellowred"]
    away_red_cards = ["event_at_icon live_redcard", "event_at_icon live_yellowred"]
    for i in range(len(events_ht)):
        for j in home_red_cards:
            home_red_card = events_ht[i].find('div', class_=j)
            if home_red_card and '45+' in events_min[i].get_text():
                home_cards += 1
            elif '+' in events_min[i].get_text():
                continue
            elif int(events_min[i].get_text().replace("'", "")):
                if home_red_card and int(events_min[i].get_text().replace("'", "")) < 75:
                    home_cards += 1
        for j in away_red_cards:
            away_red_card = events_ht[i].find('div', class_=j)
            if away_red_card and '45+' in events_min[i].get_text():
                away_cards += 1
            elif '+' in events_min[i].get_text():
                continue
            elif int(events_min[i].get_text().replace("'", "")):
                if away_red_card and int(events_min[i].get_text().replace("'", "")) < 75:
                    away_cards += 1
        for j in home_goal_types:
            home_goal = events_ht[i].find('div', class_=j)
            if home_goal and '45+' in events_min[i].get_text():
                home_goals.append(45)
            elif home_goal and '90+' in events_min[i].get_text():
                home_goals.append(90)
            elif home_goal and '105+' in events_min[i].get_text():
                home_goals.append(105)
            elif home_goal and '120+' in events_min[i].get_text():
                home_goals.append(120)
            elif '+' in events_min[i].get_text():
                continue
            elif home_goal:
                home_goals.append(int(events_min[i].get_text().replace("'", "")))
        for j in away_goal_types:
            away_goal = events_at[i].find('div', class_=j)
            if away_goal and '45+' in events_min[i].get_text():
                away_goals.append(45)
            elif away_goal and '90+' in events_min[i].get_text():
                away_goals.append(90)
            elif away_goal and '105+' in events_min[i].get_text():
                away_goals.append(105)
            elif away_goal and '120+' in events_min[i].get_text():
                away_goals.append(120)
            elif '+' in events_min[i].get_text():
                continue
            elif away_goal:
                away_goals.append(int(events_min[i].get_text().replace("'", "")))
    for item in items:
        home_team = item.find('div', class_="live_game_ht").find('a').get_text()
        away_team = item.find('div', class_="live_game_at").find('a').get_text()
        home_score = item.find('div', class_="live_game_goal").find('span').get_text()
        away_score = item.find('div', class_="live_game right").find('div', class_="live_game_goal").find(
            'span').get_text()
    games.append(Match(home_team, away_team, home_score, away_score, home_goals, away_goals, home_cards, away_cards))


def zero_zero(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 0 and local_away_score == 0:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 0 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 0 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('0:0')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    


def one_one(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 1 and local_away_score == 1:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 2 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 2 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('1:1')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    


def two_two(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 2 and local_away_score == 2:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 4 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 4 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('2:2')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    
def one_zero(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 1 and local_away_score == 0:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 1 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 1 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('1:0')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    
def zero_one(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 0 and local_away_score == 1:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 1 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 1 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('0:1')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    
def two_zero(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 2 and local_away_score == 0:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 2 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 2 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('2:0')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    
def zero_two(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 0 and local_away_score == 2:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 2 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 2 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('0:2')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    
def two_one(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 2 and local_away_score == 1:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 3 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 3 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('2:1')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    
def one_two(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 1 and local_away_score == 2:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 3 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 3 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('1:2')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    
def three_zero(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 3 and local_away_score == 0:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 3 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 3 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('3:0')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    
def zero_three(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 0 and local_away_score == 3:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 3 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 3 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('0:3')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    
def three_one(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 3 and local_away_score == 1:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 4 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 4 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('3:1')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    
def one_three(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 1 and local_away_score == 3:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 4 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 4 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('1:3')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    


def three_two(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 3 and local_away_score == 2:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 5 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 5 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('3:2')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    


def two_three(games):
    total_games = 0
    passed_games = 0
    goals_and_minutes = {75: 0, 76: 0, 77: 0, 78: 0, 79: 0, 80: 0, 81: 0, 82: 0, 83: 0, 84: 0, 85: 0, 86: 0, 87: 0,
                         88: 0, 89: 0}
    for game in games:
        if game.home_cards == 0 and game.away_cards == 0:
            local_home_score = 0
            local_away_score = 0
            for goal_minute in game.home_goals:
                if goal_minute < 75:
                    local_home_score += 1
            for goal_minute in game.away_goals:
                if goal_minute < 75:
                    local_away_score += 1
            if local_home_score == 2 and local_away_score == 3:
                if 75 not in game.home_goals and 75 not in game.away_goals:
                    total_games += 1
                    print(game)
                if len(game.home_goals) + len(game.away_goals) > 5 and 75 not in game.home_goals and len(
                        game.home_goals) + len(game.away_goals) > 5 and 75 not in game.away_goals:
                    passed_games += 1
                    goal_after_75 = 0
                    for minute in sorted(game.home_goals + game.away_goals):
                        if minute > 75:
                            goal_after_75 = minute
                            break
                    for key, value in goals_and_minutes.items():
                        if key < goal_after_75:
                            goals_and_minutes[key] += 1
    print('2:3')
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    print(f'Win%: {round(passed_games * 100 / total_games, 2)}')
    


zero_zero(games)
one_one(games)
two_two(games)
one_zero(games)
zero_one(games)
two_zero(games)
zero_two(games)
two_one(games)
one_two(games)
three_zero(games)
zero_three(games)
three_one(games)
one_three(games)
three_two(games)
two_three(games)
