import statsapi
from app.utils import Utilities as ut


class GameStats:
    def __init__(self, team, schedule):
        self.team = team
        self.teamId = "121"  # nym
        self.yesterday = ut().yesterday_date()
        self.yesterday_gameStats = statsapi.schedule(
            team=self.teamId, date=self.yesterday
        )
        self.schedule = schedule

    def last_game(self):
        last_game_stats = statsapi.schedule(team=self.teamId, date=self.yesterday)
        if not last_game_stats:
            game_stats = None
            game_highlights = None
        else:
            for game in self.schedule:
                if game["game_date"] == str(self.yesterday):
                    yesterday_series_game_number = game["series_game_number"]
                    yesterday_series_length = game["series_length"]
            game_info = last_game_stats[0]
            gameId = game_info["game_id"]
            game_stats = {
                "game_date": game_info.get("game_date", None),
                "summary": game_info.get("summary", None),
                "venue_name": game_info.get("venue_name", None),
                "winning_team": game_info.get("winning_team", None),
                "series_status": game_info.get("series_status", None),
                "series_game_number": yesterday_series_game_number,
                "series_length": yesterday_series_length,
            }
            game_highlights = statsapi.game_highlights(gameId)
        return game_stats, game_highlights


if __name__ == "__main__":
    schedule = [
        {
            "game_date": "2024-08-02",
            "away_name": "New York Mets",
            "home_name": "Los Angeles Angels",
            "venue_name": "Angel Stadium",
            "series_status": "NYM leads 1-0",
            "series_game_number": 1,
            "series_length": 3,
        },
        {
            "game_date": "2024-08-03",
            "away_name": "New York Mets",
            "home_name": "Los Angeles Angels",
            "venue_name": "Angel Stadium",
            "series_status": "Series tied 1-1",
            "series_game_number": 2,
            "series_length": 3,
        },
        {
            "game_date": "2024-08-04",
            "away_name": "New York Mets",
            "home_name": "Los Angeles Angels",
            "venue_name": "Angel Stadium",
            "series_status": "LAA wins 2-1",
            "series_game_number": 3,
            "series_length": 3,
        },
    ]
    team = "New York Mets"
    (pretty_last_game_stats, game_highlights) = GameStats(team, schedule).last_game()
    print(f"{pretty_last_game_stats}\n\n{game_highlights}")
