import threading

from django.core.mail import EmailMessage
from .models import Alert

from_email = 'gift200161@gmail.com'


class EmailThread(threading.Thread):
    def __init__(self, email):
        super().__init__()
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=True)


def send_high_temperature_alert_email(temperature):
    subject = "Alert: High Temperature Detected!"
    to_email = ["giftmugaragumbojr@gmail.com"]
    email_message = f"""
    Dear User,

    The system has detected that the temperature has surpassed 25 degrees.

    The current temperature is {temperature}°C, which exceeds the safe limit.

    The Infrared Lamps have been switched off to ensure the safety and proper conditions of the poultry.

    You can login the system portal to check the status.

    With warm regards,
    Smart Poultry System
    """
    email = EmailMessage(
        subject=subject,
        to=to_email,
        body=email_message,
        from_email="gift200161@gmail.com"  # Add actual sender email address
    )
    # Send the email
    email.send()
    alert = Alert.objects.create(
        message="High Temperature",
        sensor="Temperature",
        email=True,
    )
    alert.save()


def send_low_temperature_alert_email(temperature):
    subject = "Alert: Low Temperature Detected!"
    to_email = ["giftmugaragumbojr@gmail.com"]
    email_message = f"""
    Dear User,

    The system has detected that the temperature is now below 20 degrees.

    The current temperature is {temperature}°C, which is below the safe limit.

    The Infrared Lamps have been switched on to ensure the safety and proper conditions of the poultry.

    You can login the system portal to check the status.

    With warm regards,
    Smart Poultry System
    """
    email = EmailMessage(
        subject=subject,
        to=to_email,
        body=email_message,
        from_email="gift200161@gmail.com"  # Add actual sender email address1
    )
    # Send the email
    email.send()
    alert = Alert.objects.create(
        message="Low Temperature",
        sensor="Temperature",
        email=True,
    )
    alert.save()