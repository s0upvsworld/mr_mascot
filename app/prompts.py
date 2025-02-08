from utils import Utilities as ut

### OpenAI PERSONALITY


class Prompts:
    def __init__(
        self, game_stats, game_highlights, games_schedule, today_game
    ):
        self.personality_roll = ut().roll_d4()
        dayoff_roll = ut().roll_d4()
        if dayoff_roll == 4:
            self.dayoff = "Mrs. Met History"
        else:
            self.dayoff = "Met\'s History"
        self.game_stats = game_stats
        if game_stats is None:
            self.game_date = None
            self.game_highlights = None
            self.today_game = today_game
            self.games_schedule = games_schedule
        else:
            self.game_date = game_stats["game_date"]
            self.game_summary = game_stats["summary"]
            self.ballpark = game_stats["venue_name"]
            self.winning_team = game_stats["winning_team"]
            self.series_status = game_stats["series_status"]
            self.series_game_number = game_stats["series_game_number"]
            self.series_length = game_stats["series_length"]
            self.game_highlights = game_highlights
            self.today_game = today_game

        self.mascot = None

    def personality(self):
        default_personality = """
            You are Mr. Met of the New York Mets. Address the reader only as \'Friend\'. Keep the tone hopeful, pleasant, and whimsical. Use baseball and Met\'s emojis.
            """
        if self.winning_team == "New York Mets":
            roll = self.personality_roll
            if roll == 1 or 2 or 3 or 4:
                personality = f"{default_personality}"
                self.mascot = "Mr. Met"
        else:
            personality = f"{default_personality}"
            self.mascot = "Mr. Met"
        return personality

    def subject(self):
        if not self.game_stats:
            subject_score = f"""
            No game played was played yesterday, you will be sharing {self.dayoff} instead.
            """
        else:
            subject_score = f"""
            Here is the game score from yesterday: {self.game_summary}.
            """
        subject_prompt = f"""
        {subject_score} In 35 characters, come up with a quirky subject line for an email to Friend with a Mets update. Do not use quotes or parenthesis.
        """
        return subject_prompt

    def body(self):
        prompt_length = "In four sentences and no more than 100 words"
        if not self.game_stats:
            body_prompt = f"""
            Introduce yourself. Start with a note that the Mets did not play yesterday. {prompt_length} give a fact of {self.dayoff}. Do not mention the Miracle Mets. End with some sort of question like Isnt that neat, Friend? or Dont you think thats cool, Friend? or something similar.
            """
        else:
            mascot_body_summary = """
            give a summary of the game
            """
            body_prompt = f"""
            Introduce yourself. Then, {prompt_length} {mascot_body_summary}. Note the ballpark and city the game was played in. Mention one key highlight that showcases the Met\'s performance. If they won then be very excited. If they lost remain hopeful.\n\nHere is the last game\'s data.\n\n The score: {self.game_summary},\n\nThe highlights: {self.highlights},\n\nGame Date: {self.game_date},\n\nBallpark: {self.ballpark}.
            """
        return body_prompt

    def email_end(self):
        if self.mascot == "Wally the Green Monster":
            end_prompt = """
            In one sentence wish the reader well and say \'Let\'s Go Red Sox!\' or something endearing. Sign the end.
            """
        else:
            end_prompt = """
            In one sentence recognize the doubleheader being played today at Truist Park against the Braves and how much these games matter if the Mets make the post-season or not. Then, n one sentence wish the reader well and say \'Let\'s Go Mets!\' or something endearing. Sign the end.
            """
        return end_prompt


