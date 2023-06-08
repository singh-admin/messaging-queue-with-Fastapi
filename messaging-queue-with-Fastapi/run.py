from fastapi import BackgroundTasks, FastAPI
import smtplib
from email.message import EmailMessage


SMTP_SERVER = 'sandbox.smtp.mailtrap.io'
SMTP_PORT = 2525
SMTP_USERNAME = '29c596458e9151'
SMTP_PASSWORD = 'aae621392e2ca5'
SENDER_EMAIL = 'mrigendra638@gmail.com'

app = FastAPI()

sender = "mrigendra638@gmail.com"
receiver = 'keheye5339@soremap.com'

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("29c596458e9151", "aae621392e2ca5")
    server.sendmail(sender, receiver, message)


@app.post('/send-email/')
async def send_email_route(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email)
    return {'message': 'Email has been queued for sending.'}

def send_email():
    message = EmailMessage()
    message['Subject'] = 'Hi Mailtrap'
    message['From'] = SENDER_EMAIL
    message['To'] = 'keheye5339@soremap.com'
    message.set_content('This is a test e-mail message.')

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(message)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

