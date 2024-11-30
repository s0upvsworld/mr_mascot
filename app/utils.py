from datetime import datetime, timedelta

class Utilities:
    def __init__(self):
        self.today = datetime.now().date().strftime('%Y-%m-%d')
        self.today = datetime.strptime("2024-09-02", '%Y-%m-%d').date()

    def today_date(self):
        return self.today

    def yesterday_date(self):
        yesterday = self.today - (timedelta(days=1))
        return yesterday

    def thirty_days(self):
        thirty = self.today + (timedelta(days=30))
        return thirty

if __name__ == "__main__":
    ut = Utilities()
    today = ut.today_date()
    yesterday = ut.yesterday_date()
    thirty = ut.thirty_days()
    print(today, yesterday, thirty)