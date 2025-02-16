from datetime import datetime, timedelta
import random
import statsapi


class Utilities:
    def __init__(self):
        self.today = datetime.now().date().strftime("%Y-%m-%d")

        # date for testing
        self.today = datetime.strptime("2024-08-03", "%Y-%m-%d").date()

    def today_date(self):
        return self.today

    def yesterday_date(self):
        yesterday = self.today - (timedelta(days=1))
        return yesterday

    def tomorrow_date(self):
        tomorrow = self.today + (timedelta(days=1))
        return tomorrow

    def seven_days(self):
        minus_seven = self.today - (timedelta(days=7))
        seven = self.today + (timedelta(days=7))
        return minus_seven, seven

    def roll_d4():
        return random.randint(1, 4)

    def nle():
        standings = statsapi.standings(division="nle")
        return standings

    def roster(teamId):
        roster = statsapi.roster(
            teamId, rosterType=None, season=datetime.now().year, date=None
        )
        return roster


if __name__ == "__main__":
    ut = Utilities()
    today = ut.today_date()
    yesterday = ut.yesterday_date()
    seven = ut.seven_days()
    print(today, yesterday, seven)
