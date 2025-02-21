from app.prompts.prompts_personality import mascot_personality_dayoff

### OpenAI PERSONALITY


class Prompts:
    def __init__(self, next_game):
        self.next_gane = next_game
        self.mascot, self.personality, self.dayoff_fact = mascot_personality_dayoff()
        if next_game["away_name"] == "New York Mets":
            self.next_team = next_game["home_name"]
        else:
            self.next_team = next_game["away_name"]
        self.next_game_date = next_game["game_date"]
        self.next_series_status = next_game["series_status"]
        self.next_series_game_number = next_game["series_game_number"]
        self.next_series_length = next_game["series_length"]

    def subject(self):
        subject_prompt = f"""
        No game played was played yesterday, you will be sharing {self.dayoff_fact} instead.
        """
        return subject_prompt

    def body(self):
        prompt_length = "In four sentences and no more than 100 words"
        body_prompt = f"""
        Introduce yourself. Start with a note that the Mets did not play yesterday. {prompt_length} give a fact of {self.dayoff}. End with some sort of question like Isnt that neat, Friend? or Dont you think thats cool, Friend? or something similar.
        """
        return body_prompt

    def email_end(self):
        end_prompt = f"""
        Next Game Info: On {self.next_game_date} against the {self.next_team} in a {self.next_series_length} games series. Only mention the series length if it's a new team or if it's the last game in the series. Then in one sentence wish the reader well and say \'Let\'s Go Mets!\' and something endearing. Sign the end.
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
