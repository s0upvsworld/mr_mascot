import json
from app.utils import Utilities as ut
from app.stats import GameStats as sta
from app.schedule import Schedule as sch

team = "New York Mets"
teamId = "121"

games_schedule, today_game, tomorrow_game = sch(team).seven_day_schedule()

pretty_games_schedule = json.dumps(games_schedule, indent=4)
pretty_today_game = json.dumps(today_game, indent=4)
pretty_tomorrow_game = json.dumps(tomorrow_game, indent=4)

print(
    f"Pretty Games Schedule: {pretty_games_schedule}\n\nPretty Today Game: {pretty_today_game}\n\nPretty Tomorrow Game: {pretty_tomorrow_game}"
)

game_stats, game_highlights = sta(team, games_schedule).last_game()

pretty_last_game_stats = json.dumps(game_stats, indent=4)
print(f"{pretty_last_game_stats}")
