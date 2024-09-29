import smtplib
from twilio.rest import Client

TWILIO_SID = "AC8dbae08d0abcb6704ece4b9a4b73303f"
TWILIO_AUTH_TOKEN = "80bfc037ce0b40a4a9c3c569819ea693"
TWILIO_VIRTUAL_NUMBER = "+16822975132"
TWILIO_VERIFIED_NUMBER = "+41779513941"
MAIL_PROVIDER_SMTP_ADDRESS ="smtp.gmail.com"
MY_EMAIL = "brkclk.ch@gmail.com"
MY_PASSWORD = "kxlwpkzdlwwvlmmb"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )