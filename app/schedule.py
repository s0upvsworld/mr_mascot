import statsapi
from app.utils import Utilities as ut

class Schedule:
    def __init__(self, team):
        self.team = team
        self.teamId = "121"
        self.today = ut().today_date()
        self.tomorrow = ut().tomorrow_date()
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

        # make pretty
        # pretty_schedule = json.dumps(games_schedule, indent=4)

        # return today's game
        today_game = None
        for today in games_schedule:
            if today["game_date"] == str(self.today):
                today_game = today
        
        # return tomorrow's game
        tomorrow_game = None
        for tomorrow in games_schedule:
            if tomorrow["game_date"] == str(self.tomorrow):
                tomorrow_game = tomorrow

        return games_schedule, today_game, tomorrow_game

if __name__ == "__main__":
    team = "New York Mets"
    (pretty_schedule, today_game) = Schedule(team).seven_day_schedule()
    print(f"{pretty_schedule}\n\n{today_game}")
    print(f"type: {type(pretty_schedule)}")