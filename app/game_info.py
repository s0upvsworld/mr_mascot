import statsapi
import json
from app.utils import Utilities as ut
import re


class GameInfo:
    def __init__(self, team):
        self.team = team
        self.teamId = "121"
        u = ut()
        self.yesterday = u.yesterday_date()
        self.today = u.today_date()
        self.start_date, self.end_date = u.seven_days()

    def last_next_game_schedule(self):
        # gather schedule data
        response = statsapi.schedule(
            team=self.teamId, start_date=self.start_date, end_date=self.end_date
        )
        games_schedule = []
        current_series = {}

        # arrange schedule
        for game in response:
            game_info = {
                "game_id": game.get("game_id", None),
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


        # get last and next game info
        last_game = None
        last_game_highlights = None
        next_game = None

        for game in games_schedule:
            if game["game_date"] == str(self.yesterday):
                last_game = game
                game_id = game["game_id"]
                highlights = statsapi.game_highlights(game_id)
                highlights_a = re.sub(r'http[s]?://\S+', '--', highlights)
                highlights_b = re.sub(r'\(00:\d{2}:\d{2}\)', '', highlights_a)
                last_game_highlights = re.sub(r'Condensed Game:.*', '', highlights_b, flags=re.DOTALL)
                break
            else:
                last_game = None
                last_game_highlights = None

        for game in games_schedule:
            if game["game_date"] >= str(self.today):
                next_game = game
                break

        return last_game, last_game_highlights, next_game

if __name__ == "__main__":
    team = "New York Mets"
    # sch.seven_day_schedule()
    last_game, last_game_highlights, next_game = GameInfo(team).last_next_game_schedule()
    # (pretty_last_game_stats, game_highlights) = GameStats(team, games_schedule).last_game()
    pretty_last_game = json.dumps(last_game, indent=4)
    pretty_next_game = json.dumps(next_game, indent=4)
    print(f"{pretty_last_game}\n\n{pretty_next_game}\n\n{last_game_highlights}")