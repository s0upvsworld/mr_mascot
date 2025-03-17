import json
import os
from dotenv import load_dotenv
from src.game_info import GameInfo as gi
from src.open_ai import MrMascotAI as mr
from src.send_grid import send_email as se


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
    email_data = {"subject": subject, "body": body, "end": end}
    return email_data


def users():
    with open(".users.json", "r") as f:
        user_list = json.load(f)
    return user_list


def format_email(user, email_data):
    ### string variables
    replace_name = "Friend"
    unsubscribe = "\n\n(If you'd like to part ways with Mr. Met's updates, simply reply with “unsubscribe”)"

    ### get definitions
    name = user.get("name")
    email = user.get("email")
    subject = email_data.get("subject")
    body = email_data.get("body")
    end = email_data.get("end")

    ### replace name for each email component
    full_subject = subject.replace(replace_name, name)
    new_body = body.replace(replace_name, name)
    full_end = end.replace(replace_name, name)

    ### make email body
    combine = f"{new_body} \n\n{full_end} \n\n\n\n{unsubscribe}"
    full_body = combine.replace("\n", "<br>")
    send_email_data = {"subject": full_subject, "body": full_body}
    return send_email_data, email


def send(email_data, email):
    subject = email_data.get("subject")
    body = email_data.get("body")
    se(email, subject, body)


def main():
    ### load team data
    load_dotenv()
    team = os.getenv("TEAM")
    teamId = os.getenv("TEAMID")

    ### obtain team info
    last_game, last_game_highlights, next_game = game(team, teamId)

    ### retrieve subject, body, end for email
    email_data = mascot(last_game, last_game_highlights, next_game)
    print(email_data)

    ### get user list of name and email
    user_list = users()

    ### send email to each user
    for user in user_list:
        send_email_data, email = format_email(user, email_data)
        send(send_email_data, email)


if __name__ == "__main__":
    main()
