from users.models import User
from celery import shared_task
from notifications.services import send_email

@shared_task
def check_last_login() -> None:
    
    inactive_users = User.objects.filter(last_login__isnull=True)
    inactive_users_emails = [user.email for user in inactive_users]
    mail_data = {
        "subject": "Pending Account Confirmation",
        "message": "Reminder to login tp your account and finalize registration",
        "recipients": inactive_users_emails
    }
    send_email.delay(mail_data)
