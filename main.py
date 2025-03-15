import json
import os
from dotenv import load_dotenv
from src.game_info import GameInfo as gi
from src.open_ai import MrMascotAI as mr

def game(team, teamId):
    last_game, last_game_highlights, next_game = gi(
    team, teamId
    ).last_next_game_schedule()
    return last_game, last_game_highlights, next_game

def mascot(last_game, last_game_highlights, next_game):
    start = mr(last_game, last_game_highlights, next_game)
    subject = start.email_subject()
    body = start.email_body()
    end = start.email_end()
    return json.dumps({"subject": subject, "body": body, "end": end})

def users():
    with open('.users.json', 'r') as f:
        user_list = json.load(f)
    return user_list

def format_email(user, email_data):
    replace_name = "Friend"
    unsubscribe = '\n\n(If you\'d like to part ways with Mr. Met\'s updates, simply reply with “unsubscribe”)'

    name = user.get("name")
    email = user.get("email")
    subject = email_data("subject")
    body = email_data("body")
    end = email_data("end")
    
    full_subject = subject.replace(replace_name, name)
    new_body = body.replace(replace_name, name)
    full_end = end.replace(replace_name, name)
    combine = f'{new_body} \n\n{full_end} \n\n\n\n{unsubscribe}'
    full_body = combine.replace('\n', '<br>')
    return json.dumps({"subject": full_subject, "body": full_body, "end": full_end}), email

    
def send():
    print('start')

def main():
    load_dotenv()
    team = os.environ.get('TEAM')
    teamId = os.environ.get('TEAMID')
    last_game, last_game_highlights, next_game = game(team, teamId)
    email_data = mascot(last_game, last_game_highlights, next_game)
    
    user_list = users()


if __name__ == "__main__":
    main()