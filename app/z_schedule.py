import statsapi
import json
from app.utils import Utilities as ut
from datetime import datetime


class Schedule:
    def __init__(self, team):
        self.team = team
        self.teamId = "121"
        self.yesterday = ut().yesterday_date()
        self.start_date, self.end_date = ut().seven_days()

    def seven_day_schedule(self):
        # gather schedule data
        response = statsapi.schedule(
            team=self.teamId, start_date=self.start_date, end_date=self.end_date
        )
        games_schedule = []
        current_series = {}

        # arrange schedule
        for game in response:
            game_info = {
                "game_date": game.get("game_date", None),
                "away_name": game.get("away_name", None),
                "home_name": game.get("home_name", None),
                "venue_name": game.get("venue_name", None),
                "series_status": game.get("series_status", None),
            }
            games_schedule.append(game_info)

        # do math for series_game_number and series_length
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
        
        # seperate next game
        next_game = None
        for game in games_schedule:
            game_date = datetime.strptime(game["game_date"], "%Y-%m-%d").date()
            if game_date > self.yesterday:
                next_game = game

        return games_schedule, next_game

        # make pretty
        # pretty_schedule = json.dumps(games_schedule, indent=4)
        # print(pretty_schedule)


    # def next_game_info(self):

    #     next_game = None
    #     next_game = []
    #     for game in games_schedule:
    #         if game["game_date"] > self.yesterday:
    #             next_game = game


    # # return today's game
    #     today_game = None
    #     for today in games_schedule:
    #         if today["game_date"] == str(self.today):
    #             today_game = today
    #             if today["away_name"] == "New York Mets":
    #                 today_team = today["home_name"]
    #             series_length = today["series_length"]

    #     # return tomorrow's game
    #     tomorrow_game = None
    #     for tomorrow in games_schedule:
    #         if tomorrow["game_date"] == str(self.tomorrow):
    #             tomorrow_game = tomorrow
    #             if tomorrow["away_name"] == "New York Mets":
    #                 tomorrow_team = today["home_name"]
    #             series_length = tomorrow["series_length"]

    #     return today_game, tomorrow_game, series_length


if __name__ == "__main__":
    team = "New York Mets"
    sch = Schedule(team)
    (games_schedule, next_game) = sch.seven_day_schedule()

    pretty_schedule = json.dumps(games_schedule, indent=4)
    pretty_next_game = json.dumps(next_game, indent=4)
    print(f"{pretty_schedule}\n\n{pretty_next_game}")
