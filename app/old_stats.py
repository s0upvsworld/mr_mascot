import statsapi
import json
from app.utils import Utilities as ut


"""
[
    {
        "game_date": "2024-08-02",
        "away_name": "New York Mets",
        "home_name": "Los Angeles Angels",
        "venue_name": "Angel Stadium",
        "series_status": "NYM leads 1-0",
        "series_game_number": 1,
        "series_length": 3
    },
    {
        "game_date": "2024-08-03",
        "away_name": "New York Mets",
        "home_name": "Los Angeles Angels",
        "venue_name": "Angel Stadium",
        "series_status": "Series tied 1-1",
        "series_game_number": 2,
        "series_length": 3
    },
    {
        "game_date": "2024-08-04",
        "away_name": "New York Mets",
        "home_name": "Los Angeles Angels",
        "venue_name": "Angel Stadium",
        "series_status": "LAA wins 2-1",
        "series_game_number": 3,
        "series_length": 3
    }
]
"""


class TeamStats:
    def __init__(self, team):
        self.team = team
        self.teamId = "121"
        self.today = ut().today_date()
        self.tomorrow = ut().tomorrow_date()
        self.yesterday = ut().yesterday_date()
        self.today_gameStats = statsapi.schedule(team=self.teamId, date=self.today)
        self.yesterday_gameStats = statsapi.schedule(
            team=self.teamId, date=self.yesterday
        )
        (
            self.pretty_schedule,
            self.today_series_game_number,
            self.today_series_length,
            self.tomorrow_game,
        ) = self.schedule()

    def yesterday_game(self):
        yesterday_gameStats = statsapi.schedule(team=self.teamId, date=self.yesterday)

        if not yesterday_gameStats:
            yesterday_pretty_game_stats = None
        else:
            game_info = yesterday_gameStats[0]
            gameId = game_info["game_id"]
            game_stats = {
                "game_date": game_info.get("game_date", None),
                "summary": game_info.get("summary", None),
                "ballpark": game_info.get("ballpark", None),
                "winning_team": game_info.get("winning_team", None),
                "series_status": game_info.get("series_status", None),
                "series_game_number": self.today_series_game_number,
                "series_length": self.today_series_length,
            }
            yesterday_pretty_game_stats = json.dumps(game_stats, indent=4)
            return yesterday_pretty_game_stats

        if not self.today_gameStats:
            game_stats = None
            game_highlights = None
        else:
            game_info = self.today_gameStats[0]
            gameId = game_info["game_id"]
            game_stats = {
                "game_date": game_info.get("game_date", None),
                "summary": game_info.get("summary", None),
                "ballpark": game_info.get("ballpark", None),
                "winning_team": game_info.get("winning_team", None),
                "series_status": game_info.get("series_status", None),
                "series_game_number": self.today_series_game_number,
                "series_length": self.today_series_length,
            }
            pretty_game_stats = json.dumps(game_stats, indent=4)
            game_highlights = statsapi.game_highlights(gameId)
            return (
                yesterday_pretty_game_stats,
                pretty_game_stats,
                game_highlights,
                pretty_schedule,
            )

    def today_game(self):
        today_gameStats = statsapi.schedule(team=self.teamId, date=self.today)
        yesterday_gameStats = statsapi.schedule(team=self.teamId, date=self.yesterday)

        (
            pretty_schedule,
            today_series_game_number,
            today_series_length,
            tomorrow_game,
        ) = self.schedule()

        if not yesterday_gameStats:
            yesterday_pretty_game_stats = None
        else:
            game_info = yesterday_gameStats[0]
            gameId = game_info["game_id"]
            game_stats = {
                "game_date": game_info.get("game_date", None),
                "summary": game_info.get("summary", None),
                "ballpark": game_info.get("ballpark", None),
                "winning_team": game_info.get("winning_team", None),
                "series_status": game_info.get("series_status", None),
                "series_game_number": today_series_game_number,
                "series_length": today_series_length,
            }
            yesterday_pretty_game_stats = json.dumps(game_stats, indent=4)
            return yesterday_pretty_game_stats

        if not today_gameStats:
            game_stats = None
            game_highlights = None
        else:
            game_info = today_gameStats[0]
            gameId = game_info["game_id"]
            game_stats = {
                "game_date": game_info.get("game_date", None),
                "summary": game_info.get("summary", None),
                "ballpark": game_info.get("ballpark", None),
                "winning_team": game_info.get("winning_team", None),
                "series_status": game_info.get("series_status", None),
                "series_game_number": today_series_game_number,
                "series_length": today_series_length,
            }
            pretty_game_stats = json.dumps(game_stats, indent=4)
            game_highlights = statsapi.game_highlights(gameId)
            return (
                yesterday_pretty_game_stats,
                pretty_game_stats,
                game_highlights,
                pretty_schedule,
            )

    def schedule(self):
        start_date, end_date = ut().seven_days()
        response = statsapi.schedule(
            team=self.teamId, start_date=start_date, end_date=end_date
        )
        games_schedule = []
        current_series = {}

        for game in response:
            game_info = {
                "game_date": game.get("game_date", None),
                "away_name": game.get("away_name", None),
                "home_name": game.get("home_name", None),
                "venue_name": game.get("venue_name", None),
                "series_status": game.get("series_status", None),
            }
            games_schedule.append(game_info)

        for game in games_schedule:
            series_key = (game["away_name"], game["home_name"])
            if series_key not in current_series:
                current_series[series_key] = []
            current_series[series_key].append(game)

        for series in current_series.values():
            series_length = len(series)
            for index, game in enumerate(series):
                game["series_game_number"] = index + 1
                game["series_length"] = series_length

        games_schedule = [game for game in games_schedule if game["series_length"] > 1]

        for today in games_schedule:
            if today["game_date"] == str(self.today):
                today_series_game_number = today["series_game_number"]
                today_series_length = today["series_length"]

        for tomorrow in games_schedule:
            if tomorrow["game_date"] == str(self.tomorrow):
                tomorrow_game = tomorrow

        pretty_schedule = json.dumps(games_schedule, indent=4)
        return (
            pretty_schedule,
            today_series_game_number,
            today_series_length,
            tomorrow_game,
        )


if __name__ == "__main__":
    ts = TeamStats("New York Mets")
    (
        yesterday_pretty_game_stats,
        pretty_game_stats,
        game_highlights,
        pretty_schedule,
    ) = ts.today_game()
    print(f"{yesterday_pretty_game_stats}\n\n{pretty_game_stats}\n\n{pretty_schedule}")


"""

Ok I need these things,

methods:
1. yesterday's game stats as formatted
2. today game's stats

schedule:
1. seven days
2. tomorrow

I should be running schedule for schedule_dict and tomorrow

then using the schedule dict in both yesterday_game and today_game

if None = None for all

"""
