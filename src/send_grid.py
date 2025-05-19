import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from jinja2 import Template

load_dotenv()

def send_email(email, full_subject, full_body):
    unsubscribe = "If you'd like to part ways with Mr. Met's updates, reply with “unsubscribe”"
    with open("src/email_template.html", "r") as file:
        template_content = file.read()

    template = Template(template_content)
    rendered_body = template.render(subject=full_subject, body=full_body, unsubscribe=unsubscribe)

    with open("email_preview.html", "w") as preview_file:
        preview_file.write(rendered_body)

    message = Mail(
        from_email="mrmet.alerts@gmail.com",
        to_emails=email,
        subject=full_subject,
        html_content=rendered_body,
    )
    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    email = "s0upvsworld@gmail.com"
    full_subject = "Test Subject"
    full_body = (
        "This is the full body of the email. "
        "The weather today is sunny with a slight breeze. "
        "Remember to stay hydrated and take breaks while working. "
        "Did you know that April is National Poetry Month? "
        "Here's a fun fact: Honey never spoils, even after thousands of years. "
        "Lastly, keep an eye out for exciting updates coming your way!"
    )
    send_email(email, full_subject, full_body)
