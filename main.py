import json
from app.game_info import GameInfo as gi
from app.open_ai import MrMascotAI as mr


def game():
    last_game, last_game_highlights, next_game = gi(
    "New York Mets"
    ).last_next_game_schedule()
    return last_game, last_game_highlights, next_game

def mascot(last_game, last_game_highlights, next_game):
    start = mr(last_game, last_game_highlights, next_game)
    subject = start.email_subject()
    body = start.email_body()
    end = start.email_end()
    return subject, body, end

def users():
    with open('.users.json', 'r') as f:
        users = json.load(f)

    print(users)
    return users

def send():
    print('start')

def main():
    start = users()
    print(start)


if __name__ == "__main__":
    main()