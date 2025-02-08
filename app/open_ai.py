from openai import OpenAI

# from stats import lastGame
from prompts import Prompts

client = OpenAI()


class MrMascotAI:
    def __init__(
        self, summary, game_date, gameHighlights, ballpark, winning_team, series_status
    ):
        self.prompt = Prompts(
            summary, game_date, gameHighlights, ballpark, winning_team, series_status
        )
        self.personality = self.prompt.personality()
        self.summary = summary
        self.highlights = gameHighlights
        self.game_date = game_date

    def email_subject(self):
        subject_prompt = self.prompt.subject()
        subject_init = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": self.personality},
                {"role": "user", "content": subject_prompt},
            ],
        )
        subject = subject_init.choices[0].message.content
        self.subject_prompt = subject_prompt
        self.subject = subject
        return subject

    def email_body(self):
        body_prompt = self.prompt.body()
        body_init = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": self.personality},
                {"role": "user", "content": self.subject_prompt},
                {"role": "assistant", "content": self.subject},
                {"role": "user", "content": body_prompt},
            ],
        )
        body = body_init.choices[0].message.content
        self.body_prompt = body_prompt
        self.body = body
        return body

    def email_end(self):
        end_prompt = self.prompt.email_end()
        end_init = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": self.personality},
                {"role": "user", "content": self.subject_prompt},
                {"role": "assistant", "content": self.subject},
                {"role": "user", "content": self.body_prompt},
                {"role": "assistant", "content": self.body},
                {"role": "user", "content": end_prompt},
            ],
        )
        end = end_init.choices[0].message.content
        return end


if __name__ == "__main__":
    # summary, game_date, gameHighlights = lastGame()
    # summary, game_date, gameHighlights = 'mets win against marlins 3-2', 'june 13', 'Francisco Lindor 3 run homerun in the 9th inning'
    summary = "Mets win 4-1"
    game_date = "10-9-24"
    gameHighlights = "Francisco Lindor 4 run home run"
    winning_team = "New York Mets"
    series_status = "Mets WIN 3-1"
    ballpark = "Citifield"
    start = MrMascotAI(
        summary, game_date, gameHighlights, ballpark, winning_team, series_status
    )
    subject = start.email_subject()
    body = start.email_body()
    end = start.email_end()
    print(f"{subject} \n******\n {body} \n******\n {end}")