if __name__ == "__main__":
    # summary = 'Mets ovev Red Sox, 3-2'
    # game_date = '2024-07-05'
    # gameHighlights = 'Jarren Duran 2 run homer against the Mets. Lindor 3 run homeruner against the Red Sox'
    # winning_team = 'New York Mets'
    # series_status = 'a'
    # ballpark = 'Citifield'
    summary, game_date, gameHighlights = (
        "2024-07-04 - New York Mets (0) @ Washington Nationals (1) (FinalFinal)",
        "2024-07-04",
        """
    Mark Vientos' backhanded grab (00:00:18)
    Mark Vientos makes a slick backhanded catch off Joey Meneses' liner for the final out of the bottom of the 1st
    https://mlb-cuts-diamond.mlb.com/FORGE/2024/2024-07/04/0fbf1002-a28f72bc-c18168ba-csvm-diamondx64-asset_1280x720_59_4000K.mp4

    Jake Irvin strikes out Francisco Alvarez (00:00:16)
    Jake Irvin gets Francisco Alvarez to strike out swinging in the top of the 1st for his first strikeout of the game
    https://mlb-cuts-diamond.mlb.com/FORGE/2024/2024-07/04/59ba6464-b0339c5f-a1fb0472-csvm-diamondx64-asset_1280x720_59_4000K.mp4

    Jose Quintana strikes out CJ Abrams (00:00:07)
    Jose Quintana gets CJ Abrams to strike out swinging in the bottom of the 5th
    https://mlb-cuts-diamond.mlb.com/FORGE/2024/2024-07/05/a93826ef-675d5c66-802b4fee-csvm-diamondx64-asset-4000K.mp4

    Mets turn inning-ending double play (00:00:15)
    The Mets combine for a double play off Nick Senzel's grounder to end the bottom of the 4th and keep the game scoreless
    https://mlb-cuts-diamond.mlb.com/FORGE/2024/2024-07/04/ff426db4-ffa3fc69-cf86bfd6-csvm-diamondx64-asset_1280x720_59_4000K.mp4

    Jesse Winker's go-ahead solo homer (10) (00:00:29)
    Jesse Winker launches a solo home run to right-center field to give the Nats a 1-0 lead in the bottom of the 8th
    https://mlb-cuts-diamond.mlb.com/FORGE/2024/2024-07/04/41623543-238e466c-8d7b29da-csvm-diamondx64-asset_1280x720_59_4000K.mp4

    Jake Irvin's eighth K (00:00:18)
    Jake Irvin strikes out Tyrone Taylor to end the top of the 8th
    https://mlb-cuts-diamond.mlb.com/FORGE/2024/2024-07/04/6f8c4b46-8df4deec-d04814d5-csvm-diamondx64-asset_1280x720_59_4000K.mp4

    Derek Law seals Nats' 1-0 win with strikeout (00:00:28)
    Derek Law gets Brandon Nimmo to strike out swinging to secure the Nationals' 1-0 win
    https://mlb-cuts-diamond.mlb.com/FORGE/2024/2024-07/04/867db3c2-42b5b145-7d5d5e9c-csvm-diamondx64-asset_1280x720_59_4000K.mp4

    Jake Irvin K's eight in strong start (00:01:08)
    Jake Irvin collects eight strikeouts over eight one-hit innings during his start against the Mets
    https://mlb-cuts-diamond.mlb.com/FORGE/2024/2024-07/04/6c443ed1-5919f3e3-37faef47-csvm-diamondx64-asset_1280x720_59_4000K.mp4

    Mets vs. Nationals Highlights (00:03:04)
    Jose Quintana and the Mets take on Jake Irvin and the Nationals on July 4th, 2024
    https://mlb-cuts-diamond.mlb.com/FORGE/2024/2024-07/04/67508508-e498efff-beb16c9b-csvm-diamondx64-asset_1280x720_59_4000K.mp4

    Condensed Game: NYM@WSH - 7/4/24 (00:09:12)
    Condensed Game: Jose Quintana and the Mets take on Jake Irvin and the Nationals on July 4th, 2024
    https://mlb-cuts-diamond.mlb.com/FORGE/2024/2024-07/04/846ff73c-73e4e010-2100d215-csvm-diamondx64-asset_1280x720_59_4000K.mp4
    """,
    )
    ballpark = "Citifield"
    winning_team = "New York Mets"
    series_status = "na"
    start = Prompts(
        summary, game_date, gameHighlights, ballpark, winning_team, series_status
    )
    personality = start.personality()
    print(personality)
    subject = start.subject()
    print(subject)
    body = start.body()
    print(body)
    end = start.email_end()
    print(end)
