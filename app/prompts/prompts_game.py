from app.prompts.prompts_personality import mascot_personality
from app.utils import Utilities as ut

### OpenAI PERSONALITY


class Prompts:
    def __init__(self, last_game, game_highlights, next_game):
        self.game_date = last_game["game_date"]
        self.game_summary = last_game["summary"]
        self.ballpark = last_game["venue_name"]
        self.winning_team = last_game["winning_team"]
        self.series_status = last_game["series_status"]
        self.series_game_number = last_game["series_game_number"]
        self.series_length = last_game["series_length"]
        self.game_highlights = game_highlights
        self.next_game_date = next_game["game_date"]
        self.next_series_status = next_game["series_status"]
        self.next_series_game_number = next_game["series_game_number"]
        self.next_series_length = next_game["series_length"]
        if next_game["away_name"] == "New York Mets":
            self.next_team = next_game["home_name"]
        else:
            self.next_team = next_game["away_name"]
        self.mascot, self.personality, self.body_summary = mascot_personality(
            self.winning_team
        )
        self.today_date = ut().today_date()

    def subject(self):
        subject_score = f"""
        Yesterday's Game Score: {self.game_summary}.
        """
        subject_prompt = f"""
        {subject_score} In 35 characters, come up with a subject line for an email to Friend with a Mets update. Do not use quotes or parenthesis.
        """
        return subject_prompt

    def body(self):
        series_info = f"""
        {self.series_status} in a {self.series_length} game series
        """
        prompt_length = "In four sentences and no more than 100 words"
        body_prompt = f"""
        Introduce yourself. Then, {prompt_length}, {self.body_summary}. Note the ballpark and city the game was played in and what game of the seriesi it is. Mention one key highlight that showcases the Met\'s performance. If they won then be very excited. If they lost remain hopeful.\n\nHere is the last game\'s data.\n\n The score: {self.game_summary},\n\nThe highlights: {self.game_highlights},\n\nGame Date: {self.game_date},\n\nBallpark: {self.ballpark},\n\nSeries Info:{series_info}.
        """
        return body_prompt

    def email_end(self):
        if self.next_series_game_number == 1:
            series_length = f"""
            It will be the first game in a {self.next_series_length} game series
            """
        else:
            series_length = f"""
            It will be game number {self.series_game_number} in the current {self.series_length} game series
            """
        end_prompt = f"""
        Today's Date: {self.today_date}.\n\nNext Game Info: {self.next_game_date} against the {self.next_team}. {series_length}. \n\nOnly mention the series length if it's a new team or if it's the last game in the series. The reader will be reading this and the previous paragraph together, so no need to great them again. Then in one sentence wish the reader well and say \'Let\'s Go Mets!\' and something endearing. Sign the end.
        """
        return end_prompt
