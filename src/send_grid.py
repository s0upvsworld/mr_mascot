import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()


def send_email(email, full_subject, full_body):
    message = Mail(
        from_email="mrmet.alerts@gmail.com",
        to_emails=email,
        subject=full_subject,
        html_content=full_body,
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e.message)


if __name__ == "__main__":
    email = "s0upvsworld@gmail.com"
    full_subject = "Test Subject"
    full_body = "Test Body"
    send_email(email, full_subject, full_body)
