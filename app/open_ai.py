from openai import OpenAI
from app.prompts.prompts_game import Prompts as pgame
from app.prompts.prompts_dayoff import Prompts as pdayoff
from app.prompts.prompts_personality import (
    mascot_personality,
    mascot_personality_dayoff,
)

client = OpenAI()


class MrMascotAI:
    def __init__(self, last_game, last_game_highlights, next_game):
        if last_game is None:
            self.prompt = pdayoff(next_game)
            self.mascot, self.personality, self.dayoff_fact = (
                mascot_personality_dayoff()
            )
        else:
            self.prompt = pgame(last_game, last_game_highlights, next_game)
            winning_team = last_game["winning_team"]
            self.mascot, self.personality, self.body_summary = mascot_personality(
                winning_team
            )

    def email_subject(self):
        subject_prompt = self.prompt.subject()
        subject_init = client.chat.completions.create(
            model="gpt-4o",
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
            model="gpt-4o",
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
        end_prompt = self.prompt.end()
        end_init = client.chat.completions.create(
            model="gpt-4o",
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
    from app.game_info import GameInfo

    last_game, last_game_highlights, next_game = GameInfo(
        "New York Mets"
    ).last_next_game_schedule()

    start = MrMascotAI(last_game, last_game_highlights, next_game)
    subject = start.email_subject()
    body = start.email_body()
    end = start.email_end()
    print(f"{subject} \n******\n {body} \n******\n {end}")
