import statsapi
from utils import Utilities as ut

class TeamStats:
    def __init__(self, team):
        self.team = team
        self.teamId = "121"

        ### To be added below
        # today = datetime.now().date().strftime('%Y-%m-%d')
        # yesterday = today - timedelta(days=1)
        # thirty_days = today + timedelta(days=30)

        # For yesterday
        self.gameStats = statsapi.schedule(team=self.teamId, date="2024-09-01")

    def lastGame(self):
        try:
            if not self.gameStats:
                summary = None
                game_date = None
                gameHighlights = None
                ballpark = None
                winning_team = None
                series_status = None
            else:
                gameId = self.gameStats[0]['game_id']
                game_date = self.gameStats[0]['game_date']
                summary = self.gameStats[0]['summary']
                ballpark = self.gameStats[0]['venue_name']
                winning_team = self.gameStats[0]['winning_team']
                series_status = self.gameStats[0]['series_status']
                gameHighlights = statsapi.game_highlights(gameId)             
        except Exception:
            summary = None
            game_date = None
            gameHighlights = None
            ballpark = None
            winning_team = None
            series_status = None

        return summary, game_date, gameHighlights, ballpark, winning_team, series_status

    def schedule(self):
        today = ut().today_date()
        return today
        

if __name__ == '__main__':
    ts = TeamStats("New York Meats")
    summary, game_date, gameHighlights, ballpark, winning_team, series_status = ts.lastGame()
    enter = '\n\n'
    print(summary, enter, game_date, enter, gameHighlights, ballpark, winning_team, series_status)
    today = ts.schedule()
    print(today)