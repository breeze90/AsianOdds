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
        return "{} - {} {}:{}, goals: {} - {}, cards: {} - {}".format(self.home_team, self.away_team, self.home_score,
                                                                      self.away_score, self.home_goals, self.away_goals,
                                                                      self.home_cards, self.away_cards)


URL = ["Https://soccer365.ru/competitions/474/results/", "Https://soccer365.ru/competitions/473/results/",
       "Https://soccer365.ru/competitions/12/results/", "Https://soccer365.ru/competitions/485/results/",
       "Https://soccer365.ru/competitions/487/results/", "Https://soccer365.ru/competitions/565/results/",
       "Https://soccer365.ru/competitions/17/results/", "Https://soccer365.ru/competitions/587/results/",
       "Https://soccer365.ru/competitions/586/results/", "Https://soccer365.ru/competitions/591/results/",
       "Https://soccer365.ru/competitions/585/results/", "Https://soccer365.ru/competitions/560/results/",
       "Https://soccer365.ru/competitions/606/results/", "Https://soccer365.ru/competitions/16/results/",
       "Https://soccer365.ru/competitions/15/results/", "Https://soccer365.ru/competitions/596/results/",
       "Https://soccer365.ru/competitions/595/results/", "Https://soccer365.ru/competitions/747/results/",
       "Https://soccer365.ru/competitions/684/results/", "Https://soccer365.ru/competitions/667/results/",
       "Https://soccer365.ru/competitions/436/results/", "Https://soccer365.ru/competitions/723/results/",
       "Https://soccer365.ru/competitions/721/results/", "Https://soccer365.ru/competitions/14/results/",
       "Https://soccer365.ru/competitions/735/results/", "Https://soccer365.ru/competitions/577/results/",
       "Https://soccer365.ru/competitions/18/results/", "Https://soccer365.ru/competitions/554/results/",
       "Https://soccer365.ru/competitions/716/results/", "Https://soccer365.ru/competitions/715/results/",
       "Https://soccer365.ru/competitions/712/results/", "Https://soccer365.ru/competitions/19/results/",
       "Https://soccer365.ru/competitions/20/results/"]
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0',
           'accept': '*/*'}
links = []


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_games(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all(class_='game_block')
    for item in items:
        links.append('https://soccer365.ru' + item.find('a').get('href'))
    return links


def parse_league():
    for i in URL:
        html = get_html(i)
        print(i)
        get_games(html.text)


def get_scores(html):
    home_goals, away_goals = [], []
    home_team, away_team = '', ''
    home_score, away_score = 0, 0
    home_cards, away_cards = 0, 0
    soup = BeautifulSoup(html, 'lxml')
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
    return Match(home_team, away_team, home_score, away_score, home_goals, away_goals, home_cards, away_cards)


def parse_scores():
    parse_league()
    parsed_games = []
    for link in links:
        html = get_html(link)
        # html = get_html('https://soccer365.ru/games/1367824/')
        parsed_games.append(get_scores(html.text))
    return parsed_games


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
    print(f'Всего игр: {total_games}')
    print(f'Прошло игр: {passed_games}')
    for i, j in goals_and_minutes.items():
        print(i, j)


list_of_parsed_scores = parse_scores()
one_zero(list_of_parsed_scores)
