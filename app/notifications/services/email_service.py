from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
    
@shared_task
def send_email(mail_data: dict[str, any]) -> None:
    
    email = EmailMessage(
        mail_data['subject'], 
        mail_data['message'], 
        settings.DEFAULT_FROM_EMAIL, 
        mail_data['recipients']
    )
    email.send()    
    